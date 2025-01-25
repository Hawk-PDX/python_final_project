from sqlalchemy.orm import Session
from models import Enemy, Player, Game, Item, User
from .exceptions import InvalidInputError, PlayerNotFoundError, GameNotFoundError, EnemyNotFoundError, ItemNotFoundError, DatabaseError
from passlib.hash import bcrypt

def create_user(session: Session, username: str, email: str, password: str) -> User:
    hashed_password = bcrypt.hash(password)
    user = User(username=username, email=email, password=hashed_password)
    session.add(user)
    session.commit()
    return user

def validate_user_credentials(session: Session, username: str, password: str) -> User:
    user = session.query(User).filter_by(username=username).first()
    if not user:
        raise PlayerNotFoundError(f"User  with username '{username}' not found.")
    if not bcrypt.verify(password, user.password):
        raise InvalidInputError("Invalid credentials.")
    return user

def create_player(session: Session, name: str, user_id: int, char_class: str) -> Player:
    player = Player(name=name, user_id=user_id, char_class=char_class)
    session.add(player)
    session.commit()
    return player

def create_game(session: Session, name: str, description: str, player_id: int) -> Game:
    game = Game(name=name, description=description, player_id=player_id)
    session.add(game)
    session.commit()
    return game

def create_enemy(session: Session, name: str, game_id: int, health: int = 100, attack: int = 10, defense: int = 5) -> Enemy:
    enemy = Enemy(name=name, game_id=game_id, health=health, attack=attack, defense=defense)
    session.add(enemy)
    session.commit()
    return enemy