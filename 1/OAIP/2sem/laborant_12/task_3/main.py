def main():
    try:
        with open('lines.txt', 'r', encoding='UTF8') as file:
            lines = [line.strip() for line in file.readlines()]

        #  Вывод чётных строк
        print("Чётные строки:")
        for line in lines[1::2]:
            print(line)

        print('\n---')

        #  Вывод нечётных строк
        print("\nНечётные строки:")
        for line in lines[0::2]:
            print(line)

    except FileNotFoundError:
        print('Файл не найден')


if __name__ == '__main__':
    main()
