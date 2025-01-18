from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base

ForeignKey()


class Battle(Base):
    __tablename__ = 'battles'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    enemy_id = Column(Integer, ForeignKey('enemies.id'))
    
    player = relationship("Player", back_populates="battles")
    enemy = relationship("Enemy", back_populates="battles")