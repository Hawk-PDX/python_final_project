# models/level.py
from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Level(Base):
    __tablename__ = 'levels'

    id = Column(Integer, primary_key=True)
    level_number = Column(Integer, nullable=False)
    enemies = Column(String, nullable=False)  # JSON or serialized data
    rewards = Column(String, nullable=False)  # JSON or serialized data

    def __repr__(self):
        return f"Level(id={self.id}, level_number={self.level_number}, enemies={self.enemies}, rewards={self.rewards})"