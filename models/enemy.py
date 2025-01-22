from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class Enemy(BaseModel):
    __tablename__ = 'enemies'

    # Unique attributes
    name = Column(String, nullable=False)
    health = Column(Integer, default=100)  # Default health in %
    attack = Column(Integer, default=10)   # Default attack power
    defense = Column(Integer, default=5)   # Default defense
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)

    # Relationships
    game = relationship("Game", back_populates="enemies")

    def __repr__(self):
        return f"<Enemy name={self.name}, health={self.health}, attack={self.attack}>"