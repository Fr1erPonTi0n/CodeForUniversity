import numpy as np
from scipy.optimize import bisect, newton

# Функция
def f(x):
    return (np.cos(x)) ** 2 + 2 / 35 * np.cos(x) - 1 / 35

# Производная от функции
def f_prime(x):
    return -2 * np.cos(x) * np.sin(x) - (2 / 35) * np.sin(x)


# Локализируем корни
a, b = 1.0, 1.5

# Точности для исследования
epsilons = [1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10]

# Метод половинного деления
print("Метод половинного деления:")
for eps in epsilons:
    root = bisect(f, a, b, xtol=eps)
    print(f"ε={eps:.0e}: корень={root:.10f}, итераций≈{int(np.ceil(np.log2((b - a) / eps)))}")

# Метод хорд
print("\nМетод хорд:")
for eps in epsilons:
    x0, x1 = a, b
    iterations = 0
    while abs(x1 - x0) > eps and iterations < 1000:
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_next
        iterations += 1
    print(f"ε={eps:.0e}: корень={x1:.10f}, итераций={iterations}")

# Метод касательных
print("\nМетод касательных:")
for eps in epsilons:
    root, info = newton(f, x0=(a + b) / 2, fprime=f_prime, tol=eps, full_output=True)
    print(f"ε={eps:.0e}: корень={root:.10f}, итераций={info.iterations}")