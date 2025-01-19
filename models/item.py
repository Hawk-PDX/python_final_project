from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    value = Column(Integer, default=0)
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship("Player", back_populates="items")
    drops = relationship("Drop", back_populates="item") # might need drop from this file