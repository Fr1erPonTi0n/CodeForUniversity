from fastapi import APIRouter
from rest.main_views import router as main_views_router

router = APIRouter()

router.include_router(main_views_router,
                      include_in_schema=False)