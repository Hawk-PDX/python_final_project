from crud import create_user, get_user_by_username, create_player, get_player_by_id
from models import User, Player

def test_user_crud():
    user = create_user("john", "john@example.com", "password")
    assert user.username == "john"
    assert user.email == "john@example.com"
    assert user.password == "password"

    user = get_user_by_username("john")
    assert user.username == "john"
    assert user.email == "john@example.com"
    assert user.password == "password"

def test_player_crud():
    player = create_player("John Doe", 1)
    assert player.name == "John Doe"
    assert player.user_id == 1

    player = get_player_by_id(1)
    assert player.name == "John Doe"
    assert player.user_id == 1

test_user_crud()
test_player_crud()