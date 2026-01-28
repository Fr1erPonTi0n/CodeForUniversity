from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str
    message: str
    