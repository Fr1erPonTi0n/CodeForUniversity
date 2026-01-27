class Component:
    def operation(self) -> str:
        pass


class TextPrinter(Component):
    def __init__(self, text: str) -> None:
        self.text = text

    def operation(self) -> str:
        return self.text


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class UpperCaseDecorator(Decorator):
    def operation(self) -> str:
        return self.component.operation().upper()


class ExclamationDecorator(Decorator):
    def operation(self) -> str:
        return self.component.operation() + "!!!"


class BorderDecorator(Decorator):
    def operation(self) -> str:
        text = self.component.operation()
        line = "*" * (len(text) + 4)
        return f"{border}\n* {text} *\n{line}"


def client_code(component: Component) -> None:
    print(f"Результат:\n{component.operation()}", end="")


if __name__ == "__main__":
    simple = TextPrinter("Макан")
    print("Клиент: У меня есть простой компонент:")
    client_code(simple)
    print("\n\n")

    # Декоратор верхнего регистра
    upper = UpperCaseDecorator(simple)
    print("Клиент: Теперь у меня есть компонент, оформленный заглавными буквами:")
    client_code(upper)
    print("\n\n")

    # Декоратор восклицательных знаков
    exclamation = ExclamationDecorator(simple)
    print("Клиент: Теперь у меня есть компонент, украшенный восклицательным знаком:")
    client_code(exclamation)
    print("\n\n")

    # Комбинация: верхний регистр + восклицательные знаки
    upper_excl = ExclamationDecorator(UpperCaseDecorator(simple))
    print("Клиент: Теперь у меня есть компонент, оформленный заглавными буквами и восклицательным знаком:")
    client_code(upper_excl)
    print("\n\n")

    # Декоратор рамки
    border = BorderDecorator(simple)
    print("Клиент: Теперь у меня есть компонент с декором в виде границы:")
    client_code(border)
    print("\n\n")

    # Комбинация всех декораторов
    all_decorated = BorderDecorator(ExclamationDecorator(UpperCaseDecorator(simple)))
    print("Клиент: Теперь у меня есть все декорированные компоненты.:")
    client_code(all_decorated)
    print("\n\n")

    # Другая комбинация: рамка + восклицательные знаки
    border_excl = BorderDecorator(ExclamationDecorator(simple))
    print("Клиент: Теперь у меня есть компонент с рамкой и восклицательным знаком.:")
    client_code(border_excl)
    print("\n")
