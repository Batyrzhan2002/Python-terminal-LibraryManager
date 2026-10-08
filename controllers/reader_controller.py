class ReaderController:
    def __init__(self, reader_service):
        self.reader_service = reader_service


    def show_menu(self):
        while True:
            print('\n--- Читатели ---')
            print('1. Показать всех')
            print('2. Добавить')
            print('3. Найти по ID')
            print('4. Редактировать')
            print('5. Удалить')
            print('6. Заблокировать')
            print('7. Разблокировать')
            print('8. Поиск по Именю ФИО/email')
            print('0. Назад')

            try:
                choice = int(input('Выбор: '))
            except ValueError:
                print('Введите число')
                continue

            if choice == 1:
                self.show_all_readers()
            elif choice == 2:
                self.add_reader_view()
            elif choice == 3:
                self.get_reader_by_id_view()
            elif choice == 4:
                self.edit_reader_view()
            elif choice == 5:
                self.delete_reader_view()
            elif choice == 6:
                self.block_reader_view()
            elif choice == 7:
                self.unblock_reader_view()
            elif choice == 8:
                self.search_reader_view()
            elif choice == 0:
                break
            else:
                print('Неверный выбор')


    def show_all_readers(self):
        readers = self.reader_service.get_all()
        if not readers:
            print('Нет читателей')
            return
        for reader in readers:
            status = 'заблокирован' if reader.is_blocked else 'активен'
            print(f'ID: {reader.id} - {reader.full_name} ({status})')


    def add_reader_view(self):
        full_name = input('Введите ФИО: ')
        email = input('Введите email: ')
        phone = input('Введите номер телефона: ')
        address = input('Введите адрес: ')
        birth_date = input('Введите дату рождения: ')

        try:
            reader = self.reader_service.add(full_name, email, phone, address, birth_date)
            if reader:
                print(f'Читатель добавлен с ID: {reader.id}')
            else:
                print('Не удалось добавить читателя')
        except ValueError as e:
            print(f'Ошибка валидации: {e}')


    def get_reader_by_id_view(self):
        try:
            reader_id = int(input('Введите id читателя: '))
        except ValueError:
            print('Введите корректный id')
            return

        reader = self.reader_service.get_by_id(reader_id)
        if reader is None:
            print('Читатель не найден')
            return

        status = 'заблокирован' if reader.is_blocked else 'активен'

        print(f'''
id: {reader.id}
ФИО: {reader.full_name}
email: {reader.email}
Номер телефона: {reader.phone}
Адрес: {reader.address}
Дата рождения: {reader.birth_date}
Статус: {status}
''')

    def edit_reader_view(self):
        try:
            reader_id = int(input('Введите id читателя: '))
        except ValueError:
            print('Введите корректный id')
            return

        reader = self.reader_service.get_by_id(reader_id)
        if reader is None:
            print('Читатель не найден')
            return

        status = 'заблокирован' if reader.is_blocked else 'активен'

        print(f'''
id: {reader.id}
ФИО: {reader.full_name}
email: {reader.email}
Номер телефона: {reader.phone}
Адрес: {reader.address}
Дата рождения: {reader.birth_date}
Статус: {status}
''')
        full_name = input('Введите ФИО: ')
        email = input('Введите email: ')
        phone = input('Введите номер телефона: ')
        address = input('Введите адрес: ')
        birth_date = input('Введите дату рождения: ')

        try:
            result = self.reader_service.update(reader_id, full_name, email, phone, address, birth_date)
            if result:
                print(f'Читатель с ID: {reader_id} успешно изменен')
            else:
                print('Не удалось изменить читателя')
        except ValueError as e:
            print(f'Ошибка валидации: {e}')


    def delete_reader_view(self):
        try:
            reader_id = int(input('Введите id читателя: '))
        except ValueError:
            print('Введите корректный id')
            return

        reader = self.reader_service.get_by_id(reader_id)
        if reader is None:
            print('Читатель не найден')
            return

        print(f'Вы действительно хотите удалить {reader.id}.{reader.full_name}?')
        try:
            delete_choice = int(input('1.Да \n2.Нет\n'))
        except ValueError:
            print('Введите число 1 или 2')
            return
        if delete_choice == 1:
            if self.reader_service.delete(reader_id):
                print('Читатель успешно удален')
            else:
                print('Не удалось удалить читателя')
        elif delete_choice == 2:
            return
        else:
            print('Введите правильное значение')
            return


    def block_reader_view(self):
        try:
            reader_id = int(input('Введите id читателя: '))
        except ValueError:
            print('Введите корректный id')
            return

        if self.reader_service.block_reader(reader_id):
            print('Читатель заблокирован')
        else:
            print('Не удалось заблокировать читателя')


    def unblock_reader_view(self):
        try:
            reader_id = int(input('Введите id читателя: '))
        except ValueError:
            print('Введите корректный id')
            return

        if self.reader_service.unblock_reader(reader_id):
            print('Читатель разблокирован')
        else:
            print('Не удалось разблокировать читателя')


    def search_reader_view(self):
        keyword = input('Введите ФИО/email для поиска: ').lower()
        if not keyword:
            print('Введите данные')
            return

        readers = self.reader_service.get_all()
        found = []
        for reader in readers:
            if keyword in reader.full_name.lower() or keyword in reader.email.lower():
                found.append(reader)

        if not found:
            print('Ничего не найдено')
            return

        for reader in found:
            print(f'ID: {reader.id}, {reader.full_name} - {reader.email}')

