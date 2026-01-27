import json
import os


data = {
    'first_name': 'Steve',
    'last_name': 'Semenkov',
    'surname': 'Vladimirovich',
    'year_birth': 2006,
    'city_birth': 'Minecraft',
    'place_study': 'BSPU'
 }


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'file.json')

    with open(file_path, 'w') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))

    with open(file_path) as f:
        loaded_data = json.load(f)

        for key, value in loaded_data.items():
            print(f"{key}: {value}")


if __name__ == '__main__':
    main()
