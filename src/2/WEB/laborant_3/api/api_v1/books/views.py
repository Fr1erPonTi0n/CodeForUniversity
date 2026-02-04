from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from .dependencies import Book, BookCreate
from .crud import BOOKS

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=list[Book])
def get_books():
    return BOOKS

@router.post("/", response_model=Book)
def create_book(book_in: BookCreate) -> Book:
    return Book(**book_in.model_dump())

def prefetch_book(slug: str) -> Book:
    book: Book | None = next(
        (book for book in BOOKS if book.slug == slug),
        None,
    )
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Slug {slug!r} not found",
    )

@router.get("/{slug}")
def get_book_details_by_slug(
    book: Annotated[Book, Depends(prefetch_book)],
) -> Book | None:
    return book