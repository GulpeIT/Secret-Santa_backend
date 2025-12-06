from typing import Optional
from typing import TYPE_CHECKING
from datetime import datetime
from src.core.models import Base

from sqlalchemy import (
    DateTime,
    ForeignKey,
    String,
    Text
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

if TYPE_CHECKING:
    from src.core.models import (
        User,
        Room,
    )


class UserRoomAssociation(Base):
    __tablename__ = 'users_rooms'
    
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)
    id_room: Mapped[int] = mapped_column(ForeignKey('rooms.id'), primary_key=True)
    join_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    role: Mapped[Optional[str]] = mapped_column(String(50), default='member')
    want_gift: Mapped[str] = mapped_column(Text, nullable=True)
    
    user: Mapped['User'] = relationship(
        back_populates='user_association',
    )
    room: Mapped['Room'] = relationship(
        back_populates='room_association',
    )