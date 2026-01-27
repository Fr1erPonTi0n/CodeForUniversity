from stack import Stack


def main():
    # Инициализация стека размером 3
    stack = Stack(size=3)

    # Тест 1: Добавление и извлечение значений
    stack.push(10)
    stack.push(-5)
    assert stack.pop() == -5
    assert stack.pop() == 10

    # Тест 2: Проверка на переполнение
    try:
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)  # StackOverflow
    except Exception as e:
        assert str(e) == "Стек переполнен"

    # Тест 3: Проверка на опустошение
    stack.clear()
    try:
        stack.pop()  # StackUnderflow
    except Exception as e:
        assert str(e) == "Стек пуст"

    # Тест 4: Проверка флагов после push/pop
    stack.push(0)
    assert stack.registers[0].flags.zero == 1
    stack.push(-42)
    assert stack.registers[1].flags.negative == 1
    print("Все тесты пройдены успешно!")


if __name__ == "__main__":
    main()
