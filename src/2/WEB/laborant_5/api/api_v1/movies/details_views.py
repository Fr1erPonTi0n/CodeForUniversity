from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from .dependencies import Movie, MovieUpdate, MoviePartialUpdate
from .crud import storage

router = APIRouter(tags=["movies"])


def prefetch_movie(slug: str) -> Movie:
    movie = storage.get_by_slug(slug)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Фильм с slug '{slug}' не найден",
    )


MovieDep = Annotated[Movie, Depends(prefetch_movie)]

COMMON_404_RESPONSE = {
    status.HTTP_404_NOT_FOUND: {
        "description": "Фильм не найден",
        "content": {
            "application/json": {
                "example": {"detail": "Фильм с slug 'harry' не найден"}
            }
        },
    }
}


@router.get(
    "/{slug}",
    response_model=Movie,
    summary="Получить фильм по slug",
    description="Возвращает детальную информацию о фильме по его slug",
    responses=COMMON_404_RESPONSE
)
def get_movie_details_by_slug(
        movie: MovieDep,
) -> Movie:
    return movie


@router.put(
    "/{slug}",
    response_model=Movie,
    summary="Полное обновление фильма",
    description="Полностью обновляет информацию о фильме",
    responses=COMMON_404_RESPONSE
)
def update_movie(
        movie: MovieDep,
        movie_in: MovieUpdate,
) -> Movie:
    return storage.update(movie, movie_in)


@router.patch(
    "/{slug}",
    response_model=Movie,
    summary="Частичное обновление фильма",
    description="Частично обновляет информацию о фильме",
    responses=COMMON_404_RESPONSE
)
def partial_update_movie(
        movie: MovieDep,
        movie_in: MoviePartialUpdate,
) -> Movie:
    return storage.partial_update(movie, movie_in)


@router.delete(
    "/{slug}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить фильм",
    description="Удаляет фильм из каталога по его slug",
    responses={
        **COMMON_404_RESPONSE,
        status.HTTP_204_NO_CONTENT: {
            "description": "Фильм успешно удален",
            "content": None
        }
    }
)
def delete_movie(
        movie: MovieDep,
):
    storage.delete(movie)
    return None
