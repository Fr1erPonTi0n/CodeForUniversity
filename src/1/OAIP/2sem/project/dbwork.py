import re
import sqlite3
import datetime
import os

class BaseClass:
    def __init__(self):
        project_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(project_dir, "base.db")
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def reg_guests(self, name: str,
                   surname: str,
                   phone: int,
                   passport_num: str,
                   patronymic: str = None,
                   preferences: str = None) -> str:
        self.cursor.execute("""SELECT * FROM Guests WHERE name = ? AND surname = ? AND (patronymic = ? OR 
        (patronymic IS NULL AND ? IS NULL)) AND phone = ? AND passport_num = ?""", (name, surname,
                                                                                    patronymic, patronymic, phone,
                                                                                    passport_num))
        existing_guest = self.cursor.fetchone()

        if existing_guest:
            return "Гость уже был зарегистрирован!"
        reg_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.cursor.execute("""
                    INSERT INTO Guests (name, surname, patronymic, phone, passport_num, reg_date, preferences)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (name, surname, patronymic, phone, passport_num, reg_date, preferences))
        self.conn.commit()
        return "Гость успешно зарегистрирован!"

    def get_guest(self, guest_id: int) -> list:
        self.cursor.execute("SELECT * FROM Guests WHERE guest_id = ?", (guest_id,))
        guest = self.cursor.fetchone()
        return guest if guest else "Гость не найден!"

    def get_guests(self) -> list:
        self.cursor.execute("SELECT * FROM Guests")
        guests = self.cursor.fetchall()
        return guests

    def delete_guests(self, guest_id: int) -> str:
        self.cursor.execute("DELETE FROM Guests WHERE guest_id = ?", (guest_id,))
        self.conn.commit()
        return "Гость успешно удалён!" if self.cursor.rowcount > 0 else "Гость не найден!"

    def reg_worker(self,
                   name: str,
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
        self.cursor.execute("""SELECT * FROM Workers WHERE name = ? AND surname = ? AND (patronymic = ? OR (? IS NULL 
        AND patronymic IS NULL)) AND phone = ? AND passport_num = ? AND date_birth = ? AND position = ? 
        AND salary = ? AND place_residence = ? AND (work_schedule = ? OR (? IS NULL AND work_schedule IS NULL))""",
                            (name, surname, patronymic, patronymic, phone, passport_num, date_birth, position,
                             salary, place_residence, work_schedule, work_schedule))
        existing_worker = self.cursor.fetchone()
        if existing_worker:
            return "Работник уже был зарегистрирован!"

        hire_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.cursor.execute("""INSERT INTO Workers (name, surname, patronymic, phone, passport_num, date_birth, 
                            position, salary, place_residence, citizenship, hire_date, work_schedule)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
            name, surname, patronymic, phone, passport_num, date_birth, position,
            salary, place_residence, citizenship, hire_date, work_schedule))
        self.conn.commit()
        return "Работник успешно зарегистрирован!"

    def get_worker(self, worker_id: int) -> list:
        self.cursor.execute("SELECT * FROM Workers WHERE worker_id = ?", (worker_id,))
        worker = self.cursor.fetchone()
        return worker if worker else "Работник не найден!"

    def get_workers(self) -> list:
        self.cursor.execute("SELECT * FROM Workers")
        workers = self.cursor.fetchall()
        return workers

    def delete_worker(self, worker_id: int) -> str:
        self.cursor.execute("DELETE FROM Workers WHERE worker_id = ?", (worker_id,))
        self.conn.commit()
        return "Работник успешно удалён!" if self.cursor.rowcount > 0 else "Работник не найден!"

    def worker_cleaning(self, worker_id: int) -> list:
        cleans = self.cursor.execute("SELECT * FROM Cleanings WHERE worker_id = ?", (worker_id,)).fetchall()
        return cleans

    def start_cleaning(self,
                       worker_id: int,
                       room_id: int,
                       cleaning_date: str) -> str:
        self.cursor.execute("SELECT COUNT(*) FROM Workers WHERE worker_id = ?", (worker_id,))
        worker_exists = self.cursor.fetchone()[0] > 0

        self.cursor.execute("SELECT COUNT(*) FROM Rooms WHERE room_id = ?", (room_id,))
        room_exists = self.cursor.fetchone()[0] > 0

        if not worker_exists:
            return f"Работник с ID {worker_id} не найден."
        if not room_exists:
            return f"Комната с ID {room_id} не найдена."
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", cleaning_date):
            return "Неправильно введена дата: гггг-мм-дд."

        self.cursor.execute(
            "INSERT INTO Cleanings (room_id, worker_id, cleaning_date, status) VALUES (?, ?, ?, ?)",
            (room_id, worker_id, cleaning_date, 0)
        )
        self.conn.commit()

        return f"Уборка для комнаты {room_id} начата работником {worker_id} в {cleaning_date}."

    def end_cleaning(self,
                     worker_id: int,
                     room_id: int) -> str:
        self.cursor.execute("SELECT COUNT(*) FROM Workers WHERE worker_id = ?", (worker_id,))
        worker_exists = self.cursor.fetchone()[0] > 0

        self.cursor.execute("SELECT COUNT(*) FROM Rooms WHERE room_id = ?", (room_id,))
        room_exists = self.cursor.fetchone()[0] > 0

        if not worker_exists:
            return f"Работник с ID {worker_id} не найден."
        if not room_exists:
            return f"Комната с ID {room_id} не найдена."

        self.cursor.execute(
            "UPDATE Cleanings SET status = ? WHERE worker_id = ? AND room_id = ? AND status = ?",
            (1, worker_id, room_id, 0)
        )
        self.conn.commit()

        if self.cursor.rowcount == 0:
            return f"Активная уборка для комнаты {room_id} работником {worker_id} не найдена."

        return f"Уборка для комнаты {room_id} завершена работником {worker_id}."

    def add_room(self,
                 room_num: int,
                 room_type: str,
                 price_day: int) -> str:
        self.cursor.execute("SELECT * FROM Rooms WHERE room_num = ?", (room_num,))
        existing_room = self.cursor.fetchone()
        if existing_room:
            return "Комната уже была зарегистрирована!"
        self.cursor.execute("""INSERT INTO Rooms (room_num, room_type, price_day) 
                            VALUES (?, ?, ?)""", (room_num, room_type, price_day))
        self.conn.commit()
        return "Комната успешно зарегистрирована!"

    def delete_room(self,
                    room_id: int) -> str:
        self.cursor.execute("DELETE FROM Rooms WHERE room_id = ?", (room_id,))
        self.conn.commit()
        return "Комната успешно удалена!" if self.cursor.rowcount > 0 else "Комната не найдена!"

    def get_room(self,
                 room_id: int) -> list:
        self.cursor.execute("SELECT * FROM Rooms WHERE room_id = ?", (room_id,))
        room = self.cursor.fetchone()
        return room if room else "Комната не найдена!"

    def get_rooms(self) -> list:
        self.cursor.execute("SELECT * FROM Rooms")
        rooms = self.cursor.fetchall()
        return rooms

    def reservation_room(self,
                         guest_id: int,
                         check_out_date: str,
                         check_in_date: str,
                         room_id: int = 0,
                         money: int = 0) -> str:
        guest = self.get_guest(guest_id)
        if isinstance(guest, str):
            return "Гость не найден!"

        if room_id == 0:
            self.cursor.execute("SELECT room_id FROM Rooms WHERE price_day <= ? AND status = 0", (money,))
            available_rooms = self.cursor.fetchall()
            if available_rooms:
                room_id = available_rooms[0][0]
            else:
                return "Нет доступных комнат по вашему бюджету."

        self.cursor.execute("SELECT * FROM Rooms WHERE room_id = ? AND status = 0",
                            (room_id,))
        room = self.cursor.fetchone()
        if not room:
            return "Комната занята!"

        self.cursor.execute(
            "SELECT check_in_date, check_out_date FROM Bookings WHERE room_id = ? AND (check_in_date <= ? "
            "AND check_out_date >= ?)",
            (room_id, check_out_date, check_in_date))

        dates = self.cursor.fetchone()
        if dates:
            return f"Комната занята в указанные даты {dates[0]} - {dates[1]}."

        total_price = int(self.cursor.execute("SELECT price_day FROM Rooms WHERE room_id = ?",
                                              (room_id,)).fetchone()[0] * (datetime.datetime.strptime(check_out_date,
                                                                                                      '%Y-%m-%d') -
                                                                           datetime.datetime.strptime(check_in_date,
                                                                                                      '%Y-%m-%d')).days)
        self.cursor.execute(
            "INSERT INTO Bookings (guest_id, room_id, check_in_date, check_out_date, total_price) VALUES "
            "(?, ?, ?, ?, ?)", (guest_id, room_id, check_in_date, check_out_date, total_price))
        self.cursor.execute("UPDATE Rooms SET status = 1 WHERE room_id = ?", (room_id,))
        self.conn.commit()
        return "Комната успешно забронирована."

    def rental_room(self, room_id: int) -> str:
        room = self.get_room(room_id)
        if isinstance(room, str):
            return room

        self.cursor.execute("SELECT status FROM Cleanings WHERE room_id = ? ORDER BY cleaning_date DESC LIMIT 1",
                            (room_id,))
        cleaning_status = self.cursor.fetchone()
        if cleaning_status and cleaning_status[0] == 0:
            self.cursor.execute("UPDATE Rooms SET status = 0 WHERE room_id = ?", (room_id,))
            self.conn.commit()
            return "Комната успешно сдана."
        return "Комната не может быть сдана, так как она в процессе уборки."

    def check_room(self, guest_id: int) -> dict or str:
        guest = self.get_guest(guest_id)
        if isinstance(guest, str):
            return guest

        self.cursor.execute("SELECT room_id, status FROM Bookings WHERE guest_id = ?", (guest_id,))
        bookings = self.cursor.fetchall()
        return {room_id: status for room_id, status in bookings}

    def check_rooms(self) -> str:

        self.cursor.execute("""UPDATE Bookings SET status = CASE WHEN EXISTS (SELECT 1 FROM Rooms 
                WHERE Rooms.room_id = Bookings.room_id AND Rooms.status != 0) THEN 1
                WHEN EXISTS (SELECT 1 FROM Cleanings WHERE Cleanings.room_id = Bookings.room_id 
                AND Cleanings.status != 0) THEN 1 ELSE 0 END""")

        self.conn.commit()

        return "Успешно обновлены статусы комнат."

    def get_bookings(self) -> list:
        self.cursor.execute("SELECT * FROM Bookings")
        bookings = self.cursor.fetchall()
        return bookings

    def add_service(self,
                    name: str,
                    price: int,
                    description: str = None) -> str:
        self.cursor.execute("SELECT * FROM Services WHERE name = ? AND price = ? AND description = ?",
                            (name, price, description))
        existing_service = self.cursor.fetchone()
        if existing_service:
            return "Услуга уже была зарегистрирована!"
        self.cursor.execute("""INSERT INTO Services (name, price, description) 
                            VALUES (?, ?, ?)""", (name, price, description))
        self.conn.commit()
        return "Услуга успешно зарегистрирована!"

    def delete_service(self, service_id: int) -> str:
        self.cursor.execute("DELETE FROM Services WHERE service_id = ?", (service_id,))
        self.conn.commit()
        return "Услуга успешно удалена!" if self.cursor.rowcount > 0 else "Услуга не найдена!"

    def get_services(self) -> list:
        self.cursor.execute("SELECT * FROM Services")
        services = self.cursor.fetchall()
        return services

    def get_service(self, service_id: int) -> list:
        self.cursor.execute("SELECT * FROM Services WHERE service_id = ?", (service_id,))
        service = self.cursor.fetchone()
        return service if service else "Услуга не найдена!"

    def get_guest_services(self) -> list:
        self.cursor.execute("SELECT * FROM GuestServices")
        guest_services = self.cursor.fetchall()
        return guest_services

    def check_service(self,
                      guest_id: int,
                      service_id: int,
                      quantity: int) -> str:
        guest = self.get_guest(guest_id)
        if isinstance(guest, str):
            return guest

        service = self.get_service(service_id)
        if isinstance(service, str):
            return service

        total_price = service[3] * quantity
        order_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.cursor.execute("INSERT INTO GuestServices (guest_id, service_id, order_date, quantity, price)"
                            "VALUES (?, ?, ?, ?, ?)", (guest_id, service_id, order_date, quantity, total_price))
        self.conn.commit()

        return f"Гость {guest[1]} {guest[2]} заказал {quantity} услуги {service[1]}. Общая стоимость: {total_price}."

    def data_selection_like(self, pattern: str) -> list:
        self.cursor.execute("SELECT * FROM Guests WHERE reg_date LIKE ?", (f"%{pattern}%",))
        return self.cursor.fetchall()

    def data_selection_between(self, start_price: int, end_price: int) -> list:
        self.cursor.execute("SELECT * FROM Rooms WHERE price_day BETWEEN ? AND ?", (start_price, end_price))
        return self.cursor.fetchall()

    def data_selection_nested_query(self, guest_id: int) -> list:
        self.cursor.execute("""
                SELECT * FROM Bookings
                WHERE guest_id = (SELECT guest_id FROM Guests WHERE guest_id = ?)
                """, (guest_id,))
        return self.cursor.fetchall()

    def data_selection_join(self, guest_id: int) -> list:
        self.cursor.execute("""
            SELECT Guests.name, Guests.surname, Rooms.room_num, Bookings.check_in_date, Bookings.check_out_date
            FROM Bookings
            JOIN Guests ON Bookings.guest_id = Guests.guest_id
            JOIN Rooms ON Bookings.room_id = Rooms.room_id
            WHERE Guests.guest_id = ?
        """, (guest_id,))
        return self.cursor.fetchall()
