from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, base_rate, position):
        self.name = name
        self.base_rate = base_rate
        self.position = position

    @abstractmethod
    def calculate_salary(self):
        pass

    def get_info(self):
        salary = self.calculate_salary()
        print(f"Сотрудник: {self.name} ({self.position}). Зарплата: {salary}. ", end="")
        self.work()

    def work(self):
        pass


class Manager(Employee):
    def __init__(self, name, base_rate, position='Менеджер'):
        super().__init__(name, base_rate, position)

    def calculate_salary(self):
        return self.base_rate * 1.5

    def promote(self, amount=800):
        self.base_rate += amount
        print(f"{self.name} получил повышение! Новая базовая ставка: {self.base_rate}")

    def work(self):
        print("Организует работу команды.")


class Developer(Employee):
    def __init__(self, name, base_rate, position='Разработчик'):
        super().__init__(name, base_rate, position)

    def calculate_salary(self):
        return self.base_rate + 500

    def promote(self, amount=500):
        self.base_rate += amount
        print(f"{self.name} получил повышение! Новая базовая ставка: {self.base_rate}")

    def work(self):
        print("Пишет код и исправляет ошибки.")


employees = [
    Manager("Иван", 5000),
    Developer("Анна", 5000),
    Manager("Петр", 6000),
    Developer("Мария", 4500)
]

print("Информация о сотрудниках:")
for employee in employees:
    employee.get_info()

print("\nПроцедура повышения:")
for employee in employees:
    employee.promote()

print("\nОбновленная информация после повышения:")
for employee in employees:
    employee.get_info()
