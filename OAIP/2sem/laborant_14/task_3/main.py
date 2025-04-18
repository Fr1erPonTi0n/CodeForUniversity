import csv

with open('wares.csv', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter=';'))[1:]

    for line in reader:
        if int(line[1]) > int(line[2]):
            print(line[0])
