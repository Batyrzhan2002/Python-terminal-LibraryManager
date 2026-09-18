import json
from models.loan import Loan


class LoanRepositories:

    def __init__(self, file_path):    
        self.file_path = file_path
        self.loans = []


    def load(self):
        if self.file_path.exists():
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for item in data:
                    loan = Loan.from_dict(item)
                    self.loans.append(loan)
        else:
            with open(self.file_path,'w', encoding='utf-8') as file:
                json.dump([], file)


    def save(self):
        data = []
        for loan in self.loans:
            data.append(loan.to_dict())

        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def get_all(self):
        return self.loans.copy()


    def get_by_id(self, id):
        for loan in self.loans:
            if loan.id == id:
                return loan

        return None



    def add(self, loan):
        new_id = max((item.id for item in self.loans), default=0) + 1
        loan.id = new_id
        self.loans.append(loan)
        self.save()
        return loan


    def update(self, loan):
        for i, item in enumerate(self.loans):
            if item.id == loan.id:
                self.loans[i] = loan
                self.save()
                return True

        return False


    def delete(self, loan_id):
        for i, item in enumerate(self.loans):
            if item.id == loan_id:
                self.loans.pop(i)
                self.save()
                return True

        return False