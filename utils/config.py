DATABASE_URL = 'sqlite:///game_database.db'
from utils.database import Session
from utils.crud_utils import create_user, get_user, update_user, delete_user

# Create a new user
session = Session()
new_user = create_user(session, username='john_doe', email='john@example.com', password='password123')

# Fetch the user
user = get_user(session, new_user.id)

# Update the user
updated_user = update_user(session, user.id, email='john.doe@example.com')

# Delete the user
delete_user(session, user.id)
session.close()