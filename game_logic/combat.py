from rich.console import Console
from rich.table import Table

console = Console()

class Combat:
    def __init__(self, character, enemy):
        self.character = character
        self.enemy = enemy

    def start(self):
        if self.character.health <= 0 or self.enemy["health"] <= 0:
            console.print("[bold red]Cannot start combat: one or both participants are already dead.[/bold red]")
            return

        console.print(f"[bold yellow]Combat started between {self.character.name} and {self.enemy['name']}![/bold yellow]")
        while self.character.health > 0 and self.enemy["health"] > 0:
            self.display_combat_status()
            action = console.input("[bold]Choose action (1/2/3/4/5): [/bold]").strip()

            if action == "1":
                self.attack()
            elif action == "2":
                self.defend()
            elif action == "3":
                self.character.use_health_potion()
            elif action == "4":
                self.character.use_attack_potion()
            elif action == "5":
                console.print("[bold red]You ran away![/bold red]")
                break
            else:
                console.print("[bold red]Invalid action! Please choose 1, 2, 3, 4, or 5.[/bold red]")
                continue

            # Enemy attacks after the player's turn
            if self.enemy["health"] > 0:
                self.enemy_attack()

        if self.character.health > 0:
            console.print(f"[bold green]You defeated {self.enemy['name']}![/bold green]")
        else:
            console.print("[bold red]You were defeated![/bold red]")

    def display_combat_status(self):
        """Display the combat status using rich."""
        status_table = Table(title="Combat Status", border_style="bright_blue")
        status_table.add_column("Character", justify="left", style="cyan")
        status_table.add_column("Health", justify="right", style="green")
        status_table.add_row(f"{self.character.name}", f"{self.character.health}")
        status_table.add_row(f"{self.enemy['name']}", f"{self.enemy['health']}")
        console.print(status_table)

        action_table = Table(title="Actions", show_header=False, border_style="bright_yellow")
        action_table.add_column("Option", justify="center", style="cyan")
        action_table.add_column("Description", justify="left", style="magenta")
        action_table.add_row("1", "Attack")
        action_table.add_row("2", "Defend")
        action_table.add_row("3", "Use Health Potion")
        action_table.add_row("4", "Use Attack Potion")
        action_table.add_row("5", "Run")
        console.print(action_table)

    def attack(self):
        damage = self.character.attack - self.enemy["defense"]
        if damage > 0:
            self.enemy["health"] -= damage
            console.print(f"[bold green]You dealt {damage} damage to {self.enemy['name']}![/bold green]")
        else:
            console.print(f"[bold yellow]{self.enemy['name']} blocked your attack![/bold yellow]")

    def defend(self):
        self.character.temporary_defense_boost = 5  # Apply a temporary defense boost
        console.print(f"[bold cyan]{self.character.name} is defending![/bold cyan]")

    def enemy_attack(self):
        # Calculate damage with temporary defense boost
        damage = self.enemy["attack"] - (self.character.defense + self.character.temporary_defense_boost)
        if damage > 0:
            self.character.take_damage(damage)
            console.print(f"[bold red]{self.enemy['name']} dealt {damage} damage to you![/bold red]")
        else:
            console.print(f"[bold yellow]You blocked {self.enemy['name']}'s attack![/bold yellow]")
        
        # Reset temporary defense boost after the enemy's attack
        self.character.temporary_defense_boost = 0