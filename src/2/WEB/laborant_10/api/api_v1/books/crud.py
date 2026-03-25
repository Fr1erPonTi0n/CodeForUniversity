from pydantic import BaseModel

from schemas.book import Book, BookCreate, BookUpdate, BookPartialUpdate
from redis import Redis
from core import config

redis = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_BOOKS,
    decode_responses=True
)

class BooksStorage(BaseModel):
    slug_to_book: dict[str, Book] = {}

    @classmethod
    def save_book(cls, book: Book):
        redis.hset(
            name=config.REDIS_BOOKS_HASH_NAME, 
            key=book.slug, 
            value=book.model_dump_json()
            )
        
    def get(self) -> list[Book]:
        all_books = redis.hvals(name=config.REDIS_BOOKS_HASH_NAME)
        books = []
        for book_json in all_books:
            books.append(Book.model_validate_json(book_json))
        return books

    def get_by_slug(self, slug: str) -> Book | None:
        data = redis.hget(
            name=config.REDIS_BOOKS_HASH_NAME,
            key=slug
        )
        if data:
            return Book.model_validate_json(data)
        return None

    def create(self, book_in: BookCreate) -> Book:
        book = Book(**book_in.model_dump())
        self.save_book(book=book)
        return book

    def delete_by_slug(self, slug: str) -> None:
        redis.hdel(config.REDIS_BOOKS_HASH_NAME, slug)

    def delete(self, book: Book) -> None:
        self.delete_by_slug(slug=book.slug)

    def update(
        self,
        book: Book,
        book_in: BookUpdate,
    ) -> Book:
        for field, value in book_in:
            setattr(book, field, value)
        self.save_book(book=book)
        return book

    def partial_update(
        self,
        book: Book,
        book_in: BookPartialUpdate,
    ) -> Book:
        for field, value in book_in.model_dump(exclude_unset=True).items():
            setattr(book, field, value)
        self.save_book(book=book)
        return book


storage = BooksStorage()


storage.create(
    BookCreate(
        title="Harry Potter",
        slug="harry",
        description="Some description",
        pages=400,
    )
)

storage.create(
    BookCreate(
        title="Lord's of the ring",
        slug="ring",
        description="Some description",
        pages=800,
    )
)
