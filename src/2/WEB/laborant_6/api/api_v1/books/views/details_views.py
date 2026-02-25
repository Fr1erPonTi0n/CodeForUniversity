from fastapi import APIRouter, status, Depends
from schemas import Book, BookUpdate, BookPartialUpdate
from ..crud import storage
from ..dependencies import BookDep, api_token_required

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

router = APIRouter(tags=["books"],
                   dependencies=[Depends(api_token_required)],
                   responses=COMMON_404_RESPONSE)

@router.get(
    "/{slug}",
    response_model=Book,
    summary="Получить книгу по slug",
    description="Возвращает детальную информацию о книге по ее slug",
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
)
def delete_book(
        book: BookDep,
):
    storage.delete(book)
    return None
