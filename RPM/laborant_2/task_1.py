class Inventory:
    def __init__(self, weigth_limit: int = 50):
        self.__items = {}
        self.__weight_limit = weigth_limit
        self.__current_weight = 0
        self.__slots = 20

    def __str__(self):
        return f'Inventory (capacity: {self.__current_weight}): ' \
               f'{{{", ".join(f"{key}: {value}" for key, value in self.__items.items())}}}'

    def __iter__(self):
        return [[key, value] for key, value in self.__items.items()]

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, item):
        return self.__items.get(item)

    def __setitem__(self, key, value):
        new_weight = self.__current_weight + value
        if (new_weight > self.__weight_limit) or (not(key in self.__items) and len(self.__items) + 1 > self.__slots):
            raise ValueError('Превышена максимальная вместимость')
        self.__items[key] = value
        self.__current_weight = new_weight

    def __delitem__(self, key):
        try:
            del self.__items[key]
        except KeyError:
            raise KeyError('Такого предмета нету в инвентаре')

    def __contains__(self, item):
        return item in self.__items

    def __add__(self, other):
        if not isinstance(other, Inventory):
            return NotImplemented('Класс не является инвентарём')
        new_capacity = max(self.__weight_limit, other.__weight_limit)
        if (new_capacity > self.__weight_limit) or (len(self.__items) + len(other.__items) > self.__slots):
            raise ValueError('Превышена максимальная вместимость')
        new_inventory = Inventory(new_capacity)
        new_inventory.__items = self.__items.copy()
        for key, value in other:
            new_inventory.__items[key] = new_inventory.__items.get(key, 0) + value
        return new_inventory
