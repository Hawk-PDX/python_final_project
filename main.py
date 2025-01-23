from utils.database import Session, engine
from models.base import Base
from models.player import Player
from models.game_base import Game
from models.enemy_base import Enemy
from models.user import User
from utils.cli_utils import display_welcome_message, get_player_input
from utils.game_utils import fight
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.style import Style
from rich.progress import Progress

console = Console()

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
    console.print(Panel("1. Create new account\n2. Login to existing account", title="[bold green]Login Menu[/bold green]", border_style="bright_cyan"))
    choice = get_player_input("Choose an option: ")

    if choice == "1":
        username = get_player_input("Enter username: ")
        email = get_player_input("Enter email: ")
        password = get_player_input("Enter password: ")
        console.print(f"User     [bold]{username}[/bold] created successfully!", style="bold green")
        return {"username": username, "email": email, "password": password}
    elif choice == "2":
        username = get_player_input("Enter username: ")
        password = get_player_input("Enter password: ")
        console.print(f"Welcome back, [bold]{username}[/bold]!", style="bold green")
        return {"username": username, "email": "", "password": password}
    else:
        console.print("Invalid choice", style="bold red")
        return None

# Character menu
def character_menu(user):
    console.print(Panel("1. Create character\n2. Select existing character\n3. Delete existing game session", title="[bold green]Character Menu[/bold green]", border_style="bright_cyan"))
    choice = get_player_input("Choose an option: ")

    if choice == "1":
        player_name = get_player_input("Enter your player name: ")
        console.print("Choose a character class:", style="bold blue")
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Option", style="dim", width=12)
        table.add_column("Class", style="bold green")
        table.add_column("Health", justify="right")
        table.add_column("Mana", justify="right")
        table.add_column("Attack", justify="right")
        table.add_column("Defense", justify="right")
        table.add_column("Role", style="bold cyan")

        for key, value in CHARACTER_CLASSES.items():
            table.add_row(
                key,
                value['name'],
                str(value['health']),
                str(value['mana']),
                str(value['attack']),
                str(value['defense']),
                value['role']
            )
        console.print(table)
        class_choice = get_player_input("Enter the number of your choice: ")
        if class_choice not in CHARACTER_CLASSES:
            console.print("Invalid choice. Exiting...", style="bold red")
            return None
        char_class = CHARACTER_CLASSES[class_choice]
        console.print(f"Player [bold]{player_name}[/bold] created successfully!", style="bold green")
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
        console.print("Select a character:", style="bold blue")
        console.print("1. Character 1")
        console.print("2. Character 2")
        choice = get_player_input("Enter the number of your choice: ")
        player_name = f"Character {choice}"
        console.print(f"Selected character: [bold]{player_name}[/bold]", style="bold green")
        return {"name": player_name, "user_id": user["username"]}
    elif choice == "3":
        console.print("Select a character to delete:", style="bold blue")
        console.print("1. Character 1")
        console.print("2. Character 2")
        choice = get_player_input("Enter the number of your choice: ")
        player_name = f"Character {choice}"
        console.print(f"Character [bold]{player_name}[/bold] deleted successfully!", style="bold green")
        return None
    else:
        console.print("Invalid choice. Exiting...", style="bold red")
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
    console.print(Panel("Game started successfully!", style="bold green"))

    # Level 1
    console.print(Panel("\n--- Level 1: Lumber Jacks and Speakeasys ---", style="bold blue"))
    console.print("Location: Old Town China Town, Portland, Oregon", style="italic")
    console.print("Player: Oh look, a creepy tunnel!!!… let's explore.", style="italic")
    console.print("Wait… did you hear that??", style="italic")
    console.print("Let's go!", style="bold green")

    # Create enemy - level 1
    enemy = Enemy(name=LEVEL_ENEMIES[1]["name"], game_id=game.id, health=LEVEL_ENEMIES[1]["health"], attack=LEVEL_ENEMIES[1]["attack"], defense=LEVEL_ENEMIES[1]["defense"])

    # Start battle
    console.print(Panel("Starting battle...", style="bold red"))
    fight(player, enemy)

    # Check if player survived
    if player["health"] <= 0:
        console.print(Panel("Try again?… I'll be waiting", style="bold red"))
        return
    else:
        console.print(Panel("You survived! Congratulations!", style="bold green"))
        console.print("You little… I'll get you next time!!!", style="italic")

    # Level 2
    console.print(Panel("\n--- Level 2: The Dark Forest ---", style="bold blue"))
    console.print("Location: Forest Park, Portland, Oregon", style="italic")
    console.print("Player: The forest is eerily quiet...", style="italic")
    console.print("Suddenly, an Orc appears!", style="bold red")

    # enemy - level 2
    enemy = Enemy(name=LEVEL_ENEMIES[2]["name"], game_id=game.id, health=LEVEL_ENEMIES[2]["health"], attack=LEVEL_ENEMIES[2]["attack"], defense=LEVEL_ENEMIES[2]["defense"])

    # Start battle
    console.print(Panel("Starting battle...", style="bold red"))
    fight(player, enemy)

    # Check if player survived
    if player["health"] <= 0:
        console.print(Panel("Try again?… I'll be waiting", style="bold red"))
        return
    else:
        console.print(Panel("You survived! Congratulations!", style="bold green"))
        console.print("You little… I'll get you next time!!!", style="italic")

    # Level 3
    console.print(Panel("\n--- Level 3: The Dragon's Lair ---", style="bold blue"))
    console.print("Location: Mount Hood, Oregon", style="italic")
    console.print("Player: The air is thick with smoke...", style="italic")
    console.print("A Dragon emerges from the shadows!", style="bold red")

    # enemy - level 3
    enemy = Enemy(name=LEVEL_ENEMIES[3]["name"], game_id=game.id, health=LEVEL_ENEMIES[3]["health"], attack=LEVEL_ENEMIES[3]["attack"], defense=LEVEL_ENEMIES[3]["defense"])

    # Start battle
    console.print(Panel("Starting battle...", style="bold red"))
    fight(player, enemy)

    # Check if player survived
    if player["health"] <= 0:
        console.print(Panel("Try again?… I'll be waiting", style="bold red"))
        return
    else:
        console.print(Panel("You survived! Congratulations!", style="bold green"))
        console.print("You little… I'll get you next time!!!", style="italic")

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