from random import choice


def main():
    try:
        with open('lines.txt', 'r', encoding='UTF8') as file:
            lines = [line.strip() for line in file.readlines()]

        #  Выбор случайной строки из всех строк в файле
        print(choice(lines))

    except FileNotFoundError:
        print('Файл не найден')


if __name__ == '__main__':
    main()
