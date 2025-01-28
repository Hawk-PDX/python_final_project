from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .character import Character
from .level import Level

Base = declarative_base()

class Combat(Base):
    __tablename__ = 'combats'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, nullable=False)
    enemy_id = Column(Integer, nullable=False)
    level_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Combat(id={self.id}, character_id={self.character_id}, enemy_id={self.enemy_id}, level_id={self.level_id})"

    def start(self):
        character = session.query(Character).get(self.character_id)
        enemy = session.query(Enemy).get(self.enemy_id)
        level = session.query(Level).get(self.level_id)

        print(f"Combat started between {character.name} and {enemy.name} on Level {level.level_number}...")
        while character.health > 0 and enemy.health > 0:
            print(f"{character.name}'s health: {character.health}")
            print(f"{enemy.name}'s health: {enemy.health}")
            action = input("What do you want to do? (attack/use skill/use health potion/run): ").strip().lower()

            if action == "attack":
                enemy.health -= character.attack
                print(f"{character.name} attacked {enemy.name} for {character.attack} damage!")
            elif action == "use skill":
                skill = input("Which skill do you want to use? (Healing Strike/Shield Block): ").strip().lower()
                if skill == "healing strike":
                    character.health += 5
                    enemy.health -= 10
                    character.mana -= 10  # skill used, mana reduced accordingly
                    print(f"{character.name} used Healing Strike on {enemy.name}!")
                elif skill == "shield block":
                    character.defense += 20
                    character.mana -= 10  # same logic as above
                    print(f"{character.name} used Shield Block!")
                else:
                    print("Invalid skill selected.")
            elif action == "use health potion":
                if character.health_potions > 0:
                    character.health += 15
                    character.health_potions -= 1
                    print(f"{character.name} used a minor health potion and restored 15 health!")
                else:
                    print("No health potions remaining.")
            elif action == "run":
                print("You ran away!")
                break
            else:
                print("Invalid action selected.")

            if enemy.health > 0:
                character.health -= enemy.attack
                print(f"{enemy.name} attacked {character.name} for {enemy.attack} damage!")

        if character.health > 0:
            print(f"{character.name} defeated {enemy.name}!")
        else:
            print(f"{character.name} was defeated by {enemy.name}!")

# Create a SQLAlchemy engine
engine = create_engine('sqlite:///game.db')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Create the tables
Base.metadata.create_all(engine)