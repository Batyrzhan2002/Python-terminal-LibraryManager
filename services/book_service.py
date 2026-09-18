from models.book import Book

class BookService:
    def __init__(self, book_repository):
        self.book_repo = book_repository


    def add(self, title, author, isbn, year, genre, total_copies):
        book = Book(id=0, title=title, author=author, isbn=isbn, year=year, genre=genre, total_copies=total_copies)
        return self.book_repo.add(book)


    def get_all(self):
        return self.book_repo.get_all()


    def get_by_id(self, book_id):
        return self.book_repo.get_by_id(book_id)