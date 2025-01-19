CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE players (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    health INTEGER DEFAULT 100,
    level INTEGER DEFAULT 1,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    value INTEGER DEFAULT 0,
    player_id INTEGER,
    FOREIGN KEY (player_id) REFERENCES players (id)
);

CREATE TABLE quests (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    difficulty INTEGER NOT NULL,
    reward INTEGER DEFAULT 0,
    creator_id INTEGER,
    player_id INTEGER,
    FOREIGN KEY (creator_id) REFERENCES users (id),
    FOREIGN KEY (player_id) REFERENCES players (id)
);

CREATE TABLE battles (
    id INTEGER PRIMARY KEY,
    player_id INTEGER,
    enemy_id INTEGER,
    FOREIGN KEY (player_id) REFERENCES players (id),
    FOREIGN KEY (enemy_id) REFERENCES enemies (id)
);

CREATE TABLE enemies (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    health INTEGER NOT NULL,
    level INTEGER NOT NULL
);

CREATE TABLE drops (
    id INTEGER PRIMARY KEY,
    enemy_id INTEGER,
    item_id INTEGER,
    FOREIGN KEY (enemy_id) REFERENCES enemies (id),
    FOREIGN KEY (item_id) REFERENCES items (id)
);