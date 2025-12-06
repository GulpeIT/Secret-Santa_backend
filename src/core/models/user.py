from typing import List
from typing import TYPE_CHECKING

from src.core.models import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import UserRoomAssociation


class User(Base):
    __tablename__="users"
    
    name: Mapped[str]
    surname: Mapped[str]
    
    room_association: Mapped[List["UserRoomAssociation"]] = relationship(
        back_populates="room"
    )
    
    @property
    def rooms(self):
        return [assoc.room for assoc in self.room_association]
