import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt6.QtCore import QTimer, Qt
from random import randint, choice
from string import ascii_letters, digits


class MatrixRain(QWidget):
    def __init__(self):
        super().__init__()
        self.chars = ascii_letters + digits
        self.column_count = 30
        self.row_count = 20
        self.grid_layout = None
        self.columns = []

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 650, 450)
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle("Matrix Effect")

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        for col in range(self.column_count):
            column = []
            for row in range(self.row_count):
                label = QLabel(self)
                label.setStyleSheet(f'color: rgba(0, 255, 0, '
                                    f'{1 - row / self.row_count}); font-size: 20px;')

                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.grid_layout.addWidget(label, row, col)
                column.append(label)
            self.columns.append(column)

        # Use a single timer for all columns
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_columns)
        self.timer.start(100)  # Adjust the interval as needed

    def update_columns(self):
        for index in range(self.column_count):
            column = self.columns[index]
            for i in range(self.row_count - 1, 0, -1):
                column[i].setText(column[i - 1].text())
            column[0].setText(choice(self.chars))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    matrix = MatrixRain()
    matrix.show()
    sys.exit(app.exec())
