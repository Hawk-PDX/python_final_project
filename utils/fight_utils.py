from .exceptions import InsufficientHealthError, InvalidActionError
from models import Player, Enemy

def fight(player: Player, enemy: Enemy):
    while player.health > 0 and enemy.health > 0:
        print(f"Player health: {player.health}, Mana: {player.mana}")
        print(f"Enemy health: {enemy.health}")
        action = input("What do you want to do? (attack/use skill/use health potion/run): ").strip().lower()
        
        try:
            if action == "attack":
                enemy.health -= player.attack
                print(f"You attacked {enemy.name} for {player.attack} damage!")
            elif action == "use skill":
                skill = input("Which skill do you want to use? (Healing Strike/Shield Block): ").strip().lower()
                if skill == "healing strike":
                    player.health += 5
                    enemy.health -= 10
                    player.mana -= 10  # skill used, mana reduced accordingly
                    print(f"You used Healing Strike on {enemy.name}!")
                elif skill == "shield block":
                    player.defense += 20
                    player.mana -= 10  # same logic as above
                    print(f"You used Shield Block!")
                else:
                    raise InvalidActionError("Invalid skill selected.")
            elif action == "use health potion":
                if player.health_potions > 0:
                    player.health += 10
                    player.health_potions -= 1
                    print(f"You used a health potion!")
                else:
                    raise InsufficientHealthError("No health potions remaining.")
            elif action == "run":
                print("You ran away!")
                break
            else:
                raise InvalidActionError("Invalid action selected.")
            
            if enemy.health > 0:
                player.health -= enemy.attack
                print(f"{enemy.name} attacked you for {enemy.attack} damage!")
        except (InvalidActionError, InsufficientHealthError) as e:
            print(f"Error: {str(e)}")
            continue
    
    if player.health <= 0:
        print("You died!")
    else:
        print("You survived! Congratulations!")
        print("You little… I'll get you next time!!!")