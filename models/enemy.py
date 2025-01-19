from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Enemy(Base):
    __tablename__ = 'enemies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)
    battles = relationship("Battle", back_populates="enemy")
    drops = relationship("Drop", back_populates="enemy")