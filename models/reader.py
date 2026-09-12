from dataclasses import dataclass
from datetime import datetime
from config import FORMAT_FOR_DATE


@dataclass
class Reader:
    id: int
    full_name: str
    email: str
    phone: str
    address: str
    birth_date: str
    is_blocked: bool = False


    def __post_init__(self):
        if not self.full_name.strip():
            raise ValueError('ФИО не может быть пустым')


        if '@' not in self.email or '.' not in self.email:
            raise ValueError('Введен некорректный email.')


        clean_phone = ''.join(filter(str.isdigit, self.phone))
        if not clean_phone.startswith('7') or len(clean_phone) != 11:
            raise ValueError('Телефон должен быть в формате +7XXXXXXXXXX')


        try:
            birth_date = datetime.strptime(self.birth_date, FORMAT_FOR_DATE)
        except ValueError:
            raise ValueError(f'Дата должна быть в формате {FORMAT_FOR_DATE}')

        now_date = datetime.now()
        if birth_date > now_date:
            raise ValueError('Дата рождения не может быть в будущем')

        age = (now_date - birth_date).days // 365
        if age < 6:
            raise ValueError('Читатель должен быть старше 6 лет')


