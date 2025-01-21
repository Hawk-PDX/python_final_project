from .base import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Enemy(BaseModel):
    __tablename__ = 'enemies'
    name = Column(String, nullable=False)
    health = Column(Integer, default=50)
    attack = Column(Integer, default=5)
    defense = Column(Integer, default=2)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)
    game = relationship("Game", back_populates="enemies")