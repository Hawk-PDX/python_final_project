from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, default=100)
    level = Column(Integer, default=1)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populate='players')
    items = relationship("Item", back_populates="player")
    battles = relationship("Battle", back_populates="player")
        

    def __repr__(self):
        return f"Player {self.role} Beginner Stats: {self.attributes}"

    def select_role(self):
        roles = ["Paladin", "Bard", "Rogue", "Ranger"]
        print("Select a role:")
        for i, role in enumerate(roles):
            print(f"{i+1}. {role}")
        choice = input("Enter the number of your chosen role: ")
        self.role = roles[int(choice) - 1]
        print(f"You have chosen the role of {self.role}.")

    def add_item_to_inventory(self, item):
        if len(self.inventory) < 20:
            self.inventory.append(item)
            print(f"{item} added to inventory.")
        else:
            print("Inventory is full.")

    def remove_item_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} removed from inventory.")
        else:
            print(f"{item} not found in inventory.")

    def equip_item(self, item, slot):
        if item in self.inventory:
            if self.equipable_slots[slot] is not None:
                self.remove_item_from_inventory(self.equipable_slots[slot])
            self.equipable_slots[slot] = item
            self.remove_item_from_inventory(item)
            print(f"{item} equipped to {slot} slot.")
        else:
            print(f"{item} not found in inventory.")

    def unequip_item(self, slot):
        if self.equipable_slots[slot] is not None:
            item = self.equipable_slots[slot]
            self.add_item_to_inventory(item)
            self.equipable_slots[slot] = None
            print(f"{item} unequipped from {slot} slot.")
        else:
            print(f"{slot} slot is empty.")

    def update_stat(self, stat, value):
        if stat in self.attributes:
            self.attributes[stat] += value
            print(f"{stat} updated to {self.attributes[stat]}.")
        else:
            print(f"{stat} not found in attributes.")

# Example usage:
player = Player(0, 0)
player.select_role()
player.add_item_to_inventory("Sword")
player.equip_item("Sword", "weapon")
player.update_stat("health", 10)
print(player.attributes)
print(player.equipable_slots)