from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance, owner, account_number):
        self.balance = balance
        self.owner = owner
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self):
        pass

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно средств на счете")

    def account_info(self):
        interest = self.calculate_interest()
        return f"Счет №{self.account_number} (Владелец: {self.owner}). Баланс: {self.balance}. Проценты: {interest}"


class SavingsAccount(BankAccount):
    def __init__(self, balance, owner, account_number):
        super().__init__(balance, owner, account_number)

    def calculate_interest(self):
        return self.balance * 0.05


class CheckingAccount(BankAccount):
    def __init__(self, balance, owner, account_number):
        super().__init__(balance, owner, account_number)

    def calculate_interest(self):
        return 0


savings = SavingsAccount(10000, "Иван", "12345")
checking = CheckingAccount(5000, "Анна", "67890")
print(savings.account_info())
print(checking.account_info())
