import json


data = {
    'first_name': 'Steve',
    'last_name': 'Semenkov',
    'surname': 'Vladimirovich',
    'year_birth': 2006,
    'city_birth': 'Minecraft',
    'place_study': 'BSPU'
 }


def main():
    with open('file.json', 'w') as f:
        f.write(json.dumps(data, indent=4))

    with open('file.json') as f:
        loaded_data = json.load(f)

        for key, value in loaded_data.items():
            print(f"{key}: {value}")


if __name__ == '__main__':
    main()
