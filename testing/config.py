DATABASE_URL = 'sqlite:///game_database.db'
from utils.database import Session
from utils.crud_utils import create_user, get_user, update_user, delete_user

# Create user
session = Session()
new_user = create_user(session, username='john_doe', email='john@example.com', password='password123')

# Get user
user = get_user(session, new_user.id)

# Update user
updated_user = update_user(session, user.id, email='john.doe@example.com')

# Delete user
delete_user(session, user.id)
session.close()