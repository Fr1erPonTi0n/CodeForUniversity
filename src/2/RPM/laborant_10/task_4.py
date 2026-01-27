import random
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, \
    QMessageBox, QHBoxLayout
from PyQt6.QtCore import Qt


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Генератор случайных чисел")

        layout = QVBoxLayout()

        self.label = QLabel('Введите диапозон чисел от и до:')
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_n1 = QLineEdit()
        self.input_n1.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_n2 = QLineEdit()
        self.input_n2.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.button = QPushButton("Сгенерировать")
        self.button.clicked.connect(self.the_button_was_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.input_n1)
        button_layout.addWidget(self.input_n2)

        layout.addStretch(1)
        layout.addWidget(self.label)
        layout.addLayout(button_layout)
        layout.addWidget(self.button)
        layout.addStretch(1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        n1 = self.input_n1.text()
        n2 = self.input_n2.text()
        message = RandomNum(n1, n2)
        message.exec()


class RandomNum(QMessageBox):
    def __init__(self, n1, n2):
        super().__init__()
        self.setWindowTitle("Случайное число")

        try:
            self.num1 = int(n1)
            self.num2 = int(n2)
            if self.num1 > self.num2:
                output = 'Первое число должно быть меньше или равно второму!'
            else:
                output = str(random.randint(self.num1, self.num2))
        except ValueError:
            output = 'Какое-то число не является целым или не является числом!'

        self.setText(output)


def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
