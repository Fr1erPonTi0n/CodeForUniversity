from pydantic import BaseModel
from typing import Optional
from .dependencies import Book, BookCreate

class BooksStorage(BaseModel):
    slug_to_book: dict[str, Book] = {}

    def get_all(self) -> list[Book]:
        return list(self.slug_to_book.values())
    
    def get_by_slug(self, slug: str) -> Optional[Book]:
        return self.slug_to_book.get(slug)
    
    def create(self, book_in: BookCreate) -> Book:
        if book_in.slug not in self.slug_to_book:
            book = Book(**book_in.model_dump())
            self.slug_to_book[book.slug] = book
            return book
        return False
    
    def delete_by_slug(self, slug: str) -> bool:
        if slug in self.slug_to_book:
            del self.slug_to_book[slug]
            return True
        return False
    
    def delete(self, book: Book) -> bool:
        return self.delete_by_slug(slug=book.slug)
    
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