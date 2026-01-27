from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, 
                             QTableWidgetItem, QPushButton, QHeaderView,
                             QHBoxLayout, QLabel, QMessageBox)
from PyQt6.QtCore import Qt
from app.addDataWin import AddDataWindow


class ViewDataWindow(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.selected_student_id = None
        self.init_ui()
        self.load_data()
    
    def init_ui(self):
        self.setWindowTitle("SRM-Система про студентов")
        self.setGeometry(150, 150, 700, 500)
        
        layout = QVBoxLayout()

        self.title_label = QLabel("Таблица студентов")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        layout.addWidget(self.title_label)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Имя", "Возраст", "Оценка"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.table.itemSelectionChanged.connect(self.on_selection_changed)
        
        action_layout = QHBoxLayout()
        
        self.edit_button = QPushButton("Изменить")
        self.delete_button = QPushButton("Удалить")

        button_style = """
            QPushButton {
                font-size: 12px;
                padding: 6px;
                margin: 2px;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """

        self.edit_button.setStyleSheet(button_style)
        self.delete_button.setStyleSheet(button_style)
        
        action_layout.addWidget(self.edit_button)
        action_layout.addWidget(self.delete_button)
        
        control_layout = QHBoxLayout()
        self.refresh_button = QPushButton("Обновить")
        self.close_button = QPushButton("Закрыть")
        
        self.refresh_button.setStyleSheet(button_style)
        self.close_button.setStyleSheet(button_style)
        
        control_layout.addWidget(self.refresh_button)
        control_layout.addWidget(self.close_button)
        
        layout.addWidget(self.table)
        layout.addLayout(action_layout)
        layout.addLayout(control_layout)
        
        self.setLayout(layout)

        self.edit_button.clicked.connect(self.edit_selected_student)
        self.delete_button.clicked.connect(self.delete_selected_student)
        self.refresh_button.clicked.connect(self.load_data)
        self.close_button.clicked.connect(self.close)
    
    def load_data(self):
        """Загрузка данных в таблицу"""
        students = self.db.get_all_students()
        self.table.setRowCount(len(students))
        
        for row, student in enumerate(students):
            self.table.setItem(row, 0, QTableWidgetItem(str(student['id'])))
            self.table.setItem(row, 1, QTableWidgetItem(student['name']))
            self.table.setItem(row, 2, QTableWidgetItem(str(student['age'])))
            self.table.setItem(row, 3, QTableWidgetItem(student['grade']))

        self.selected_student_id = None
    
    def on_selection_changed(self):
        """Обработчик изменения выбора строки в таблице"""
        selected_items = self.table.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            student_id_item = self.table.item(row, 0)
            if student_id_item:
                self.selected_student_id = int(student_id_item.text())
        else:
            self.selected_student_id = None
    
    def edit_selected_student(self):
        """Редактирование выбранного студента"""
        if self.selected_student_id:
            self.close()
            self.edit_window = AddDataWindow(self.db, self.selected_student_id)
            self.edit_window.show()
        else:
            QMessageBox.warning(self, "Warning", "Пожалуйста, выберите студента для редактирования")
    
    def delete_selected_student(self):
        """Удаление выбранного студента"""
        if self.selected_student_id:
            reply = QMessageBox.question(
                self, 
                "Confirm Delete", 
                f"Вы уверены, что хотите удалить студента с ID {self.selected_student_id}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                success = self.db.delete_student(self.selected_student_id)
                if success:
                    QMessageBox.information(self, "Success", "Студент успешно удален")
                    self.load_data()
                else:
                    QMessageBox.warning(self, "Error", "Не удалось удалить студента")
        else:
            QMessageBox.warning(self, "Warning", "Пожалуйста, выберите студента для удаления")
