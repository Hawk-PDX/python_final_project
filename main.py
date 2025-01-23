from utils.database import Session, engine
from models.base import Base
from models.player import Player
from models.game import Game
from models.enemy import Enemy
from models.user import User
from utils.cli_utils import display_welcome_message, get_player_input
from utils.game_utils import fight

# DB Creation
Base.metadata.create_all(engine)

# character roles and stats
CHARACTER_CLASSES = {
    "1": {"name": "Paladin", "health": 200, "mana": 100, "attack": 15, "defense": 20, "role": "Tank"},
    "2": {"name": "Mage", "health": 110, "mana": 150, "attack": 25, "defense": 5, "role": "Damage"},
    "3": {"name": "Rogue", "health": 140, "mana": 120, "attack": 20, "defense": 10, "role": "Damage"},
    "4": {"name": "Ranger", "health": 150, "mana": 100, "attack": 18, "defense": 12, "role": "Support"},
}

# enemies for each level
LEVEL_ENEMIES = {
    1: {"name": "Goblin", "health": 100, "attack": 10, "defense": 5},
    2: {"name": "Orc", "health": 150, "attack": 15, "defense": 10},
    3: {"name": "Dragon", "health": 200, "attack": 20, "defense": 15},
}

# login logic
def login():
    print("1. Create new account\n2. Login to existing account")
    choice = get_player_input("Choose an option: ")

    if choice == "1":
        username = get_player_input("Enter username: ")
        email = get_player_input("Enter email: ")
        password = get_player_input("Enter password: ")
        print(f"User  {username} created successfully!")
        return {"username": username, "email": email, "password": password}
    elif choice == "2":
        username = get_player_input("Enter username: ")
        password = get_player_input("Enter password: ")
        print(f"Welcome back, {username}!")
        return {"username": username, "email": "", "password": password}
    else:
        print("Invalid choice")
        return None

# Character menu
def character_menu(user):
    print("1. Create character\n2. Select existing character\n3. Delete existing game session")
    choice = get_player_input("Choose an option: ")

    if choice == "1":
        player_name = get_player_input("Enter your player name: ")
        print("Choose a character class:")
        for key, value in CHARACTER_CLASSES.items():
            print(f"{key}. {value['name']} (Health: {value['health']}, Mana: {value['mana']}, Attack: {value['attack']}, Defense: {value['defense']}, Role: {value['role']})")
        class_choice = get_player_input("Enter the number of your choice: ")
        if class_choice not in CHARACTER_CLASSES:
            print("Invalid choice. Exiting...")
            return None
        char_class = CHARACTER_CLASSES[class_choice]
        print(f"Player {player_name} created successfully!")
        return {
            "name": player_name,
            "user_id": user["username"],
            "health": char_class["health"],
            "mana": char_class["mana"],
            "attack": char_class["attack"],
            "defense": char_class["defense"],
            "char_class": char_class["name"],
            "char_role": char_class["role"],
        }
    elif choice == "2":
        # Fetch existing characters for the user
        print("Select a character:")
        print("1. Character 1")
        print("2. Character 2")
        choice = get_player_input("Enter the number of your choice: ")
        player_name = f"Character {choice}"
        print(f"Selected character: {player_name}")
        return {"name": player_name, "user_id": user["username"]}
    elif choice == "3":
        # Delete existing game session
        print("Select a character to delete:")
        print("1. Character 1")
        print("2. Character 2")
        choice = get_player_input("Enter the number of your choice: ")
        player_name = f"Character {choice}"
        print(f"Character {player_name} deleted successfully!")
        return None
    else:
        print("Invalid choice. Exiting...")
        return None

# Start game
def start_game(player):
    session = Session()
    game = Game(
        name="My Game",
        description="This is my game",
        char_class=player["char_class"],
        char_role=player["char_role"],
        player_id=player["user_id"],
    )
    session.add(game)
    session.commit()
    print("Game started successfully!")

    # Level 1
    print("\n--- Level 1: Lumber Jacks and Speakeasys ---")
    print("Location: Old Town China Town, Portland, Oregon")
    print("Player: Oh look, a creepy tunnel!!!… let's explore.")
    print("Wait… did you hear that??")
    print("Let's go!")

    # Create enemy - level 1
    enemy = Enemy(name=LEVEL_ENEMIES[1]["name"], game_id=game.id, health=LEVEL_ENEMIES[1]["health"], attack=LEVEL_ENEMIES[1]["attack"], defense=LEVEL_ENEMIES[1]["defense"])

    # Start battle
    print("Starting battle...")
    fight(player, enemy)

    # Check if player survived
    if player["health"] <= 0:
        print("Try again?… I'll be waiting")
        return
    else:
        print("You survived! Congratulations!")
        print("You little… I'll get you next time!!!")

    # Level 2
    print("\n--- Level 2: The Dark Forest ---")
    print("Location: Forest Park, Portland, Oregon")
    print("Player: The forest is eerily quiet...")
    print("Suddenly, an Orc appears!")

    # enemy - level 2
    enemy = Enemy(name=LEVEL_ENEMIES[2]["name"], game_id=game.id, health=LEVEL_ENEMIES[2]["health"], attack=LEVEL_ENEMIES[2]["attack"], defense=LEVEL_ENEMIES[2]["defense"])

    # Start battle
    print("Starting battle...")
    fight(player, enemy)

    # Check if player survived
    if player["health"] <= 0:
        print("Try again?… I'll be waiting")
        return
    else:
        print("You survived! Congratulations!")
        print("You little… I'll get you next time!!!")

    # Level 3
    print("\n--- Level 3: The Dragon's Lair ---")
    print("Location: Mount Hood, Oregon")
    print("Player: The air is thick with smoke...")
    print("A Dragon emerges from the shadows!")

    # enemy - level 3
    enemy = Enemy(name=LEVEL_ENEMIES[3]["name"], game_id=game.id, health=LEVEL_ENEMIES[3]["health"], attack=LEVEL_ENEMIES[3]["attack"], defense=LEVEL_ENEMIES[3]["defense"])

    # Start battle
    print("Starting battle...")
    fight(player, enemy)

    # Check if player survived
    if player["health"] <= 0:
        print("Try again?… I'll be waiting")
        return
    else:
        print("You survived! Congratulations!")
        print("You little… I'll get you next time!!!")

# Main function
def main():
    display_welcome_message()
    user = login()
    if user:
        player = character_menu(user)
        if player:
            start_game(player)

if __name__ == "__main__":
    main()