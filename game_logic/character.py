from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    char_class = Column(String, nullable=False)
    health = Column(Integer, nullable=False)
    mana = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    char_role = Column(String, nullable=False)

    def __repr__(self):
        return f"Character(id={self.id}, name={self.name}, class={self.char_class}, health={self.health}, mana={self.mana}, attack={self.attack}, defense={self.defense}, role={self.char_role})"

    def take_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            if self.health < 0:
                self.health = 0

    def heal(self, amount):
        self.health += amount

    def use_health_potion(self):
        if self.health_potions > 0:
            self.heal(15)
            self.health_potions -= 1
            print(f"{self.name} used a minor health potion and restored 15 health!")
        else:
            print("No health potions remaining!")

    def use_attack_potion(self):
        if self.attack_potions > 0:
            self.attack *= 1.05  # Apply a 5% damage boost
            self.attack_potions -= 1
            print(f"{self.name} used a minor attack potion and increased their damage by 5%!")
        else:
            print("No attack potions remaining!")

    def set_level(self, level):
        self.level = level
        self.health_potions = 1  # Replenish health potion at the start of each level
        self.attack_potions = 1  # Replenish attack potion at the start of each level
        self.temporary_defense_boost = 0  # Reset temporary defense boost at the start of each level

# Create a SQLAlchemy engine
engine = create_engine('sqlite:///game.db')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Create the tables
Base.metadata.create_all(engine)