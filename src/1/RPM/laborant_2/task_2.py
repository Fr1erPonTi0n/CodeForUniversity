from functools import lru_cache


@lru_cache
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)
    else:
        return "Факториал определяется только для целых чисел."