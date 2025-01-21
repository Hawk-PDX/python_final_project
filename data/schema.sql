-- Users Table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- Players Table
CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    health INTEGER DEFAULT 100,
    attack INTEGER DEFAULT 10,
    defense INTEGER DEFAULT 5,
    level INTEGER DEFAULT 1,
    skills TEXT,
    health_potions INTEGER DEFAULT 2,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    item_name STRING NOT NULL
    quantity INTEGER NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(id)
);


-- Character Selection
CREATE TABLE character_selection (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    character_id INTEGER NOT NULL,
    job_class STRING NOT NULL
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (character_id) REFERENCES players(id)
);

-- Character Stats
CREATE TABLE character_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    character_id INTEGER NOT NULL,
    health INTEGER NOT NULL,
    attack INTEGER NOT NULL,
    defense INTEGER NOT NULL,
    FOREIGN KEY (character_id) REFERENCES players(id)
);

-- Games Table
CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    char_class TEXT,
    char_role TEXT,
    player_id INTEGER NOT NULL,
    level INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(id)
);

-- Enemies Table
CREATE TABLE enemies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    health INTEGER DEFAULT 50,
    attack INTEGER DEFAULT 5,
    defense INTEGER DEFAULT 2,
    game_id INTEGER NOT NULL,
    FOREIGN KEY (game_id) REFERENCES games(id)
);

-- Items Table
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    value INTEGER DEFAULT 0,
    player_id INTEGER NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(id)
);