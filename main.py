from models.database import init_db
from models.player import Player
from utils.cli_utils import display_welcome_message, get_player_input
from utils.game_utils import start_game

def main():
    # *** Initialize database ***
    init_db()

    # *** greet user ***
    display_welcome_message()

    # *** player input ***
    player_name = get_player_input("Enter your character's name: ")

    # *** Create player ***
    player = Player(name=player_name)

    # *** Start the game!@$#$@#%@!! :)) ***
    start_game(player)

if __name__ == "__main__":
    main()