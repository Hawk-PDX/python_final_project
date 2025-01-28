from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .character import Character

Base = declarative_base()

class Level(Base):
    __tablename__ = 'levels'

    id = Column(Integer, primary_key=True)
    level_number = Column(Integer, nullable=False)
    enemies = Column(String, nullable=False)  # JSON or serialized data
    rewards = Column(String, nullable=False)  # JSON or serialized data

    def __repr__(self):
        return f"Level(id={self.id}, level_number={self.level_number}, enemies={self.enemies}, rewards={self.rewards})"

    def set_character(self, character):
        self.character = character
        self.character.health_potions = 1  # Replenish health potion at the start of each level
        self.character.attack_potions = 1  # Replenish attack potion at the start of each level
        self.character.temporary_defense_boost = 0  # Reset temporary defense boost at the start of each level

    def start(self):
        print(f"Starting Level {self.level_number}...")
        print(f"Enemies: {self.enemies}")
        print(f"Rewards: {self.rewards}")

# Create a SQLAlchemy engine
engine = create_engine('sqlite:///game.db')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Create the tables
Base.metadata.create_all(engine)