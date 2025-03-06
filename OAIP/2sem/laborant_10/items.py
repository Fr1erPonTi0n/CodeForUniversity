# Предметы получаемые с крафтов
class StoneSword:
    def __init__(self):
        self.attack_damage = 4
        self.endurance = 100
        self.name = 'Каменный меч'

    def info(self):
        output = "\n".join([f'Урон меча: {self.attack_damage}',
                            f'Прочность меча: {self.endurance}'])
        return f'Информация о "{self.name}":\n{output}'

    def damage(self, mob='Зомби'):
        if self.endurance > 0:
            self.endurance -= 5
            return f'{self.name} ударил {mob} уроном в {self.attack_damage}!'
        else:
            return f'{self.name} сломан, нужно его починить!'

    def repair(self):
        self.endurance = 100
        return f'{self.name} полностью востановлен!'


class IronSword:
    def __init__(self):
        self.attack_damage = 6
        self.endurance = 100
        self.name = 'Железный меч'

    def info(self):
        output = "\n".join([f'Урон меча: {self.attack_damage}',
                            f'Прочность меча: {self.endurance}'])
        return f'Информация о "{self.name}":\n{output}'

    def damage(self, mob='Зомби'):
        if self.endurance > 0:
            self.endurance -= 5
            return f'{self.name} ударил {mob} уроном в {self.attack_damage}!'
        else:
            return f'{self.name} сломан, нужно его починить!'

    def repair(self):
        self.endurance = 100
        return f'{self.name} полностью востановлен!'


class DiamondSword:
    def __init__(self):
        self.__attack_damage = 10
        self.__endurance = 100
        self.__name = 'Алмазный меч'

    def info(self):
        output = "\n".join([f'Урон меча: {self.__attack_damage}',
                            f'Прочность меча: {self.__endurance}'])
        return f'Информация о "{self.__name}":\n{output}'

    def damage(self, mob='Зомби'):
        if self.__endurance > 0:
            self.__endurance -= 5
            return f'{self.__name} ударил {mob} уроном в {self.__attack_damage}!'
        else:
            return f'{self.__name} сломан, нужно его починить!'

    def repair(self):
        self.__endurance = 100
        return f'{self.__name} полностью востановлен!'
