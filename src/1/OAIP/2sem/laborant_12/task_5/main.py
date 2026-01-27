import os 

def main():
    #  Считаем и такие символы: \n, \t и т.д.
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'input.txt')

        with open(file_path, 'r', encoding='UTF8') as file:
            lines = file.readlines()

        count_len = 0

        for i in range(len(lines)):
            count_len += len(lines[i])

        total_bits = count_len * 8
        total_bytes = total_bits / 8

        #  Переводим в более крупные единицы
        units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
        size = total_bytes
        unit_index = 0

        while size >= 1024 and unit_index < len(units) - 1:
            size /= 1024
            unit_index += 1

        print(f'Размер текста: {size:.2f} {units[unit_index]}')

    except FileNotFoundError:
        print('Файл не найден')


if __name__ == '__main__':
    main()
