from utils.database import Session
from utils.crud_utils import create_user, validate_user_credentials

def test_registration():
    session = Session()
    user = create_user(session, username="john_doe", email="john@example.com", password="password123")
    assert user.username == "john_doe", "User  registration failed!"
    print(f"User  created: {user.username}")
    session.close()

def test_login():
    session = Session()
    user = validate_user_credentials(session, username="john_doe", password="password123")
    assert user is not None, "Login failed!"
    print(f"Login successful! Welcome, {user.username}.")
    session.close()

if __name__ == "__main__":
    test_registration()
    test_login()