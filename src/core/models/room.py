from typing import TYPE_CHECKING
from typing import List
from datetime import datetime
from src.core.models import Base

from sqlalchemy import (
    DateTime,
    UUID
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

if TYPE_CHECKING:
    from core.models import UserRoomAssociation


class Room(Base):
    __tablename__ = 'rooms'
    
    address: Mapped[str] = mapped_column(UUID, unique=True, primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    
    user_association: Mapped[List['UserRoomAssociation']] = relationship(
        back_populates='user'
    )
    
    @property
    def users(self):
        return [assoc.user for assoc in self.user_association]