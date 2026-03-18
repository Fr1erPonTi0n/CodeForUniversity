from fastapi import (
    APIRouter,
    status,
    Depends,
)

from api.api_v1.books.crud import storage
from api.api_v1.books.dependencies import (
    api_token_required,
    basic_user_auth,
    user_auth_or_api_token_required,
)
from schemas.book import Book, BookCreate

router = APIRouter(
    prefix="/books",
    tags=["Books"],
    dependencies=[
        # Depends(api_token_required),
        # Depends(basic_user_auth)
        Depends(user_auth_or_api_token_required)
    ],
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
)
def create_book(
    book_in: BookCreate,
) -> Book:
    return storage.create(book_in=book_in)
