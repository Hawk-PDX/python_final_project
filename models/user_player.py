from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

user_players = Table(
    "user_players",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("player_id", Integer, ForeignKey("players.id"), primary_key=True),
)

# Export user_players table
__all__ = ["user_players"]