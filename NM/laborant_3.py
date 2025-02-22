import random

# Класс для создания матрицы 3 на 3.
class Matrix:
    def __init__(self, matrix=None):
        # Инициализация матрицы.
        self.length, self.width = 3, 3
        if matrix:
            if len(matrix) != self.length or any(len(row) != self.width for row in matrix):
                raise ValueError("Матрица должна быть размером 3x3.")
            self.matrix = matrix
            self.matrix = matrix
        else:
            if self.__answer():
                self.matrix = self.__input_matrix()
            else:
                self.matrix = self.__generate_matrix()

    def __answer(self):
        # Задать вопрос пользователю, какую матрицу создать, если он не указал заранее матрицу.
        while True:
            print('Так как вы не указали матрицу, выберите какую матрицу создать?')
            print("(1) Матрица, которая введенна с клавиатуры.")
            print("(2) Матрица, которая заполняется случайными числами и имеет случайный размер.")
            try:
                choice_answer = int(input(">\t"))
            except ValueError:
                print('Введено значение, которое не является числом.')
                continue
            print()
            if choice_answer == 1:
                return True
            elif choice_answer == 2:
                return False
            else:
                print('Вы ввели неправильное число!')

    def __input_matrix(self):
        # Ввод данных для матрицы, построчно.
        matrix = []
        print("Введите элементы матрицы построчно:")
        for i in range(3):
            while True:
                row_input = input(f"Введите 3 элементов для строки {i + 1} через пробел:\n>\t")
                try:
                    row = list(map(int, row_input.split()))
                    if len(row) != 3:
                        print(f"Ожидается 3 элементов. Попробуйте снова.")
                        continue
                    matrix.append(row)
                    break
                except ValueError:
                    print("Введены некорректные данные. Попробуйте снова.")
        return matrix

    def __generate_matrix(self):
        # Рандомная генерация матрицы 3 на 3.
        return [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]

    def output_matrix(self):
        # Вывод матрицы.
        return f'Матрица:\n{"\n".join(["\t".join(map(str, row)) for row in self.matrix])}'

    def output_size(self):
        # Вывод размера матрицы.
        return f'Размер матрицы:\nВ длину = {self.length}\nВ ширину = {self.width}'

    def transpose(self):
        # Транспонирование матрицы.
        matrix = [list(row) for row in zip(*self.matrix)]
        self.matrix = matrix

    def multiply_by_number(self, number):
        # Умножение матрицы на число.
        matrix = [[element * number for element in row] for row in self.matrix]
        self.matrix = matrix

    def add(self, other):
        # Сложение матриц.
        matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.width)] for i in range(self.length)]
        self.matrix = matrix

    def subtract(self, other):
        # Вычитание матриц.
        matrix = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.width)] for i in range(self.length)]
        self.matrix = matrix

    def multiply(self, other):
        # Умножение матриц.
        matrix = [[0 for _ in range(other.width)] for _ in range(self.length)]
        for i in range(self.length):
            for j in range(other.width):
                for k in range(self.width):
                    matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        self.matrix = matrix


# Создаем две матрицы 3x3
matrix_1 = [
    [7, 7, -2],
    [1, -2, -4],
    [3, -6, 4]
]

matrix_2 = [
    [-4, 2, 9],
    [-9, 2, -2],
    [-3, -1, 2]
]

# Создаем объекты Matrix
exam_1 = Matrix(matrix_1)
exam_2 = Matrix(matrix_2)

# Вывод матриц
print("Матрица 1:")
print(exam_1.output_matrix())
print(exam_1.output_size())

print("\nМатрица 2:")
print(exam_2.output_matrix())
print(exam_2.output_size())

# Транспонирование матрицы 1
exam_1.transpose()
print("\nТранспонированная матрица 1:")
print(exam_1.output_matrix())

# Умножение матрицы 2 на число 3
exam_2.multiply_by_number(3)
print("\nМатрица 2, умноженная на 3:")
print(exam_2.output_matrix())

# Сложение матриц 1 и 2
exam_1.add(exam_2)
print("\nРезультат сложения матриц 1 и 2:")
print(exam_1.output_matrix())

# Вычитание матриц 1 и 2
exam_1.subtract(exam_2)
print("\nРезультат вычитания матриц 1 и 2:")
print(exam_1.output_matrix())

# Умножение матриц 1 и 2
exam_1.multiply(exam_2)
print("\nРезультат умножения матриц 1 и 2:")
print(exam_1.output_matrix())

# Создание случайной матрицы
print("\nСоздание случайной матрицы:")
exam_3 = Matrix()
print(exam_3.output_matrix())
print(exam_3.output_size())

# Создание матрицы вручную
print("\nСоздание матрицы вручную:")
exam_4 = Matrix()
print(exam_4.output_matrix())
print(exam_4.output_size())