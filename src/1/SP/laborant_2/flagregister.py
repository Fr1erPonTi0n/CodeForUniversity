class FlagsRegister:
    def __init__(self):
        self.zero = False
        self.negative = False
        self.overflow = False
        self.carry = False

    def update(self, value, operand1, operand2, operation):
        int_value = self._twos_complement_to_int(value)
        self.zero = int_value == 0
        self.negative = value[0] == 1
        if operation in ("add", "sub"):
            max_positive = 2 ** 31 - 1
            min_negative = -2 ** 31
            if operation == "add":
                result = operand1 + operand2
                self.overflow = (
                        (operand1 >= 0 and operand2 >= 0 and result > max_positive) or
                        (operand1 < 0 and operand2 < 0 and result < min_negative)
                )
            elif operation == "sub":
                result = operand1 - operand2
                self.overflow = (
                        (operand1 >= 0 > operand2 and result > max_positive) or
                        (operand1 < 0 <= operand2 and result < min_negative)
                )
        if operation in ("add", "sub"):
            carry_result = operand1 + operand2 if operation == "add" else operand1 - operand2
            self.carry = (carry_result >> 32) != 0

    @staticmethod
    def _twos_complement_to_int(bits):
        if bits[0] == 1:
            return -(2 ** (len(bits) - 1)) + int("".join(map(str, bits[1:])), 2)
        return int("".join(map(str, bits)), 2)
