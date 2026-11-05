from datetime import datetime
from config import FORMAT_FOR_DATE


class LoanController:
    def __init__(self, loan_service):
        self.loan_service = loan_service


    def show_menu(self):
        while True:
            print('\n--- Выдачи ---')
            print('1. Показать все')
            print('2. Выдать книгу')
            print('3. Вернуть книгу')
            print('4. Найти по ID')
            print('5. Просроченные')
            print('0. Назад')


            try:
                choice = int(input('Выбор: '))
            except ValueError:
                print('Введите число')
                continue

            if choice == 1:
                self.show_all_loans()
            elif choice == 2:
                self.issue_loan_view()
            elif choice == 3:
                self.return_loan_view()
            elif choice == 4:
                self.get_loan_by_id_view()
            elif choice == 5:
                self.get_overdue_loans_view()
            elif choice == 0:
                break
            else:
                print('Неверный выбор')

    def show_all_loans(self):
        loans = self.loan_service.get_all()
        if not loans:
            print('Нет выдач')
            return
        for loan in loans:
            if loan.return_date is not None:
                status = 'возвращена'
            else:
                due = datetime.strptime(loan.due_date, FORMAT_FOR_DATE)
                if datetime.now() > due:
                    status = 'просрочена'
                else:
                    status = 'активна'

            print(f'ID: {loan.id} | Книга: {loan.book_id} | Читатель: {loan.reader_id} | {loan.loan_date} → {loan.due_date} | {status}')

    def issue_loan_view(self):
        pass

    def return_loan_view(self):
        pass

    def get_loan_by_id_view(self):
        pass

    def get_overdue_loans_view(self):
        pass