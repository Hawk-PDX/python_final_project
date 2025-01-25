# game_logic/level.py
class Level:
    def __init__(self, level_number, enemies, rewards):
        self.level_number = level_number
        self.enemies = enemies  # List of enemies
        self.rewards = rewards  # List of rewards (e.g., items, gold)
        self.character = None  # Reference to the current character

    def __repr__(self):
        return f"Level(level_number={self.level_number}, enemies={self.enemies}, rewards={self.rewards})"

    def set_character(self, character):
        self.character = character

    def start(self):
        print(f"Starting Level {self.level_number}...")
        print(f"Enemies: {self.enemies}")
        print(f"Rewards: {self.rewards}")