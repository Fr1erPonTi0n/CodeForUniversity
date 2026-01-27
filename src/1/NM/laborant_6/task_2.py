# Исходные данные
A = [
    [39.6, 0, 17.5, 9.9, 12],
    [79.2, 120, 0, 39.6, 0],
    [19.8, -21, 46, 0, 5],
    [49.5, 19, 19, 89.1, 0],
    [9.9, 25, 10, -39.6, 85],
]

b = [
    38.5,
    38.8,
    93.7,
    43,
    -49.7, 
]
n = len(A)

# Преобразование системы к виду x = Cx + d
C = [[0] * n for _ in range(n)]
d = [0] * n

for i in range(n):
    d[i] = b[i] / A[i][i]
    for j in range(n):
        if i != j:
            C[i][j] = -A[i][j] / A[i][i]

# Проверка условия сходимости
norm_C = max(sum(abs(C[i][j]) for j in range(n)) for i in range(n))
if norm_C >= 1:
    print("Условие сходимости не выполняется! ||C|| =", norm_C)
else:
    print("Условие сходимости выполняется ||C|| =", norm_C)

# Метод Зейделя
def seidel_method(C, d, iterations, x0=None):
    if x0 is None:
        x0 = [0] * n
    x = x0[:]
    for _ in range(iterations):
        for i in range(n):
            x[i] = d[i] + sum(C[i][j] * x[j] for j in range(n))
    return x

# Выполнение 10 итераций
iterations = 10
x_iter = seidel_method(C, d, iterations)

# Точное решение (предполагаем, что оно известно)
x_exact = [3.0, 4.0, 2.0, 1.0, -2.0]

# Вычисление погрешностей
abs_error = sum(abs(x_iter[i] - x_exact[i]) for i in range(n))
rel_error = abs_error / sum(abs(x_exact[i]) for i in range(n))

print(f"Точное решение: {x_exact}")
print(f"Итерационное решение после 10 итераций: {x_iter}")
print(f"Абсолютная погрешность: {abs_error}")
print(f"Относительная погрешность: {rel_error}")

# Попробуем другое начальное приближение
x0_new = [0, 0, 0, 0, 0]
x_iter_new = seidel_method(C, d, iterations, x0_new)

abs_error_new = sum(abs(x_iter_new[i] - x_exact[i]) for i in range(n))
rel_error_new = abs_error_new / sum(abs(x_exact[i]) for i in range(n))

print(f"Итерационное решение с новым начальным приближением: {x_iter_new}")
print(f"Абсолютная погрешность с новым начальным приближением: {abs_error_new}")
print(f"Относительная погрешность с новым начальным приближением: {rel_error_new}")
