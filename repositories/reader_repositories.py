import json
from models.reader import Reader


class ReaderRepositories:

    def __init__(self, file_path):
        self.file_path = file_path
        self.readers = []

    def load(self):
        if self.file_path.exists():
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for item in data:
                    reader = Reader.from_dict(item)
                    self.readers.append(reader)
        else:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file)



    def save(self):
        data = []
        for reader in self.readers:
            data.append(reader.to_dict())

        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def get_all(self):
        return self.readers.copy()


    def get_by_id(self, id):
        for reader in self.readers:
            if reader.id == id:
                return reader

        return None


    def add(self, reader):
        new_id = max((item.id for item in self.readers), default=0) + 1
        reader.id = new_id
        self.readers.append(reader)
        self.save()
        return reader


    def update(self, reader):
        for i, item in enumerate(self.readers):
            if item.id == reader.id:
                self.readers[i] = reader
                self.save()
                return True

        return False


    def delete(self, reader_id):
        for i, item in enumerate(self.readers):
            if item.id == reader_id:
                self.readers.pop(i)
                self.save()
                return True

        return False