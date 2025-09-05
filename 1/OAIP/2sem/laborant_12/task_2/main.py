def main():
    try:
        with open('prices.txt', 'r', encoding='UTF8') as file:
            lines = [line.strip() for line in file.readlines()]

        result = 0

        for i in range(len(lines)):
            line = lines[i].split()

            try:
                #  Получаем количество товара
                count = int(line[1])
            except ValueError:
                print('Введено неверное целое число')
                break

            try:
                #  Получаем цену товара
                amount = float(line[2])
            except ValueError:
                print('Введено неверное дробное число')
                break

            #  Считаем общую сумму
            result += count * amount

        print(result)

    except FileNotFoundError:
        print('Файл не найден')


if __name__ == '__main__':
    main()
