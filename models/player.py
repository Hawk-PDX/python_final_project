from .base import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Player(BaseModel):
    __tablename__ = 'players'
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User ", back_populates="players")
    health = Column(Integer, default=100)
    attack = Column(Integer, default=10)
    defense = Column(Integer, default=5)
    level = Column(Integer, default=1)
    skills = Column(String)
    health_potions = Column(Integer, default=2)
    games = relationship("Game", back_populates="player")
    items = relationship("Item", back_populates="player")