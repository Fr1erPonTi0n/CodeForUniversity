from fastapi import (
    APIRouter,
    status,
    Depends,
    HTTPException,
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
    responses={
        409: {"description": "Книга с таким заголовком уже существует"},
    }
)
def create_book(
    book_in: BookCreate,
) -> Book:
    existing_book = storage.get_by_slug(book_in.slug)
    if existing_book:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Книга с таким заголовком '{book_in.slug}' уже существует"
        )
    return storage.create(book_in=book_in)
