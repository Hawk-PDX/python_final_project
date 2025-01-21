from .base import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Game(BaseModel):
    __tablename__ = 'games'
    name = Column(String, nullable=False)
    description = Column(String)
    char_class = Column(String)
    char_role = Column(String)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    player = relationship("Player", back_populates="games")
    level = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    enemies = relationship("Enemy", back_populates="game")