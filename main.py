from utils.database import Session
from utils.crud_utils import create_user, validate_user_credentials, create_player, create_game, create_enemy, create_item
from utils.cli_utils import display_welcome_message, get_player_input
from utils.game_utils import fight
from models.player import Player
from models.game import Game
from models.enemy import Enemy

# Initialize login logic
def login():
    print("1. Create new account\n2. Login to existing account")
    choice = get_player_input("Choose an option: ")

    if choice == "1":
        username = get_player_input("Enter username: ")
        email = get_player_input("Enter email: ")
        password = get_player_input("Enter password: ")
        print(f"User    {username} created successfully!")
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
        print(f"Player {player_name} created successfully!")
        return {"name": player_name, "user_id": user["username"]}
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
    game = Game(name="My Game", description="This is my game", char_class="Warrior", char_role="Tank", player_id=player["user_id"])
    print("Game started successfully!")

    # Level 1
    print("Level 1: Lumber Jacks and Speakeasys")
    print("Location: Old Town China Town, Portland, Oregon")
    print("Player: Oh look, a creepy tunnel!!!… let's explore.")
    print("Wait… did you hear that??")
    print("Let's go!")

    # Create enemy for level 1
    enemy = Enemy(name="Goblin", game_id=game.id)

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
        return

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