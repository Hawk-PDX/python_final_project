from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Enemy(Base):
    __tablename__ = 'enemies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    health = Column(Integer, nullable=False, default=100)
    attack = Column(Integer, nullable=False, default=10)
    defense = Column(Integer, nullable=False, default=5)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)

    game = relationship('Game', back_populates='enemies')

    def __repr__(self):
        return f"Enemy(id={self.id}, name='{self.name}', game_id={self.game_id}, health={self.health}, attack={self.attack}, defense={self.defense})"