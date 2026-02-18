from typing import Annotated, Optional
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
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
    slug: str


class BookUpdate(BookBase):
    '''
    Модель для полного обновления книги
    '''


class BookPartialUpdate(BaseModel):
    '''
    Модель для частичного обновления книги
    '''
    title: Optional[str] = None
    description: Optional[str] = None
    pages: Optional[int] = None
