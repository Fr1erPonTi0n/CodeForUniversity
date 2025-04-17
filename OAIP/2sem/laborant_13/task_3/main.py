import json


def main():
    with open('file.json') as f:
        data = json.load(f)

    key = input('Какой ключ в словаре вы хотите изменить:\t')

    if key in data:

        data[key] = input('Введите значение:\t')

        with open('file.json', 'w') as f:
            f.write(json.dumps(data, indent=4))

    else:
        print('Введен неправильный ключ')

    #  Проверка файла
    with open('file.json') as f:
        loaded_data = json.load(f)

        for key, value in loaded_data.items():
            print(f"{key}: {value}")


if __name__ == '__main__':
    main()
