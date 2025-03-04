"""Числа Фибоначчи (строка Фибоначчи) — числовая последовательность,
первые два числа которой являются 0 и 1, а каждое последующее
         за ними число является суммой двух предыдущих"""


def fibonacci_iterative(n):
    # Базовые случаи
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Инициализация первых двух чисел Фибоначчи
    a, b = 0, 1

    # Вычисляем числа Фибоначчи от 2 до n
    for _ in range(2, n + 1):
        a, b = b, a + b  # Обновляем значения a и b

    return b

def fibonacci_recursive(n):
    if n <= 1:
        return n # если значение = 0 или 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(f"Число Фибоначчи, итерацией:\n{fibonacci_iterative(10)}")
print(f"Число Фибоначчи, рекурсией:\n{fibonacci_recursive(10)}")
