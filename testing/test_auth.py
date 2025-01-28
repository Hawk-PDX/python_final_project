from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User
from utils.crud_utils import create_user, validate_user_credentials

DATABASE_URL = 'sqlite:///game_database.db'
engine = create_engine(DATABASE_URL)
Session = Session(bind=engine)

def test_registration():
    session = Session()
    user = create_user(session, username="john_doe", email="john@example.com", password="password123")
    assert user.username == "john_doe"
    print(f"User   created: {user.username}")
    session.close()

def test_login():
    session = Session()
    user = validate_user_credentials(session, username="john_doe", password="password123")
    assert user is not None
    print(f"Login successful! Welcome, {user.username}.")
    session.close()