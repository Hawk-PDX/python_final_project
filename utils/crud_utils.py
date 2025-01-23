from sqlalchemy.orm import Session
from models import Enemy, Player, Game, Enemy, Item, User
from .exceptions import InvalidInputError, PlayerNotFoundError, GameNotFoundError, EnemyNotFoundError, ItemNotFoundError, InsufficientHealthError, DatabaseError
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

# Create user function
def create_user(session: Session, username: str, email: str, password: str) -> User:
    """
    Creates a new user in the database.

    Args:
        session (Session): The database session.
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        User: The created user object.
    """
    check_required_params({"username": username, "email": email, "password": password}, ["username", "email", "password"])
    hashed_password = bcrypt.hash(password)
    user = User(username=username, email=email, password=hashed_password)
    session.add(user)
    session.commit()
    return user

# Validate user credentials
def validate_user_credentials(session: Session, username: str, password: str) -> User:
    """
    Validates user credentials.

    Args:
        session (Session): The database session.
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        User: The user object if credentials are valid.

    Raises:
        PlayerNotFoundError: If the user is not found.
        InvalidInputError: If the credentials are invalid.
    """
    check_required_params({"username": username, "password": password}, ["username", "password"])
    user = session.query(User).filter_by(username=username).first()
    if not user:
        raise PlayerNotFoundError(f"User     with username '{username}' not found.")
    if not bcrypt.verify(password, user.password):
        raise InvalidInputError("Invalid credentials.")
    return user

# Create player function
def create_player(session: Session, name: str, user_id: int) -> Player:
    """
    Creates a new player in the database.

    Args:
        session (Session): The database session.
        name (str): The name of the player.
        user_id (int): The ID of the user associated with the player.

    Returns:
        Player: The created player object.
    """
    check_required_params({"name": name, "user_id": user_id}, ["name", "user_id"])
    player = Player(name=name, user_id=user_id)
    session.add(player)
    session.commit()
    return player

# Create game function
def create_game(session: Session, name: str, description: str, char_class: str, char_role: str, player_id: int) -> Game:
    """
    Creates a new game in the database.

    Args:
        session (Session): The database session.
        name (str): The name of the game.
        description (str): The description of the game.
        char_class (str): The character class.
        char_role (str): The character role.
        player_id (int): The ID of the player associated with the game.

    Returns:
        Game: The created game object.
    """
    check_required_params({"name": name, "description": description, "char_class": char_class, "char_role": char_role, "player_id": player_id}, ["name", "description", "char_class", "char_role", "player_id"])
    game = Game(name=name, description=description, char_class=char_class, char_role=char_role, player_id=player_id)
    session.add(game)
    session.commit()
    return game

# Create enemy function
def create_enemy(session: Session, name: str, game_id: int, health: int = DEFAULT_ENEMY_HEALTH, attack: int = DEFAULT_ENEMY_ATTACK, defense: int = DEFAULT_ENEMY_DEFENSE) -> Enemy:
    """
    Creates a new enemy in the database.

    Args:
        session (Session): The database session.
        name (str): The name of the enemy.
        game_id (int): The ID of the game associated with the enemy.
        health (int): The health of the enemy.
        attack (int): The attack power of the enemy.
        defense (int): The defense power of the enemy.

    Returns:
        Enemy: The created enemy object.
    """
    check_required_params({"name": name, "game_id": game_id}, ["name", "game_id"])
    enemy = Enemy(name=name, game_id=game_id, health=health, attack=attack, defense=defense)
    session.add(enemy)
    session.commit()
    return enemy

# Create item function
def create_item(session: Session, name: str, type: str, player_id: int, value: int = DEFAULT_ITEM_VALUE) -> Item:
    """
    Creates a new item in the database.

    Args:
        session (Session): The database session.
        name (str): The name of the item.
        type (str): The type of the item.
        player_id (int): The ID of the player associated with the item.
        value (int): The value of the item.

    Returns:
        Item: The created item object.
    """
    check_required_params({"name": name, "type": type, "player_id": player_id}, ["name", "type", "player_id"])
    item = Item(name=name, type=type, player_id=player_id, value=value)
    session.add(item)
    session.commit()
    return item