import sys
import os
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

class QuoteGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.quotes = self.load_quotes()
        self.initUI()

    def load_quotes(self):
        try:
            project_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(project_dir, 'quotes.txt')
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return ["Цитаты не найдены. Пожалуйста, создайте файл quotes.txt."]

    def initUI(self):
        self.setWindowTitle("Генератор случайных цитат")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()
        self.quote_label = QLabel("Нажмите кнопку для получения цитаты", self)
        self.quote_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.quote_label)

        self.button = QPushButton("Получить цитату", self)
        self.button.clicked.connect(self.show_random_quote)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_random_quote(self):
        if self.quotes:
            random_quote = random.choice(self.quotes)
            self.quote_label.setText(random_quote)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = QuoteGenerator()
    generator.show()
    sys.exit(app.exec())