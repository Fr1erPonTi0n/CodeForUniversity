from pydantic import BaseModel
from redis import Redis

from schemas.book import (
    Book,
    BookCreate,
    BookUpdate,
    BookPartialUpdate,
)
from core import config

redis = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_BOOKS,
    decode_responses=True,
)


class BooksStorage(BaseModel):

    def get(self) -> list[Book]:
        return [
            Book.model_validate_json(value)
            for value in redis.hvals(name=config.REDIS_HASH_NAME_BOOKS)
        ]

    def get_by_slug(self, slug: str) -> Book | None:
        data = redis.hget(
            name=config.REDIS_HASH_NAME_BOOKS,
            key=slug,
        )
        if data:
            return Book.model_validate_json(data)
        return None

    @classmethod
    def save_book(cls, book: Book):
        redis.hset(
            name=config.REDIS_HASH_NAME_BOOKS,
            key=book.slug,
            value=book.model_dump_json(),
        )

    def create(self, book_in: BookCreate) -> Book:
        book = Book(**book_in.model_dump())
        self.save_book(book)
        return book

    def delete_by_slug(self, slug: str) -> None:
        redis.hdel(
            config.REDIS_HASH_NAME_BOOKS,
            slug,
        )

    def delete(self, book: Book) -> None:
        self.delete_by_slug(slug=book.slug)

    def update(
        self,
        book: Book,
        book_in: BookUpdate,
    ) -> Book:
        for field, value in book_in:
            setattr(book, field, value)
        self.save_book(book)
        return book

    def partial_update(
        self,
        book: Book,
        book_in: BookPartialUpdate,
    ) -> Book:
        for field, value in book_in.model_dump(exclude_unset=True).items():
            setattr(book, field, value)
        self.save_book(book)
        return book
    
    def exists(
        self,
        slug: str
    ) -> bool:
        return redis.hexists(
            name=config.REDIS_HASH_NAME_BOOKS,
            key=slug
        )
    
    def create_or_raise_if_exists(
        self,
        book_in: BookCreate
    ) -> Book:
        if not self.exists(book_in.slug):
            return self.create(
                book_in=book_in
                )
        raise BookAlreadyExistsError(
            book_in.slug
            )
        

class BookBaseError(Exception):
    pass

class BookAlreadyExistsError(BookBaseError):
    pass

storage = BooksStorage()
