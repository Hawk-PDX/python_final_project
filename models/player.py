from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class Player(BaseModel):
    __tablename__ = 'players'

    # Unique attributes
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    health = Column(Integer, default=100)  # Default health in %
    mana = Column(Integer, default=100)    # Default mana in %
    role = Column(String, nullable=False)  # Player role (e.g., Paladin, Mage, Rogue, Ranger)
    attack = Column(Integer, default=10)   # Default attack power
    defense = Column(Integer, default=5)   # Default defense

    # Relationships
    games = relationship("Game", secondary="player_games", back_populates="players")
    items = relationship("Item", back_populates="player")

    def __repr__(self):
        return f"<Player name={self.name}, role={self.role}, health={self.health}>"