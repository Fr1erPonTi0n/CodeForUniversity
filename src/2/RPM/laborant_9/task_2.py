import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count_click = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Кликер")

        layout = QVBoxLayout()

        self.text = QLabel('Число кликов: 0')
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
        self.count_click += 1
        self.text.setText(f"Число кликов: {self.count_click}")


def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

