from fastapi import APIRouter
from src.config import settings

from src.api.v1.routers.user import router as user_router

router = APIRouter(
    prefix=settings.api.v1.prefix
)

router.include_router(
    router=user_router,
    prefix=settings.api.v1.user
)

