from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int = 0
    price: float = 0


def sorting_books_by_year(books):
    return sorted(books, key=lambda book: book.year)


if __name__ == '__main__':
    books = [
        Book("Убить пересмешника", "Харпер Ли", 1960, 850.0),
        Book("Преступление и наказание", "Ф. Достоевский", 1866, 1100.0),
        Book("1984", "Джордж Оруэлл", 1949, 600.0),
    ]

    sorted_books = sorting_books_by_year(books)

    for book in sorted_books:
        print(f'{book.title}, {book.author}, {book.year}, {book.price}')
