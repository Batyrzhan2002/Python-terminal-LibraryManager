from enum import Enum
from pathlib import Path

MAX_LIMIT_DAY = 14
LATE_PAYMENT_PENALTY = 10
MAX_LIMIT_BOOKS = 3
FORMAT_FOR_DATE = '%d.%m.%Y'

MAIN_FILE_ADDRESS = Path('data/')
MAIN_FILE_ADDRESS.mkdir(parents=True, exist_ok=True)
JSON_BOOK_ADDRESS = MAIN_FILE_ADDRESS + 'books.json'
JSON_LOAN_ADDRESS = MAIN_FILE_ADDRESS + 'loans.json'
JSON_READER_ADDRESS = MAIN_FILE_ADDRESS +'readers.json'

class GenresBooks(Enum):
    FANTASY = 'Фантастика'
    CLASSIC = 'Классика'
    DETECTIVE = 'Детектив'


class LoanStatus(Enum):
    ACTIVE = 'Активен'
    RETURNED = 'Возвращен'
    OVERDUE = 'Просрочен'
