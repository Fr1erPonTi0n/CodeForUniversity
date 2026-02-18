from fastapi import APIRouter, HTTPException, status
from schemas import Book, BookCreate
from ..crud import storage

router = APIRouter(tags=["books"])


@router.get(
    "/",
    response_model=list[Book],
    summary="Получить все книги",
    description="Возвращает список всех книг в каталоге"
)
def get_books():
    return storage.get_all()


@router.post(
    "/",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
    summary="Создать книгу",
    description="Создает новую книгу в каталоге"
)
def create_book(book_in: BookCreate) -> Book:
    book = storage.create(book_in)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"Книга с slug '{book_in.slug}' уже существует"
    )
