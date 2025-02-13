import random


class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(20, 80)  # Начальный уровень голода
        self.happiness = random.randint(20, 80)  # Начальный уровень счастья
        self.energy = random.randint(20, 80)  # Начальный уровень энергии
        self.is_sleeping = False  # Состояние сна
        self.is_alive_flag = True  # Флаг жизни питомца

    def is_alive(self):
        if self.hunger >= 100 or self.is_alive_flag is False:
            self.is_alive_flag = False
            return True
        return False

    def feed(self):
        if self.is_alive():
            print(f'{self.name} умер...')
            return
        if self.is_sleeping:
            print(f'{self.name} спит и не может есть сейчас.')
            return
        self.hunger = max(0, self.hunger - random.randint(10, 30))
        self.happiness = min(100, self.happiness + random.randint(5, 15))
        print(f'{self.name} покормлен. Уровень голода: {self.hunger}')


    def play(self):
        if self.is_alive():
            print(f'{self.name} умер...')
            return
        if self.is_sleeping:
            print(f'{self.name} спит и не может играть сейчас.')
            return
        self.happiness = min(100, self.happiness + random.randint(10, 20))
        self.energy = max(0, self.energy - random.randint(10, 20))
        self.hunger = min(100, self.hunger + random.randint(5, 15))
        print(f'{self.name} поиграл. Уровень счастья: {self.happiness}, энергия: {self.energy}')

    def sleep(self):
        if self.is_alive():
            print(f'{self.name} умер...')
            return
        self.is_sleeping = True
        print(f'{self.name} лег спать.')

    def wake_up(self):
        if self.is_alive():
            print(f'{self.name} умер...')
            return
        self.is_sleeping = False
        self.energy = min(100, self.energy + random.randint(20, 40))
        self.hunger = min(100, self.hunger + random.randint(5, 15))
        print(f'{self.name} проснулся. Энергия: {self.energy}')

    def info_status(self):
        if self.is_alive():
            print(f'{self.name} умер...')
            return
        print(f'Состояние {self.name}:')
        print(f'Голод - {self.hunger}.')
        print(f'Счастье - {self.happiness}.')
        print(f'Энергия - {self.energy}.')
        print(f'Состояние сна - {'Спит' if self.is_sleeping else 'Бодрствует'}.')