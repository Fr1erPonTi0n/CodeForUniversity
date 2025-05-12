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
    pass


class Product(BaseModel):
    pass


print(BaseModel.registry)
