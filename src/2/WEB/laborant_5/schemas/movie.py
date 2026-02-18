from typing import Annotated, Optional
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    description: str
    year: int
    duration: int


class MovieCreate(MovieBase):
    '''
    Модель для создания фильма
    '''
    slug: Annotated[str, MinLen(3), MaxLen(30)]


class Movie(MovieBase):
    '''
    Модель фильма
    '''
    slug: str


class MovieUpdate(MovieBase):
    '''
    Модель для полного обновления фильма
    '''


class MoviePartialUpdate(BaseModel):
    '''
    Модель для частичного обновления фильма
    '''
    title: Optional[str] = None
    description: Optional[str] = None
    year: Optional[int] = None
    duration: Optional[int] = None
