import json
from models.book import Book


class BookRepository:

    def __init__(self, file_path):
        self.file_path = file_path
        self.books = []


    def load(self):
        if self.file_path.exists():
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for item in data:
                    book = Book.from_dict(item)
                    self.books.append(book)
        else:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file)


    def save(self):
        data = []
        for book in self.books:
            data.append(book.to_dict())

        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def get_all(self):
        return self.books.copy()


    def get_by_id(self, id):
        for item in self.books:
            if item.id == id:
                return item
        return None


    def add(self, book):
        new_id = max((item.id for item in self.books), default=0) + 1
        book.id = new_id
        self.books.append(book)
        self.save()
        return book


    def update(self, book):
        for i, item in enumerate(self.books):
            if item.id == book.id:
                self.books[i] = book
                self.save()
                return True
        return False


    def delete(self, book_id):
        for i, item in enumerate(self.books):
            if item.id == book_id:
                self.books.pop(i)
                self.save()
                return True
        return False
