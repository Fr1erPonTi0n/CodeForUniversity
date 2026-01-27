from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Product:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Customer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Customer) -> None:
        pass

    @abstractmethod
    def notify(self, product: Product) -> None:
        pass


class Store(Subject):
    _products: List[Product] = []
    _customers: List[Customer] = []

    def attach(self, observer: Customer) -> None:
        print(f"Магазин: Прикрепленный клиент: {observer.name}.")
        self._customers.append(observer)

    def detach(self, observer: Customer) -> None:
        print(f"Магазин: Отключен клиент: {observer.name}.")
        self._customers.remove(observer)

    def notify(self, product: Product) -> None:
        print("Магазин: Информирование покупателей о новых продуктах...")
        for customer in self._customers:
            customer.update(product)

    def add_product(self, product: Product) -> None:
        print(f"Магазин: Добавление нового продукта: {product.name}")
        self._products.append(product)
        self.notify(product)


class Customer(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def update(self, product: Product) -> None:
        pass


class CustomerOne(Customer):
    def update(self, product: Product) -> None:
        print(f"Клиент 1 {self.name}: Ого, новый продукт '{product.name}'! Обязательно куплю!")


class CustomerTwo(Customer):
    def update(self, product: Product) -> None:
        print(f"Клиент 2 {self.name}: Слышал о «{product.name}», но сначала хочу проверить отзывы.")


if __name__ == "__main__":
    store = Store()

    customer_a = CustomerOne("Денис")
    store.attach(customer_a)

    customer_b = CustomerTwo("Серега")
    store.attach(customer_b)

    # Добавляем новые товары
    store.add_product(Product("Беспроводные наушникиs"))
    store.add_product(Product("Умные часы"))

    # Отсоединяем одного покупателя
    store.detach(customer_b)

    # Добавляем ещё один товар
    store.add_product(Product("Bluetooth-динамик"))
