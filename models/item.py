from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    player = relationship("Player", backref="items")
    value = Column(Integer, default=0)

    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', type='{self.type}', player_id={self.player_id}, value={self.value})"