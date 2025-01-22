class InvalidInputError(Exception):
    """Raised when the user provides invalid input."""
    pass

class PlayerNotFoundError(Exception):
    """Raised when a player is not found in the database."""
    pass

class GameNotFoundError(Exception):
    """Raised when a game is not found in the database."""
    pass

class EnemyNotFoundError(Exception):
    """Raised when an enemy is not found in the database."""
    pass

class ItemNotFoundError(Exception):
    """Raised when an item is not found in the database."""
    pass

class InsufficientHealthError(Exception):
    """Raised when a player's health is insufficient for an action."""
    pass

class InvalidActionError(Exception):
    """Raised when an invalid action is attempted."""
    pass

class DatabaseError(Exception):
    """Raised when there is an issue with the database."""
    pass
