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
            print('4. Редактировать')
            print('5. Удалить')
            print('6. Поиск по автору/названию')
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
            elif choice == 4:
                self.edit_book_view()
            elif choice == 5:
                self.delete_book_view()
            elif choice == 6:
                self.search_book_view()
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


    def edit_book_view(self):
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
            book = self.book_service.update(book_id, title, author, isbn, year, genre, total_copies)
            if book:
                print(f'Книга успешна изменена (ID: {book_id})')
            else:
                print('Не удалось изменить книгу')
        except ValueError as e:
            print(f'Ошибка валидации: {e}')


    def delete_book_view(self):
        try:
            book_id = int(input('Введите ID книги: '))
        except ValueError:
            print('Введите корректный id')
            return

        book = self.book_service.get_by_id(book_id)
        if book is None:
            print('Книга не найдена')
            return

        print(f'Вы действительно хотите удалить {book.id}.{book.title}?')
        try:
            delete_choice = int(input('1.Да \n2.Нет\n'))
        except ValueError:
            print('Введите число 1 или 2')
            return
        if delete_choice == 1:
            if self.book_service.delete(book_id):
                print('Книга успешно удалена')
            else:
                print('Не удалось удалить книгу')
        elif delete_choice == 2:
            return
        else:
            print('Введите правильное значение')
            return


    def search_book_view(self):
        keyword = input('Введите слово для поиска: ').lower()
        if not keyword:
            print('Введите слово')
            return

        books = self.book_service.get_all()
        found = []
        for book in books:
            if keyword in book.title.lower() or keyword in book.author.lower():
                found.append(book)

        if not found:
            print('Ничего не найдено')
            return

        for book in found:
            print(f'ID: {book.id}, {book.title} - {book.author}')