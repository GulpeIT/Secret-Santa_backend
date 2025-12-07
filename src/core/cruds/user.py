from sqlalchemy.ext.asyncio import AsyncSession

from src.core.schemas import (
    UserBase,
    UserCreate,
)

async def create(
    session: AsyncSession,
    schemas: UserCreate
    ):
    return ...