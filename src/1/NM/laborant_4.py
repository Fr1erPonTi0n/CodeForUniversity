from random import randint as random_number


def output_matrix(matrix):
    matrix = "\n".join(["\t".join(map(str, map(lambda x: round(x, 2), row[:-1]))) + f'\t| {round(row[-1], 2)}'
                        for row in matrix])
    print(matrix)


def gauss_method(matrix):
    for i in range(len(matrix)):
        max_row = i
        for string in range(i + 1, len(matrix)):
            if abs(matrix[string][i]) > abs(matrix[max_row][i]):
                max_row = string

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        for string in range(i + 1, len(matrix)):
            if matrix[i][i] == 0:
                print('Ошибка')
            else:
                factor = matrix[string][i] / matrix[i][i]
                for j in range(i, len(matrix[i])):
                    matrix[string][j] -= factor * matrix[i][j]
    output_matrix(matrix)


# Матрица из лабораторной работы для теста
matrix1 = [[3, 2, -1, 1], [2, -2, 4, -2], [-1, 0.5, -1, 0]]

# Рандомная матрица для теста
width = random_number(3, 5)
length = width - 1
matrix2 = [[random_number(-10, 10) for _ in range(width)] for _ in range(length)]

print('Матрица 1')
output_matrix(matrix1)
print('\nПрямой метод Гаусса')
gauss_method(matrix1)

print('\nМатрица 2')
output_matrix(matrix2)
print('\nПрямой метод Гаусса')
gauss_method(matrix2)
