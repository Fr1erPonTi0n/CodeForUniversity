from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QLabel


class TestMainWindow:
    def test_window_initialization(self, main_window):
        """Тест инициализации окна"""
        assert main_window.windowTitle() == "SRM-Система про студентов"
        assert main_window.isVisible() is False

    def test_widgets_existence(self, main_window):
        """Тест наличия виджетов"""
        assert isinstance(main_window.title_label, QLabel)
        assert isinstance(main_window.view_button, QPushButton)
        assert isinstance(main_window.add_button, QPushButton)
        assert isinstance(main_window.exit_button, QPushButton)
        assert main_window.title_label.text() == "SRM-Система про студентов"
        assert main_window.view_button.text() == "Посмотреть студентов"
        assert main_window.add_button.text() == "Добавить студента"
        assert main_window.exit_button.text() == "Выйти"

    def test_button_clicks(self, qtbot, main_window):
        """Тест кликов по кнопкам с использованием фикстуры"""
        with qtbot.waitSignal(main_window.view_button.clicked, timeout=1000):
            qtbot.mouseClick(main_window.view_button, Qt.MouseButton.LeftButton)
        with qtbot.waitSignal(main_window.add_button.clicked, timeout=1000):
            qtbot.mouseClick(main_window.add_button, Qt.MouseButton.LeftButton)
        with qtbot.waitSignal(main_window.exit_button.clicked, timeout=1000):
            qtbot.mouseClick(main_window.exit_button, Qt.MouseButton.LeftButton)
