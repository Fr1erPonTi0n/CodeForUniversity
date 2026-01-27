from tabulate import tabulate
from dbwork import *
import sys

database = BaseClass()


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число!")


def print_table(headers, data):
    if isinstance(data, (list, tuple)):
        if all(isinstance(row, (list, tuple)) for row in data) and data:
            print(tabulate(data, headers=headers, tablefmt="grid", stralign="center"))
        elif data:
            print(tabulate([data], headers=headers, tablefmt="grid", stralign="center"))
    else:
        print(data)


def guests_menu():
    try:
        guests_var = input_int("""Выберите нужный пункт для работы с гостями:
        1) Регистрация гостя (имя, фамилия, телефон, паспортный номер, отчество, предпочтения)
        2) Узнать гостя по его id
        3) Получить список всех гостей
        4) Удалить с базы данных гостя
        5) Выход\n>\t""")

        headers = ["ID", "Имя", "Фамилия", "Отчество", "Телефон", "Паспорт", "Дата", "Предпочтения"]

        if guests_var == 1:
            print(database.reg_guests(
                name=input('Введите имя:\t'),
                surname=input('Введите фамилию:\t'),
                patronymic=input('Введите отчество (если есть):\t') or None,
                phone=input_int('Введите номер телефона:\t'),
                passport_num=input('Введите паспортный номер:\t'),
                preferences=input('Введите пожелание гостя (если есть):\t') or None
            ))
        elif guests_var == 2:
            guest = database.get_guest(input_int('Введите ID гостя:\t'))
            print_table(headers, guest)
        elif guests_var == 3:
            guests = database.get_guests()
            print_table(headers, guests)
        elif guests_var == 4:
            print(database.delete_guests(guest_id=input_int('Введите ID гостя:\t')))
        elif guests_var == 5:
            return
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
        7) Прекратить уборку работника
        8) Выход\n>\t""")

        headers_1 = ["ID", "Имя", "Фамилия", "Отчество", "Гражданство", "Паспорт", "День рождения",
                     "Должность", "Телефон", "Оклад", "График работы", "Место жительства", "Дата найма"]
        headers_2 = ["ID", "ID Комнаты", "ID Работника", "Дата уборки", "Статус уборки"]

        if workers_var == 1:
            print(database.reg_worker(
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
            worker = database.get_worker(input_int('Введите ID работника:\t'))
            print_table(headers_1, worker)
        elif workers_var == 3:
            workers = database.get_workers()
            print_table(headers_1, workers)
        elif workers_var == 4:
            print(database.delete_worker(worker_id=input_int('Введите ID работника:\t')))
        elif workers_var == 5:
            cleans = database.worker_cleaning(input_int('Введите ID работника:\t'))
            print_table(headers_2, cleans)
        elif workers_var == 6:
            print(database.start_cleaning(
                worker_id=input_int('Введите ID работника:\t'),
                room_id=input_int('Введите ID комнаты:\t'),
                cleaning_date=input('Введите дату уборки (ГГГГ-ММ-ДД):\t')
            ))
        elif workers_var == 7:
            print(database.end_cleaning(
                worker_id=input_int('Введите ID работника:\t'),
                room_id=input_int('Введите ID комнаты:\t')
            ))
        elif workers_var == 8:
            return
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
        8) Проверка всех комнат
        9) Получение информации о всех бронирований
        10) Выход\n>\t""")

        headers_1 = ['ID', 'Номер комнаты', 'Тип комнаты', 'Стоимость в день', 'Статус']
        headers_2 = ['ID', 'ID Гостя', 'ID Комнаты', 'Дата заезда', 'Дата выезда', 'Статус', 'Общая цена']

        if rooms_var == 1:
            print(database.add_room(
                room_num=input_int('Введите номер комнаты:\t'),
                room_type=input('Введите тип комнаты:\t'),
                price_day=input_int('Введите стоимость комнаты за день:\t')
            ))
        elif rooms_var == 2:
            print(database.delete_room(room_id=input_int('Введите ID комнаты:\t')))
        elif rooms_var == 3:
            room = database.get_room(input_int('Введите ID комнаты:\t'))
            print_table(headers_1, room)
        elif rooms_var == 4:
            rooms = database.get_rooms()
            print_table(headers_1, rooms)
        elif rooms_var == 5:
            guest_id = int(input('Введите ID гостя:\t'))
            check_in_date = input('Введите дату заезда (ГГГГ-ММ-ДД):\t')
            check_out_date = input('Введите дату выезда (ГГГГ-ММ-ДД):\t')
            room_id = int(input('Введите ID комнаты (или 0 для автоматического выбора):\t'))

            if room_id == 0:
                money = int(input('Введите бюджет:\t'))
                print(database.reservation_room(guest_id=guest_id,
                                             check_in_date=check_in_date,
                                             check_out_date=check_out_date,
                                             money=money))
            else:
                print(database.reservation_room(guest_id=guest_id,
                                             check_in_date=check_in_date,
                                             check_out_date=check_out_date,
                                             room_id=room_id))
        elif rooms_var == 6:
            print(database.rental_room(room_id=input_int('Введите ID комнаты:\t')))
        elif rooms_var == 7:
            result = database.check_room(guest_id=input_int('Введите ID гостя:\t'))
            if isinstance(result, dict):
                table_data = [[k, "Занята" if v else "Свободна"] for k, v in result.items()]
                print_table(["ID Комнаты", "Статус"], table_data)
            else:
                print(result)
        elif rooms_var == 8:
            print(database.check_rooms())
        elif rooms_var == 9:
            bookings = database.get_bookings()
            print_table(headers_2, bookings)
        elif rooms_var == 10:
            return
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
        5) Заказать услугу для гостя
        6) Получение информации по заказанным услугам
        7) Выход\n>\t""")

        headers_1 = ['ID', 'Название', 'Цена', 'Описание']
        headers_2 = ['ID', 'ID гостя', 'ID услуги', 'Дата заказа', 'Количество', 'Общяя стоимость']

        if service_var == 1:
            print(database.add_service(
                name=input('Введите название услуги:\t'),
                price=input_int('Введите цену услуги:\t'),
                description=input('Введите описание услуги (необязательно):\t') or None
            ))
        elif service_var == 2:
            service = database.get_service(input_int('Введите ID услуги:\t'))
            print_table(headers_1, service)
        elif service_var == 3:
            services = database.get_services()
            print_table(headers_1, services)
        elif service_var == 4:
            print(database.delete_service(
                service_id=input_int('Введите ID услуги для удаления:\t')
            ))
        elif service_var == 5:
            print(database.check_service(
                guest_id=input_int('Введите ID гостя:\t'),
                service_id=input_int('Введите ID услуги:\t'),
                quantity=input_int('Введите количество:\t')
            ))
        elif service_var == 6:
            guest_services = database.get_guest_services()
            print_table(headers_2, guest_services)
        elif service_var == 7:
            return
        else:
            print("Неверный выбор пункта меню")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def other_menu():
    try:
        other_var = input_int("""Выберите нужный пункт для работы с данными:
        1) Сортировка по регистрации дат (LIKE)
        2) Сортировка цен на комнаты (BETWEEN)
        3) Вывести список арендованных комнат гостем (Вложенный запрос)
        4) Данные о госте (JOIN)
        5) Выход\n>\t""")

        headers_1 = ["ID", "Имя", "Фамилия", "Отчество", "Телефон", "Паспорт", "Дата", "Предпочтения"]
        headers_2 = ['ID', 'Номер комнаты', 'Тип комнаты', 'Стоимость в день', 'Статус']
        headers_3 = ['ID', 'ID Гостя', 'ID Комнаты', 'Дата заезда', 'Дата выезда', 'Статус', 'Стоимость']
        headers_4 = ['Имя', 'Фамилия', 'Номер комнаты', 'Дата заезда', 'Дата выезда']

        if other_var == 1:
            output = database.data_selection_like(input('Введите шаблон для дат регистрации (например 2023%):\t'))
            print_table(headers_1, output)
        elif other_var == 2:
            output = database.data_selection_between(
                start_price=input_int('Введите минимальную цену:\t'),
                end_price=input_int('Введите максимальную цену:\t')
            )
            print_table(headers_2, output)
        elif other_var == 3:
            output = database.data_selection_nested_query(input_int('Введите ID гостя:\t'))
            print_table(headers_3, output)
        elif other_var == 4:
            output = database.data_selection_join(input_int('Введите ID гостя:\t'))
            print_table(headers_4, output)
        elif other_var == 5:
            return
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
