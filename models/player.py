from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, default=100)
    level = Column(Integer, default=1)

    # One-to-many relationship with items
    items = relationship("Item", back_populates="player")

    def __repr__(self):
        return f"<Player(name='{self.name}', health={self.health}, level={self.level})>"
    
    
    class Player:
    
#     def __init__(self, name, level, health, inventory, exp_points):
#         self.name = name
#         self.level = level
#         self.health = health
#         self.inventory = inventory
#         self.exp_points = exp_points