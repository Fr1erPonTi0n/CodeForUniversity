class MathUtils:
    PI = 3.14159
    E = 2.71828

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multipy(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return 'Делить на ноль нельзя'
        return a / b

    @staticmethod
    def power(base, exponent):
        return base ** exponent

    @staticmethod
    def circle_area(radius):
        if radius < 0:
            return 'Радиус не должен быть отрицательным'
        return MathUtils.PI * radius ** 2

    @staticmethod
    def is_even(number):
        return number % 2 == 0


print(MathUtils.PI)
print(MathUtils.E)
print(MathUtils.add(1, 2))
print(MathUtils.subtract(2, 1))
print(MathUtils.multipy(3, 2))
print(MathUtils.divide(10, 2))
print(MathUtils.power(2, 4))
print(MathUtils.circle_area(45))
print(MathUtils.is_even(5))