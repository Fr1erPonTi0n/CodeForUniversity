from stack import Stack


class AssemblerCommands:
    def __init__(self):
        self.registers = {}
        self.stack = Stack()

    def mov(self, dest: str, src: str | int):
        if isinstance(src, int):
            self.registers[dest].load(src)
        else:
            self.registers[dest] = self.registers[src].to_int()

    def add(self, dest: str, src: str | int):
        if isinstance(src, int):
            self.registers[dest].load(self.registers[dest].to_int() + src)
        else:
            self.registers[dest].add(self.registers[src].to_int())

    def sub(self, dest: str, src: str | int):
        if isinstance(src, int):
            self.registers[dest].load(self.registers[dest].to_int() - src)
        else:
            self.registers[dest].sub(self.registers[src].to_int())

    def cmp(self, op1: str | int, op2: str | int):
        val1 = op1 if isinstance(op1, int) else self.registers[op1].to_int()
        val2 = op2 if isinstance(op2, int) else self.registers[op2].to_int()

        print((val1 == val2), (val1 < val2))

    def push(self, value: str | int):
        if isinstance(value, int):
            self.stack.push(value)
        else:
            self.stack.push(self.registers[value].to_int())

    def pop(self, dest: str):
        self.registers[dest].load(self.stack.pop())
