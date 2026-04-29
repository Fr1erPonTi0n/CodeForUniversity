from typing import Annotated

from fastapi import (
    Depends,
    status,
    APIRouter,
)

from api.api_v1.books.crud import storage
from api.api_v1.books.dependencies import prefetch_book
from schemas.book import (
    Book,
    BookUpdate,
    BookPartialUpdate,
)

router = APIRouter(
    prefix="/{slug}",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Book not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Book 'slug' not found",
                    },
                },
            },
        },
    },
)

book_by_slug = Annotated[Book, Depends(prefetch_book)]


@router.get(
    "/",
    response_model=Book,
)
def get_book_details_by_slug(
    book: book_by_slug,
) -> Book | None:
    return book


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_by_slug(
    book: book_by_slug,
) -> None:
    storage.delete(book=book)


@router.put(
    "/",
    response_model=Book,
)
def update_book(
    book: book_by_slug,
    book_in: BookUpdate,
):
    return storage.update(book=book, book_in=book_in)


@router.patch(
    "/",
    response_model=Book,
)
def partial_update_book(
    book: book_by_slug,
    book_in: BookPartialUpdate,
):
    return storage.partial_update(
        book=book,
        book_in=book_in,
    )
