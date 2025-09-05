class AutoRegister(type):
    def __new__(cls, name, bases, attrs):
        obj = super().__new__(cls, name, bases, attrs)
        if not hasattr(cls, 'registry'):
            cls.registry = []
        cls.registry.append(obj)
        return obj


class BaseModel(metaclass=AutoRegister):
    pass


class User(BaseModel):
    pass


class Product(BaseModel):
    pass


print(BaseModel.registry)
