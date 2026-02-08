from .storage import storage

def get_movies():
    return storage.get_all()

def get_movie_by_slug(slug: str):
    return storage.get_by_slug(slug)

def create_movie(movie_in):
    return storage.create(movie_in)

def delete_movie_by_slug(slug: str):
    return storage.delete_by_slug(slug)