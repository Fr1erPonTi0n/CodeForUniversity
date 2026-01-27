import json
import os


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'file.json')

    with open(file_path) as f:
        data = json.load(f)

    key = input('Какой ключ в словаре вы хотите изменить:\t')

    if key in data:

        data[key] = input('Введите значение:\t')

        with open(file_path, 'w') as f:
            f.write(json.dumps(data, indent=4))

    else:
        print('Введен неправильный ключ')

    #  Проверка файла
    with open(file_path) as f:
        loaded_data = json.load(f)

        for key, value in loaded_data.items():
            print(f"{key}: {value}")


if __name__ == '__main__':
    main()
