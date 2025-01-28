import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@host:port/dbname")
engine = create_engine(DATABASE_URL)
Session = Session(bind=engine)