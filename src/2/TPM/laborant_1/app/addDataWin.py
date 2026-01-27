from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QComboBox, QLineEdit, QTextEdit, QMessageBox, QLabel
from PyQt6.QtGui import QIcon
from database.scripts.db import Data
from PyQt6.QtCore import pyqtSignal # Добавлена библиотека для отправки сигналов
from pathlib import Path


class AddDataWin(QWidget):
    order_saved = pyqtSignal() # Сигнал успешного завершения изменения клиента

    def __init__(self, data = None):
        super().__init__()
        self.db = Data(str(Path(__file__).parent.parent / "database" / "service_center.db")) # из-за того, что путь к папке неверен (внутри апп нету датабайс, он выше), программа не считывала базу
        self.data = data
        self.initUI()
        if data:
            self.upload_editable_data()

    def initUI(self):
        self.setWindowIcon(QIcon('resources/computer.ico')) # Не обьявлен QIcon
        self.setWindowTitle("Добавить новый заказ")
        self.setGeometry(100, 100, 400, 800)    # Размер экрана был изменен, на более оптимальный
        self.work_label = QLabel("Тип работы:") # Не обьявлен QLabel
        self.work_input = QComboBox()
        self.load_work_types()
        self.description_label = QLabel("Описание работы:")
        self.description_input = QTextEdit()
        self.date_label = QLabel("Дата принятия (YYYY-MM-DD):") # Правильное название QLabel дата
        self.date_input = QLineEdit()
        self.customer_label = QLabel("Клиент:") # Правильное название QLabel клиент
        self.customer_input = QLineEdit()
        self.executor_label = QLabel("Исполнитель:")
        self.executor_input = QComboBox()
        self.load_executors()
        self.status_label = QLabel("Статус:")
        self.status_input = QComboBox()
        self.load_statuses()
        if self.data: # Изменение название кнопки: 1) изменение переданного заказа из таблицы, 2) создание нового заказа
            self.save_button = QPushButton("Изменить заказ")
        else:
            self.save_button = QPushButton("Добавить заказ")
        self.back_button = QPushButton("Назад") # Добавление кнопки назад
        layout = QVBoxLayout()
        layout.addWidget(self.work_label)
        layout.addWidget(self.work_input)
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_input)
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.customer_label)
        layout.addWidget(self.customer_input)
        layout.addWidget(self.executor_label)
        layout.addWidget(self.executor_input)
        layout.addWidget(self.status_label)
        layout.addWidget(self.status_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.back_button)
        self.setLayout(layout)
        self.save_button.clicked.connect(self.save_order)   # Добавление connect к функции кнопки сохранения заказа
        self.back_button.clicked.connect(self.go_back)  # Добавление connect к функции кнопки назад

    def upload_editable_data(self):
        self.work_input.setCurrentText(self.data[1])
        self.description_input.setText(self.data[2])
        self.date_input.setText(self.data[3])   # Изменение на правильный параметр даты
        self.customer_input.setText(self.data[4])   # Изменение на правильный параметр клиента
        self.executor_input.setCurrentText(self.data[-2])
        self.status_input.setCurrentText(self.data[-1])

    def load_work_types(self):
        self.work_input.clear()
        self.db.get_work_types()
        for id_work, work in self.db.data:
            self.work_input.addItem(work, id_work)

    def load_executors(self):
        self.executor_input.clear()
        self.db.get_executors()
        for id_employee, employee in self.db.data:
            self.executor_input.addItem(employee, id_employee)

    def load_statuses(self):
        self.status_input.clear()
        self.db.get_statuses()
        for id_status, status in self.db.data:
            self.status_input.addItem(status, id_status)

    def save_order(self):   # Изменение название функции 
        type_of_work = self.work_input.currentData()
        description = self.description_input.toPlainText()
        acceptance_date = self.date_input.text()    # Добавление даты 
        customer = self.customer_input.text()
        executor = self.executor_input.currentData()
        status = self.status_input.currentData()
        if self.data:
            id_order = self.data[0]
            answer = self.db.update_order(type_of_work=type_of_work, description=description, 
                                       acceptance_date=acceptance_date,
                                       customer=customer, executor=executor, status=status, id_order=id_order)
        else:
            answer = self.db.add_order(type_of_work=type_of_work, description=description, acceptance_date=acceptance_date,
                                       customer=customer, executor=executor, status=status)
        QMessageBox.information(self, "Инфо", answer)
        self.order_saved.emit() # Отправляем сигнал об успешном сохранении
        self.close()

    def go_back(self): # Добавление функции кнопки назад
        self.close()