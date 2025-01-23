from sqlalchemy import Table, Column, Integer, ForeignKey, Boolean
from .base import Base
from .game_base import Game
from .enemy_base import Enemy

game_enemies = Table(
    "game_enemies",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("game_id", Integer, ForeignKey("games.id")),
    Column("enemy_id", Integer, ForeignKey("enemies.id")),
    Column("spawned", Boolean, default=False),
    Column("defeated", Boolean, default=False),
)

# Export game_enemies table
__all__ = ["game_enemies"]