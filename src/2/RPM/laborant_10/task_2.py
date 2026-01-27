import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, \
    QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Конвертация валюты")

        layout = QVBoxLayout()

        self.rubs = QLabel('Введите определенное кол-во рублей:')
        self.rubs.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_rubs = QLineEdit()
        self.input_rubs.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.button1 = QPushButton("USD")
        self.button1.clicked.connect(self.the_button_was_clicked)

        self.button2 = QPushButton("KZT")
        self.button2.clicked.connect(self.the_button_was_clicked)

        self.button3 = QPushButton("UAN")
        self.button3.clicked.connect(self.the_button_was_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)

        layout.addStretch(1)
        layout.addWidget(self.rubs)
        layout.addWidget(self.input_rubs)
        layout.addLayout(button_layout)
        layout.addStretch(1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        try:
            rub_amount = float(self.input_rubs.text())
            sender = self.sender()
            currency = sender.text()

            message = ConvertValue(currency, rub_amount)
            message.exec()
        except ValueError:
            message = ConvertValue(None, None)
            message.exec()


class ConvertValue(QMessageBox):
    def __init__(self, currency, rub_amount):
        super().__init__()
        self.setWindowTitle("Результат конвертации")

        output = 'Конвертация рубля'
        if currency == "USD":
            output += f' в USD: {rub_amount * 0.011}'
        elif currency == "KZT":
            output += f' в KZT:{rub_amount * 5.0}'
        elif currency == "UAN":
            output += f' в UAN:{rub_amount * 0.30}'
        else:
            output = 'Ошибка при конвертации валюты!'

        self.setText(output)


def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
