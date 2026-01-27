from flagregister import FlagsRegister

class Register:
    def __init__(self, name: str, size: int = 32):
        self.name = name
        if size <= 32:
            self.size = size
            self.value = [0] * size
            self.flags = FlagsRegister()
        else:
            raise Exception('Размер регистра не должен превышать 32 бита')

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

    def __update_register(self, other, op_name: str, result: int):
        operand1, operand2 = self.to_int(), other.to_int()
        self.load(result % (2 ** self.size))
        if op_name in ('add', 'sub'):
            self.flags.update(self.value, operand1, operand2, op_name)
        else:
            self.flags.update(self.value, 0, 0, op_name)

    def add(self, other):
        return self.__update_register(other, 'add', self.to_int() + other.to_int())

    def sub(self, other):
        return self.__update_register(other, 'sub', self.to_int() - other.to_int())

    def mul(self, other):
        return self.__update_register(other, 'mul', self.to_int() * other.to_int())

    def div(self, other):
        if other.to_int() == 0:
            raise ZeroDivisionError("Division by zero")
        return self.__update_register(other, 'div', self.to_int() // other.to_int())

    def __repr__(self):
        return f"Register:\n\nname={self.name},\nvalue={self.to_int()},\nflags={self.flags}"
