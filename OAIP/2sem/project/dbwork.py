import re
import sqlite3
import datetime


def connect_db():
    return sqlite3.connect('base.db')


class Guests:
    @staticmethod
    def reg_guests(name: str,
                   surname: str,
                   phone: int,
                   passport_num: str,
                   patronymic: str = None,
                   preferences: str = None) -> str:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                        SELECT * FROM Guests 
                        WHERE name = ? AND surname = ? AND 
                              (patronymic = ? OR (? IS NULL AND patronymic IS NULL)) AND
                              phone = ? AND passport_num = ?)
                    ''', (name, surname, patronymic, patronymic, phone, passport_num, preferences, preferences))
            existing_guest = cursor.fetchone()
            if existing_guest:
                return "Гость уже был зарегистрирован!"
            reg_date = datetime.datetime.now().strftime("%Y-%m-%d")
            cursor.execute('''
                        INSERT INTO Guests (name, surname, patronymic, phone, passport_num, reg_date, preferences)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (name, surname, patronymic, phone, passport_num, reg_date, preferences))
            conn.commit()
        return "Гость успешно зарегистрирован!"

    @staticmethod
    def get_guest(guest_id: int) -> list:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Guests WHERE guest_id = ?', (guest_id,))
            guest = cursor.fetchone()
        return guest if guest else "Гость не найден!"

    @staticmethod
    def get_guests() -> list:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Guests')
            guests = cursor.fetchall()
        return guests

    @staticmethod
    def delete_guests(guest_id: int) -> str:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM Guests WHERE guest_id = ?', (guest_id,))
            conn.commit()
        return "Гость успешно удалён!" if cursor.rowcount > 0 else "Гость не найден!"


class Workers:
    @staticmethod
    def reg_worker(name: str,
                   surname: str,
                   phone: int,
                   passport_num: str,
                   date_birth: str,
                   position: str,
                   salary: int,
                   place_residence: str,
                   citizenship: str,
                   patronymic: str = None,
                   work_schedule: str = None) -> str:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM Workers 
                              WHERE name = ? AND surname = ? AND (patronymic = ? OR (? IS NULL AND patronymic IS NULL)) 
                              phone = ? AND passport_num = ? AND date_birth = ? AND position = ? AND salary = ?
                              AND place_residence = ? AND (work_schedule = ? OR 
                              (? IS NULL AND work_schedule IS NULL))''', (
                              name, surname, patronymic, patronymic, phone, passport_num, date_birth, position,
                              salary, place_residence, work_schedule, work_schedule))
            existing_worker = cursor.fetchone()
            if existing_worker:
                return "Работник уже был зарегистрирован!"
            hire_date = datetime.datetime.now().strftime("%Y-%m-%d")
            cursor.execute('''INSERT INTO Workers (name, surname, patronymic, phone, passport_num, date_birth, position, 
                              salary, place_residence, citizenship, hire_date, work_schedule)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
                              name, surname, patronymic, phone, passport_num, date_birth, position,
                              salary, place_residence, citizenship, hire_date, work_schedule))
            conn.commit()
        return "Работник успешно зарегистрирован!"

    @staticmethod
    def get_worker(worker_id: int) -> list:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Workers WHERE worker_id = ?', (worker_id,))
            worker = cursor.fetchone()
        return worker if worker else "Работник не найден!"

    @staticmethod
    def get_workers() -> list:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Workers')
            workers = cursor.fetchall()
        return workers

    @staticmethod
    def delete_worker(worker_id: int) -> str:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM Guests WHERE guest_id = ?', (worker_id,))
            conn.commit()
        return "Работник успешно удалён!" if cursor.rowcount > 0 else "Работник не найден!"

    @staticmethod
    def worker_cleaning(worker_id: int) -> list:
        with connect_db() as conn:
            cursor = conn.cursor()
            cleans = cursor.execute('SELECT * FROM Cleanings WHERE worker_id = ?', (worker_id, )).fetchall()
        return cleans

    @staticmethod
    def start_cleaning(worker_id: int, 
                       room_id: int,
                       cleaning_date: str) -> str:
        with connect_db() as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM Workers WHERE worker_id = ?", (worker_id,))
            worker_exists = cursor.fetchone()[0] > 0

            cursor.execute("SELECT COUNT(*) FROM Rooms WHERE room_id = ?", (room_id,))
            room_exists = cursor.fetchone()[0] > 0

            if not worker_exists:
                return f"Работник с ID {worker_id} не найден."
            if not room_exists:
                return f"Комната с ID {room_id} не найдена."
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", cleaning_date):
                return 'Неправильно введена дата: гггг-мм-дд.'

            cursor.execute(
                "INSERT INTO Cleanings (room_id, worker_id, cleaning_date, status) VALUES (?, ?, ?, ?)",
                (room_id, worker_id, cleaning_date, 0)
            )
            conn.commit()

            return f"Уборка для комнаты {room_id} начата работником {worker_id} в {cleaning_date}."

    @staticmethod
    def end_cleaning(worker_id: int, 
                     room_id: int) -> str:
        with connect_db() as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM Workers WHERE worker_id = ?", (worker_id,))
            worker_exists = cursor.fetchone()[0] > 0

            cursor.execute("SELECT COUNT(*) FROM Rooms WHERE room_id = ?", (room_id,))
            room_exists = cursor.fetchone()[0] > 0

            if not worker_exists:
                return f"Работник с ID {worker_id} не найден."
            if not room_exists:
                return f"Комната с ID {room_id} не найдена."

            cursor.execute(
                "UPDATE Cleanings SET status = ? WHERE worker_id = ? AND room_id = ? AND status = ?",
                (1, worker_id, room_id, 0)
            )
            conn.commit()

            if cursor.rowcount == 0:
                return f"Активная уборка для комнаты {room_id} работником {worker_id} не найдена."

            return f"Уборка для комнаты {room_id} завершена работником {worker_id}."


class Rooms:
    @staticmethod
    def add_room(room_num: int,
                 room_type: str,
                 price_day: int) -> str:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM Rooms WHERE room_num = ?))''', (room_num,))
            existing_worker = cursor.fetchone()
            if existing_worker:
                return "Комната уже была зарегистрирована!"
            cursor.execute('''INSERT INTO Rooms (room_num, room_type, price_day) 
                                VALUES (?, ?, ?)''', (room_num, room_type, price_day))
            conn.commit()
        return "Комната успешно зарегистрирована!"

    @staticmethod
    def delete_room(room_id: int) -> str:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM Guests WHERE room_id = ?', (room_id,))
            conn.commit()
        return "Комната успешно удалена!" if cursor.rowcount > 0 else "Комната не найдена!"

    @staticmethod
    def get_room(room_id: int) -> list:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Guests WHERE room_id = ?', (room_id,))
            room = cursor.fetchone()
        return room if room else "Комната не найдена!"

    @staticmethod
    def get_rooms() -> list:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Rooms')
            rooms = cursor.fetchall()
        return rooms

    @staticmethod
    def reservation_room(guest_id: int,
                         check_out_date: str,
                         check_in_date: str,
                         money: int,
                         room_id: int = None) -> str:
        if Guests.get_guest(guest_id) is list and Rooms.get_room(room_id) is list:
            with connect_db() as conn:
                cursor = conn.cursor()
                if room_id is None:
                    cursor.execute("SELECT room_id FROM Rooms WHERE price_day <= ? AND status = 0", (money,))
                    available_rooms = cursor.fetchall()
                    if available_rooms:
                        room_id = available_rooms[0][0]
                    else:
                        return "Нет доступных комнат по вашему бюджету."
                cursor.execute("SELECT * FROM Rooms WHERE room_id = ? AND price_day <= ? AND status = 0",
                               (room_id, money))
                if cursor:
                    return "Не хватает денег на аренду комнаты или комната занята!"

                cursor.execute(
                    "SELECT check_in_date, check_out_date FROM Bookings WHERE room_id = ? AND (check_in_date <= ? "
                    "AND check_out_date >= ?)",
                    (room_id, check_in_date, check_in_date))

                dates = cursor.fetchone()
                if dates:
                    return f"Комната занята в указанные даты {dates[0]} - {dates[1]}."
                cursor.execute(
                    "INSERT INTO Bookings (guest_id, room_id, check_in_date, check_out_date) VALUES (?, ?, ?, ?)",
                    (guest_id, room_id, check_in_date, check_out_date))
                conn.commit()
                return "Комната успешно забронирована."
        return "Комната или гость нету в базе данных!"

    @staticmethod
    def rental_room(room_id: int) -> str:
        if Rooms.get_room(room_id) is list:
            with connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT status FROM Cleanings WHERE room_id = ? ORDER BY cleaning_date DESC LIMIT 1",
                               (room_id,))
                cleaning_status = cursor.fetchone()
                if cleaning_status and cleaning_status[0] == 1:
                    cursor.execute("UPDATE Rooms SET status = 0 WHERE room_id = ?", (room_id,))
                    conn.commit()
                    return "Комната успешно сдана."
                return "Комната не может быть сдана, так как она в процессе уборки."
        return "Комнаты нету в базе данных!"

    @staticmethod
    def check_room(guest_id: int) -> dict or str:
        if Guests.get_guest(guest_id) is list:
            with connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT room_id, status FROM Bookings WHERE guest_id = ?", (guest_id,))
                bookings = cursor.fetchall()
                return {room_id: status for room_id, status in bookings}
        return 'Гостя нету в базе данных!'

    @staticmethod
    def check_rooms() -> str:
        with connect_db() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                        UPDATE Rooms
                        SET status = (
                            CASE 
                                WHEN MAX(Cleanings.status) = 1 THEN 1
                                WHEN MAX(Bookings.status) = 1 THEN 1
                                ELSE 0
                            END
                        )
                        FROM Rooms
                        LEFT JOIN Cleanings ON Rooms.room_id = Cleanings.room_id
                        LEFT JOIN Bookings ON Rooms.room_id = Bookings.room_id
                        GROUP BY Rooms.room_id
                    """)

            conn.commit()

            return 'Успешно обновлены статусы комнат.'


class Services:
    @staticmethod
    def add_service(name: str,
                    price: int,
                    description: str = None) -> str:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM Services WHERE name = ? AND price = ? AND description = ?))''',
                           (name, price, description))
            existing_worker = cursor.fetchone()
            if existing_worker:
                return "Услуга уже была зарегистрирована!"
            cursor.execute('''INSERT INTO Services (name, price, description) 
                                VALUES (?, ?, ?)''', (name, price, description))
            conn.commit()
        return "Услуга успешно зарегистрирована!"

    @staticmethod
    def delete_service(service_id: int) -> str:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM Guests WHERE service_id = ?', (service_id,))
            conn.commit()
        return "Услуга успешно удалена!" if cursor.rowcount > 0 else "Услуга не найдена!"

    @staticmethod
    def get_services() -> list:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Rooms')
            services = cursor.fetchall()
        return services

    @staticmethod
    def get_service(service_id: int) -> list:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Services WHERE service_id = ?', (service_id,))
            service = cursor.fetchone()
        return service if service else "Услуга не найдена!"

    @staticmethod
    def check_service(guest_id: int,
                      service_id: int,
                      quantity: int) -> str:
        if Guests.get_guest(guest_id) is list and Services.get_service(service_id):
            with connect_db() as conn:
                cursor = conn.cursor()

                cursor.execute("SELECT * FROM Guests WHERE guest_id = ?", (guest_id,))
                guest = cursor.fetchone()

                cursor.execute("SELECT * FROM Services WHERE service_id = ?", (service_id,))
                service = cursor.fetchone()

                total_price = service[3] * quantity
                return f"Гость {guest[1]} {guest[2]} заказал {quantity} услуги '{service[1]}'. Общая стоимость: " \
                       f"{total_price}."
        return 'Гость или услуги не были найдены!'


class Other:
    @staticmethod
    def one():
        pass

    @staticmethod
    def two():
        pass

    @staticmethod
    def three():
        pass

    @staticmethod
    def four():
        pass
