from register import Register


class StackOverflow(Exception):
    pass


class StackUnderflow(Exception):
    pass


class Stack:
    def __init__(self, size: int = 8):
        self.registers = [Register() for _ in range(size)]
        self.size = size
        self.sp = -1

    def push(self, value: int) -> None:
        if self.is_full():
            raise StackOverflow('Стек переполнен')
        self.sp += 1
        self.registers[self.sp].load(value)
        self.registers[self.sp].flags.update(self.registers[self.sp].value)

    def pop(self) -> int:
        if self.is_empty():
            raise StackUnderflow('Стек пуст')
        value = self.registers[self.sp].to_int()
        self.sp -= 1
        return value

    def is_empty(self) -> bool:
        return self.sp == -1

    def is_full(self) -> bool:
        return self.sp == self.size - 1

    def clear(self):
        self.sp = -1
        for register in self.registers:
            register.load(0)
            register.flags.zero = False
            register.flags.negative = False
            register.flags.overflow = False
            register.flags.carry = False
