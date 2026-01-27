import sqlite3
import os
from typing import List, Optional, Dict, Any


class Database:
    def __init__(self, db_path: str = "students.db"):
        project_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(project_dir, db_path)
        self.init_db()
    
    def init_db(self):
        """Инициализация базы данных"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL
                )
            ''')
            conn.commit()
    
    def add_student(self, name: str, age: int, grade: str) -> int:
        """Добавление студента"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
                (name, age, grade)
            )
            conn.commit()
            return cursor.lastrowid
    
    def get_all_students(self) -> List[Dict[str, Any]]:
        """Получение всех студентов"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            return [dict(row) for row in cursor.fetchall()]
    
    def update_student(self, student_id: int, name: str, age: int, grade: str) -> bool:
        """Обновление студента"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE students SET name=?, age=?, grade=? WHERE id=?",
                (name, age, grade, student_id)
            )
            conn.commit()
            return cursor.rowcount > 0
    
    def delete_student(self, student_id: int) -> bool:
        """Удаление студента"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    def get_student(self, student_id: int) -> Optional[Dict[str, Any]]:
        """Получение студента по ID"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
