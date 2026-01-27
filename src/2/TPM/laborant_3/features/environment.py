import sys
import os
import tempfile
import time
from PyQt6.QtWidgets import QApplication

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db import Database


class TestContext:
    """Контекст для тестирования"""
    def __init__(self):
        self.app = None
        self.main_window = None
        self.current_window = None
        self.temp_db_path = None
        self.db = None
        self.test_data = []

def before_all(context):
    """Выполняется перед всеми тестами"""
    context.test_context = TestContext()
    context.test_context.temp_db_path = tempfile.NamedTemporaryFile(
        suffix='.db', delete=False
    ).name
    if QApplication.instance() is None:
        context.test_context.app = QApplication([])
    else:
        context.test_context.app = QApplication.instance()

def before_scenario(context, scenario):
    """Выполняется перед каждым сценарием"""
    if os.path.exists(context.test_context.temp_db_path):
        if hasattr(context.test_context, 'db') and context.test_context.db:
            if hasattr(context.test_context.db, 'close'):
                context.test_context.db.close()
        time.sleep(0.1)
        for _ in range(3):
            try:
                os.remove(context.test_context.temp_db_path)
                break
            except PermissionError:
                time.sleep(0.1)
    context.test_context.db = Database(context.test_context.temp_db_path)
    context.db = context.test_context.db

def after_scenario(context, scenario):
    """Выполняется после каждого сценария"""
    if hasattr(context, 'windows'):
        for window in context.windows:
            if hasattr(window, 'close'):
                window.close()
    if hasattr(context, 'temp_files'):
        for temp_file in context.temp_files:
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except:
                    pass

def after_all(context):
    """Выполняется после всех тестов"""
    if context.test_context.app:
        context.test_context.app.quit()
    if (context.test_context.temp_db_path and 
        os.path.exists(context.test_context.temp_db_path)):
        try:
            os.remove(context.test_context.temp_db_path)
        except:
            pass
