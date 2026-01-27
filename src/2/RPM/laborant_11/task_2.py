import sys
import os
from PyQt6.QtWidgets import \
    (QApplication, QMainWindow, QLineEdit, QPushButton, QPlainTextEdit, QVBoxLayout, QWidget, QHBoxLayout, QLabel)


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Текстовый редактор')

        self.filename_edit = QLineEdit(self)

        self.new_button = QPushButton("Создать новый", self)
        self.new_button.clicked.connect(self.new_file)

        self.save_button = QPushButton("Сохранить файл", self)
        self.save_button.clicked.connect(self.save_file)

        self.open_button = QPushButton("Открыть файл", self)
        self.open_button.clicked.connect(self.open_file)

        self.text_edit = QPlainTextEdit(self)

        self.char_count_label = QLabel("Количество символов: 0")
        self.word_count_label = QLabel("Количество слов: 0")
        self.longest_word_label = QLabel("Самое длинное слово: нету")
        self.shortest_word_label = QLabel("Самое короткое слово: нету")
        self.most_common_word_label = QLabel("Самое частое слово: нету")

        layout = QVBoxLayout()
        layout.addWidget(self.filename_edit)
        layout.addWidget(self.new_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.open_button)
        layout.addStretch(1)
        layout.addWidget(self.char_count_label)
        layout.addWidget(self.word_count_label)
        layout.addWidget(self.longest_word_label)
        layout.addWidget(self.shortest_word_label)
        layout.addWidget(self.most_common_word_label)

        main_layout = QHBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addWidget(self.text_edit)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def new_file(self):
        self.filename_edit.setText("")
        self.text_edit.setPlainText("")
        self.update_stats("")

    def save_file(self):
        if self.filename_edit.text() != "":
            project_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(project_dir, self.filename_edit.text())
            with open(file_path, "w", encoding="utf-8") as file:
                plain_text = self.text_edit.toPlainText()
                file.write(plain_text)
                self.update_stats(plain_text)

    def open_file(self):
        self.text_edit.clear()
        try:
            project_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(project_dir, self.filename_edit.text())
            with open(file_path, "r", encoding="utf-8") as file:
                data = file.read()
                self.text_edit.setPlainText(data)
                self.update_stats(data)
        except FileNotFoundError:
            self.update_stats("")

    def update_stats(self, text):
        if not text.strip():
            self.char_count_label.setText("Количество символов: 0")
            self.word_count_label.setText("Количество слов: 0")
            self.longest_word_label.setText("Самое длинное слово: нету")
            self.shortest_word_label.setText("Самое короткое слово: нету")
            self.most_common_word_label.setText("Самое частое слово: нету")
            return

        char_count = len(text)
        words = text.split()
        word_count = len(words)

        if words:
            longest_word = max(words, key=len)
            shortest_word = min(words, key=len)
            word_freq = {}
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
            most_common_word = max(word_freq, key=word_freq.get) if word_freq else "нету"
        else:
            longest_word = "нету"
            shortest_word = "нету"
            most_common_word = "нету"

        self.char_count_label.setText(f"Количество символов: {char_count}")
        self.word_count_label.setText(f"Количество слов: {word_count}")
        self.longest_word_label.setText(f"Самое длинное слово: {longest_word}")
        self.shortest_word_label.setText(f"Самое короткое слово: {shortest_word}")
        self.most_common_word_label.setText(f"Самое частое слово: {most_common_word}")


def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
