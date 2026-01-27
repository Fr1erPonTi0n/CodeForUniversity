class FlagsRegister:
    def __init__(self):
        self.zero = False
        self.negative = False
        self.overflow = False
        self.carry = False

    def update(self, value: list):
        result = self.to_int(value)
        self.zero = (result == 0)
        self.negative = (result < 0)
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            self.overflow = True
        else:
            self.overflow = False
        if len(value) > 32:
            self.carry = True
        else:
            self.carry = False

    def to_int(self, value):
        return self._twos_complement_to_int(value)  # преобразует список битов в положительное целое число

    @staticmethod
    def _twos_complement_to_int(bits):
        if bits[0] == 1:
            return -(2 ** (32 - 1)) + int("".join(map(str, bits[1:])), 2)
        return int("".join(map(str, bits)), 2)
