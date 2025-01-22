import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Use environment variables for database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///game.db")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)