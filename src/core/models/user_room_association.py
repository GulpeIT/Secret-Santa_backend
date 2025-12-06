from typing import Optional
from typing import TYPE_CHECKING

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models import Base

if TYPE_CHECKING:
    from core.models import User
    from core.models import Room

class UserRoomAssociation(Base):
    __tablename__ = "users_rooms"
    
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)
    id_room: Mapped[int] = mapped_column(ForeignKey('rooms.id'), primary_key=True)
    join_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    role: Mapped[Optional[str]] = mapped_column(String(50), default="member")
    want_gift: Mapped[str] = mapped_column()
    
    user: Mapped["User"] = relationship(
        back_populates="user_association",
    )
    room: Mapped["Room"] = relationship(
        back_populates="room_association",
    )