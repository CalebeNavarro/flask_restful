from sqlalchemy import Column, Integer, String, ForeignKey
from app.settings.database import Base
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Honor(Base):
    id: int
    data: datetime
    honor: int

    __tablename__ = 'honor'
    id = Column(Integer, primary_key=True)
    data = Column(String(127))
    honor = Column(Integer)

    users_id = Column(Integer, ForeignKey('users.id'))
    # users = relationship("Users", back_populates="honors")
