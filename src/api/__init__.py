from typing import Annotated
from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import settings
from src.core.models import db_helper


async_session = Annotated[AsyncSession, Depends(db_helper.session_getter)]

router = APIRouter(
    prefix=settings.api.prefix
)
