import json


def main():
    with open('file.json') as f:
        templates = json.load(f)

    for i in range(len(templates)):
        print(templates[f'data{i + 1}']['name'])


if __name__ == '__main__':
    main()
