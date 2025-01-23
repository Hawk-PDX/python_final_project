from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Enemy(Base):
    __tablename__ = "enemies"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Define the relationship to the Game model
    games = relationship("Game", secondary="game_enemies", back_populates="enemies")

    health = Column(Integer, default=100)
    attack = Column(Integer, default=10)
    defense = Column(Integer, default=5)

    def __repr__(self):
        return f"Enemy(id={self.id}, name='{self.name}', health={self.health}, attack={self.attack}, defense={self.defense})"