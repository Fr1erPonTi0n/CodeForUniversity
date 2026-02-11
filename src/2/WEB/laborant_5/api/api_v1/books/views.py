from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from .dependencies import Book, BookCreate
from .crud import storage

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=list[Book])
def get_books():
    return storage.get_all()

@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_in: BookCreate) -> Book:
    book = storage.create(book_in)
    if book:
        return book
    raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Книга с slug '{book_in.slug}' уже существует"
            )

def prefetch_book(slug: str) -> Book:
    book = storage.get_by_slug(slug)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Книга с slug '{slug}' не найден",
    )

@router.get("/{slug}")
def get_book_details_by_slug(
    book: Annotated[Book, Depends(prefetch_book)],
) -> Book | None:
    return book

@router.delete("/{slug}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
    book: Annotated[Book, Depends(prefetch_book)],
):
    storage.delete(book)
    return None