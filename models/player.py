from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Define the relationship to the User model
    user = relationship("User", back_populates="players")  

    # Define the relationship to the Game model
    games = relationship("Game", back_populates="player")

    # Character stats
    health = Column(Integer, default=100)
    mana = Column(Integer, default=100)
    attack = Column(Integer, default=10)
    defense = Column(Integer, default=5)
    char_class = Column(String, nullable=False)  # Added character class
    char_role = Column(String, nullable=False)  # Added character role

    def __repr__(self):
        return f"Player(id={self.id}, name='{self.name}', user_id={self.user_id}, health={self.health}, mana={self.mana}, attack={self.attack}, defense={self.defense}, char_class='{self.char_class}', char_role='{self.char_role}')"