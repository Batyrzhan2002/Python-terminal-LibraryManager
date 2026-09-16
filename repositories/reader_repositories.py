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