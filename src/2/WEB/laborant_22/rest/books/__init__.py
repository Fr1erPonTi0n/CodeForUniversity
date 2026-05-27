from .list_views import router as list_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(list_router,
                      include_in_schema=False)
