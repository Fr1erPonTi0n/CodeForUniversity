import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt

accounts = {
    'admin': 'admin',
    'pelmen': '666',
    'denis': 'arch1488',
    'sergey': 'detrio'
}


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Авторизация")

        layout = QVBoxLayout()

        self.login = QLabel('Введите логин:')
        self.login.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_login = QLineEdit()
        self.input_login.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.password = QLabel('Введите пароль:')
        self.password.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_password = QLineEdit()
        self.input_password.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.button = QPushButton("Вход")
        self.button.clicked.connect(self.the_button_was_clicked)

        layout.addStretch(1)
        layout.addWidget(self.login)
        layout.addWidget(self.input_login)
        layout.addStretch(1)
        layout.addWidget(self.password)
        layout.addWidget(self.input_password)
        layout.addStretch(1)
        layout.addWidget(self.button)
        layout.addStretch(1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        login = self.input_login.text()
        password = self.input_password.text()
        check = accounts.get(login) == password
        message = CheckAccount(check)
        message.exec()


class CheckAccount(QMessageBox):
    def __init__(self, check=True):
        super().__init__()
        self.setWindowTitle("Результат авторизации")
        self.text = 'Вы прошли авторизацию!' if check else 'Вы не прошли авторизацию!'
        self.setText(self.text)


def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
