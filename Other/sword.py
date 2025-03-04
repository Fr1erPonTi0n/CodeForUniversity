class __BaseSword:
    def __init__(self):
        self.damage = None
        self.endurance = 100
        self.material = None
        self.spell = None

    def __count_damage_spell(self):
        if self.spell == 'Острота 1':
            return 2
        elif self.spell == 'Острота 2':
            return 4
        elif self.spell == 'Острота 3':
            return 6
        else:
            return 0

    def info_sword(self):
        output = "\n".join([f'Урон меча: {self.damage}',
                            f'Прочность меча: {self.endurance}',
                            f'Из чего был создан меч: {self.material}',
                            f'Зачарование меча: {self.spell if self.spell else "Нету"}'])
        return f'Информация о мече:\n{output}'

    def damage_mob(self, mob):
        if self.endurance > 0:
            damage = self.damage + self.__count_damage_spell()
            self.endurance -= 5
            return f'Меч ударил {mob} уроном в {damage}!'
        else:
            return 'Меч сломан, нужно его починить!'

    def enchant_sword(self, spell):
        self.spell = spell
        self.endurance -= 10
        return f'Меч был зачарован на {spell}!'

    def repair_sword(self):
        self.endurance = 100
        return 'Меч полностью востановлен!'


class WoodenSword(__BaseSword):
    def __init__(self):
        super().__init__()
        self.damage = 2
        self.material = 'Дерево'


class IronSword(__BaseSword):
    def __init__(self):
        super().__init__()
        self.damage = 4
        self.material = 'Железо'


class GoldenSword(__BaseSword):
    def __init__(self):
        super().__init__()
        self.damage = 6
        self.material = 'Золото'


class DiamondSword(__BaseSword):
    def __init__(self):
        super().__init__()
        self.damage = 8
        self.material = 'Алмаз'


class NetheriteSword(__BaseSword):
    def __init__(self):
        super().__init__()
        self.damage = 10
        self.material = 'Незерит'


def bubugaga(sword, mob="Зомби", spell='Острота 1'):
    print(f"Проверяем: {sword.__class__.__name__}")
    print(sword.info_sword())
    print(sword.damage_mob(mob))
    print(sword.enchant_sword(spell))
    print(sword.info_sword())
    print(sword.damage_mob(mob))
    print(sword.repair_sword())
    print(sword.info_sword())
    print()


wooden_sword = WoodenSword()
bubugaga(wooden_sword)

iron_sword = IronSword()
bubugaga(iron_sword)

golden_sword = GoldenSword()
bubugaga(golden_sword)

diamond_sword = DiamondSword()
bubugaga(diamond_sword)

netherite_sword = NetheriteSword()
bubugaga(netherite_sword)
