from __main__ import PlayerCharacter
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    players = relationship("Player", back_populates="user")
    
    def login(self, session):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        player = session.query(PlayerCharacter).filter_by(name=username).first()
        if player and player.password == password:  # Assuming you have a password field
            print("Login successful!")
            return player
        else:
            print("Invalid username or password.")
        return None