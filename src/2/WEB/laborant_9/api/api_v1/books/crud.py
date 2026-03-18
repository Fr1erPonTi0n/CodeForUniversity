from pydantic import BaseModel

from schemas.book import Book, BookCreate, BookUpdate, BookPartialUpdate


class BooksStorage(BaseModel):
    slug_to_book: dict[str, Book] = {}

    def get(self) -> list[Book]:
        return list(self.slug_to_book.values())

    def get_by_slug(self, slug: str) -> Book | None:
        return self.slug_to_book.get(slug)

    def create(self, book_in: BookCreate) -> Book:
        book = Book(**book_in.model_dump())
        self.slug_to_book[book.slug] = book
        return book

    def delete_by_slug(self, slug: str) -> None:
        self.slug_to_book.pop(slug, None)

    def delete(self, book: Book) -> None:
        self.delete_by_slug(slug=book.slug)

    def update(
        self,
        book: Book,
        book_in: BookUpdate,
    ) -> Book:
        for field, value in book_in:
            setattr(book, field, value)
        self.slug_to_book[book.slug] = book
        return book

    def partial_update(
        self,
        book: Book,
        book_in: BookPartialUpdate,
    ) -> Book:
        for field, value in book_in.model_dump(exclude_unset=True).items():
            setattr(book, field, value)
        self.slug_to_book[book.slug] = book
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
