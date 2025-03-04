import random


class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(20, 80)  # Начальный уровень голода
        self.happiness = random.randint(20, 80)  # Начальный уровень счастья
        self.energy = random.randint(20, 80)  # Начальный уровень энергии
        self.is_sleeping = False  # Состояние сна
        self.is_alive_flag = True  # Флаг жизни питомца

    def __is_alife(self):
        if self.hunger >= 100 or self.is_alive_flag is False:
            self.is_alive_flag = False
            print(f'{self.name} умер...')
            return False
        return True

    def __is_sleep(self):
        if self.is_sleeping:
            print(f'{self.name} спит и не может есть сейчас.')
            return True
        return False

    def feed(self):
        if self.__is_alife() and not self.__is_sleep():
            if random.random() <= 0.05:
                print(f'{self.name} умер от отравления...')
                self.is_alive_flag = False
                return
            self.hunger = max(0, self.hunger - random.randint(10, 30))
            self.happiness = min(100, self.happiness + random.randint(5, 15))
            print(f'{self.name} покормлен. Уровень голода: {self.hunger}')

    def play(self):
        if self.__is_alife() and not self.__is_sleep():
            self.happiness = min(100, self.happiness + random.randint(10, 20))
            self.energy = max(0, self.energy - random.randint(10, 20))
            self.hunger = min(100, self.hunger + random.randint(5, 15))
            print(f'{self.name} поиграл. Уровень счастья: {self.happiness}, энергия: {self.energy}')

    def sleep(self):
        if self.__is_alife():
            self.is_sleeping = True
            print(f'{self.name} лег спать.')

    def wake_up(self):
        if self.__is_alife():
            self.is_sleeping = False
            self.energy = min(100, self.energy + random.randint(20, 40))
            self.hunger = min(100, self.hunger + random.randint(5, 15))
            print(f'{self.name} проснулся. Энергия: {self.energy}')

    def info_status(self):
        if self.__is_alife():
            print(f'Состояние {self.name}:')
            print(f'Голод - {self.hunger}.')
            print(f'Счастье - {self.happiness}.')
            print(f'Энергия - {self.energy}.')
            print(f'Состояние сна - {"Спит" if self.is_sleeping else "Бодрствует"}.')
        
