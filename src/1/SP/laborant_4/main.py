from assembler import AssemblerCommands
from register import Register
from stack import Stack


def main():
    # Инициализация
    assembler = AssemblerCommands()
    assembler.registers = {"eax": Register("eax"), "ebx": Register("ebx")}
    assembler.stack = Stack(size=4)
    # Тест 1: MOV и ADD
    assembler.mov("eax", 10)
    assembler.add("eax", 5)
    assert assembler.registers["eax"].to_int() == 15
    # Тест 2: CMP и условный переход (заглушка)
    assembler.mov("ebx", 10)
    assembler.cmp("eax", "ebx")
    assert assembler.registers["eax"].flags.zero == 0
    # Тест 3: PUSH и POP
    assembler.push(42)
    assembler.pop("ebx")
    assert assembler.registers["ebx"].to_int() == 42
    print("Все тесты пройдены!")


if __name__ == "__main__":
    main()
