def factorial(n: int):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
