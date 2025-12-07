from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QPushButton, QLabel)
from PyQt6.QtCore import Qt
from app.viewDataWin import ViewDataWindow
from app.addDataWin import AddDataWindow
from app.db import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("SRM-Система про студентов")
        self.setGeometry(100, 100, 400, 300)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        self.title_label = QLabel("SRM-Система про студентов")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        layout.addWidget(self.title_label)
        self.view_button = QPushButton("Посмотреть студентов")
        self.add_button = QPushButton("Добавить студента")
        self.exit_button = QPushButton("Выйти")
        button_style = """
            QPushButton {
                font-size: 14px;
                padding: 8px;
                margin: 5px;
            }
        """
        self.view_button.setStyleSheet(button_style)
        self.add_button.setStyleSheet(button_style)
        self.exit_button.setStyleSheet(button_style)
        layout.addWidget(self.view_button)
        layout.addWidget(self.add_button)
        layout.addWidget(self.exit_button)
        central_widget.setLayout(layout)
        self.view_button.clicked.connect(self.open_view_window)
        self.add_button.clicked.connect(self.open_add_window)
        self.exit_button.clicked.connect(self.close)
    
    def open_view_window(self):
        """Открытие окна просмотра студентов"""
        self.view_window = ViewDataWindow(self.db)
        self.view_window.show()
    
    def open_add_window(self):
        """Открытие окна добавления студента"""
        self.add_window = AddDataWindow(self.db)
        self.add_window.show()
