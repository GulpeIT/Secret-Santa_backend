from typing import Annotated
from src.config import settings

from sqlalchemy import MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)
from sqlalchemy.ext.asyncio import AsyncAttrs

id_pk = Annotated[int, mapped_column(autoincrement=True, primary_key=True)]

class Base(DeclarativeBase, AsyncAttrs):
    metadata = MetaData(naming_convention=settings.db.naming_convention)
    
    id: Mapped[id_pk]