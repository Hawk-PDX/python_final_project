from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Character(Base):
    __abstract__ = True
    health = Column(Integer, default=100)
    level = Column(Integer, default=1)
    
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    players = relationship("Player", back_populates="user")

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, default=100)
    level = Column(Integer, default=1)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User ", back_populates="players")
    items = relationship("Item", back_populates="player")

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    value = Column(Integer, default=0)
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship("Player", back_populates="items")

# Create all tables in the engine
Base.metadata.create_all(engine)

#######################

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import DATABASE_URL
from player import Player
from item import Item
from models import Base 

engine = create_engine(DATABASE_URL)
Base.METADATA.create_all(engine)

class Database:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def create_tables(self):
        Base.metadata.create_all(engine)

    def drop_tables(self):
        Base.metadata.drop_all(engine)
        
    from base import Database

db = Database()
db.create_tables()

# Create a new player
player = Player(name="John Doe")
db.session.add(player)
db.session.commit()

# Create a new item
item = Item(name="Sword", type="Weapon", value=10)
db.session.add(item)
db.session.commit()

# Assign the item to the player
player.items.append(item)
db.session.commit()

# Query the database
players = db.session.query(Player).all()
for player in players:
    print(player.name)

items = db.session.query(Item).all()
for item in items:
    print(item.name)
    
Session = sessionmaker(bind=engine)