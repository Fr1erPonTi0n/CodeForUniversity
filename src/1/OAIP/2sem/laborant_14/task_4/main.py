import csv
import os

n, m = map(int, input('Введите два числа через пробел:\t').split())

text_var = 'Введите данные (Фамилия имя результат1 результат2 результат3):'
result = [['Фамилия', 'Имя', 'Результат 1', 'Результат 2', 'Результат 3', 'Сумма']]


while True:
    var = input(f'{text_var}\n')
    if var.strip() == 'Стоп':
        break

    data = var.split()
    surname, name = data[0], data[1]
    scores = list(map(int, data[2:5]))

    total = sum(scores)

    if not(total >= n and scores[0] >= m and scores[1] >= m and scores[2] >= m):
        continue

    result.append([surname, name] + scores + [total])

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'exam.csv')

with open(file_path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(result)
