from dataclasses import dataclass
from datetime import datetime
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


    def __post_init__():
        pass