import sqlite3

class Quest:
    def __init__(self, title, description, reward, player_id):
        self.title = title
        self.description = description
        self.reward = reward
        self.player_id = player_id

    def __repr__(self):
        return f"<Quest(title='{self.title}', status='incomplete')>"