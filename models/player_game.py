from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

player_games = Table(
    "player_games",
    Base.metadata,
    Column("player_id", Integer, ForeignKey("players.id"), primary_key=True),
    Column("game_id", Integer, ForeignKey("games.id"), primary_key=True),
)

# Export player_games table
__all__ = ["player_games"]