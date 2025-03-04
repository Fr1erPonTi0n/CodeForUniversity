length = 2
width = 2

matrix_1 = [
    [2, 4],
    [4, 6]
]

matrix_2 = [
    [6, 8],
    [8, 10]
]


def output_matrix(matrix):
    """Вывод матрицы."""
    return f'{"\n".join(["\t".join(map(str, row)) for row in matrix])}'


def multiply(matrix1, matrix2):
    """Умножение матриц."""
    # Создание результирующей матрицы
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Умножение матриц
    for i in range(len(matrix1)):  # Внешний цикл: проход по строкам matrix1
        for j in range(len(matrix2[0])):  # Средний цикл: проход по столбцам matrix2
            for k in range(len(matrix2)):  # Внутренний цикл: проход по элементам строки matrix1 и столбца matrix2
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    # Каждая итерация включает 3 элементарные операции(умножение, сложение, присваивание).
    # Итого: 3 * len(matrix1) * len(matrix2[0]) * len(matrix2) операций.
    return result, 3 * len(matrix1) * len(matrix2[0]) * len(matrix2)

# Вывод исходных матриц
print("Матрица 1:")
print(output_matrix(matrix_1))
print("Матрица 2:")
print(output_matrix(matrix_2))

result_matrix = multiply(matrix_1, matrix_2)
print(f"Результат умножения матриц:\n{output_matrix(result_matrix[0])}")
print(f'{result_matrix[1]} операции было в функции.')
