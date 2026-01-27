from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, \
    QMessageBox, QLineEdit, QHBoxLayout, QComboBox
from PyQt6.QtGui import QIcon
from app.addDataWin import AddDataWin
from database.scripts.db import Data
from pathlib import Path    # Добавление импорта Path


class ViewDataWin(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Data(str(Path(__file__).parent.parent / "database" / "service_center.db"))    # Из-за того, что путь к папке неверен (внутри app нету database, он выше), программа не считывала db.py
        self.initUI()
        self.load_data()

    def initUI(self):
        self.setWindowTitle("Выборки из базы данных")
        self.setGeometry(100, 100, 750, 500)    # Размер экрана был изменен, на более оптимальный
        self.query_label = QLabel("Выберите выборку:")
        self.query_combo = QComboBox()  # Нету обьявлении в импорте QComboBox
        self.query_combo.addItem("Все заказы", "all_orders")
        self.query_combo.addItem("Тип работы", "work")  # Изменено на корректное название колонка
        self.query_combo.addItem("Описание", "description") # Добавление в меню выборки описания
        self.query_combo.addItem("Дата", "acceptance_date")
        self.query_combo.addItem("Клиент", "customer")    # Добавление в меню выборки клиента
        self.query_combo.addItem("Исполнитель", "surname")
        self.query_combo.addItem("Статус заказа", "status")
        self.filter = QLineEdit()
        self.filter.setPlaceholderText('Введите фильтр')
        self.table = QTableWidget()
        self.back_button = QPushButton("Назад")
        self.del_entry = QPushButton("Удалить")
        self.edit_entry = QPushButton("Изменить")
        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        main_l.addWidget(self.query_label)
        main_l.addWidget(self.query_combo)
        main_l.addWidget(self.filter)
        main_l.addWidget(self.table)
        h_l1.addWidget(self.back_button)    # Добалени кнопки выхода в h_l1
        h_l1.addWidget(self.del_entry)
        h_l1.addWidget(self.edit_entry)
        main_l.addLayout(h_l1)
        self.setLayout(main_l)
        self.del_entry.clicked.connect(self.delete_order)   # Добавление connect к функции кнопки удалить
        self.filter.textChanged.connect(self.load_data)
        self.query_combo.currentIndexChanged.connect(self.load_data)
        self.back_button.clicked.connect(self.go_back)
        self.edit_entry.clicked.connect(self.edit_orders)

    def load_data(self):
        query_type = self.query_combo.currentData()
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        if query_type == "all_orders":
            self.load_orders()
        elif query_type == "status":
            self.load_orders('status')
        elif query_type == "surname":
            self.load_orders('surname') # Исправлено 'surnam' на 'surname'
        elif query_type == "work":
            self.load_orders('work')
        elif query_type == "acceptance_date":
            self.load_orders('acceptance_date')
        elif query_type == "customer":  # Добавление выборки клиентов
            self.load_orders('customer')
        elif query_type == "description":   # Добавление выборки описания
            self.load_orders('description')


    def load_orders(self, column=None):
        self.db.get_all_orders(column, self.filter.text().capitalize())
        if type(self.db.data) is list:
            self.table.setColumnCount(7)    # Неккоректное число столбцов
            self.table.setHorizontalHeaderLabels(
                ['ID заказа', 'Тип работы', 'Описание', 'Дата принятия', 'Клиент', 'Исполнитель', 'Статус'])
            self.table.setRowCount(len(self.db.data))
            for row_idx, row_data in enumerate(self.db.data):
                for col_idx, col_data in enumerate(row_data):
                    self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
        else:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные: {self.db.data}")

    def delete_order(self): # Исправлено имя функции delite
        if self.table.selectedItems():
            confirmation_dialog = QMessageBox()
            confirmation_dialog.setWindowTitle("Подтверждение удаления")
            confirmation_dialog.setText(f"Вы уверены, что хотите удалить запись:\n{self.table.item(self.table.currentRow(), 2).text()}?")
            confirmation_dialog.setIcon(QMessageBox.Icon.Warning)
            confirmation_dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            confirmation_dialog.setDefaultButton(QMessageBox.StandardButton.No)
            user_response = confirmation_dialog.exec()
            if user_response == QMessageBox.StandardButton.Yes: # Изменено условие диалога, если нажать да, то удаляется запись
                QMessageBox.information(self, "Инфо", self.db.delete_order(id_order=self.table.item(self.table.currentRow(), 0).text()))
                self.load_data()

    def edit_orders(self):
        if self.table.selectedItems(): # Добавлена проверка выбранного клиента
            self.win_a = AddDataWin([self.table.item(self.table.selectedItems()[0].row(), col).text() for col in range(self.table.columnCount())])
            self.win_a.order_saved.connect(self.load_data) # Добавлен сигнал успешного изменения 
            self.win_a.destroyed.connect(self.load_data)
            self.win_a.show()
        else: # Если клиент не выбран, то выдает предупреждение
            QMessageBox.warning(self, "Предупреждение", "Выберите запись для редактирования")

    def go_back(self):
        self.close()