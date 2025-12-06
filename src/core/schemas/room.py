from datetime import datetime
from pydantic import BaseModel


class RoomBase(BaseModel):
    address: str
    created_at: datetime