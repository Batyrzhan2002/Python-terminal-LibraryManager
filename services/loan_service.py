from config import MAX_LIMIT_BOOKS, FORMAT_FOR_DATE, MAX_LIMIT_DAY, LATE_PAYMENT_PENALTY
from models.loan import Loan
from datetime import datetime, timedelta


class LoanService:

    def __init__(self, loan_repository, book_repository, reader_repository):
        self.loan_repo = loan_repository
        self.book_repo = book_repository
        self.reader_repo = reader_repository


    def get_all(self):
        return self.loan_repo.get_all()


    def get_by_id(self, loan_id):
        return self.loan_repo.get_by_id(loan_id)


    def issue_loan(self, book_id, reader_id):
        book = self.book_repo.get_by_id(book_id)
        if book is None:
            return False
        if book.available_copies <= 0:
            return False

        reader = self.reader_repo.get_by_id(reader_id)
        if reader is None:
            return False
        if reader.is_blocked:
            return False

        loans = self.loan_repo.get_all()
        loan_copies = 0
        for loan in loans:
            if loan.reader_id == reader_id:
                if loan.return_date is None:
                    loan_copies += 1
        if loan_copies >= MAX_LIMIT_BOOKS:
            return False

        book.available_copies -= 1
        self.book_repo.update(book)

        loan_date = datetime.now()
        due_date = loan_date + timedelta(days=MAX_LIMIT_DAY)

        loan = Loan(
            id=0,
            book_id=book_id,
            reader_id=reader_id,
            loan_date=loan_date.strftime(FORMAT_FOR_DATE),
            due_date=due_date.strftime(FORMAT_FOR_DATE),
            return_date=None,
            fine=0,
        )

        return self.loan_repo.add(loan)


    def return_loan(self, loan_id):
        loan = self.loan_repo.get_by_id(loan_id)
        if loan is None:
            return False
        
        if loan.return_date is not None:
            return False

        today = datetime.now()
        loan.return_date = today.strftime(FORMAT_FOR_DATE)

        due = datetime.strptime(loan.due_date, FORMAT_FOR_DATE)
        if today > due:
            days_late = (today - due).days
            loan.fine = days_late * LATE_PAYMENT_PENALTY
        else:
            loan.fine = 0

        book = self.book_repo.get_by_id(loan.book_id)
        if book is None:
            return False
        book.available_copies += 1
        self.book_repo.update(book)

        return self.loan_repo.update(loan)


    def get_overdue_loans(self):
        overdue = []
        today = datetime.now()
        for loan in self.loan_repo.get_all():
            if loan.return_date is None:
                due = datetime.strptime(loan.due_date, LATE_PAYMENT_PENALTY)
                if today > due:
                    overdue.append(loan)
        return overdue