def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args in cache_dict:
            print(f"Результат для {args[0]} взят из кэша.")
            return cache_dict[args]

        result = func(*args)
        cache_dict[args] = result
        print(f"Результат для {args[0]} вычислен и сохранен в кэш.")
        return result

    return wrapper


@cache
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)
    else:
        return "Факториал определяется только для целых чисел."
