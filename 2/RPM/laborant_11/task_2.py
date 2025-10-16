import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QPlainTextEdit, QVBoxLayout, QWidget, QHBoxLayout


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Текстовый редактор')

        self.filename_edit = QLineEdit(self)

        self.new_button = QPushButton("Создать новый", self)
        self.new_button.clicked.connect(self.new_btn_func)

        self.save_button = QPushButton("Сохранить файл", self)
        self.save_button.clicked.connect(self.save_btn_func)

        self.open_button = QPushButton("Открыть файл", self)
        self.open_button.clicked.connect(self.open_btn_func)

        self.text_edit = QPlainTextEdit(self)

        layout = QVBoxLayout()
        layout.addWidget(self.filename_edit)
        layout.addWidget(self.new_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.open_button)
        layout.addStretch(1)

        main_layout = QHBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addWidget(self.text_edit)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def new_btn_func(self):
        self.filename_edit.setText("")
        self.text_edit.setPlainText("")

    def save_btn_func(self):
        if self.filename_edit.text() != "":
            with open(self.filename_edit.text(), "w", encoding="utf-8") as file:
                plain_text = self.text_edit.toPlainText()
                file.write(plain_text)

    def open_btn_func(self):
        self.text_edit.clear()
        try:
            with open(self.filename_edit.text(), "r", encoding="utf-8") as file:
                data = file.read()
                self.text_edit.setPlainText(data)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())
    
