import csv
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'vps.csv')

with open(file_path, encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)[1:]

    n = int(input())
    output = []

    for row in data:
        if int(row[4]) >= n:
            output.append(row[0])

    print('\n'.join(output) if output else 'Нету')
