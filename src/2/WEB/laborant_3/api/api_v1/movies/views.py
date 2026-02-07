from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from .dependencies import Movie, MovieCreate
from .crud import MOVIES

router = APIRouter(prefix="/movies", tags=["movies"])

@router.get("/", response_model=list[Movie])
def get_list_movies():
    return MOVIES

@router.post("/", response_model=Movie)
def create_movie(movie_in: MovieCreate) -> Movie:
    return Movie(**movie_in.model_dump())

def prefetch_movie(slug: str) -> Movie:
    movie: Movie | None = next(
        (movie for movie in MOVIES if movie.slug == slug),
        None,
    )
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Slug {slug!r} not found",
    )

@router.get("/{slug}")
def get_movie_details_by_slug(
    movie: Annotated[Movie, Depends(prefetch_movie)],
) -> Movie | None:
    return movie