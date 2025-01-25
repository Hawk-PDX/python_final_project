from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)

    player = relationship("Player", back_populates="games")
    enemies = relationship("Enemy", back_populates="game")

    def __repr__(self):
        return f"Game(id={self.id}, name='{self.name}', description='{self.description}', player_id={self.player_id})"