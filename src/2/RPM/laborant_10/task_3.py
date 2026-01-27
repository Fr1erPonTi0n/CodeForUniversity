import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt

random_num = random.randint(1, 100)


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Угадай число")

        layout = QVBoxLayout()

        self.label = QLabel('Введите число:')
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_num = QLineEdit()
        self.input_num.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.button = QPushButton("Угадать число")
        self.button.clicked.connect(self.the_button_was_clicked)

        layout.addStretch(1)
        layout.addWidget(self.label)
        layout.addWidget(self.input_num)
        layout.addStretch(1)
        layout.addWidget(self.button)
        layout.addStretch(1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        num = self.input_num.text()
        message = NumCheck(num)
        message.exec()


class NumCheck(QMessageBox):
    def __init__(self, num):
        super().__init__()
        self.setWindowTitle("Угадай число")

        try:
            self.n = int(num)
            if self.n > random_num:
                output = 'Меньше'
            elif self.n < random_num:
                output = 'Больше'
            else:
                output = 'Угадал!'
        except ValueError:
            output = 'Введено не целое число!'

        self.setText(output)


def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
