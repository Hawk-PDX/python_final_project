from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class Item(BaseModel):
    __tablename__ = 'items'

    # Unique attributes
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    value = Column(Integer, default=0)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)

    # Relationships
    player = relationship("Player", back_populates="items")

    def __repr__(self):
        return f"<Item name={self.name}, type={self.type}, value={self.value}>"