import numbers
import typing

T = typing.TypeVar('T', bound=numbers.Number)  # T должен быть числом


class TypedArray(typing.Generic[T]):
    def __init__(self):
        self._items: typing.List[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def get(self, index: int) -> T:
        return self._items[index]

    def __str__(self) -> str:
        return f'{self._items}'


int_array = TypedArray[int]()
int_array.add(1)
int_array.add('a')
int_array.add([])
int_array.get(0)
print(int_array)


