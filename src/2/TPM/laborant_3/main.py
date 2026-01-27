from PyQt6.QtWidgets import QApplication
from app.mainWin import MainWindow
import sys
import traceback


def excepthook(exc_type, exc_value, exc_tb):
    print("".join(traceback.format_exception(exc_type, exc_value, exc_tb)))


def main():
    sys.excepthook = excepthook
    app = QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
