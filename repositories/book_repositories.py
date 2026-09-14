
class BookRepository:

    def __init__(self, file_path):
        self.file_path = file_path
        self.books = []

    def load(self):
        if self.file_path.exists():
            with open(self.file_path, 'r', encoding='utf-8') as file:
                pass
        else:
            pass