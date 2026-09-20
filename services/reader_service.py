from models.reader import Reader


class ReaderService:
    def __init__(self, reader_repository, loan_repository):
        self.reader_repo = reader_repository
        self.loan_repo = loan_repository


    def add(self, full_name, email, phone, address,  birth_date):
        reader = Reader(id=0, full_name=full_name, email=email, phone=phone, address=address, birth_date=birth_date)
        return self.reader_repo.add(reader)


    def get_all(self):
        return self.reader_repo.get_all()


    def get_by_id(self, reader_id):
        return self.reader_repo.get_by_id(reader_id)


    def update(self, reader_id, full_name, email, phone, address, birth_date):
        existing = self.reader_repo.get_by_id(reader_id)

        if existing is None:
            return False


        existing.full_name = full_name
        existing.email = email
        existing.phone = phone
        existing.address = address
        existing.birth_date = birth_date

        return self.reader_repo.update(existing)


    def block_reader(self, reader_id):
        reader = self.reader_repo.get_by_id(reader_id)
        if reader is None:
            return False

        reader.is_blocked = True
        return self.reader_repo.update(reader)


    def unblock_reader(self, reader_id):
        reader = self.reader_repo.get_by_id(reader_id)
        if reader is None:
            return False

        reader.is_blocked = False
        return self.reader_repo.update(reader)


    def delete(self, reader_id):
        reader = self.reader_repo.get_by_id(reader_id)
        if reader is None:
            return False

        loans = self.loan_repo.get_all()
        for loan in loans:
            if loan.reader_id == reader_id and loan.return_date is None:
                return False

        return self.reader_repo.delete(reader_id)