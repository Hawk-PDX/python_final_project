from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.style import Style

console = Console()

def display_menu():
    """Display the main menu using rich."""
    menu_table = Table(title="Main Menu", show_header=False, border_style="bright_green")
    menu_table.add_column("Option", justify="center", style="cyan")
    menu_table.add_column("Description", justify="left", style="magenta")
    menu_table.add_row("1", "Create Character")
    menu_table.add_row("2", "Start Game")
    menu_table.add_row("3", "Exit")
    console.print(menu_table)