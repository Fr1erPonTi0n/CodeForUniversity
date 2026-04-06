from unittest import TestCase
from schemas.book import BookCreate, Book, BookUpdate, BookPartialUpdate
from pydantic import ValidationError
class BookCreateTestCase(TestCase):
    def test_book_can_be_created_from_create_schema(self) -> None:
        book_in = BookCreate(
            slug='some slug',
            description='some description',
            title='some title',
            pages=123
        )
        book = Book(**book_in.model_dump())
        self.assertEqual(book_in.slug, book.slug)
        self.assertEqual(book_in.description, book.description)
        self.assertEqual(book_in.title, book.title)
        self.assertEqual(book_in.pages, book.pages)

    def test_book_create_accepts_different_slug(self) -> None:
        slugs = [
            'foobar',
            'bar',
            'r',
            'some-slug',
            'new-some-slug-new-some-slug-new-some-slug-new-some-slug',
            'new',
        ]
        for slug in slugs:
            with self.subTest(slug=slug, msg=f'test-slug-{slug}'):
                book_in = BookCreate(
                    slug=slug,
                    title='some title',
                    description='some descriprion',
                    pages=100,
                )
                self.assertEqual(slug, book_in.slug)

    def test_book_create_accepts_different_pages(self) -> None:
        pages_books = [
            9,
            100,
            10.10,
            0.99,
            42,
            67,
        ]
        for pages in pages_books:
            with self.subTest(pages=pages, msg=f'test-pages-{pages}'):
                book_in = BookCreate(
                    slug='some title',
                    title='some title',
                    description='some descriprion',
                    pages=pages,
                )
                self.assertEqual(pages, book_in.pages)

    def test_book_slug_too_long(self) -> None:
        with self.assertRaises(
            expected_exception=ValidationError,
        ) as exc_info:
            book_in = BookCreate(
                            slug='r' * 31,
                            title='some title',
                            description='some descriprion',
                            pages=100,
                        )
        detail_type = exc_info.exception.errors()[0]
        exception_type = "string_too_long"
        self.assertEqual(exception_type, detail_type['type'])
        
    def test_book_slug_too_long_with_regex(self) -> None:
        with self.assertRaisesRegex(
                expected_exception=ValidationError,
                expected_regex='String should have at most 30 characters'
            ) as exc_info:
                book_in = BookCreate(
                            slug='r' * 31,
                            title='some title',
                            description='some descriprion',
                            pages=100,
                        )
        detail_type = exc_info.exception.errors()[0]
        exception_type = "string_too_long"
        self.assertEqual(exception_type, detail_type['type'])

    def test_book_slug_too_short(self) -> None:
        with self.assertRaises(
            expected_exception=ValidationError,
        ) as exc_info:
            book_in = BookCreate(
                            slug='r',
                            title='some title',
                            description='some descriprion',
                            pages=100,
                        )

        detail_type = exc_info.exception.errors()[0]
        exception_type = "string_too_short"
        self.assertEqual(exception_type, detail_type['type'])
    
    def test_book_slug_too_short_with_regex(self) -> None:
        with self.assertRaisesRegex(
                expected_exception=ValidationError,
                expected_regex='String should have at least 3 characters'
            ) as exc_info:
                book_in = BookCreate(
                            slug='r',
                            title='some title',
                            description='some descriprion',
                            pages=100,
                        )
        detail_type = exc_info.exception.errors()[0]
        exception_type = "string_too_short"
        self.assertEqual(exception_type, detail_type['type'])

class BookUpdateTestCase(TestCase):
    def test_book_can_be_updated_with_a_changed_description(self) -> None:
        book_create = BookCreate(
            slug='some slug',
            description='some description',
            title='some title',
            pages=123
        )
        book = Book(**book_create.model_dump())
        
        new_description = 'some description changed'
        new_title = 'some title changed'
        new_pages = 456

        book_update = BookUpdate(
            description=new_description,
            title=new_title,
            pages=new_pages
        )
        for field, value in book_update:
            setattr(book, field, value)

        self.assertEqual(book.description, new_description)
        self.assertEqual(book.title, new_title)
        self.assertEqual(book.pages, new_pages)

class BookParticalUpdate(TestCase):
    def test_partical_update_book(self) -> None:
        book = Book(
            slug='original-slug',
            description='original description',
            title='original title',
            pages=10
        )

        new_description = 'some description changed'
        new_title = 'some title changed'
        new_pages = 123

        book_partical_update = BookPartialUpdate(
            description=new_description,
            title=new_title,
            pages=new_pages,
        )
        for field, value in book_partical_update.model_dump(exclude_unset=True).items():
            setattr(book, field, value)

        self.assertEqual(book.description, new_description)
        self.assertEqual(book.title, new_title)
        self.assertEqual(book.pages, new_pages)

    def test_partical_update_book_checking_the_integrity_field_description(self) -> None:
        book = Book(
            slug='original-slug',
            description='original description',
            title='original title',
            pages=10
        )
        
        new_description = 'some description changed 1'

        book_partical_update = BookPartialUpdate(
            description=new_description,
        )
        for field, value in book_partical_update.model_dump(exclude_unset=True).items():
            setattr(book, field, value)

        self.assertEqual(book.description, new_description)

    def test_partical_update_book_checking_the_integrity_field_title(self) -> None:
        book = Book(
            slug='original-slug',
            description='original description',
            title='original title',
            pages=10
        )
        
        new_title = 'some title changed 1'

        book_partical_update = BookPartialUpdate(
            title=new_title,
        )
        for field, value in book_partical_update.model_dump(exclude_unset=True).items():
            setattr(book, field, value)

        self.assertEqual(book.title, new_title)

    def test_partical_update_book_checking_the_integrity_field_pages(self) -> None:
        book = Book(
            slug='original-slug',
            description='original description',
            title='original title',
            pages=10
        )
        
        new_pages = 67

        book_partical_update = BookPartialUpdate(
            pages=new_pages,
        )
        for field, value in book_partical_update.model_dump(exclude_unset=True).items():
            setattr(book, field, value)

        self.assertEqual(book.pages, new_pages)