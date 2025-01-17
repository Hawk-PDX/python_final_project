from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base

class Item(Base):
    __tablename__ = 'items'
# *** nullable *** required for sql interaction; None doesnt work?
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    value = Column(Integer, default=0)
    player_id = Column(Integer, ForeignKey('players.id'))

    # Many-to-one
    player = relationship("Player", back_populates="items")
    
    def __repr__(self):
        return f"<Item(name='{self.name}', Type='{self.type}', Value={self.value})>"

