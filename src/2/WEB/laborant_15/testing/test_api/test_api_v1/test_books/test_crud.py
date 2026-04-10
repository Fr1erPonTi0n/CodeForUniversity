from unittest import TestCase
from schemas.book import BookCreate, BookUpdate, BookPartialUpdate
from api.api_v1.books.crud import storage
import random

def create_str(n1, n2) -> str:
    return ''.join([random.choice('denikodem1488') for _ in range(random.randint(n1, n2))])

def total(n1, n2):
    return n1 + n2

class TotalTestCase(TestCase):
    def test_total(self) -> None:
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        result = total(n1, n2)
        expected_result = n1 + n2
        self.assertEqual(result, expected_result)

class BooksStorageUpdateTestCase(TestCase):
    books = []
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass() 
        cls.books = [
            cls.create_book(
                slug=create_str(4, 19),
                description=create_str(10, 30),
                title=create_str(8, 16),
                pages=random.randint(20, 300)
            )
            for i in range(3)
        ]
        for book in cls.books:
            storage.create(book)
    
    @classmethod
    def tearDownClass(cls):
        for book in cls.books:
            storage.delete(book)
        super().tearDownClass()
    
    @classmethod
    def create_book(cls,
                         slug='some slug',
                         description='some description',
                         title='some title',
                         pages=123):
        return BookCreate(
            slug=slug,
            description=description,
            title=title,
            pages=pages
        )

    def setUp(self):
        self.book = self.create_book(
            slug=create_str(4, 19),
            description=create_str(10, 30),
            title=create_str(8, 16),
            pages=random.randint(20, 300)
        )

    def tearDown(self):
        storage.delete(self.book)

    def test_update(self) -> None:
        book_update = BookUpdate(
            **self.book.model_dump(),
        )
        source_descriprion = self.book.description
        book_update.description *= 2
        updated_book = storage.update(
            book=self.book,
            book_in=book_update
        )

        self.assertNotEqual(
            source_descriprion,
            updated_book.description
        )
        self.assertEqual(
            book_update.description,
            updated_book.description
        )

    def test_partical_update(self) -> None:
        source_title = self.book.title
        source_pages = self.book.pages
        source_slug = self.book.slug
        
        new_description = self.book.description * 2
        book_partial_update = BookPartialUpdate(
            description=new_description
        )
        
        updated_book = storage.partial_update(
            book=self.book,
            book_in=book_partial_update
        )
        
        self.assertEqual(
            new_description,
            updated_book.description
        )
        
        self.assertEqual(
            source_title,
            updated_book.title
        )
        self.assertEqual(
            source_pages,
            updated_book.pages
        )
        self.assertEqual(
            source_slug,
            updated_book.slug
        )
    
    def test_get_list(self) -> None:
        all_books = storage.get()
        
        expected_slugs = [book.slug for book in self.__class__.books]
        actual_slugs = [book.slug for book in all_books]
        
        for expected_slug in expected_slugs:
            self.assertIn(
                expected_slug,
                actual_slugs,
                f"Expected slug '{expected_slug}' not found in {actual_slugs}"
            )
        
        self.assertGreaterEqual(
            len(all_books),
            len(expected_slugs),
            f"Expected at least {len(expected_slugs)} books, got {len(all_books)}"
        )
    
    def test_get_by_slug(self) -> None:
        for expected_book in self.__class__.books:
            with self.subTest(book_slug=expected_book.slug):
                retrieved_book = storage.get_by_slug(expected_book.slug)
            
                self.assertIsNotNone(
                    retrieved_book,
                    f"Book with slug '{expected_book.slug}' not found"
                )
                
                self.assertEqual(
                    expected_book.slug,
                    retrieved_book.slug,
                    f"Slug mismatch for book '{expected_book.slug}'"
                )
                self.assertEqual(
                    expected_book.title,
                    retrieved_book.title,
                    f"Title mismatch for book '{expected_book.slug}'"
                )
                self.assertEqual(
                    expected_book.description,
                    retrieved_book.description,
                    f"Description mismatch for book '{expected_book.slug}'"
                )
                self.assertEqual(
                    expected_book.pages,
                    retrieved_book.pages,
                    f"Pages mismatch for book '{expected_book.slug}'"
                )
        
        with self.subTest(book_slug="non-existent-slug"):
            non_existent = storage.get_by_slug("non-existent-slug")
            self.assertIsNone(
                non_existent,
                "Getting non-existent book should return None"
            )