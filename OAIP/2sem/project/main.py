from dbwork import *


def guests_menu():
    guests_var = int(input("""Выберите нужный пункт для работы с гостями:
        1) Регистрация гостя (имя, фамилия, телефон, паспортный номер, фамилия, предпочтения)
        2) Узнать гостя по его id
        3) Получить список всех гостей
        4) Удалить с базы данных гостя\n>\t"""))

    headers = ["ID", "Имя", "Фамилия", "Отчество", "Телефон", "Паспорт", "Дата", "Предпочтения"]

    if guests_var == 1:
        print(Guests.reg_guests(
            name=input('Введите имя:\t'),
            surname=input('Введите фамилию:\t'),
            patronymic=input('Введите отчество:\t'),
            phone=int(input('Введите номер:\t')),
            passport_num=input('Введите паспортный номер:\t'),
            preferences=input('Введите пожелание гостя, если надо:\t')
        ))
    elif guests_var == 2:
        guest = Guests.get_guest(int(input('Введите ID гостя: ')))
        if guest:
            print("\t|\t".join(headers))
            print("\t|\t".join(str(x) for x in guest))
        else:
            print("Гость с таким ID не найден")
    elif guests_var == 3:
        print("\t|\t".join(headers))
        for g in Guests.get_guests():
            print("\t|\t".join(str(x) for x in g))
    elif guests_var == 4:
        print(Guests.delete_guests(guest_id=int(input('Введите ID гостя:'))))
    else:
        print("Неверный выбор пункта меню")

def workers_menu():
    workers_var = int(input("""Выберите нужный пункт для работы с работниками:
        1) Регистрация работника (имя, фамилия, телефон, паспортный номер, день рождения, должность, оклад, место жительства, гражданство, фамилия, график работы)
        2) Узнать работника по его id
        3) Получить список всех работников
        4) Удалить с базы данных работника
        5) Узнать чем занят работник
        6) Назначить работнику уборку
        7) Прекратить уборку работника\n>\t"""))

    headers_1 = ["ID", "Имя", "Фамилия", "Отчество", "Гражданство", "Паспорт", "День рождения", "Должность", "Номер телефона", "Оклад", "График работы", "Отработаные часы", "Место жительства"]
    headers_2 = ["ID", "ID Комнаты", "ID Работника", "Дата уборки", "Статус уборки"]

    if workers_var == 1:
        print(Workers.reg_worker(name=input('Введите имя:\t'),
             surname=input('Введите фамилию:\t'),
             patronymic=input('Введите отчество:\t'),
             phone=int(input('Введите телефона:\t')),
             passport_num=input('Введите паспортный номер:\t'),
             date_birth=input('Введите день рождение:\t'),
             position=input('Введите должность:\t'),
             salary=int(input('Введите оклад:\t')),
             place_residence=input('Введите место жительства:\t'),
             citizenship=input('Введите гражданство:\t'),
             work_schedule=input('Введите график работы:\t')
        ))

    elif workers_var == 2:
        worker = Workers.get_worker(int(input('Введите ID гостя:\t')))
        if worker:
            print("\t|\t".join(headers_1))
            print("\t|\t".join(str(x) for x in worker))
        else:
            print("Работник с таким ID не найден")
    elif workers_var == 3:
        print("\t|\t".join(headers_1))
        for w in Workers.get_workers():
            print("\t|\t".join(str(x) for x in w))
    elif workers_var == 4:
        print(Workers.delete_worker(worker_id=int(input('Введите ID работника:\t'))))
    elif workers_var == 5:
        worker = Workers.worker_cleaning(int(input('Введите ID гостя:\t')))
        if worker:
            print("\t|\t".join(headers_2))
            print("\t|\t".join(str(x) for x in worker))
        else:
            print("Уборка/и работника с таким ID не найден/ы")
    elif workers_var == 6:
        print(Workers.start_cleaning(worker_id=int(input('Введите ID работника:\t')),
                               room_id=int(input('Введите ID комнаты:\t')),
                               cleaning_date=input('Введите дату уборки:\t')))
    elif workers_var == 7:
        print(Workers.end_cleaning(worker_id=int(input('Введите ID работника:\t')),
                                   room_id=int(input('Введите ID комнаты'))))
    else:
        print("Неверный выбор пункта меню")

def rooms_menu():
    rooms_var = int(input("""Выберите нужный пункт для работы с гостями:
        1) Регистрация комнаты (номер комнаты, тип комнаты, стоимость комнаты за один день)
        2) Удаления комнаты по id
        3) Получение информации о комнате по id
        4) Получение информации о всех комнат
        5) Аренда комнаты (id гостя, со сколько по скольки, деньги, id комнаты)
        6) Сдача комнаты после аренды (id комнаты)
        7) Проверка комнаты по id комнаты
        8) Проверка всех комнат\n>\t"""))

    headers_1 = ['ID', 'Номер комнаты', 'Тип комнаты', 'Стоимость в 1 день', 'Статус']

    if rooms_var == 1:
        print(Rooms.add_room(room_num=int(input('Введите номер комнаты:\t')),
                             room_type=input('Введите тип комнаты:\t'),
                             price_day=int(input('Введите стоимость комнаты за один день:\t'))
                             ))
    elif rooms_var == 2:
        print(Rooms.delete_room(room_id=int(input('Введите ID комнаты:\t'))))
    elif rooms_var == 3:
        room = Rooms.get_room(int(input('Введите ID комнаты:\t')))
        if room:
            print("\t|\t".join(headers_1))
            print("\t|\t".join(str(x) for x in room))
        else:
            print("Комната с таким ID не найдена")
    elif rooms_var == 4:
        rooms = Rooms.get_rooms()
        if rooms:
            print("\t|\t".join(headers_1))
            for room in rooms:
                print("\t|\t".join(str(x) for x in room))
        else:
            print("Нет зарегистрированных комнат")
    elif rooms_var == 5:
        print(Rooms.reservation_room(
            guest_id=int(input('Введите ID гостя:\t')),
            check_out_date=input('Введите дату выезда (ГГГГ-ММ-ДД):\t'),
            check_in_date=input('Введите дату заезда (ГГГГ-ММ-ДД):\t'),
            money=int(input('Введите бюджет:\t')),
            room_id=int(input('Введите ID комнаты (или 0 для автоматического выбора):\t')) or None))
    elif rooms_var == 6:
        print(Rooms.rental_room(room_id=int(input('Введите ID комнаты:\t'))))
    elif rooms_var == 7:
        result = Rooms.check_room(guest_id=int(input('Введите ID гостя:\t')))
        if isinstance(result, dict):
            for room_id, status in result.items():
                print(f"Комната {room_id}: {'Занята' if status else 'Свободна'}")
        else:
            print(result)
    elif rooms_var == 8:
        print(Rooms.check_rooms())
    else:
        print("Неверный выбор пункта меню")


def services_menu():
    service_var = int(input("""Выберите нужный пункт для работы с услугами:
        1) Добавить услугу (название, цена, описание)
        2) Получить информацию об услуге по ID
        3) Получить список всех услуг
        4) Удалить услугу
        5) Заказать услугу для гостя\n>\t"""))

    headers = ['ID услуги', 'Название', 'Цена', 'Описание']

    if service_var == 1:
        print(Services.add_service(name=input('Введите название услуги:\t'),
            price=int(input('Введите цену услуги:\t')),
            description=input('Введите описание услуги (необязательно):\t') or None
        ))
    elif service_var == 2:
        service = Services.get_service(int(input('Введите ID услуги:\t')))
        if service:
            print("\t|\t".join(headers))
            print("\t|\t".join(str(x) for x in service))
        else:
            print('Услуга не найдена!')
    elif service_var == 3:
        services = Services.get_services()
        if services:
            print("\t|\t".join(headers))
            for service in services:
                print("\t|\t".join(str(x) for x in service))
        else:
            print("Нет доступных услуг")
    elif service_var == 4:
        print(Services.delete_service(
            service_id=int(input('Введите ID услуги для удаления:\t'))
        ))
    elif service_var == 5:
        print(Services.check_service(
            guest_id=int(input('Введите ID гостя:\t')),
            service_id=int(input('Введите ID услуги:\t')),
            quantity=int(input('Введите количество:\t'))
        ))
    else:
        print("Неверный выбор пункта меню")


def other_menu():
    other_var = int(input("""Выберите нужный пункт для работы с гостями:
            1)Корректировка данных
            2)Выборка данных (LIKE)
            3)Выборка данных (BETWEEN)
            4)Выборка данных (Вложенный запрос)
            5)Выборка данных (JOIN)\n>\t"""))
    if other_var == 1:
        Other.one()
    elif other_var == 2:
        Other.two()
    elif other_var == 3:
        Other.three()
    elif other_var == 4:
        Other.four()
    elif other_var == 5:
        Other.five()


if __name__ == '__main__':
    while True:
        var = int(input("""Выберите нужный пункт для управления меню гостиницы "Уют":
        1) Гости
        2) Рабочие
        3) Комнаты
        4) Услуги
        5) Другое (Запросы SQL)\n>\t"""))
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
