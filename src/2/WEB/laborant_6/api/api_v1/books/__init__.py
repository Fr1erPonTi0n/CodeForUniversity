from fastapi import APIRouter
from .views import router as views_router

router = APIRouter()
router.include_router(views_router)
