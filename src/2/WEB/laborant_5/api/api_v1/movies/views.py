from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from .dependencies import Movie, MovieCreate
from .crud import storage

router = APIRouter(prefix="/movies", tags=["movies"])

@router.get("/", response_model=list[Movie])
def get_list_movies():
    return storage.get_all()

@router.post("/", response_model=Movie, status_code=status.HTTP_201_CREATED)
def create_movie(movie_in: MovieCreate) -> Movie:
    movie = storage.create(movie_in)
    if movie:
        return movie
    raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Фильм с slug '{movie_in.slug}' уже существует"
            )

def prefetch_movie(slug: str) -> Movie:
    movie = storage.get_by_slug(slug)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Фильм с slug '{slug}' не найден",
    )

@router.get("/{slug}")
def get_movie_details_by_slug(
    movie: Annotated[Movie, Depends(prefetch_movie)],
) -> Movie | None:
    return movie

@router.delete("/{slug}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(
    movie: Annotated[Movie, Depends(prefetch_movie)],
):
    storage.delete(movie)
    return None