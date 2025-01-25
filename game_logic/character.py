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

    def __repr__(self):
        return f"Character(name={self.name}, class={self.char_class}, health={self.health}, mana={self.mana}, attack={self.attack}, defense={self.defense}, role={self.char_role})"

    def take_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            if self.health < 0:
                self.health = 0

    def heal(self, amount):
        self.health += amount

    def set_level(self, level):
        self.level = level