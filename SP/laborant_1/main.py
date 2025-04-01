from register import Register

def main():
    reg = Register("ecx")
    reg.load(42)
    assert reg.to_int() == 42
    assert reg.value == [0] * 26 + [1, 0, 1, 0, 1, 0]
    reg1 = Register("eax")
    reg2 = Register("ebx")
    reg1.load(15)
    reg2.load(10)
    reg1.add(reg2)
    assert reg1.to_int() == 25, f"Результат сложения = 25, ваш ответ: {reg1.to_int()}"
    assert reg1.flags.zero == 0, f"Флаг Z установлен, что является неверным"
    assert reg1.flags.negative == 0, f"Флаг N установлен, что является неверным"
    assert reg1.flags.overflow == 0, f"Флаг O установлен, что является неверным"
    reg1.load(20)
    reg2.load(15)
    reg1.sub(reg2)
    assert reg1.to_int() == 5, f"Результат вычитания = 5, ваш ответ: {reg1.to_int()}"
    assert reg1.flags.zero == 0, f"Флаг Z установлен, что является неверным"
    assert reg1.flags.negative == 0, f"Флаг N установлен, что является неверным"
    assert reg1.flags.overflow == 0, f"Флаг O установлен, что является неверным"
    reg1.load(4294967295)
    reg2.load(1)
    reg1.add(reg2)
    assert reg1.to_int() == 0, f"Результат сложения = 0, ваш ответ: {reg1.to_int()}"
    assert reg1.flags.zero == 1, f"Флаг Z не установлен, что является неверным"
    assert reg1.flags.negative == 0, f"Флаг N установлен, что является неверным"
    assert reg1.flags.overflow == 1, f"Флаг O не установлен, что являетсяне верным"
    reg1.load(10)
    reg2.load(10)
    reg1.sub(reg2)
    assert reg1.to_int() == 0, f"Результат вычитания = 0, ваш ответ: {reg1.to_int()}"
    assert reg1.flags.zero == 1, f"Флаг Z не установлен, что является неверным"
    assert reg1.flags.negative == 0, f"Флаг N установлен, что является неверным"
    assert reg1.flags.overflow == 0, f"Флаг O установлен, что является неверным"
    reg1.load(10)
    reg2.load(25)
    reg1.mul(reg2)
    assert (reg1.to_int() == 250), f"Результат умножения = 250, ваш ответ: {reg1.to_int()}"
    assert reg1.flags.zero == 0, f"Флаг Z установлен, что является неверным"
    assert reg1.flags.negative == 0, f"Флаг N установлен, что является неверным"
    assert reg1.flags.overflow == 0, f"Флаг O установлен, что является неверным"


if __name__ == "__main__":
    main()
