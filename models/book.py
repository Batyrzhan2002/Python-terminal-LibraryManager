from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional
from config import GenresBooks, FORMAT_FOR_DATE


@dataclass
class Book:
    id: int
    title: str
    author: str
    isbn: str
    year: int
    genre: GenresBooks
    total_copies: int
    available_copies: Optional[int] = None


    def __post_init__(self):
        if not self.title.strip():
            raise ValueError('Название не может быть пустым')


        if not self.author.strip():
            raise ValueError('Автор не может быть пустым')


        isbn = self.isbn
        isbn_clean = ''.join(filter(str.isdigit, isbn))
        if len(isbn_clean) not in (10, 13):
            raise ValueError('Некорректный isbn')


        year = self.year
        now_year = date.today().year
        if not (1 <= year <= now_year):
            raise ValueError(f"Год должен быть от 1 до {now_year}")


        if not isinstance(self.genre, GenresBooks):
            raise ValueError('Некорректный жанр')


        if self.total_copies <= 0:
            raise ValueError('Количество экземпляров должно быть больше 0')


        if self.available_copies is None:
            self.available_copies = self.total_copies
        elif self.available_copies > self.total_copies:
            raise ValueError('Доступных экземпляров не может быть больше общего количества')


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'year': self.year,
            'genre': self.genre.value,
            'total_copies': self.total_copies,
            'available_copies': self.available_copies,
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data['id'],
            title = data['title'],
            author = data['author'],
            isbn = data['isbn'],
            year = data['year'],
            genre = GenresBooks(data['genre']),
            total_copies = data['total_copies'],
            available_copies = data['available_copies']
        )
