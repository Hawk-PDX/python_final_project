import sqlite3

class Drop:
    def __init__(self, enemy_id, item_id):
        self.enemy_id = enemy_id
        self.item_id = item_id

    def __repr__(self):
        return f"<Drop(enemy_id={self.enemy_id}, item_id={self.item_id})>"