import json
import os


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'file.json')
    
    with open(file_path) as f:
        templates = json.load(f)

    for i in range(len(templates)):
        if templates[f'data{i + 1}']['city'] == 'Moscow':
            print(templates[f'data{i + 1}']['name'])


if __name__ == '__main__':
    main()
