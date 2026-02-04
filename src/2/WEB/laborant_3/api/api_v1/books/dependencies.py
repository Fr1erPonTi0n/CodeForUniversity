from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    slug: str
    description: str
    pages: int

class BookCreate(BookBase):
    '''
    Модель для создания книги
    '''
    slug: Annotated[str, MinLen(3), MaxLen(30)]

class Book(BookBase):
    '''
    Модель книги
    '''