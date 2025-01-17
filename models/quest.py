from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base

class Quest(Base):
    __tablename__ = 'quests'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    reward = Column(Integer, default=0)
    status = Column(String, default='incomplete')
    player_id = Column(Integer, ForeignKey('players.id'))

    # *** Many-to-one relationship with player ***
    player = relationship("Player")

    def __repr__(self):
        return f"<Quest(title='{self.title}', status='{self.status}')>"
