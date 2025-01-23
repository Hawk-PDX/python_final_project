from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def display_welcome_message():
    welcome_text = Text("Welcome to PDX Underground -- My CLI Game!", style="bold blue")
    panel = Panel(welcome_text, title="[bold red]PDX Underground[/bold red]", subtitle="[italic]An RPG Adventure[/italic]", border_style="bright_yellow")
    console.print(panel)

def get_player_input(prompt):
    return input(prompt)