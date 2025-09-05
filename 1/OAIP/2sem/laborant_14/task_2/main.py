import csv

with open('vps.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)[1:]

    n = int(input())
    output = []

    for row in data:
        if int(row[4]) >= n:
            output.append(row[0])

    print('\n'.join(output) if output else 'Нету')
