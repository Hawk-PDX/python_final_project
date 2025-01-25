class Character:
    def __init__(self, name, char_class, health, mana, attack, defense, char_role):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.char_role = char_role
        self.level = None  # Reference to the current level
        self.health_potions = 1  # Each player starts with 1 minor health potion
        self.attack_potions = 1  # Each player starts with 1 minor attack potion

    def __repr__(self):
        return f"Character(name={self.name}, class={self.char_class}, health={self.health}, mana={self.mana}, attack={self.attack}, defense={self.defense}, role={self.char_role})"

    def take_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            if self.health < 0:
                self.health = 0

    def heal(self, amount):
        self.health += amount

    def use_health_potion(self):
        if self.health_potions > 0:
            self.heal(15)
            self.health_potions -= 1
            print(f"{self.name} used a minor health potion and restored 15 health!")
        else:
            print("No health potions remaining!")

    def use_attack_potion(self):
        if self.attack_potions > 0:
            self.attack *= 1.05  # Apply a 5% damage boost
            self.attack_potions -= 1
            print(f"{self.name} used a minor attack potion and increased their damage by 5%!")
        else:
            print("No attack potions remaining!")

    def set_level(self, level):
        self.level = level
        self.health_potions = 1  # Replenish health potion at the start of each level
        self.attack_potions = 1  # Replenish attack potion at the start of each level