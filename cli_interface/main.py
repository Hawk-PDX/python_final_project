from game_logic.character import Character
from game_logic.level import Level
from game_logic.combat import Combat

class CLIInterface:
    def __init__(self):
        self.character = None
        self.level = None

    def display_welcome_message(self):
        print("Welcome to PDX Underground -- My CLI Game!")
        print("1. Create Character")
        print("2. Start Game")
        print("3. Exit")

    def create_character(self):
        name = input("Enter your character's name: ")
        char_class = input("Choose a class (Paladin/Mage/Rogue/Ranger): ")
        health = 100
        mana = 100
        attack = 10
        defense = 5
        char_role = "Adventurer"
        self.character = Character(name, char_class, health, mana, attack, defense, char_role)
        print(f"Character {name} created successfully!")

    def start_game(self):
        if not self.character:
            print("Please create a character first!")
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
        while True:
            self.display_welcome_message()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.create_character()
            elif choice == "2":
                self.start_game()
            elif choice == "3":
                print("Exiting game. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")