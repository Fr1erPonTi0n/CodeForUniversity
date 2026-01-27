import math


def approximate_value(x, flag):
    """Функция, которая вычисляет приближенного значения суммы ряда Тейлора."""
    s, a, n = 1, x, 1
    if flag:  # УСТОЙЧИВЫЙ АЛГОРИТМ (НЕ СДЕЛАН)
        while s + a != s:
            s += a
            n += 1
            a = a * (abs(x) / n)
        if a < 0:
            s = abs(1 / s)
    else:  # НЕУСТОЙЧИВЫЙ АЛГОРИТМ (СДЕЛАН)
        while s + a != s:
            s += a
            n += 1
            a = a * (x / n)
    return s


nums = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]

print('НЕУСТОЙЧИВЫЙ АЛГОРИТМ')
for elem in nums:
    num1 = approximate_value(elem, False)      # Число с написанной нашей функции, неустойчивый алгоритм.
    num2 = math.exp(elem)                           # Число из библиотеки math, функция exp.
    num3 = abs(num2 - num1) / num2                  # Относительная погрешность
    print(f"{f'x = {elem}':<15} {f's = {num1}':<30} {f'math_exp = {num2}':<40} {f'Δ = {num3}':<35}")

print('\nУСТОЙЧИВЫЙ АЛГОРИТМ')
for elem in nums:
    num1 = approximate_value(elem, True)        # Число с написанной нашей функции, устойчивый алгоритм.
    num2 = math.exp(elem)                            # Число из библиотеки math, функция exp.
    num3 = abs(num2 - num1) / num2                   # Относительная погрешность
    print(f"{f'x = {elem}':<15} {f's = {num1}':<30} {f'math_exp = {num2}':<40} {f'Δ = {num3}':<35}")