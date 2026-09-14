from datetime import datetime
from dataclasses import dataclass
from typing import Optional
from config import FORMAT_FOR_DATE


@dataclass
class Loan:
    id: int
    book_id: int
    reader_id: int
    loan_date: str
    due_date: str
    return_date: Optional[str] = None
    fine: float = 0


    def __post_init__(self):
        try:
            loan_date = datetime.strptime(self.loan_date, FORMAT_FOR_DATE)
        except ValueError:
            raise ValueError(f'Дата должна быть в формате {FORMAT_FOR_DATE}')


        try:
            due_date = datetime.strptime(self.due_date, FORMAT_FOR_DATE)
        except ValueError:
            raise ValueError(f'Дата должна быть в формате {FORMAT_FOR_DATE}')
        if loan_date > due_date:
            raise ValueError('Дата возврата неверна')


        if self.return_date is not None:
            try:
                return_date = datetime.strptime(self.return_date, FORMAT_FOR_DATE)
            except ValueError:
                raise ValueError(f'Дата должна быть в формате {FORMAT_FOR_DATE}')
            
            if return_date < loan_date:
                raise ValueError('Дата возврата указана неверно')


    def to_dict(self):
        return {
            'id': self.id,
            'book_id': self.book_id,
            'reader_id': self.reader_id,
            'loan_date': self.loan_date,
            'due_date': self.due_date,
            'return_date': self.return_date,
            'fine': self.fine,
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data['id'],
            book_id = data['book_id'],
            reader_id = data['reader_id'],
            loan_date = data['loan_date'],
            due_date = data['due_date'],
            return_date = data.get('return_date', None),
            fine = data.get('fine', 0)
        )