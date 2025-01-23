from .fight_utils import fight

def start_game(player):
    # Initialize health and mana/energy for player
    player["health"] = 100  # Set player health to 100%
    player["mana"] = 100    # Set player mana to 100%

    # Create enemy - level 1
    enemy = Enemy(name="Goblin", health=100, attack=10, defense=5)

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