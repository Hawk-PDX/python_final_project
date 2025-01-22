from sqlalchemy.orm import Session, joinedload
from models.player import Player
from models.enemy import Enemy
from models.game import Game
from models.item import Item
from models.user import User
from .exceptions import InvalidInputError, PlayerNotFoundError, DatabaseError
from passlib.hash import bcrypt

# Constants for default values
DEFAULT_ENEMY_HEALTH = 100
DEFAULT_ENEMY_ATTACK = 10
DEFAULT_ENEMY_DEFENSE = 5
DEFAULT_ITEM_VALUE = 0

# Utility function for parameter checks
def check_required_params(params, required_fields):
    for field in required_fields:
        if not params.get(field):
            raise InvalidInputError(f"{field} is required.")

# Consolidated function for creating entities
def create_entity(session: Session, entity_type: str, **kwargs):
    try:
        if entity_type == "user":
            check_required_params(kwargs, ["username", "email", "password"])
            hashed_password = bcrypt.hash(kwargs["password"])
            entity = User(username=kwargs["username"], email=kwargs["email"], password=hashed_password)
        elif entity_type == "player":
            check_required_params(kwargs, ["name", "user_id"])
            entity = Player(name=kwargs["name"], user_id=kwargs["user_id"], **kwargs)
        elif entity_type == "game":
            check_required_params(kwargs, ["name", "description", "char_class", "char_role", "player_id"])
            entity = Game(name=kwargs["name"], description=kwargs["description"], char_class=kwargs["char_class"], char_role=kwargs["char_role"], player_id=kwargs["player_id"])
        elif entity_type == "enemy":
            check_required_params(kwargs, ["name", "game_id"])
            entity = Enemy(name=kwargs["name"], game_id=kwargs["game_id"], health=kwargs.get("health", DEFAULT_ENEMY_HEALTH), attack=kwargs.get("attack", DEFAULT_ENEMY_ATTACK), defense=kwargs.get("defense", DEFAULT_ENEMY_DEFENSE))
        elif entity_type == "item":
            check_required_params(kwargs, ["name", "type", "player_id"])
            entity = Item(name=kwargs["name"], type=kwargs["type"], player_id=kwargs["player_id"], value=kwargs.get("value", DEFAULT_ITEM_VALUE))
        else:
            raise InvalidInputError(f"Invalid entity type: {entity_type}")

        session.add(entity)
        session.commit()
        return entity
    except Exception as e:
        session.rollback()
        raise DatabaseError(f"Failed to create {entity_type}: {str(e)}")

# Consolidated function for fetching entities
def get_entity(session: Session, entity_type: str, entity_id: int):
    if entity_type == "user":
        return session.query(User).filter(User.id == entity_id).first()
    elif entity_type == "player":
        return session.query(Player).options(joinedload(Player.items)).filter(Player.id == entity_id).first()
    elif entity_type == "game":
        return session.query(Game).options(joinedload(Game.enemies)).filter(Game.id == entity_id).first()
    elif entity_type == "enemy":
        return session.query(Enemy).filter(Enemy.id == entity_id).first()
    elif entity_type == "item":
        return session.query(Item).filter(Item.id == entity_id).first()
    else:
        raise InvalidInputError(f"Invalid entity type: {entity_type}")

# Consolidated function for updating entities
def update_entity(session: Session, entity_type: str, entity_id: int, **kwargs):
    entity = get_entity(session, entity_type, entity_id)
    if entity:
        for key, value in kwargs.items():
            setattr(entity, key, value)
        session.commit()
        session.refresh(entity)  # Refresh the entity after update
    return entity

# Consolidated function for deleting entities
def delete_entity(session: Session, entity_type: str, entity_id: int):
    entity = get_entity(session, entity_type, entity_id)
    if entity:
        session.delete(entity)
        session.commit()

# Specific function for validating user credentials
def validate_user_credentials(session: Session, username: str, password: str):
    check_required_params({"username": username, "password": password}, ["username", "password"])
    user = session.query(User).filter(User.username == username).first()
    if not user:
        raise PlayerNotFoundError(f"User    with username '{username}' not found.")
    if not bcrypt.verify(password, user.password):
        raise InvalidInputError("Invalid credentials.")
    return user

def add_player_to_game(session: Session, player_id: int, game_id: int):
    session.execute(player_games.insert().values(player_id=player_id, game_id=game_id))
    session.commit()

def add_enemy_to_game(session: Session, enemy_id: int, game_id: int):
    session.execute(game_enemies.insert().values(enemy_id=enemy_id, game_id=game_id))
    session.commit()

def add_player_to_user(session: Session, player_id: int, user_id: int):
    session.execute(user_players.insert().values(player_id=player_id, user_id=user_id))
    session.commit()