from .base import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Item(BaseModel):
    __tablename__ = 'items'
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    value = Column(Integer, default=0)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    player = relationship("Player", back_populates="items")