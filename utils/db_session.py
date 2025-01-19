# utils/db_session.py

from models.database import Session

def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()