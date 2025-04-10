class FlagsRegister:
    def __init__(self):
        self.zero, self.negative, self.overflow = [False] * 3

    def update(self, value: list, operand1: int, operand2: int, operation: str):  # Принимает список битов (результат операции) и обновляет значения флагов на основе анализа результата.
        int_value = int("".join(map(str, value)), 2)
        self.zero = int_value == 0
        self.negative = False

        if operation == "add":
            # Переполнение при сложении
            max_positive = 2 ** 31 - 1
            min_negative = -2 ** 31
            result = operand1 + operand2
            self.overflow = (operand1 >= 0 and operand2 >= 0 and result > max_positive) or \
                            (operand1 < 0 and operand2 < 0 and result < min_negative)
        elif operation == "sub":
            # Переполнение при вычитании
            max_positive = 2 ** 31 - 1
            min_negative = -2 ** 31
            result = operand1 - operand2
            self.overflow = (operand1 >= 0 > operand2 and result > max_positive) or \
                            (operand1 < 0 <= operand2 and result < min_negative)
        else:
            self.overflow = False
