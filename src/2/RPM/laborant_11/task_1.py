import sys

from PyQt6.QtWidgets import \
    (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QDialog, QFileDialog, QSlider, QHBoxLayout)
from PyQt6.QtGui import QImage, QPixmap, QColor, QTransform


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Задание 1")

        self.button_1 = QPushButton("Изменение прозрачности")
        self.button_1 .clicked.connect(self.open_first_win)

        self.button_2 = QPushButton("PIL 2.0")
        self.button_2.clicked.connect(self.open_second_win)

        layout = QVBoxLayout()

        layout.addStretch(1)
        layout.addWidget(self.button_1)
        layout.addStretch(1)
        layout.addWidget(self.button_2)
        layout.addStretch(1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_first_win(self):
        dialog = FirstWin()
        dialog.exec()

    def open_second_win(self):
        dialog = SecondWin()
        dialog.exec()


class FirstWin(QDialog):
    def __init__(self):
        super().__init__()

        self.original_image = None
        self.curr_image = None
        self.opacity = 100

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Изменение прозрачности")

        self.button_open_file = QPushButton("Открыть файл")
        self.button_open_file.clicked.connect(self.open_image)

        self.slider = QSlider()
        self.slider.setValue(100)
        self.slider.valueChanged.connect(self.set_opacity)

        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap())

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.slider)
        bottom_layout.addWidget(self.image_label)

        layout = QVBoxLayout()
        layout.addWidget(self.button_open_file)
        layout.addLayout(bottom_layout)

        self.setLayout(layout)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть изображение", "",
                                                   "Изображения (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.original_image = QImage(file_path)
            if self.original_image.isNull():
                return
            self.opacity = 100
            self.slider.setValue(100)
            self.curr_image = self.original_image.copy()
            self.update_display()

    def update_display(self):
        self.image_label.setPixmap(QPixmap.fromImage(self.curr_image))

    def set_opacity(self, value):
        if self.original_image is None and self.curr_image is None:
            return
        self.opacity = value
        self.curr_image = self.original_image.copy()
        alpha = int((value / 100.0) * 255)
        for i in range(self.curr_image.width()):
            for j in range(self.curr_image.height()):
                color = self.curr_image.pixelColor(i, j)
                color.setAlpha(alpha)
                self.curr_image.setPixelColor(i, j, color)
        self.update_display()


class SecondWin(QDialog):
    def __init__(self):
        super().__init__()

        self.original_image = None
        self.curr_image = None
        self.degree = 0

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Изменение прозрачности")
        self.setBaseSize(600, 400)

        self.button_open_file = QPushButton("Открыть файл")
        self.button_open_file.clicked.connect(self.open_image)

        self.button_R = QPushButton('R')
        self.button_R.clicked.connect(self.edit_color)

        self.button_G = QPushButton('G')
        self.button_G.clicked.connect(self.edit_color)

        self.button_B = QPushButton('B')
        self.button_B.clicked.connect(self.edit_color)

        self.button_ALL = QPushButton('ALL')
        self.button_ALL.clicked.connect(self.edit_color)

        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap())

        self.button_counterclockwise = QPushButton('Против часовой стрелки')
        self.button_counterclockwise.clicked.connect(self.edit_rotate)

        self.button_clockwise = QPushButton('По часовой стрелки')
        self.button_clockwise.clicked.connect(self.edit_rotate)

        bottom_layout = QVBoxLayout()
        bottom_layout.addWidget(self.button_R)
        bottom_layout.addWidget(self.button_G)
        bottom_layout.addWidget(self.button_B)
        bottom_layout.addWidget(self.button_ALL)

        part_layout_1 = QHBoxLayout()
        part_layout_1.addLayout(bottom_layout)
        part_layout_1.addWidget(self.image_label)

        part_layout_2 = QHBoxLayout()
        part_layout_2.addWidget(self.button_counterclockwise)
        part_layout_2.addWidget(self.button_clockwise)

        layout = QVBoxLayout()
        layout.addWidget(self.button_open_file)
        layout.addLayout(part_layout_1)
        layout.addLayout(part_layout_2)

        self.setLayout(layout)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть изображение", "",
                                                   "Изображения (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.original_image = QImage(file_path)
            self.curr_image = self.original_image.copy()
            self.degree = 0
            self.update_image()

    def update_image(self):
        self.image_label.setPixmap(QPixmap.fromImage(self.curr_image))

    def edit_color(self):
        if self.original_image is None and self.curr_image is None:
            return
        self.curr_image = self.original_image.copy()
        sender_text = self.sender().text()
        for i in range(self.curr_image.width()):
            for j in range(self.curr_image.height()):
                r, g, b, _ = self.curr_image.pixelColor(i, j).getRgb()
                if sender_text == 'R':
                    self.curr_image.setPixelColor(i, j, QColor(r, 0, 0))
                elif sender_text == 'G':
                    self.curr_image.setPixelColor(i, j, QColor(0, g, 0))
                elif sender_text == 'B':
                    self.curr_image.setPixelColor(i, j, QColor(0, 0, b))
                elif sender_text == 'ALL':
                    self.curr_image.setPixelColor(i, j, QColor(r, g, b))
        self.curr_image = self.curr_image.transformed(QTransform().rotate(self.degree))
        self.update_image()

    def edit_rotate(self):
        if self.original_image is None and self.curr_image is None:
            return
        sender_text = self.sender().text()
        if sender_text == 'Против часовой стрелки':
            self.degree -= 90
        elif sender_text == 'По часовой стрелки':
            self.degree += 90
        self.curr_image = self.original_image.copy()
        self.curr_image = self.curr_image.transformed(QTransform().rotate(self.degree))
        self.update_image()


def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    
