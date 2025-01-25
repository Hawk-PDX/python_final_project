from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    char_class = Column(String, nullable=False)
    char_role = Column(String, nullable=False)

    user = relationship("User ", back_populates="players")
    games = relationship("Game", back_populates="player")
    items = relationship("Item", back_populates="player")

    def __repr__(self):
        return f"Player(id={self.id}, name='{self.name}', user_id={self.user_id}, char_class='{self.char_class}', char_role='{self.char_role}')"