from sqlalchemy import Column, Integer, String, Boolean
from app.settings.database import Base
from dataclasses import dataclass


@dataclass
class User(Base):
    id: int
    name: str
    username: str
    admin: bool

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(127), unique=True)
    username = Column(String(127), unique=True)
    admin = Column(Boolean)

    def __repr__(self):
        return f'<User {self.name!r}>'
