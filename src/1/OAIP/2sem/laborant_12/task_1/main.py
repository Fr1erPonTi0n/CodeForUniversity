from random import choice
import os


def main():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'lines.txt')

        with open(file_path, 'r', encoding='UTF8') as file:
            lines = [line.strip() for line in file.readlines()]

        #  Выбор случайной строки из всех строк в файле
        print(choice(lines))

    except FileNotFoundError:
        print('Файл не найден')


if __name__ == '__main__':
    main()
