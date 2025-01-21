from utils.database import Session
from utils.crud_utils import create_user, validate_user_credentials, create_player, create_game, create_enemy, create_item
from utils.cli_utils import display_welcome_message, get_player_input

def main():
    session = Session()
    display_welcome_message()

    # User Registration/Login
    print("1. Register\n2. Login")
    choice = get_player_input("Choose an option: ")

    if choice == "1":
        username = get_player_input("Enter username: ")
        email = get_player_input("Enter email: ")
        password = get_player_input("Enter password: ")
        user = create_user(session, username, email, password)
        print(f"User   {username} created successfully!")
    elif choice == "2":
        username = get_player_input("Enter username: ")
        password = get_player_input("Enter password: ")
        user = validate_user_credentials(session, username, password)
        if user:
            print(f"Welcome back, {username}!")
        else:
            print("Invalid credentials. Exiting...")
            session.close()
            return
    else:
        print("Invalid choice. Exiting...")
        session.close()
        return

    # Create a player for the user
    player_name = get_player_input("Enter your player name: ")
    player = create_player(session, name=player_name, user_id=user.id)

    # Create a game for the player
    game = create_game(session, name="You've be Shang-hai'd!", description="Save the Speakeasy", char_class="Warrior", char_role="Tank", player_id=player.id)

    # Create an enemy for the game
    enemy = create_enemy(session, name="Goblin", game_id=game.id)

    # Create an item for the player
    item = create_item(session, name="Health Potion", type="Consumable", player_id=player.id, value=10)

    print("Game setup complete! Let the adventure begin!")
    session.close()

if __name__ == "__main__":
    main()