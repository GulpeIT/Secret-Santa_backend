from typing import List
from typing import TYPE_CHECKING

from src.core.models import Base

from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from src.core.models.room import Room

if TYPE_CHECKING:
    from src.core.models import (
        UserRoomAssociation,
    )


class User(Base):
    __tablename__ = 'users'
    
    username: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
    surname: Mapped[str]
    phone_number: Mapped[str] = mapped_column(String(length=11), unique=True)
    
    room_association: Mapped[List['UserRoomAssociation']] = relationship(
        back_populates='room'
    )
    
    @property
    def rooms(self) -> List[Room]:
        return [assoc.room for assoc in self.room_association]
