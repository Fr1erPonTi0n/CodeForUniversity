class FlagsRegister:
    def __init__(self):
        self.zero, self.negative, self.overflow = [False] * 3

    def update(self, value: list):  # Принимает список битов (результат операции) и обновляет значения флагов на основе анализа результата.
        int_value = int("".join(map(str, value)), 2)
        self.zero = int_value == 0
        self.negative = False
        self.overflow = int_value > (2 ** 32 - 1)
