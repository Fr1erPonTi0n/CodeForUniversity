from pydantic import BaseModel
from typing import Optional
from schemas import Movie, MovieCreate, MovieUpdate, MoviePartialUpdate


class MoviesStorage(BaseModel):
    slug_to_movie: dict[str, Movie] = {}

    def get_all(self) -> list[Movie]:
        return list(self.slug_to_movie.values())

    def get_by_slug(self, slug: str) -> Optional[Movie]:
        return self.slug_to_movie.get(slug)

    def create(self, movie_in: MovieCreate) -> Movie | bool:
        if movie_in.slug not in self.slug_to_movie:
            movie = Movie(**movie_in.model_dump())
            self.slug_to_movie[movie.slug] = movie
            return movie
        return False

    def delete_by_slug(self, slug: str) -> bool:
        if slug in self.slug_to_movie:
            del self.slug_to_movie[slug]
            return True
        return False

    def delete(self, movie: Movie) -> bool:
        return self.delete_by_slug(slug=movie.slug)

    def update(self, movie: Movie, movie_in: MovieUpdate) -> Movie:
        for field, value in movie_in:
            setattr(movie, field, value)
        self.slug_to_book[movie.slug] = movie
        return movie

    def partial_update(self, movie: Movie, movie_in: MoviePartialUpdate) -> Movie:
        for field, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field, value)
        self.slug_to_book[movie.slug] = movie
        return movie

storage = MoviesStorage()

storage.create(
    MovieCreate(
        slug="harry",
        title="Harry Potter",
        description="Some description",
        year=2002,
        duration=150,
    )
)

storage.create(
    MovieCreate(
        slug="ring",
        title="Lord's of the ring",
        description="Some description",
        year=2000,
        duration=200,
    )
)
