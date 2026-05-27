from .books.views.list_views import router as books_router

from fastapi import APIRouter

router = APIRouter(prefix="/api_v1")

router.include_router(books_router)
