class Component:
    def get_cost(self) -> float:
        pass

    def get_description(self) -> str:
        pass


class Coffee(Component):
    def __init__(self, cost: float, description: str) -> None:
        self.cost = cost
        self.description = description

    def get_cost(self) -> float:
        return self.cost

    def get_description(self) -> str:
        return self.description


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def get_cost(self) -> float:
        return self._component.get_cost()

    def get_description(self) -> str:
        return self._component.get_description()


class MilkDecorator(Decorator):
    def get_cost(self) -> float:
        return self.component.get_cost() + 50

    def get_description(self) -> str:
        return self.component.get_description() + ", молоко"


class SugarDecorator(Decorator):
    def get_cost(self) -> float:
        return self.component.get_cost() + 30

    def get_description(self) -> str:
        return self.component.get_description() + ", сахар"


class SyrupDecorator(Decorator):
    def get_cost(self) -> float:
        return self.component.get_cost() + 80

    def get_description(self) -> str:
        return self.component.get_description() + ", сироп"


def client_code(component: Component) -> None:
    print(f"Результат:\n{component.get_description()} - {component.get_cost():.2f} руб.", end="")


if __name__ == "__main__":
    # Базовый кофе
    coffee = Coffee(100, "Кофе Американо")
    print("Клиент: У меня кофе Американо:")
    client_code(coffee)
    print("\n\n")

    # Кофе с молоком
    milk_coffee = MilkDecorator(coffee)
    print("Клиент: Теперь у меня есть кофе с молоком:")
    client_code(milk_coffee)
    print("\n\n")

    # Кофе с сахаром
    sugar_coffee = SugarDecorator(coffee)
    print("Клиент: Теперь у меня есть кофе с сахаром:")
    client_code(sugar_coffee)
    print("\n\n")

    # Комбинация: молоко + сахар
    milk_sugar_coffee = SugarDecorator(MilkDecorator(coffee))
    print("Клиент: Теперь у меня есть кофе с молоком и сахаром:")
    client_code(milk_sugar_coffee)
    print("\n\n")

    # Комбинация: молоко + сахар + сироп
    full_coffee = SyrupDecorator(SugarDecorator(MilkDecorator(coffee)))
    print("Клиент: Теперь у меня есть кофе с молоком, сахаром и сиропом:")
    client_code(full_coffee)
    print("\n\n")

    # Другая комбинация: только сироп
    syrup_coffee = SyrupDecorator(coffee)
    print("Клиент: Теперь у меня есть кофе с сиропом:")
    client_code(syrup_coffee)
    print("\n")
