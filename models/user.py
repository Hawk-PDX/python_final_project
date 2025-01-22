from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from passlib.hash import bcrypt

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.hash(password)

    def __repr__(self):
        return f"User (id={self.id}, username='{self.username}', email='{self.email}')"

    def check_password(self, password):
        return bcrypt.verify(password, self.password)