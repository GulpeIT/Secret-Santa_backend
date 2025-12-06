from typing import TYPE_CHECKING
from typing import List

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from src.core.models import Base

if TYPE_CHECKING:
    from core.models import UserRoomAssociation


class Room(Base):
    __tablename__ = "rooms"
    
    address: Mapped[str] = mapped_column(unique=True)
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    
    user_association: Mapped[List["UserRoomAssociation"]] = relationship(
        back_populates="user"
    )
    
    @property
    def user(self):
        return [assoc.user for assoc in self.user_association]