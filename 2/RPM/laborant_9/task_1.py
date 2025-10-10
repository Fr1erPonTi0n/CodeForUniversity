import random
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Генератор случайных чисел")

        layout = QVBoxLayout()

        self.text = QLabel('0')
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("Нажми на меня!")
        self.button.clicked.connect(self.the_button_was_clicked)

        layout.addStretch(1)
        layout.addWidget(self.text)
        layout.addStretch(1)
        layout.addWidget(self.button)
        layout.addStretch(1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        self.text.setText(f'{random.randint(1, 10000)}')


def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


