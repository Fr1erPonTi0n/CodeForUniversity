# Основной файл
from resources import *
from items import *


class CraftingTable:
        def __init__(self):
        self.__resources = {
            'stick': 0,
            'stone': 0,
            'iron': 0,
            'diamond': 0
        }

    def add_resource(self, resource):
        if isinstance(resource, Stick):
            self.__resources['stick'] += resource.get_amount()
        elif isinstance(resource, Stone):
            self.__resources['stone'] += resource.get_amount()
        elif isinstance(resource, Iron):
            self.__resources['iron'] += resource.get_amount()
        elif isinstance(resource, Diamond):
            self.__resources['diamond'] += resource.get_amount()

    def craft_stone_sword(self):
        if self.__resources['stick'] >= 1 and self.__resources['stone'] >= 2:
            self.__resources['stick'] -= 1
            self.__resources['stone'] -= 2
            return StoneSword()
        else:
            print("Недостаточно ресурсов для крафта Алмазного меча.")

    def craft_iron_sword(self):
        if self.__resources['stick'] >= 1 and self.__resources['iron'] >= 2:
            self.__resources['stick'] -= 1
            self.__resources['iron'] -= 2
            return IronSword()
        else:
            print("Недостаточно ресурсов для крафта Алмазного меча.")

    def craft_diamond_sword(self):
        if self.__resources['stick'] >= 1 and self.__resources['diamond'] >= 2:
            self.__resources['stick'] -= 1
            self.__resources['diamond'] -= 2
            return DiamondSword()
        else:
            print("Недостаточно ресурсов для крафта Алмазного меча.")

    def info(self):
        output = '\n'
        for key, value in self.__resources.items():
            if key == 'stick':
                output += f'{"Палка"}: {value}\n'
            elif key == 'stone':
                output += f'{"Камень"}: {value}\n'
            elif key == 'iron':
                output += f'{"Железо"}: {value}\n'
            elif key == 'diamond':
                output += f'{"Алмаз"}: {value}\n'
        return f">> Ресурсы на столе крафта << {output}"


crafting_table = CraftingTable()

crafting_table.add_resource(Stick(5))
crafting_table.add_resource(Stone(3))
crafting_table.add_resource(Iron(2))
crafting_table.add_resource(Diamond(1))

print(crafting_table.info())

stone_sword = crafting_table.craft_stone_sword()
print(stone_sword.info() if stone_sword else '>> Крафт предмета не получился <<')

iron_sword = crafting_table.craft_iron_sword()
print(iron_sword.info() if iron_sword else '>> Крафт предмета не получился <<')

diamond_sword = crafting_table.craft_diamond_sword()
print(diamond_sword.info() if diamond_sword else '>> Крафт предмета не получился <<')

print(crafting_table.info())
