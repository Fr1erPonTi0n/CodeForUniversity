import typing

T = typing.TypeVar('T')


class Point(typing.Generic[T]):
    def __init__(self, x: T, y: T, z: T):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'{self.x}, {self.y}, {self.z}'


int_point = Point[int](1, 2, 3)
print(int_point)

float_point = Point[float](1.1, 2.1, 3.1)
print(float_point)