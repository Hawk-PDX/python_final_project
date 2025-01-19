import cmd

class Game(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = '(game) '

    def do_login(self, arg):
        username = input('Enter username: ')
        password = input('Enter password: ')
        user = session.query(User).filter_by(username=username, password=password).first()
        if user:
            print('Login successful!')
            self.user = user
        else:
            print('Invalid username or password.')

    def do_create_account(self, arg):
        username = input('Enter username: ')
        password = input('Enter password: ')
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        print('Account created!')

    def do_create_character(self, arg):
        name = input('Enter character name: ')
        class_name = input('Enter class name: ')
        class_ = session.query(Class).filter_by(name=class_name).first()
        if class_:
            character = Character(name=name, class_=class_)
            session.add(character)
            session.commit()
            print('Character created!')
        else:
            print('Invalid class name.')

    def do_quest(self, arg):
        quest_name = input('Enter quest name: ')
        quest = session.query(Quest).filter_by(name=quest_name).first()
        if quest:
            print('Quest started!')
            # Implement quest logic here
        else:
            print('Invalid quest name.')

if __name__ == '__main__':
    game = Game()
    game.cmdloop()
    
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://user:password@host:port/dbname')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    characters = relationship('Character', back_populates='user')

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(50), nullable=False)
    class_id = Column(Integer, ForeignKey('classes.id'), nullable=False)
    level = Column(Integer, nullable=False, default=1)
    experience = Column(Integer, nullable=False, default=0)
    equipment_id = Column(Integer, ForeignKey('equipment.id'), nullable=False)
    user = relationship('User ', back_populates='characters')
    class_ = relationship('Class', back_populates='characters')
    equipment = relationship('Equipment', back_populates='characters')

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    characters = relationship('Character', back_populates='class_')

class Quest(Base):
    __tablename__ = 'quests'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    experience_reward = Column(Integer, nullable=False)
    required_level = Column(Integer, nullable=False)

class Mob(Base):
    __tablename__ = 'mobs'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    level = Column(Integer, nullable=False)
    experience_reward = Column(Integer, nullable=False)
    health = Column(Integer, nullable=False)

class Equipment(Base):
    __tablename__ = 'equipment'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    stats = Column(JSONB, nullable=False)
    characters = relationship('Character', back_populates='equipment')

Session = sessionmaker(bind=engine)
session = Session()