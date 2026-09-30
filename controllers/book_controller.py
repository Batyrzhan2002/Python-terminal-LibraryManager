from config import GenresBooks

class BookController:
    def __init__(self, book_service):
        self.book_service = book_service


    def show_menu(self):
        while True:
            print('\n--- Книги ---')
            print('1. Показать все')
            print('2. Добавить')
            print('3. Найти по ID')
            print('0. Назад')

            try:
                choice = int(input('Выбор: '))
            except ValueError:
                print('Введите число')
                continue

            if choice == 1:
                self.show_all_books()
            elif choice == 2:
                self.add_book_view()
            elif choice == 3:
                self.get_book_by_id_view()
            elif choice == 0:
                break
            else:
                print('Неверный выбор')

    def show_all_books(self):
        books = self.book_service.get_all()
        if not books:
            print('Нет книг')
            return
        for book in books:
            print(f'ID: {book.id}, {book.title} - {book.author}')

    def add_book_view(self):
        title = input('Название книги: ')
        author = input('Автор книги: ')
        isbn = input('isbn книги: ')

        try:
            year = int(input('Укажите Год: '))
            total_copies = int(input('Количество книг: '))
        except ValueError:
            print('Введите число')
            return
            
        print('Доступные жанры:')
        for i, g in enumerate(GenresBooks, 1):
            print(f'{i}.{g.value}')
        try:
            genre_choice = int(input('Укажите жанр: '))
            genre = list(GenresBooks)[genre_choice - 1]
        except (ValueError, IndexError):
            print('Неверный выбор жанра')
            return

        try:
            book = self.book_service.add(title, author, isbn, year, genre, total_copies)
            if book:
                print(f'Книга добавлена с ID: {book.id}')
            else:
                print('Не удалось добавить книгу')
        except ValueError as e:
            print(f'Ошибка валидации: {e}')


    def get_book_by_id_view(self):
        try:
            book_id = int(input('Введите ID книги: '))
        except ValueError:
            print('Введите корректный id')
            return

        book = self.book_service.get_by_id(book_id)
        if book is None:
            print('Книга не найдена')
            return

        print(f'''
ID: {book.id}
Название: {book.title}
Автор: {book.author}
ISBN: {book.isbn}
Год: {book.year}
Жанр: {book.genre.value}
Всего: {book.total_copies}
Доступно: {book.available_copies}''')