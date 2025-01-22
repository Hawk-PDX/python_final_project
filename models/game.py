from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class Game(BaseModel):
    __tablename__ = 'games'

    # Unique attributes
    name = Column(String, nullable=False)
    description = Column(String)
    char_class = Column(String)
    char_role = Column(String)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)

    # Relationships
    enemies = relationship("Enemy", secondary="game_enemies", back_populates="game")
    players = relationship("Player", back_populates="games")

    def __repr__(self):
        return f"<Game name={self.name}, description={self.description}>"