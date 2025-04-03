class Player:
    def __init__(self, name="Новый_Игрок228", health=100, level=1, experience=0):
        self.name = name
        self._health = health
        self._level = level
        self._experience = experience

    def __str__(self):
        return f"Игрок: {self.name}, Уровень: {self._level}, Здоровье: {self._health}, Опыт: {self._experience}"

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @health.deleter
    def health(self):
        print(f"У {self.name} закончилось все здоровье!")
        self._health = 0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 1:
            self._level = 1
        else:
            self._level = value

    @level.deleter
    def level(self):
        print(f"У {self.name} обнулен уровень!")
        self._level = 0

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value < 0:
            self._experience = 0
        else:
            self._experience = value
            while self._experience >= 100:
                self._experience -= 100
                self._level += 1
                print(f"{self.name} повысил свой уровень до {self._level}.")

    @experience.deleter
    def experience(self):
        print(f"Опыт {self.name} обнулен!")
        self._experience = 0
