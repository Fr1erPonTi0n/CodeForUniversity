from .list_views import router as list_router
from .details_views import router as details_router
from fastapi import APIRouter

router = APIRouter(prefix="/movies", tags=["movies"])
router.include_router(list_router)
router.include_router(details_router)