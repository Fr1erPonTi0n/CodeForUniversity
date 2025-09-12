from __future__ import annotations

import random
from abc import ABC, abstractmethod
from typing import List


class RouteContext:
    def __init__(self, strategy: RouteStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> RouteStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: RouteStrategy) -> None:
        self._strategy = strategy

    def find_route(self) -> None:
        data = [1, 2, 3, 4, 5, 6]
        result = self._strategy.calculate_route(data)
        print(f"Маршрут: {','.join(result)}")


class RouteStrategy(ABC):
    @abstractmethod
    def calculate_route(self, data: List):
        pass


class ShortestRouteStrategy(RouteStrategy):
    def calculate_route(self, data: List) -> List:
        return [str(point) for point in data]


class FastestRouteStrategy(RouteStrategy):
    def calculate_route(self, data: List) -> List:
        return [str(point) for point in reversed(data)]


class CheapestRouteStrategy(RouteStrategy):
    def calculate_route(self, data: List) -> List:
        shuffled = data.copy()
        random.shuffle(shuffled)
        return [str(point) for point in shuffled]


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]

    context = RouteContext(ShortestRouteStrategy())
    print("Кратчайший маршрут:")
    context.find_route()

    print("Самый быстрый маршрут:")
    context.strategy = FastestRouteStrategy()
    context.find_route()

    print("Самый дешевый маршрут:")
    context.strategy = CheapestRouteStrategy()
    context.find_route()
