from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QMessageBox,
                             QFormLayout)
from PyQt6.QtCore import Qt


class AddDataWindow(QWidget):
    def __init__(self, db, student_id=None):
        super().__init__()
        self.db = db
        self.student_id = student_id
        self.init_ui()
        
        if student_id:
            self.load_student_data()
    
    def init_ui(self):
        self.setWindowTitle("SRM-Система про студентов")
        self.setGeometry(150, 150, 400, 300)
        
        layout = QVBoxLayout()

        self.title_text = "Добавить нового студента" if not self.student_id else "Изменить данные студента"
        self.title_label = QLabel(self.title_text)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        layout.addWidget(self.title_label)

        self.form_layout = QFormLayout()
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите имя студента")
        
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Введите возраст студента")
        
        self.grade_input = QLineEdit()
        self.grade_input.setPlaceholderText("Введите оценку студента")
        
        self.form_layout.addRow("Имя:", self.name_input)
        self.form_layout.addRow("Возраст:", self.age_input)
        self.form_layout.addRow("Оценка:", self.grade_input)

        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Сохранить")
        self.cancel_button = QPushButton("Отменить")
        
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)
        
        layout.addLayout(self.form_layout)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)

        self.save_button.clicked.connect(self.save_data)
        self.cancel_button.clicked.connect(self.close)
    
    def load_student_data(self):
        """Загрузка данных студента для редактирования"""
        if self.student_id:
            student = self.db.get_student(self.student_id)
            if student:
                self.name_input.setText(student['name'])
                self.age_input.setText(str(student['age']))
                self.grade_input.setText(student['grade'])
    
    def save_data(self):
        """Сохранение данных"""
        name = self.name_input.text().strip()
        age_text = self.age_input.text().strip()
        grade = self.grade_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Требуется имя")
            return
        
        try:
            age = int(age_text)
            if age <= 0:
                raise ValueError("Возраст должен быть положительным")
        except ValueError:
            QMessageBox.warning(self, "Error", "Возраст должен быть положительным целым числом")
            return
        
        if not grade:
            QMessageBox.warning(self, "Error", "Требуется оценка")
            return

        try:
            if self.student_id:
                success = self.db.update_student(self.student_id, name, age, grade)
                if success:
                    QMessageBox.information(self, "Success", "Студент успешно обновлен")
                else:
                    QMessageBox.warning(self, "Error", "Не удалось обновить данные студента")
            else:
                student_id = self.db.add_student(name, age, grade)
                QMessageBox.information(self, "Success", f"Студент успешно добавлен (ID: {student_id})")
            
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Не удалось сохранить студента: {str(e)}")
