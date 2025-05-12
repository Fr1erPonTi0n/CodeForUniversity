class AutoRegister(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if not hasattr(cls, 'registry'):
            cls.registry = []
        else:
            cls.registry.append(cls)


class BaseModel(metaclass=AutoRegister):
    registry = []

    def __init__(self):
        pass


class User(BaseModel):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email


class Product(BaseModel):
    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price


print(BaseModel.registry)