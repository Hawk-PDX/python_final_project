** python_final_project **

# CONSIDER... 
    Some elements of your actual experience may not be reflected in current implementation. This game is for educational/ demonstrative purposes, as of now. 

    It is probable that more advanced features/content will be added in the future. However, due to time constraints... we now move ahead in our coverage! XD

######

***

Dev notes (notes for relaying my implementation/understanding of specific case uses, additionally, questions for Sakib):

	• Reduced login logic to provide a more ‘test-friendly/demonstrative’ environment.
		— some logic remains and may appear unnecessary or redundant in regards to it’s present functionality… to include, unused imports, etc.

	• A large amount of included notes are rudimentary… most could/should/will be removed and / or amended at a later date.
	
	• some imports may appear foreign to my cohorts… and I apologize in advance!
			— if at any point, anybody digesting my final product may reach out and I would
				be happy to explain any facet outside the scope of our current Phase. 

	• kwargs — (key word arguments) allow for creation/handling of multiple named args... can be treated/referenced like a     dict w/i a function (question for Sakib, “is this considered best practice?”)

Once again, Consider:

	Project requirements included the use of SQLite as Python’s core ORM ‘friendly’…
		— as I progressed through the development of this specific project’s expected functionality, I was originally unaware that, in order to succeed in final implementation, additional dependencies would be necessary. 
		— in that light, SQLAlchemy was used in it’s stead.

######

# WALKTHROUGH -- VERBOSE

Creating or Selecting a Character
	•	After logging in, you will be prompted to:
	•	Create a new character: Enter a name for your character.
	•	Select an existing character: Choose from a list of pre-existing characters.
	•	Delete a character: Remove an existing character if needed.
4. Starting the Game
	•	Once your character is ready, the game will begin.
	•	You will enter Level 1, where you encounter your first enemy: a Goblin.
	•	Follow the on-screen instructions to attack, use skills, or heal.

Game Rules
	•	Health: You and the enemy start with 100 health. The game ends when either health reaches zero.
	•	Attacks:
	•	Base Attack: A standard attack that deals damage to the enemy.
	•	Special Attack: Earned after landing 5 successful base attacks. Can be used to deal extra damage, heal yourself, or heal your group.
	•	Healing Potion: Restores health. You can use it once per game.
	•	Enemy Attacks: The enemy's damage is mostly consistent but can increase randomly.

Classes
Choose from one of the following classes, each with unique abilities:
1. Paladin
	•	Health: 200
	•	Skills: Basic Attack, Healing, Shield Block
2. Mage
	•	Health: 110
	•	Skills: Basic Attack, Magic Missile (damage + group heal), AOE Blanket Heal (heals all party members)
3. Rogue
	•	Health: 140
	•	Skills: Sneak Attack (167% damage), Backstab (220% damage), Poison (damage over time)
4. Ranger
	•	Health: 150
	•	Skills: Basic Attack, Energy Up (increases attack power), Poison Arrow (damage + self-heal)

Commands
During gameplay, you can use the following commands:
	•	Attack: Deal damage to the enemy.
	•	Use Skill: Activate a special ability (e.g., Healing Strike, Shield Block).
	•	Use Health Potion: Restore health (limited to one use per game).
	•	Run: Escape from the battle (ends the game).

Tips for Success
	•	Use special attacks strategically to maximize damage or heal yourself.
	•	Save your healing potion for critical moments.
	•	Pay attention to the enemy's attack patterns and adjust your strategy accordingly.

Troubleshooting
	•	If the game doesn't start, ensure you have Python installed and are running the correct file (main.py).
	•	If you encounter errors, check your inputs and try again.

Enjoy the Game!
Dive into the world of PDX Underground and test your skills against challenging enemies. Good luck, and may your health never reach zero!

######

# Game Details/Objective - BASE

    Defeat the *enemy* using base or advanced attacks.
    The game will end when the *player*/ *enemy* health is <= 0.
    The *player* will start with 100% health and the *enemy* will start with 100% health.
    *Players* special attacks can be used to defeat the *enemy* as well as, in certain scenarios, heal the player and/or group. (group scenario not currently available) 
    *Player* will have the option to use a `healing potion` to restore health.
    The Enemy's attack damage will be, mostly, stagnant, but can/ will increase upon random `proc` events.


# Rules

    `tick` = 1 second
    `proc` = between 1-5 seconds... results are random
    `healing potion` = 1 use per game
    `special attack` = can be used as attained... special attack possibilities are as follows:
        -- for every 5 successfully landed base attacks, the player will gain a ** special attack **
        -- special attacks can be used to defeat the enemy, heal the player, or heal the group (this ability is shared amongst players/enemies alike...)
        -- special attacks can be used in conjunction with base attacks to increase damage output or, in kind, can be fired to provide a certain amount of hp back to all remaining (alive) players.


# Classes/ role mechanics
  

*** Class 1: Paladin ***

    Name: Paladin
    Base_health: 200
    Class_level: []
    Class_skills: Basic Attack, Healing, Shield Block
   

*** Class 2: Mage ***

    Name: Mage
    Base_health: 110
    Class_level: []
    Class_skills: Basic Attack, Magic Missile (dmg + aoe trickle hp bonus for group members within range), AOE Blanket Healz (substantial (+45 hp to all party members within range))

*** Class 3: Rogue ***

    Name: Rogue
    Base_health: 140
    Class_level: []
    Class_skills: Sneak Attack (167% of base attack dmg), 
    Backstab = (220% of base_attack, available every 5 seconds), 
    Poison = (+ and -) 3 hp (plus for self == neg hp for each enemy) every `tick`... 1 `tick` = 1/(1.5 seconds) ### 1 to 1 self healz (based on equivalent enemy HP draw...) ###

*** Class 4: Ranger ***

    Name: Hunter
    Base_health: 150
    Class_level: []
    Class_skills: Basic Attack (15hp, (every `tick`)), Energy Up (Basic Attack * 160% of base dps for 6 seconds, party members att+ 107% for same period(7 seconds)), Poison Arrow = burn (enemy) == reclammation of self hp, which denotes +- 124% of base attack dmg (dealt/received)

# Initializing the Game
    # PDX Underground - CLI Game

Welcome to **PDX Underground**, a text-based command-line game where you battle enemies, use special attacks, and survive to win! This guide will help you get started and understand the game structure.

---

## **Game Overview**

In **PDX Underground**, you play as a hero battling enemies in a series of levels. Your goal is to defeat the enemy by using base attacks, special attacks, and healing potions. The game ends when either you or the enemy's health reaches zero.

---

# PDX Underground - CLI Game

Welcome to **PDX Underground**, a text-based command-line game where you battle enemies, use special attacks, and survive to win! This guide will help you get started and understand the game structure.

---

## **Game Overview**

In **PDX Underground**, you play as a hero battling enemies in a series of levels. Your goal is to defeat the enemy by using base attacks, special attacks, and healing potions. The game ends when either you or the enemy's health reaches zero.

---
## **How to Play**

### **1. Starting the Game**
1. Open your terminal or command prompt.
2. Navigate to the folder where the game is installed.
3. Run the game by typing:
   ```bash -- zsh
   python main.py
