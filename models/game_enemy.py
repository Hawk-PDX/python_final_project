from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

game_enemies = Table(
    "game_enemies",
    Base.metadata,
    Column("game_id", Integer, ForeignKey("games.id"), primary_key=True),
    Column("enemy_id", Integer, ForeignKey("enemies.id"), primary_key=True),
)

# Export game_enemies table
__all__ = ["game_enemies"]