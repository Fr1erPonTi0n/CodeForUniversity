from PyQt6.QtWidgets import QApplication
from app.mainWin import MainWin
import sys
import traceback

# Изменение полностью структуры файла 

def excepthook(exc_type, exc_value, exc_tb):
    print("".join(traceback.format_exception(exc_type, exc_value, exc_tb)))


def main():
    sys.excepthook = excepthook
    app = QApplication([])
    win = MainWin()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()