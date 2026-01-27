def func_table(f, x_max, y_max):
    rows = []
    for x in range(x_max + 1):
        row = []
        for y in range(y_max + 1):
            result = eval(f)
            row.append(str(result))
        rows.append(row)
    for row in rows:
        print('\t'.join(row))
