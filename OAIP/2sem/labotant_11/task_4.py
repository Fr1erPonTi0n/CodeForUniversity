class Character:
    def __init__(self, name=None, hp=100, attack_power=10):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self):
        print(f'Нанесено урона: {self.attack_power}')

    def info(self):
        print(f'Имя персонажа: {self.name}\nЗдоровье: {self.hp}\nСила атаки: {self.attack_power}')


class Warrior(Character):
    def __init__(self, name, hp=100, strength=100):
        attack_power = int(strength * 0.5)
        super().__init__(name, hp=hp, attack_power=attack_power)
        self.strength = strength

    def attack(self):
        print(f'Нанесено урона мечом: {self.attack_power}')

    def info(self):
        super().info()
        print(f'Cила: {self.strength}')


class Mage(Character):
    def __init__(self, name, hp=100, mana=100):
        attack_power = int(mana * 0.3)
        super().__init__(name, hp=hp, attack_power=attack_power)
        self.mana = mana

    def attack(self):
        print(f'Нанесено урона магией: {self.attack_power}')

    def info(self):
        super().info()
        print(f'Мана: {self.mana}')


class Archer(Character):
    def __init__(self, name='Лучник', hp=100, attack_power=15, arrows=64):
        super().__init__(name, hp=hp, attack_power=attack_power)
        self.arrows = arrows

    def attack(self):
        print(f'Нанесено урона луком: {self.attack_power}')

    def info(self):
        super().info()
        print(f'Стрелы: {self.arrows}')
