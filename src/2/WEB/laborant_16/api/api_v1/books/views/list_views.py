from fastapi import (
    APIRouter,
    status,
    Depends,
    HTTPException,
)

from api.api_v1.books.crud import storage
from api.api_v1.books.dependencies import (
    user_auth_or_api_token_required,
)
from schemas.book import Book, BookCreate

router = APIRouter(
    prefix="/books",
    tags=["Books"],
    dependencies=[Depends(user_auth_or_api_token_required)],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Unauthorized. Only for unsafe methods.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid API token",
                    },
                }
            },
        }
    },
)


@router.get(
    "/",
    response_model=list[Book],
)
def get_books():
    return storage.get()


@router.post(
    "/",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "Book already exists",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Book with slug='name' already exists.",
                    },
                },
            },
        },
    },
)
def create_book(
    book_in: BookCreate,
) -> Book:
    if not (storage.get_by_slug(book_in.slug)):
        return storage.create(book_in=book_in)
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"Book with slug={book_in.slug!r} already exists",
    )
