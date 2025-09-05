def template(a, b, c):
    P = a + b + c
    S = P / 2
    if S > a and S > b and S > c:
        print(f'Периметр = {P}')
        print(f'Площадь = {(S * (S - a) * (S - b) * (S - c)) ** 0.5}')
        print(f'Равнобедренный = {"ДА" if a == b or b == c or a == c else "НЕТ"}')
        print(f'Равносторонний = {"ДА" if a == b == c else "НЕТ"}')
    else:
        print(None)
