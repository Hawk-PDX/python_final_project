from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.style import Style
from game_logic.character import Character
from game_logic.level import Level
from game_logic.combat import Combat

console = Console()

class CLIInterface:
    def __init__(self):
        self.character = None
        self.level = None

    def display_welcome_message(self):
        """Display a stylish welcome message using rich."""
        welcome_text = Text("Welcome to PDX Underground -- My CLI Game!", style="bold blue")
        panel = Panel(
            welcome_text,
            title="[bold red]PDX Underground[/bold red]",
            subtitle="[italic]An RPG Adventure[/italic]",
            border_style="bright_yellow"
        )
        console.print(panel)

    def display_menu(self):
        """Display the main menu using rich."""
        menu_table = Table(title="Main Menu", show_header=False, border_style="bright_green")
        menu_table.add_column("Option", justify="center", style="cyan")
        menu_table.add_column("Description", justify="left", style="magenta")
        menu_table.add_row("1", "Create Character")
        menu_table.add_row("2", "Start Game")
        menu_table.add_row("3", "Exit")
        console.print(menu_table)

    def create_character(self):
        """Create a character with rich styling."""
        console.print("[bold cyan]Create Your Character[/bold cyan]")
        name = console.input("[bold]Enter your character's name: [/bold]")
        char_class = console.input("[bold]Choose a class (Paladin/Mage/Rogue/Ranger): [/bold]")
        health = 100
        mana = 100
        attack = 10
        defense = 5
        char_role = "Adventurer"
        self.character = Character(name, char_class, health, mana, attack, defense, char_role)
        console.print(f"[bold green]Character {name} created successfully![/bold green]")

    def start_game(self):
        """Start the game with rich styling."""
        if not self.character:
            console.print("[bold red]Please create a character first![/bold red]")
            return

        # Initialize Level 1
        enemies = [{"name": "Goblin", "health": 100, "attack": 10, "defense": 5}]
        rewards = ["Gold", "Health Potion"]
        self.level = Level(1, enemies, rewards)
        self.level.set_character(self.character)
        self.level.start()

        # Start combat with the first enemy
        combat = Combat(self.character, enemies[0])
        combat.start()

    def main(self):
        """Main loop with rich styling."""
        while True:
            self.display_welcome_message()
            self.display_menu()
            choice = console.input("[bold]Choose an option (1/2/3): [/bold]").strip()

            if choice == "1":
                self.create_character()
            elif choice == "2":
                self.start_game()
            elif choice == "3":
                console.print("[bold red]Exiting game. Goodbye![/bold red]")
                break
            else:
                console.print("[bold red]Invalid choice. Please choose 1, 2, or 3.[/bold red]")