from register import Register

def main():
    # Тест 1: Загрузка положительного числа
    reg = Register("ecx")
    reg.load(42)
    assert reg.to_int() == 42
    assert reg.value == [0] * 26 + [1, 0, 1, 0, 1, 0]
    # Тест 2: Загрузка отрицательного числа
    reg.load(-42)
    assert reg.to_int() == -42
    assert reg.value[0] == 1 # Старший бит = 1 для отрицательного числа
    # Тест 3: Сложение положительных чисел
    reg1 = Register("eax")
    reg2 = Register("ebx")
    reg1.load(15)
    reg2.load(10)
    reg1.add(reg2)
    print(reg1)
    assert reg1.to_int() == 25
    assert reg1.flags.zero == 0
    assert reg1.flags.negative == 0
    assert reg1.flags.overflow == 0
    assert reg1.flags.carry == 0
    # Тест 4: Сложение с переполнением
    reg1.load(2147483647) # 2³¹-1
    reg2.load(1)
    reg1.add(reg2)
    assert reg1.to_int() == -2147483648 # Переполнение в отрицательное
    assert reg1.flags.zero == 0
    assert reg1.flags.negative == 1
    assert reg1.flags.overflow == 1
    assert reg1.flags.carry == 0
    # Тест 5: Вычитание с отрицательным результатом
    reg1.load(10)
    reg2.load(15)
    reg1.sub(reg2)
    assert reg1.to_int() == -5
    assert reg1.flags.zero == 0
    assert reg1.flags.negative == 1
    assert reg1.flags.overflow == 0
    assert reg1.flags.carry == 0
    # Тест 6: Умножение положительного и отрицательного
    reg1.load(10)
    reg2.load(-5)
    reg1.mul(reg2)
    assert reg1.to_int() == -50
    assert reg1.flags.zero == 0
    assert reg1.flags.negative == 1
    assert reg1.flags.overflow == 0
    assert reg1.flags.carry == 0
    # Тест 7: Деление отрицательного на положительное
    reg1.load(-100)
    reg2.load(5)
    reg1.div(reg2)
    assert reg1.to_int() == -20
    assert reg1.flags.zero == 0
    assert reg1.flags.negative == 1
    assert reg1.flags.overflow == 0
    assert reg1.flags.carry == 0
    print("Все тесты пройдены успешно!")
if __name__ == "__main__":
    main()
