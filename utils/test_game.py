from utils.database import Session
from utils.crud_utils import create_user, create_player, create_game, create_enemy
from utils.game_utils import fight
from models.player import Player
from models.enemy import Enemy
from exceptions import InsufficientHealthError, InvalidActionError, InvalidInputError, PlayerNotFoundError
from sqlalchemy.orm import validate_user_credentials


def test_user_registration():
    session = Session()
    try:
        user = create_user(session, username="test_user", email="test@example.com", password="password123")
        print(f"User  created: {user.username}")
    except InvalidInputError as e:
        print(f"Error: {str(e)}")
    finally:
        session.close()

def test_user_login():
    session = Session()
    try:
        user = validate_user_credentials(session, username="test_user", password="password123")
        print(f"Login successful: {user.username}")
    except (InvalidInputError, PlayerNotFoundError) as e:
        print(f"Error: {str(e)}")
    finally:
        session.close()
        
def test_player_creation():
    session = Session()
    try:
        player = create_player(session, username="test_user", email="test@example.com", password=" password123")
        print(f"Player created: {player.username}")
    except (InvalidInputError, PlayerNotFoundError) as e:
        print(f"Problem Creating Player Character: {str(e)}")
        
def test_fight():
    session = Session()
    try:
        player = Player(name="Test Player", health=100, attack=10, defense=5)
        enemy = Enemy(name="Test Goblin", health=50, attack=5, defense=2)
        fight(player, enemy)
    except (InsufficientHealthError, InvalidActionError) as e:
        print(f"Error: {str(e)}")
    finally:
        session.close()

if __name__ == "__main__":
    test_user_registration()
    test_player_creation()
    test_user_login()
    test_fight()