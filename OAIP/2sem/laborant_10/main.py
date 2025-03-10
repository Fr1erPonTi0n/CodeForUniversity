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
        self.__crafting_recipes = {
            'stone_sword': {'stick': 1, 'stone': 2},
            'iron_sword': {'stick': 1, 'iron': 2},
            'diamond_sword': {'stick': 1, 'diamond': 2}
        }

        self.__crafting_classes = {
            'stone_sword': StoneSword,
            'iron_sword': IronSword,
            'diamond_sword': DiamondSword
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

    def craft_item(self, item):
        if item in self.__crafting_recipes:
            recipe = self.__crafting_recipes[item]
            for resource, amount in recipe.items():
                if self.__resources[resource] < amount:
                    print(f">> Недостаточно ресурсов для крафта {item.replace('_', ' ').capitalize()}. <<")
                    return None
            for resource, amount in recipe.items():
                self.__resources[resource] -= amount
            crafted_item_class = self.__crafting_classes[item]
            return crafted_item_class()
        else:
            print(f">> Рецепт для {item} не найден. <<")
            return None

    def info(self):
        output = '\n'
        for key, value in self.__resources.items():
            if key == 'stick':
                output += f'> {"Палка"}: {value}\n'
            elif key == 'stone':
                output += f'> {"Камень"}: {value}\n'
            elif key == 'iron':
                output += f'> {"Железо"}: {value}\n'
            elif key == 'diamond':
                output += f'> {"Алмаз"}: {value}\n'
        return f">> Ресурсы на столе крафта << {output}"


crafting_table = CraftingTable()

crafting_table.add_resource(Stick(5))
crafting_table.add_resource(Stone(3))
crafting_table.add_resource(Iron(2))
crafting_table.add_resource(Diamond(1))

print(crafting_table.info())

stone_sword = crafting_table.craft_item('stone_sword')
print(stone_sword.info() if stone_sword else '>> Крафт предмета не получился <<')

iron_sword = crafting_table.craft_item('iron_sword')
print(iron_sword.info() if iron_sword else '>> Крафт предмета не получился <<')

diamond_sword = crafting_table.craft_item('diamond_sword')
print(diamond_sword.info() if diamond_sword else '>> Крафт предмета не получился <<')

print(crafting_table.info())
