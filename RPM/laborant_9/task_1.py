class InterfaceChecker(type):
    def __new__(mcs, name, bases, attrs):
        required_methods = ['load', 'save']
        for method_name in required_methods:
            if method_name not in attrs:
                raise TypeError(f"Класс {name} должен реализовывать метод {method_name}")
        return super().__new__(mcs, name, bases, attrs)


class CorrectPlugin(metaclass=InterfaceChecker):
    def load(self):
        print("Загрузка данных")

    def save(self):
        print("Сохранение данных")


class BrokenPlugin(metaclass=InterfaceChecker):
    def load(self):
        print("Загрузка данных")


try:
    BrokenPlugin()
except TypeError as T:
    print(f"Обнаружена ошибка типа: {T}")

correct_plugin = CorrectPlugin()
correct_plugin.load()
correct_plugin.save()