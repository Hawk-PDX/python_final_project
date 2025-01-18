import sqlite3

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.level = 1

    def __repr__(self):
        return f"<Enemy(name='{self.name}', health={self.health}, level={self.level})>"