import pytest
from utils.database import Session
from utils.crud_utils import create_user, validate_user_credentials, create_player, create_game, create_enemy
from models.player import Player
from models.enemy import Enemy
from models.game import Game
from models.user import User
from models.item import Item
from .exceptions import InvalidInputError, PlayerNotFoundError, DatabaseError

@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()

def test_user_registration(session):
    user = create_user(session, username="test_user", email="test@example.com", password="password123")
    assert user.username == "test_user"
    assert user.email == "test@example.com"

def test_user_login(session):
    user = validate_user_credentials(session, username="test_user", password="password123")
    assert user.username == "test_user"

def test_player_creation(session):
    player = create_player(session, name="Test Player", user_id=1, role="Paladin", health=200, mana=100)
    assert player.name == "Test Player"
    assert player.role == "Paladin"

def test_game_creation(session):
    game = create_game(session, name="Test Game", description="Test Description", char_class="Warrior", char_role="Tank", player_id=1)
    assert game.name == "Test Game"
    assert game.description == "Test Description"

def test_enemy_creation(session):
    enemy = create_enemy(session, name="Test Goblin", game_id=1, health=100, attack=10, defense=5)
    assert enemy.name == "Test Goblin"
    assert enemy.health == 100

def test_item_creation(session):
    item = create_item(session, name="Test Sword", type="Weapon", player_id=1, value=50)
    assert item.name == "Test Sword"
    assert item.type == "Weapon"

def test_add_player_to_game(session):
    player = create_player(session, name="Test Player", user_id=1, role="Paladin", health=200, mana=100)
    game = create_game(session, name="Test Game", description="Test Description", char_class="Warrior", char_role="Tank", player_id=1)
    add_player_to_game(session, player.id, game.id)
    assert session.query(player_games).filter_by(player_id=player.id, game_id=game.id).first() is not None