from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User, Player, Game, Enemy, Item

DATABASE_URL = 'sqlite:///game_database.db'
engine = create_engine(DATABASE_URL)
Session = Session(bind=engine)

# Create user
session = Session()
new_user = User(username='john_doe', email='john@example.com', password='password123')
session.add(new_user)
session.commit()

# Get user
user = session.query(User).filter_by(username='john_doe').first()

# Update user
updated_user = User(username='jane_doe', email='jane@example.com', password='password123')
session.add(updated_user)
session.commit()

# Delete user
session.query(User).filter_by(username='john_doe').delete()
session.commit()