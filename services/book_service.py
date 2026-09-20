from models.book import Book


class BookService:
    def __init__(self, book_repository, loan_repository):
        self.book_repo = book_repository
        self.loan_repo = loan_repository


    def add(self, title, author, isbn, year, genre, total_copies):
        book = Book(id=0, title=title, author=author, isbn=isbn, year=year, genre=genre, total_copies=total_copies)
        return self.book_repo.add(book)


    def get_all(self):
        return self.book_repo.get_all()


    def get_by_id(self, book_id):
        return self.book_repo.get_by_id(book_id)


    def update(self, book_id, title, author, isbn, year, genre, total_copies):
        existing = self.book_repo.get_by_id(book_id)

        if existing is None:
            return False

        existing.title = title
        existing.author = author
        existing.isbn = isbn
        existing.year = year
        existing.genre = genre
        existing.total_copies = total_copies

        return self.book_repo.update(existing)


    def delete(self, book_id):
        book = self.book_repo.get_by_id(book_id)
        if book is None:
            return False

        loans = self.loan_repo.get_all()
        for loan in loans:
            if loan.book_id == book_id and loan.return_date is None:
                return False

        return self.book_repo.delete(book_id)
