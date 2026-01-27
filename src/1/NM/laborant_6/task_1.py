A = [
    [39.6, 0, 17.5, 9.9, 12],
    [79.2, 120, 0, 39.6, 0],
    [19.8, -21, 46, 0, 5],
    [49.5, 19, 19, 89.1, 0],
    [9.9, 25, 10, -39.6, 85],
]

b = [
    -34.5,
    -530,
    102.1,
    -286.5,
    101.3,
]

n = len(A)

C = [[0] * n for _ in range(n)]
d = [0] * n

for i in range(n):
    d[i] = b[i] / A[i][i]
    for j in range(n):
        if i != j:
            C[i][j] = -A[i][j] / A[i][i]

norm_C = max(sum(abs(C[i][j]) for j in range(n)) for i in range(n))
if norm_C >= 1:
    print("Условие сходимости не выполняется! ||C|| =", norm_C)
else:
    print("Условие сходимости выполняется ||C|| =", norm_C)


def jacobi_method(C, d, iterations, x0=None):
    if x0 is None:
        x0 = [0] * n
    x = x0[:]
    for _ in range(iterations):
        x_new = [0] * n
        for i in range(n):
            x_new[i] = d[i] + sum(C[i][j] * x[j] for j in range(n))
        x = x_new[:]
    return x


iterations = 10
x_iter = jacobi_method(C, d, iterations)

x_exact = [3.0, 4.0, 2.0, 1.0, -2.0, 5.0]

abs_error = sum(abs(x_iter[i] - x_exact[i]) for i in range(n))
rel_error = abs_error / sum(abs(x_exact[i]) for i in range(n))

print(f"Точное решение: {x_exact}")
print(f"Итерационное решение после 10 итераций: {x_iter}")
print(f"Абсолютная погрешность: {abs_error}")
print(f"Относительная погрешность: {rel_error}")
