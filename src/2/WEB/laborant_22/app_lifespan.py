from fastapi import FastAPI

from storage.books import BooksStorage

async def lifespan(app: FastAPI):
    app.state.books_storage = BooksStorage()
    yield