from base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Drop(Base):
    __tablename__ = 'drops'
    id = Column(Integer, primary_key=True)
    enemy_id = Column(Integer, ForeignKey('enemies.id'))
    item_id = Column(Integer, ForeignKey('items.id'))
    enemy = relationship("Enemy", back_populates="drops")
    item = relationship("Item", back_populates="drops")