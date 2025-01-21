# test_auth.py
from utils.database import Session
from utils.crud_utils import create_user, validate_user_credentials

def test_registration():
    # Test user registration
    session = Session()
    user = create_user(session, username="john_doe", email="john@example.com", password="password123")
    print(f"User  created: {user.username}, Hashed Password: {user.password}")
    session.close()


def test_login():
    # Test user login
    session = Session()
    user = validate_user_credentials(session, username="john_doe", password="password123")
    if user:
        print(f"Login successful! Welcome, {user.username}.")
    else:
        print("Invalid credentials.")
    session.close()

if __name__ == "__main__":
    # Run the tests
    test_registration()
    test_login()