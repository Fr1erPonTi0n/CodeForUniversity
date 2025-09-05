def simple_number(n: int, div=2):
    if n < div * div:
        return True
    if n % div == 0:
        return False
    return simple_number(n, div + 1)
