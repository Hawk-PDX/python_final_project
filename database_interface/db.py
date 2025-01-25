import sqlite3

class DBInterface:
    def __init__(self):
        self.conn = sqlite3.connect('game.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                char_class TEXT NOT NULL,
                health INTEGER NOT NULL,
                mana INTEGER NOT NULL,
                attack INTEGER NOT NULL,
                defense INTEGER NOT NULL,
                char_role TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def save_character(self, character):
        self.cursor.execute('''
            INSERT INTO characters (name, char_class, health, mana, attack, defense, char_role)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (character.name, character.char_class, character.health, character.mana, character.attack, character.defense, character.char_role))
        self.conn.commit()

    def get_character(self, name):
        self.cursor.execute('SELECT * FROM characters WHERE name = ?', (name,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()