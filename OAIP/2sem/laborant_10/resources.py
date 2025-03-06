# Ресурсы для крафта предметов
class Stick:
    def __init__(self, amount):
        self.__name = 'Палка'
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def info(self):
        return f'Это {self.__name} в количестве {self.__amount}.'


class Stone:
    def __init__(self, amount):
        self.__name = 'Камень'
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def info(self):
        return f'Это {self.__name} в количестве {self.__amount}.'


class Iron:
    def __init__(self, amount):
        self.__name = 'Железо'
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def info(self):
        return f'Это {self.__name} в количестве {self.__amount}.'


class Diamond:
    def __init__(self, amount):
        self.__name = 'Алмаз'
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def info(self):
        return f'Это {self.__name} в количестве {self.__amount}.'
