from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



class Quest(Base):
    
    __tablename__ = 'quests'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    difficulty = (Column(Integer, nullable=False))
    reward = Column(Integer, default=0)
    creator_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User', back_populates='quests')
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship("Player", back_populates="quests")
    
    ipdb.set_trace()