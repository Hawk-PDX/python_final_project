from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    players = relationship('Player', back_populates='user')
    games = relationship('Game', back_populates='user')

    def __repr__(self):
        return f"User (id={self.id}, username='{self.username}', email='{self.email}')"

    def check_password(self, password):
        return password == self.password

    def get_player(self, session):
        from .player import Player  # Lazy import
        return session.query(Player).filter_by(user_id=self.id).first()