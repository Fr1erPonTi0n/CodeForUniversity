import random
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Генератор паролей")

        layout = QVBoxLayout()

        self.password_symbols = QLabel('Допустимые символы:')
        self.password_symbols.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_password_symbols = QLineEdit()
        self.input_password_symbols.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.count_symbols = QLabel('Количество символов:')
        self.count_symbols.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_count_symbols = QLineEdit()
        self.input_count_symbols.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.button = QPushButton("Сгенерировать пароль")
        self.button.clicked.connect(self.the_button_was_clicked)

        layout.addStretch(1)
        layout.addWidget(self.password_symbols)
        layout.addWidget(self.input_password_symbols)
        layout.addStretch(1)
        layout.addWidget(self.count_symbols)
        layout.addWidget(self.input_count_symbols)
        layout.addStretch(1)
        layout.addWidget(self.button)
        layout.addStretch(1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        symbols = self.input_password_symbols.text()
        length = self.input_count_symbols.text()
        message = GeneratePassword(symbols, length)
        message.exec()


class GeneratePassword(QMessageBox):
    def __init__(self, symbols, length):
        super().__init__()
        self.setWindowTitle("Пароль")

        try:
            if not symbols:
                raise ValueError("Список символов не может быть пустым!")

            length_int = int(length)

            if length_int <= 0:
                raise ValueError("Длина пароля должна быть положительным числом!")

            self.setText(''.join(random.choice(symbols) for _ in range(length_int)))

        except ValueError as e:
            self.setText(f"Ошибка введенного количества символов!")


def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
