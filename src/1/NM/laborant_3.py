import random


# Класс для создания матрицы.
class Matrix:
    def __init__(self, matrix=None):
        # Инициализация матрицы.
        if matrix:
            self.matrix = matrix
            self.length, self.width = len(matrix), len(matrix[0]) if matrix else 0
            self.__width_error()
        else:
            if self.__answer():
                self.length, self.width = self.__matrix_size()
                self.matrix = self.__input_matrix()
            else:
                self.matrix, self.length, self.width = self.__generate_matrix()

    @staticmethod
    def __answer():
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

    @staticmethod
    def __matrix_size():
        # Ввод размера матрицы, если нужно ввести матрицу построчно.
        while True:
            print('Введите высоту матрицы: ')
            try:
                length = int(input('>\t'))
                if length <= 0:
                    print('Высота матрицы должна быть положительным числом.')
                    continue
            except ValueError:
                print('Введено значение, которое не является числом.')
                continue
            print()
            print('Введите ширину матрицы: ')
            try:
                width = int(input('>\t'))
                if width <= 0:
                    print('Ширина матрицы должна быть положительным числом.')
                    continue
            except ValueError:
                print('Введено значение, которое не является числом.')
                continue
            return length, width

    @staticmethod
    def __generate_matrix():
        # Рандомная генерация матрицы.
        length = random.randint(1, 5)
        width = random.randint(1, 5)
        return [[random.randint(-10, 10) for _ in range(width)] for _ in range(length)], length, width
    
    def __width_error(self):
        temp = []
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != self.width:
                temp.append(i + 1)
        if temp:
            raise ValueError(
                f'В матрице не хватает элементов в таких строках: {", ".join([str(elem) for elem in temp])}')
        
    def __input_matrix(self):
        # Ввод данных для матрицы, построчно.
        matrix = []
        print("Введите элементы матрицы построчно:")
        for i in range(self.length):
            while True:
                row_input = input(f"Введите {self.width} элементов для строки {i + 1}, через пробел: \n>\t")
                try:
                    row = list(map(int, row_input.split()))
                    if len(row) != self.width:
                        print(f"Ожидается {self.width} элементов. Попробуйте снова.")
                        continue
                    matrix.append(row)
                    break
                except ValueError:
                    print("Введены некорректные данные. Попробуйте снова.")
        return matrix

    def __str__(self):
        # Вывод матрицы и размерности матрицы.
        matrix = "\n".join(["\t".join(map(str, row)) for row in self.matrix])
        return f'Матрица: \n{matrix} \nРазмер матрицы: \t{self.length} X {self.width}'

    def __add__(self, other):
        # Сложение матриц.
        if self.length != other.length or self.width != other.width:
            raise ValueError('Матрицы должны быть одного размера для сложения')
        result_matrix = [[self.matrix[i][j] + other.matrix[i][j]
                          for j in range(self.width)] for i in range(self.length)]
        return Matrix(result_matrix)

    def __sub__(self, other):
        # Вычитание матриц.
        if self.length != other.length or self.width != other.width:
            raise ValueError('Матрицы должны быть одного размера для вычитания')
        result_matrix = [[self.matrix[i][j] - other.matrix[i][j]
                          for j in range(self.width)] for i in range(self.length)]
        return Matrix(result_matrix)

    def __mul__(self, other):
        # Умножение матриц.
        if self.width != other.length:
            raise ValueError('Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы')
        result_matrix = [[self.matrix[i][j] * other.matrix[i][j]
                          for j in range(self.width)] for i in range(self.length)]
        return Matrix(result_matrix)

    def transpose(self):
        # Транспонирование матрицы.
        transposed_matrix = [list(row) for row in zip(*self.matrix)]
        return Matrix(transposed_matrix)

    def multiply_by_number(self, number):
        # Умножение матрицы на число.
        result_matrix = [[element * number for element in row] for row in self.matrix]
        return Matrix(result_matrix)


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
print(exam_1)

print("\nМатрица 2:")
print(exam_2)

# Транспонирование матрицы 1
exam_10 = exam_1.transpose()
print("\nТранспонированная матрица 1:")
print(exam_10)

# Умножение матрицы 2 на число 3
exam_3 = exam_2.multiply_by_number(3)
print("\nМатрица 2, умноженная на 3:")
print(exam_3)

# Сложение матриц 1 и 2
exam_4 = exam_1 + exam_2
print("\nРезультат сложения матриц 1 и 2:")
print(exam_4)

# Вычитание матриц 1 и 2
exam_5 = exam_1 - exam_2
print("\nРезультат вычитания матриц 1 и 2:")
print(exam_5)

# Умножение матриц 1 и 2
exam_6 = exam_1 * exam_2
print("\nРезультат умножения матриц 1 и 2:")
print(exam_6)

# Создание случайной матрицы
print("\nСоздание случайной матрицы:")
exam_7 = Matrix()
print(exam_7)

# Создание матрицы вручную
print("\nСоздание матрицы вручную:")
exam_8 = Matrix()
print(exam_8)
