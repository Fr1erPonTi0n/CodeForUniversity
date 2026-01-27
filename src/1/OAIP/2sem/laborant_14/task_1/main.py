import csv
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'file.csv')

with open(file_path, encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')

    sorted_rows = sorted(list(reader), key=lambda x: int(x[1]))
    output = []

    for row in sorted_rows:
        if int(row[1]) <= 1000 and not ((int(row[1]) * 10) <= 1000):
            output.append(row[0])

    print(', '.join(output) if output else 'error')
