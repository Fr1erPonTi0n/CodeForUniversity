from fastapi import APIRouter
from .main_views import router as main_views_router
from .books import router as books_router

router = APIRouter(include_in_schema=False)

router.include_router(main_views_router)
router.include_router(books_router)