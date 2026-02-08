from pydantic import BaseModel
from typing import Optional
from .dependencies import Movie, MovieCreate

class MoviesStorage(BaseModel):
    slug_to_movie: dict[str, Movie] = {}

    def get_all(self) -> list[Movie]:
        return list(self.slug_to_movie.values())
    
    def get_by_slug(self, slug: str) -> Optional[Movie]:
        return self.slug_to_movie.get(slug)
    
    def create(self, movie_in: MovieCreate) -> Movie:
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

storage = MoviesStorage()

storage.slug_to_movie = {
    "Harry": Movie(
        slug="Harry",
        title="Harry Potter",
        description="Some description",
        year=2002,
        duration=150,
    ),
    "Ring": Movie(
        slug="Ring",
        title="Lord's of the ring",
        description="Some description",
        year=2000,
        duration=200,
    ),
}