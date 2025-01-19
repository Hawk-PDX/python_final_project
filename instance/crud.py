from models import User, Player, Item
from database import session
from logging import log_error, log_info

def create_user(username, email, password):
    try:
        user = User(username=username, email=email, password=password)
        session.add(user)
        session.commit()
        log_info(f"User  created: {username}")
        return user
    except Exception as e:
        log_error(f"Error creating user: {e}")
        return None

def get_user_by_username(username):
    return session.query(User).filter_by(username=username).first()

def update_user_email(user_id, new_email):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.email = new_email
        session.commit()

def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()

def create_player(name, user_id):
    player = Player(name=name, user_id=user_id)
    session.add(player)
    session.commit()
    return player

def get_player_by_id(player_id):
    return session.query(Player).filter_by(id=player_id).first()

def update_player_health(player_id, new_health):
    player = session.query(Player).filter_by(id=player_id).first()
    if player:
        player.health = new_health
        session.commit()

def delete_player(player_id):
    player = session.query(Player).filter_by(id=player_id).first()
    if player:
        session.delete(player)
        session.commit()

def create_item(name, type, value, player_id):
    item = Item(name=name, type=type, value=value, player_id=player_id)
    session.add(item)
    session.commit()
    return item

def get_item_by_id(item_id):
    return session.query(Item).filter_by(id=item_id).first()

def update_item_value(item_id, new_value):
    item = session.query(Item).filter_by(id=item_id).first()
    if item:
        item.value = new_value
        session.commit()

def delete_item(item_id):
    item = session.query(Item).filter_by(id=item_id).first()
    if item:
        session.delete(item)
        session.commit()