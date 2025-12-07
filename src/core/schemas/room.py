from typing import (
    List,
    Optional,
    TYPE_CHECKING     
)
from datetime import datetime
from pydantic import BaseModel

if TYPE_CHECKING:
    from src.core.schemas import UserRead

class RoomBase(BaseModel):
    address: str
    created_at: datetime

class RoomRead(RoomBase):
    users: Optional[List['UserRead']]

class RoomCreate(RoomBase):
    ...