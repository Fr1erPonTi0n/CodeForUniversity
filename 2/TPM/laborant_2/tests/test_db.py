import sqlite3
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from app.db import Database

class TestDatabase:
    @pytest.fixture
    def db(self):
        """Фикстура для создания временной БД в памяти"""
        database = Database(":memory:")
        database.connect()
        database.create_tables()
        return database
    
    @pytest.fixture
    def sample_user(self):
        """Фикстура с тестовыми данными пользователя"""
        return {
            "name": "Test User",
            "age": 18,
            "grade": "отлично"
        }
    
    @pytest.fixture
    def populated_db(self):
        """База данных с предзаполненными данными"""
        database = Database(":memory:")
        database.connect()
        database.create_tables()
        database.add_user("Евгеха", 19, "хорошо")
        database.add_user("Бобер", 17, "отлично")
        database.add_user("Асадбек", 20, "удовлетворительно")
        return database
    
    def test_con(self):
        pass