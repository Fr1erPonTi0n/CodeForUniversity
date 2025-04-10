from flagregister import FlagsRegister

class Register:
    def __init__(self, name: str, size: int = 32):
        self.name = name
        if size <= 32:
            self.size, self.value, self.flags = size, [0] * size, FlagsRegister()
        else:
            raise Exception('Размер регистра не должен превышать 32 бита')

    def load(self, value: int):
        value = value % (2 ** 32)  # если значение будет выходить за пределы ограничим его до 32 бит
        self.value = list(map(int, f'{value:0{self.size}b}'))  # преобразование числа в список битов младший бит справа

    def to_int(self):
        return int("".join(map(str, self.value)), 2)  # преобразует список битов в положительное целое число

    def __create_new_register(self, operation: str, other: 'Register', result: int) -> 'Register':
        new_register = Register(f"{self.name}{operation}{other.name}")
        new_register.load(result)
        self.flags.update(new_register.value)
        return new_register

    def add(self, other: 'Register') -> 'Register':  # Сложение
        result = self.to_int() + other.to_int()
        return self.__create_new_register('+', result % (2 ** 32))

    def sub(self, other: 'Register') -> 'Register':  # Вычитание
        result = max(0, self.to_int() - other.to_int())
        return self.__create_new_register('-', result)

    def mul(self, other: 'Register') -> 'Register':  # Умножение
        result = self.to_int() * other.to_int()
        return self.__create_new_register('*', result % (2 ** 32))

    def div(self, other: 'Register') -> 'Register':  # Целочисленное деление
        result = self.to_int() // other.to_int()
        return self.__create_new_register('//', result)

    def __repr__(self):
        return f"Register:\n\nname={self.name},\nvalue={self.to_int()},\nflags={self.flags}"
