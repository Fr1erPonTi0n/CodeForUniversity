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
                return "Гость уже был зарегестрирован!"
            reg_date = datetime.datetime.now().isoformat()
            cursor.execute('''
                        INSERT INTO Guests (name, surname, patronymic, phone, passport_num, reg_date, preferences)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (name, surname, patronymic, phone, passport_num, reg_date, preferences))
            conn.commit()
        return "Гость успешно зарегестирован!"

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
                   phone: str,
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
            hire_date = datetime.datetime.now().isoformat()
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
                "INSERT INTO Cleanings (room_id, worker_id, cleaning_date, status) VALUES (?, ?, datetime('now'), ?)",
                (room_id, worker_id, 0)
            )
            conn.commit()

            return f"Уборка для комнаты {room_id} начата работником {worker_id}."

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

