from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class Product(ABC):
    @abstractmethod
    def get_total_price(self):
        pass


@dataclass
class Item(Product):
    name: str
    price: float
    quantity: int = 1

    def get_total_price(self):
        return self.price * self.quantity


@dataclass
class Order:
    items: List[Item] = None

    def __post_init__(self):
        if self.items is None:
            self.items = []

    def total_sum(self) -> float:
        return sum(item.get_total_price() for item in self.items)

    def get_items_sorted_by_price_desc(self) -> List[Item]:
        return sorted(self.items, key=lambda x: x.price, reverse=True)


if __name__ == '__main__':
    laptop = Item(name="Ноутбук", price=1000.0, quantity=1)
    mouse = Item(name="Мышь", price=25.0, quantity=2)
    keyboard = Item(name="Клавиатура", price=100.0)
    
    order1 = Order()
    order1.items.extend([laptop, mouse, keyboard])
    
    print("Заказ 1:")
    print(f"Общая сумма: {order1.total_sum()}")
    print("Товары по убыванию цены:")
    for item in order1.get_items_sorted_by_price_desc():
        print(f"{item.name}: {item.price}")
    
    order2 = Order(items=[
        Item(name="Монитор", price=300.0),
        Item(name="Наушники", price=150.0, quantity=2)
    ])
    
    print("\nЗаказ 2:")
    print(f"Общая сумма: {order2.total_sum()}")
    print("Товары по убыванию цены:")
    for item in order2.get_items_sorted_by_price_desc():
        print(f"{item.name}: {item.price}")
        
