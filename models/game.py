from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    char_class = Column(String, nullable=False)
    char_role = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    player = relationship("Player", backref="games")

    def __repr__(self):
        return f"Game(id={self.id}, name='{self.name}', description='{self.description}', char_class='{self.char_class}', char_role='{self.char_role}', player_id={self.player_id})"