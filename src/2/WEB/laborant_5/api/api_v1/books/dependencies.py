from fastapi import HTTPException, status, Depends
from typing import Annotated
from .crud import storage
from schemas import Book


def prefetch_book(slug: str) -> Book:
    book = storage.get_by_slug(slug)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Книга с slug '{slug}' не найдена",
    )


BookDep = Annotated[Book, Depends(prefetch_book)]