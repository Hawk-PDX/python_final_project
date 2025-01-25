# models/character.py
from sqlalchemy import Column, Integer, String
from .base import Base

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    char_class = Column(String, nullable=False)
    health = Column(Integer, nullable=False)
    mana = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    char_role = Column(String, nullable=False)

    def __repr__(self):
        return f"Character(id={self.id}, name={self.name}, class={self.char_class}, health={self.health}, mana={self.mana}, attack={self.attack}, defense={self.defense}, role={self.char_role})"