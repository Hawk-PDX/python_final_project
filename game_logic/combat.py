class Combat:
    def __init__(self, character, enemy):
        self.character = character
        self.enemy = enemy

    def start(self):
        if self.character.health <= 0 or self.enemy["health"] <= 0:
            print("Cannot start combat: one or both participants are already dead.")
            return

        print(f"Combat started between {self.character.name} and {self.enemy['name']}!")
        while self.character.health > 0 and self.enemy["health"] > 0:
            print(f"{self.character.name} Health: {self.character.health}")
            print(f"{self.enemy['name']} Health: {self.enemy['health']}")
            action = input("Choose action (attack/defend/run): ").strip().lower()

            if action == "attack":
                self.attack()
            elif action == "defend":
                self.defend()
            elif action == "run":
                print("You ran away!")
                break
            else:
                print("Invalid action!")

            if self.enemy["health"] > 0:
                self.enemy_attack()

        if self.character.health > 0:
            print(f"You defeated {self.enemy['name']}!")
        else:
            print("You were defeated!")

    def attack(self):
        damage = self.character.attack - self.enemy["defense"]
        if damage > 0:
            self.enemy["health"] -= damage
            print(f"You dealt {damage} damage to {self.enemy['name']}!")
        else:
            print(f"{self.enemy['name']} blocked your attack!")

    def defend(self):
        self.character.defense += 5
        print(f"{self.character.name} is defending!")

    def enemy_attack(self):
        damage = self.enemy["attack"] - self.character.defense
        if damage > 0:
            self.character.take_damage(damage)
            print(f"{self.enemy['name']} dealt {damage} damage to you!")
        else:
            print(f"You blocked {self.enemy['name']}'s attack!")