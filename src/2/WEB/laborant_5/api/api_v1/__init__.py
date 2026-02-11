from fastapi import APIRouter
from .books.views import router as books_router
from .movies.views import router as movies_router

router = APIRouter(prefix="/api/v1")
router.include_router(books_router)
router.include_router(movies_router)