def horse2(a: str):
    column = a[:1]
    line = a[1:]
    all_columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    all_lines = ['1', '2', '3', '4', '5', '6', '7', '8']
    x = all_columns.index(column)
    y = all_lines.index(line)

    xy = [(x - 2, y + 1), (x - 2, y - 1), (x - 1, y + 2),
           (x - 1, y - 2), (x + 1, y + 2), (x + 1, y - 2),
           (x + 2, y + 1), (x + 2, y - 1)]

    result = []
    for (a, b) in xy:
        if (a >= 0) and (b >= 0) and (a < 8) and (b < 8):
            result += [f'{all_columns[a]}{all_lines[b]}']
    print(*sorted(result), sep='\n')
