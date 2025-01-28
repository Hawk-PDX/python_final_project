from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    char_class = Column(String, nullable=False)
    char_role = Column(String, nullable=False)
    health = Column(Integer, nullable=False, default=100)
    mana = Column(Integer, nullable=False, default=100)
    attack = Column(Integer, nullable=False, default=10)
    defense = Column(Integer, nullable=False, default=5)

    user = relationship('User', back_populates='players')
    games = relationship('Game', back_populates='players')
    items = relationship('Item', back_populates='player')

    def __repr__(self):
        return f"Player(id={self.id}, name='{self.name}', user_id={self.user_id}, char_class='{self.char_class}', char_role='{self.char_role}')"