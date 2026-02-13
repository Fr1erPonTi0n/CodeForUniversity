from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from .dependencies import Book, BookUpdate, BookPartialUpdate
from .crud import storage

router = APIRouter(tags=["books"])


def prefetch_book(slug: str) -> Book:
    book = storage.get_by_slug(slug)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Книга с slug '{slug}' не найдена",
    )


BookDep = Annotated[Book, Depends(prefetch_book)]

COMMON_404_RESPONSE = {
    status.HTTP_404_NOT_FOUND: {
        "description": "Книга не найдена",
        "content": {
            "application/json": {
                "example": {"detail": "Книга с slug 'harry' не найдена"}
            }
        },
    }
}


@router.get(
    "/{slug}",
    response_model=Book,
    summary="Получить книгу по slug",
    description="Возвращает детальную информацию о книге по ее slug",
    responses=COMMON_404_RESPONSE
)
def get_book_details_by_slug(
        book: BookDep,
) -> Book:
    return book


@router.put(
    "/{slug}",
    response_model=Book,
    summary="Полное обновление книги",
    description="Полностью обновляет информацию о книге",
    responses=COMMON_404_RESPONSE
)
def update_book(
        book: BookDep,
        book_in: BookUpdate,
) -> Book:
    return storage.update(book, book_in)


@router.patch(
    "/{slug}",
    response_model=Book,
    summary="Частичное обновление книги",
    description="Частично обновляет информацию о книге",
    responses=COMMON_404_RESPONSE
)
def partial_update_book(
        book: BookDep,
        book_in: BookPartialUpdate,
) -> Book:
    return storage.partial_update(book, book_in)


@router.delete(
    "/{slug}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить книгу",
    description="Удаляет книгу из каталога по ее slug",
    responses={
        **COMMON_404_RESPONSE,
        status.HTTP_204_NO_CONTENT: {
            "description": "Книга успешно удалена",
            "content": None
        }
    }
)
def delete_book(
        book: BookDep,
):
    storage.delete(book)
    return None
