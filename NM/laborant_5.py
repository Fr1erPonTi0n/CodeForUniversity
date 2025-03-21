import numpy as np


# 1 ЗАДАНИЕ
def three_x_three(m):
    if (len(m[0]) == 3 and len(m[1]) == 3 and len(m[2]) == 3) and len(m) == 3:
        output = (m[0][0] * m[1][1] * m[2][2]) + (m[0][2] * m[1][0] * m[2][1]) + (m[0][1] * m[1][2] * m[2][0]) - \
                 (m[0][2] * m[1][1] * m[2][0]) - (m[2][2] * m[0][1] * m[1][0]) - (m[0][0] * m[2][1] * m[1][2])
        print(f'({m[0][0]} * {m[1][1]} * {m[2][2]}) + ({m[0][2]} * {m[1][0]} * {m[2][1]}) + ',
              f'({m[0][1]} * {m[1][2]} * {m[2][0]}) - ({m[0][2]} * {m[1][1]} * {m[2][0]}) - ',
              f'({m[2][2]} * {m[0][1]} * {m[1][0]}) - ({m[0][0]} * {m[2][1]} * {m[1][2]}) = {output}', sep='')
        return output
    print('Матрица не размером 3 x 3!')


# 2 ЗАДАНИЕ
def two_x_two(m):
    if (len(m[0]) == 2 and len(m[1]) == 2) and len(m) == 2:
        output = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
        print(f'({m[0][0]} * {m[1][1]}) - ({m[0][1]} * {m[1][0]}) = {output}')
        return output
    print('Матрица не размером 2 x 2!')


# 3 ЗАДАНИЕ
def __matrix_mul(a, b):
    res = []
    for row in a:
        res.append(int(sum(row[i] * b[i] for i in range(len(b)))))
    return res


def inverse_matrix(a, b):
    a_inv = np.linalg.inv(np.array(a))
    output = __matrix_mul(a_inv, b)
    print(output)
    return output


# ТЕСТИРОВАНИЕ
matrix1 = [[3, -2, 4],
           [3, 4, -2],
           [2, -1, -1]]

matrix2 = [[5, 2],
           [2, 1]]

matrix3 = [21, 9, 10]

two_x_two(matrix1)
two_x_two(matrix2)

three_x_three(matrix1)
three_x_three(matrix2)

inverse_matrix(matrix1, matrix3)
