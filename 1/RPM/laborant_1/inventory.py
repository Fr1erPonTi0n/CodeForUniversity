class Inventory:
    def __init__(self, weight_limit: int = 100):
        self.__items = {}
        self.__weight_limit = weight_limit
        self.__current_weight = 0
        self.__slots = 20

    def __str__(self):
        return f'Инвентарь (весит: {self.__current_weight}): ' \
               f'{{{", ".join(f"{key}: {value}" for key, value in self.__items.items())}}}'

    def __iter__(self):
        return iter(self.__items.items())

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, item):
        return self.__items.get(item)

    def __setitem__(self, key, value):
        if key in self.__items:
            new_weight = self.__current_weight - self.__items[key] + value
        else:
            new_weight = self.__current_weight + value
        if new_weight > self.__weight_limit or len(self.__items) + (1 if key not in self.__items else 0) > self.__slots:
            raise ValueError('Превышена максимальная вместимость')
        if key in self.__items:
            self.__current_weight -= self.__items[key]
        self.__items[key] = value
        self.__current_weight += value

    def __delitem__(self, key):
        try:
            weight = self.__items[key]
            del self.__items[key]
            self.__current_weight -= weight
        except KeyError:
            raise KeyError('Такого предмета нету в инвентаре')

    def __contains__(self, item):
        return item in self.__items

    def __add__(self, other):
        if not isinstance(other, Inventory):
            return NotImplemented
        new_capacity = max(self.__weight_limit, other.__weight_limit)
        if (new_capacity > self.__weight_limit) or (len(self.__items) + len(other.__items) > self.__slots):
            raise ValueError('Превышена максимальная вместимость')
        new_inventory = Inventory(new_capacity)
        new_inventory.__items = self.__items.copy()
        new_inventory.__current_weight = self.__current_weight
        for key, value in other:
            current_value = new_inventory[key] if key in new_inventory else 0
            new_inventory[key] = current_value + value
        return new_inventory
    
