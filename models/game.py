from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    char_class = Column(String, nullable=False)
    char_role = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)

    # Define the relationship to the Player model
    player = relationship("Player", back_populates="games")

    # Define the relationship to the Enemy model
    enemies = relationship("Enemy", secondary="game_enemies", back_populates="games")

    def __repr__(self):
        return f"Game(id={self.id}, name='{self.name}', description='{self.description}', char_class='{self.char_class}', char_role='{self.char_role}', player_id={self.player_id})"