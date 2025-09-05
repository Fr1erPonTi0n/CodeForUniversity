class InterfaceChecker(type):
    def __new__(cls, name, bases, attrs):
        required_methods = ['load', 'save']
        for method_name in required_methods:
            if method_name not in attrs:
                raise TypeError(f"У класса отсутствует метод {method_name}")
        return super().__new__(cls, name, bases, attrs)


class CorrectPlugin(metaclass=InterfaceChecker):
    def load(self):
        pass

    def save(self):
        pass


class BrokenPlugin(metaclass=InterfaceChecker):
    def save(self):
        pass

    def pprint(self):
        pass
