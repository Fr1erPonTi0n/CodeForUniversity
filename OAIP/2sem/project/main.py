from dbwork import *
import sys


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число!")


def guests_menu():
    try:
        guests_var = input_int("""Выберите нужный пункт для работы с гостями:
        1) Регистрация гостя (имя, фамилия, телефон, паспортный номер, отчество, предпочтения)
        2) Узнать гостя по его id
        3) Получить список всех гостей
        4) Удалить с базы данных гостя\n>\t""")

        headers = ["ID", "Имя", "Фамилия", "Отчество", "Телефон", "Паспорт", "Дата", "Предпочтения"]

        if guests_var == 1:
            print(Guests.reg_guests(
                name=input('Введите имя:\t'),
                surname=input('Введите фамилию:\t'),
                patronymic=input('Введите отчество (если есть):\t') or None,
                phone=input_int('Введите номер телефона:\t'),
                passport_num=input('Введите паспортный номер:\t'),
                preferences=input('Введите пожелание гостя (если есть):\t') or None
            ))
        elif guests_var == 2:
            guest = Guests.get_guest(input_int('Введите ID гостя:\t'))
            if isinstance(guest, list):
                print("\t|\t".join(headers))
                print("\t|\t".join(str(x) if x is not None else "" for x in guest))
            else:
                print(guest)
        elif guests_var == 3:
            guests = Guests.get_guests()
            if guests:
                print("\t|\t".join(headers))
                for g in guests:
                    print("\t|\t".join(str(x) if x is not None else "" for x in g))
            else:
                print("Нет зарегистрированных гостей")
        elif guests_var == 4:
            print(Guests.delete_guests(guest_id=input_int('Введите ID гостя:\t')))
        else:
            print("Неверный выбор пункта меню")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def workers_menu():
    try:
        workers_var = input_int("""Выберите нужный пункт для работы с работниками: 
        1) Регистрация работника 
        2) Узнать работника по его id 
        3) Получить список всех работников
        4) Удалить с базы данных работника 
        5) Узнать чем занят работник 
        6) Назначить работнику уборку 
        7) Прекратить уборку работника\n>\t""")

        headers_1 = ["ID", "Имя", "Фамилия", "Отчество", "Гражданство", "Паспорт", "День рождения",
                     "Должность", "Телефон", "Оклад", "График работы", "Место жительства", "Дата найма"]
        headers_2 = ["ID", "ID Комнаты", "ID Работника", "Дата уборки", "Статус уборки"]

        if workers_var == 1:
            print(Workers.reg_worker(
                name=input('Введите имя:\t'),
                surname=input('Введите фамилию:\t'),
                patronymic=input('Введите отчество (если есть):\t') or None,
                phone=input_int('Введите номер телефона:\t'),
                passport_num=input('Введите паспортный номер:\t'),
                date_birth=input('Введите дату рождения (ГГГГ-ММ-ДД):\t'),
                position=input('Введите должность:\t'),
                salary=input_int('Введите оклад:\t'),
                place_residence=input('Введите место жительства:\t'),
                citizenship=input('Введите гражданство:\t'),
                work_schedule=input('Введите график работы (если есть):\t') or None
            ))
        elif workers_var == 2:
            worker = Workers.get_worker(input_int('Введите ID работника:\t'))
            if isinstance(worker, list):
                print("\t|\t".join(headers_1))
                print("\t|\t".join(str(x) if x is not None else "" for x in worker))
            else:
                print(worker)
        elif workers_var == 3:
            workers = Workers.get_workers()
            if workers:
                print("\t|\t".join(headers_1))
                for w in workers:
                    print("\t|\t".join(str(x) if x is not None else "" for x in w))
            else:
                print("Нет зарегистрированных работников")
        elif workers_var == 4:
            print(Workers.delete_worker(worker_id=input_int('Введите ID работника:\t')))
        elif workers_var == 5:
            cleans = Workers.worker_cleaning(input_int('Введите ID работника:\t'))
            if isinstance(cleans, list) and cleans:
                print("\t|\t".join(headers_2))
                for clean in cleans:
                    print("\t|\t".join(str(x) for x in clean))
            else:
                print("Уборки не найдены или работник не существует")
        elif workers_var == 6:
            print(Workers.start_cleaning(
                worker_id=input_int('Введите ID работника:\t'),
                room_id=input_int('Введите ID комнаты:\t'),
                cleaning_date=input('Введите дату уборки (ГГГГ-ММ-ДД):\t')
            ))
        elif workers_var == 7:
            print(Workers.end_cleaning(
                worker_id=input_int('Введите ID работника:\t'),
                room_id=input_int('Введите ID комнаты:\t')
            ))
        else:
            print("Неверный выбор пункта меню")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def rooms_menu():
    try:
        rooms_var = input_int("""Выберите нужный пункт для работы с комнатами:
            1) Регистрация комнаты
            2) Удаление комнаты по id
            3) Получение информации о комнате по id
            4) Получение информации о всех комнатах
            5) Аренда комнаты
            6) Сдача комнаты после аренды
            7) Проверка комнаты по id гостя
            8) Проверка всех комнат\n>\t""")

        headers_1 = ['ID', 'Номер комнаты', 'Тип комнаты', 'Стоимость в день', 'Статус']
        headers_3 = ['ID', 'ID Гостя', 'ID Комнаты', 'Дата заезда', 'Дата выезда', 'Статус', 'Стоимость']

        if rooms_var == 1:
            print(Rooms.add_room(
                room_num=input_int('Введите номер комнаты:\t'),
                room_type=input('Введите тип комнаты:\t'),
                price_day=input_int('Введите стоимость комнаты за день:\t')
            ))
        elif rooms_var == 2:
            print(Rooms.delete_room(room_id=input_int('Введите ID комнаты:\t')))
        elif rooms_var == 3:
            room = Rooms.get_room(input_int('Введите ID комнаты:\t'))
            if isinstance(room, list):
                print("\t|\t".join(headers_1))
                print("\t|\t".join(str(x) for x in room))
            else:
                print(room)
        elif rooms_var == 4:
            rooms = Rooms.get_rooms()
            if rooms:
                print("\t|\t".join(headers_1))
                for room in rooms:
                    print("\t|\t".join(str(x) for x in room))
            else:
                print("Нет зарегистрированных комнат")
        elif rooms_var == 5:
            guest_id = int(input('Введите ID гостя:\t'))
            check_in_date = input('Введите дату заезда (ГГГГ-ММ-ДД):\t')
            check_out_date = input('Введите дату выезда (ГГГГ-ММ-ДД):\t')
            room_id = int(input('Введите ID комнаты (или 0 для автоматического выбора):\t'))

            if room_id == 0:
                money = int(input('Введите бюджет:\t'))
                print(Rooms.reservation_room(guest_id=guest_id,
                                             check_in_date=check_in_date,
                                             check_out_date=check_out_date,
                                             money=money))
            else:
                print(Rooms.reservation_room(guest_id=guest_id,
                                             check_in_date=check_in_date,
                                             check_out_date=check_out_date,
                                             room_id=room_id))
        elif rooms_var == 6:
            print(Rooms.rental_room(room_id=input_int('Введите ID комнаты:\t')))
        elif rooms_var == 7:
            result = Rooms.check_room(guest_id=input_int('Введите ID гостя:\t'))
            if isinstance(result, dict):
                for room_id, status in result.items():
                    print(f"Комната {room_id}: {'Занята' if status else 'Свободна'}")
            else:
                print(result)
        elif rooms_var == 8:
            print(Rooms.check_rooms())
        else:
            print("Неверный выбор пункта меню")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def services_menu():
    try:
        service_var = input_int("""Выберите нужный пункт для работы с услугами:
            1) Добавить услугу
            2) Получить информацию об услуге по ID
            3) Получить список всех услуг
            4) Удалить услугу
            5) Заказать услугу для гостя\n>\t""")

        headers = ['ID услуги', 'Название', 'Цена', 'Описание']

        if service_var == 1:
            print(Services.add_service(
                name=input('Введите название услуги:\t'),
                price=input_int('Введите цену услуги:\t'),
                description=input('Введите описание услуги (необязательно):\t') or None
            ))
        elif service_var == 2:
            service = Services.get_service(input_int('Введите ID услуги:\t'))
            if isinstance(service, list):
                print("\t|\t".join(headers))
                print("\t|\t".join(str(x) if x is not None else "" for x in service))
            else:
                print(service)
        elif service_var == 3:
            services = Services.get_services()
            if services:
                print("\t|\t".join(headers))
                for service in services:
                    print("\t|\t".join(str(x) if x is not None else "" for x in service))
            else:
                print("Нет доступных услуг")
        elif service_var == 4:
            print(Services.delete_service(
                service_id=input_int('Введите ID услуги для удаления:\t')
            ))
        elif service_var == 5:
            print(Services.check_service(
                guest_id=input_int('Введите ID гостя:\t'),
                service_id=input_int('Введите ID услуги:\t'),
                quantity=input_int('Введите количество:\t')
            ))
        else:
            print("Неверный выбор пункта меню")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def other_menu():
    try:
        other_var = input_int("""Выберите нужный пункт для работы с данными:
                1) Выборка данных (LIKE)
                2) Выборка данных (BETWEEN)
                3) Выборка данных (Вложенный запрос)
                4) Выборка данных (JOIN)\n>\t""")

        headers_1 = ["ID", "Имя", "Фамилия", "Отчество", "Телефон", "Паспорт", "Дата", "Предпочтения"]
        headers_2 = ['ID', 'Номер комнаты', 'Тип комнаты', 'Стоимость в день', 'Статус']
        headers_3 = ['ID', 'ID Гостя', 'ID Комнаты', 'Дата заезда', 'Дата выезда', 'Статус', 'Стоимость']
        headers_4 = ['Имя', 'Фамилия', 'Номер комнаты', 'Дата заезда', 'Дата выезда']

        if other_var == 1:
            output = Other.data_selection_like(input('Введите шаблон для дат регистрации (например 2023%):\t'))
            if output:
                print("\t|\t".join(headers_1))
                for elem in output:
                    print("\t|\t".join(str(x) if x is not None else "" for x in elem))
            else:
                print('Ничего не найдено!')
        elif other_var == 2:
            output = Other.data_selection_between(
                start_price=input_int('Введите минимальную цену:\t'),
                end_price=input_int('Введите максимальную цену:\t')
            )
            if output:
                print("\t|\t".join(headers_2))
                for elem in output:
                    print("\t|\t".join(str(x) for x in elem))
            else:
                print('Ничего не найдено!')
        elif other_var == 3:
            output = Other.data_selection_nested_query(input_int('Введите ID гостя:\t'))
            if output:
                print("\t|\t".join(headers_3))
                for elem in output:
                    print("\t|\t".join(str(x) for x in elem))
            else:
                print('Ничего не найдено!')
        elif other_var == 4:
            output = Other.data_selection_join(input_int('Введите ID гостя:\t'))
            if output:
                print("\t|\t".join(headers_4))
                for elem in output:
                    print("\t|\t".join(str(x) for x in elem))
            else:
                print('Ничего не найдено!')
        else:
            print("Неверный выбор пункта меню")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    while True:
        try:
            var = input_int("""Выберите нужный пункт для управления меню гостиницы "Уют":
            1) Гости
            2) Работники
            3) Комнаты
            4) Услуги
            5) Другое (Запросы SQL)
            6) Выход\n>\t""")

            if var == 1:
                guests_menu()
            elif var == 2:
                workers_menu()
            elif var == 3:
                rooms_menu()
            elif var == 4:
                services_menu()
            elif var == 5:
                other_menu()
            elif var == 6:
                print("Выход из программы...")
                sys.exit(0)
            else:
                print("Неверный выбор пункта меню")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
