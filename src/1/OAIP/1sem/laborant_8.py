def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))    # Здесь проверяется данные соответстуют целочисленному типу данных или нет.
            return value                  # Eсли число неправильное, то осуществляется повторный ввод этого числа.
        except ValueError:
            print('Ошибка: Число должно быть целочисленным')


def get_division(num1, num2):
    try:
        result_div = num1 / num2           # Здесь проверяется деление чисел, если хоть одно число является
        return result_div                  # нулем, то выводит ошибку.
    except ZeroDivisionError:
        print('Ошибка: Нельзя делить на 0')


try:
    n1 = get_integer("Первое число: ")    # Ввод первого целочисленного числа.
    n2 = get_integer("Второе число: ")    # Ввод второго целочисленного числа.

    result = n1 + n2                      # Cумма двух числе.
    print(f"Результат сложения: {result}")

    if get_division(n1, n2) is not None:  # Проверяется это условие, чтобы не выводилось: "Рез... дел... None".
        print(f"Результат деления: {get_division(n1, n2)}")

except Exception:
    print('Неизвестная ошибка')           # Выводит неизвестную ошибку, если она возникает.

finally:
    print('Выход из программы')           # Конец программы.
  
