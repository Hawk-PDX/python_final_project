import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                health INTEGER DEFAULT 100,
                level INTEGER DEFAULT 1
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS enemies (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                health INTEGER DEFAULT 100,
                level INTEGER DEFAULT 1
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS drops (
                id INTEGER PRIMARY KEY,
                enemy_id INTEGER,
                item_id INTEGER
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS quests (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                reward INTEGER DEFAULT 0,
                status TEXT DEFAULT 'incomplete',
                player_id INTEGER
            )
        """)
        self.conn.commit()

    def insert_player(self, player):
        self.cursor.execute("INSERT INTO players (name) VALUES (?)", (player.name,))
        self.conn.commit()

    def insert_enemy(self, enemy):
        self.cursor.execute("INSERT INTO enemies (name) VALUES (?)", (enemy.name,))
        self.conn.commit()

    def insert_drop(self, drop):
        self.cursor.execute("INSERT INTO drops (enemy_id, item_id) VALUES (?, ?)", (drop.enemy_id, drop.item_id))
        self.conn.commit()

    def insert_quest(self, quest):
        self.cursor.execute("INSERT INTO quests (title, description, reward, player_id) VALUES (?, ?, ?, ?)", (quest.title, quest.description, quest.reward, quest.player_id))
        self.conn.commit()

    def close(self):
        self.conn.close()