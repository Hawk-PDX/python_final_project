from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    # Unique attributes
    username = Column(String, unique=True, nullable=False, index=True)  # Indexed for faster queries
    email = Column(String, unique=True, nullable=False, index=True)     # Indexed for faster queries
    password = Column(String, nullable=False)

    # Relationships
    players = relationship("Player", secondary="user_players", back_populates="user")

    def __repr__(self):
        return f"<User    username={self.username}, email={self.email}>"