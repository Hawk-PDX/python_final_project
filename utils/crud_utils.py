from sqlalchemy.orm import Session
from models.player import Player
from models.enemy import Enemy
from models.game import Game
from models.item import Item
from models.user import User
from exceptions import InvalidInputError, PlayerNotFoundError, DatabaseError
from passlib.hash import bcrypt

# User CRUD Functions
def create_user(session: Session, username: str, email: str, password: str):
    hashed_password = bcrypt.hash(password)  # Hash the password
    user = User(username=username, email=email, password=hashed_password)
    session.add(user)
    session.commit()
    return user

def get_user(session: Session, user_id: int):
    return session.query(User).filter(User.id == user_id).first()

def get_user_by_username(session: Session, username: str):
    return session.query(User).filter(User.username == username).first()

def update_user(session: Session, user_id: int, **kwargs):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        session.commit()
    return user

def delete_user(session: Session, user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()

def validate_user_credentials(session: Session, username: str, password: str):
    if not username or not password:
        raise InvalidInputError("Username and password are required.")
    
    user = get_user_by_username(session, username)
    if not user:
        raise PlayerNotFoundError(f"User  with username '{username}' not found.")
    
    if not bcrypt.verify(password, user.password):
        raise InvalidInputError("Invalid credentials.")
    
    return user

# Player CRUD Functions

def create_player(session: Session, name: str, user_id: int, **kwargs):
    if not name or not user_id:
        raise InvalidInputError("Player name and user ID are required.")
    
    try:
        player = Player(name=name, user_id=user_id, **kwargs)
        session.add(player)
        session.commit()
        return player
    except Exception as e:
        session.rollback()
        raise DatabaseError(f"Failed to create player: {str(e)}")

def get_player(session: Session, player_id: int):
    return session.query(Player).filter(Player.id == player_id).first()

def update_player(session: Session, player_id: int, **kwargs):
    player = session.query(Player).filter(Player.id == player_id).first()
    if player:
        for key, value in kwargs.items():
            setattr(player, key, value)
        session.commit()
    return player

def delete_player(session: Session, player_id: int):
    player = session.query(Player).filter(Player.id == player_id).first()
    if player:
        session.delete(player)
        session.commit()

# Game CRUD Functions

def create_game(session: Session, name: str, description: str, char_class: str, char_role: str, player_id: int, level: int = 1):
    game = Game(name=name, description=description, char_class=char_class, char_role=char_role, player_id=player_id, level=level)
    session.add(game)
    session.commit()
    return game

def get_game(session: Session, game_id: int):
    return session.query(Game).filter(Game.id == game_id).first()

def update_game(session: Session, game_id: int, **kwargs):
    game = session.query(Game).filter(Game.id == game_id).first()
    if game:
        for key, value in kwargs.items():
            setattr(game, key, value)
        session.commit()
    return game

def delete_game(session: Session, game_id: int):
    game = session.query(Game).filter(Game.id == game_id).first()
    if game:
        session.delete(game)
        session.commit()

# Enemy CRUD Functions

def create_enemy(session: Session, name: str, game_id: int, health: int = 50, attack: int = 5, defense: int = 2):
    enemy = Enemy(name=name, game_id=game_id, health=health, attack=attack, defense=defense)
    session.add(enemy)
    session.commit()
    return enemy

def get_enemy(session: Session, enemy_id: int):
    return session.query(Enemy).filter(Enemy.id == enemy_id).first()

def update_enemy(session: Session, enemy_id: int, **kwargs):
    enemy = session.query(Enemy).filter(Enemy.id == enemy_id).first()
    if enemy:
        for key, value in kwargs.items():
            setattr(enemy, key, value)
        session.commit()
    return enemy

def delete_enemy(session: Session, enemy_id: int):
    enemy = session.query(Enemy).filter(Enemy.id == enemy_id).first()
    if enemy:
        session.delete(enemy)
        session.commit()

# Item CRUD Functions

def create_item(session: Session, name: str, type: str, player_id: int, value: int = 0):
    item = Item(name=name, type=type, player_id=player_id, value=value)
    session.add(item)
    session.commit()
    return item

def get_item(session: Session, item_id: int):
    return session.query(Item).filter(Item.id == item_id).first()

def update_item(session: Session, item_id: int, **kwargs):
    item = session.query(Item).filter(Item.id == item_id).first()
    if item:
        for key, value in kwargs.items():
            setattr(item, key, value)
        session.commit()
    return item

def delete_item(session: Session, item_id: int):
    item = session.query(Item).filter(Item.id == item_id).first()
    if item:
        session.delete(item)
        session.commit()