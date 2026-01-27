import csv
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'wares.csv')

with open(file_path, encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter=';'))[1:]

    for line in reader:
        if int(line[1]) > int(line[2]):
            print(line[0])
