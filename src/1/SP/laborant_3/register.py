from flagregister import FlagsRegister


class Register:
    def __init__(self):
        self.size = 32
        self.value = [0] * 32
        self.flags = FlagsRegister()

    def load(self, value: int):
        value = value % (1 << self.size)
        if value >= 2 ** (self.size - 1):
            value -= 1 << self.size
        self.value = self._convert_32_bit_list(value)  # преобразование числа в список битов младший бит справа

    def _convert_32_bit_list(self, value):
        if value < 0:
            value += (1 << self.size)
        return list(map(int, f'{value:0{self.size}b}'))

    def to_int(self):
        return self._twos_complement_to_int(self.value)  # преобразует список битов в положительное целое число

    def _twos_complement_to_int(self, bits):
        if bits[0] == 1:
            return -(2 ** (self.size - 1)) + int("".join(map(str, bits[1:])), 2)
        return int("".join(map(str, bits)), 2)

    def __update_register(self, op_name: str, result: int):
        self.load(result % (1 << self.size))
        if op_name in ('add', 'sub'):
            self.flags.update(self.value)  # Обновляем флаги на основе текущего значения регистра
        else:
            self.flags.update(self.value)  # Обновляем флаги, если операция не требует дополнительных аргументов

    def add(self, other):
        return self.__update_register('add', self.to_int() + other.to_int())

    def sub(self, other):
        return self.__update_register('sub', self.to_int() - other.to_int())

    def mul(self, other):
        return self.__update_register('mul', self.to_int() * other.to_int())

    def div(self, other):
        if other.to_int() == 0:
            raise ZeroDivisionError("Division by zero")
        return self.__update_register('div', self.to_int() // other.to_int())

    def __repr__(self):
        return f"Register:\n\nvalue={self.to_int()},\nflags={self.flags}"
