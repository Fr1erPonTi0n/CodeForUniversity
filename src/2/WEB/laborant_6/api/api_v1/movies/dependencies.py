from fastapi import HTTPException, status, Depends
from typing import Annotated
from .crud import storage
from schemas import Movie


def prefetch_movie(slug: str) -> Movie:
    movie = storage.get_by_slug(slug)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Фильм с slug '{slug}' не найден",
    )


MovieDep = Annotated[Movie, Depends(prefetch_movie)]
