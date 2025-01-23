** python_final_project **
# My Python Project - Game: PDX Underground

# CONSIDER... 
   
    Some elements of your actual experience may not be reflected in current implementation. This game is for educational/ demonstrative purposes, as of now. 

    It is probable that more advanced features/content will be added in the future. However, due to time constraints... we now move ahead in our coverage! XD

######


*  Dev notes (notes for relaying my implementation/
   understanding of specific case uses, additionally, questions for Sakib):

	• Reduced login logic to provide a more ‘test-friendly/demonstrative’ environment.
		— some logic remains and may appear unnecessary or redundant in regards to it’s present functionality… to include, unused imports, etc.

	• A large amount of included notes are rudimentary… most could/should/will be removed and / or amended at a later date.
	
	• some imports may appear foreign to my cohorts… and I apologize in advance!
			— if at any point, anybody digesting my final product may reach out and I would
				be happy to explain any facet outside the scope of our current Phase. 

	• kwargs — (key word arguments) allow for creation/handling of multiple named args... can be treated/referenced like a     dict w/i a function (question for Sakib, “is this considered best practice?”)

* Once again, Consider:

	Project requirements included the use of SQLite as Python’s core ORM ‘friendly’…
		— as I progressed through the development of this specific project’s expected functionality, I was originally unaware that, in order to succeed in final implementation, additional dependencies would be necessary. 
		— in that light, SQLAlchemy was used in it’s stead.

######

# WALKTHROUGH -- (Work in progess... apologies for any redundant/ unnecessary README content)

## Game Rules
	•	Health: You and the enemy start with 100 health. The game ends when either health reaches zero.
	•	Attacks:
	•	Base Attack: A standard attack that deals damage to the enemy.
	•	Special Attack: Earned after landing 5 successful base attacks. Can be used to deal extra damage, heal yourself, or heal your group.
	•	Healing Potion: Restores health. You can use it once per game.
	•	Enemy Attacks: The enemy's damage is mostly consistent but can increase randomly.



## Commands
* During gameplay, you can use the following commands:
	•	Attack: Deal damage to the enemy.
	•	Use Skill: Activate a special ability (e.g., Healing Strike, Shield Block).
	•	Use Health Potion: Restore health (limited to one use per game).
	•	Run: Escape from the battle (ends the game).

* Tips for Success
	•	Use special attacks strategically to maximize damage or heal yourself.
	•	Save your healing potion for critical moments.
	•	Pay attention to the enemy's attack patterns and adjust your strategy accordingly.

* Troubleshooting
	•	If the game doesn't start, ensure you have Python installed and are running the correct file (main.py).
	•	If you encounter errors, check your inputs and try again.

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


    # PDX Underground - CLI Game

---

## **Game Overview**

	*** PDX Underground - CLI Game ***
	
---
## Initialization notes:

	• As stated, the game's login logic has been reduced to avoid unnecessary complexity or potential problems.

			For now, please use the following credentials to login:

				username: hawk
				password: hawk1234
			
			New user creation is not currently supported.

	• If a game session is initiated, a game_database.db file will be created in the same directory as the main.py. This file will be used to store game data regarding your previous/current sesssion.
	
	• If you are reinitializing the game, the previous session's data will be overwritten. ALSO, it may be necessary to delete this file before reinitializing the game if you are experiencing issues with the game not properly resetting.

	*** HAVE FUN SUKKAS! :P ***

## **How to Play**

### **1. Starting the Game**

1. Open your terminal or command prompt.

2. Navigate to the folder where the game is installed.

3. Run the game by typing:
   ```bash
  ** python main.py
	or:
  ** python3 main.py (dependent on your python version)

## 2. Logging In

* You will be prompted to either:

* Create a new account: Enter a username, email, and password.

* Log in to an existing account: Enter your username and password.

## 3. Creating or Selecting a Character

* After logging in, you will be prompted to:

* Create a new character: Enter a name for your character and choose a class.

* Select an existing character: Choose from a list of pre-existing characters.

* Delete a character: Remove an existing character if needed.

## 4. Starting the Game

* Once your character is ready, the game will begin.

* You will enter Level 1, where you encounter your first enemy: a Goblin.

* Follow the on-screen instructions to attack, use skills, or heal.

# Game Rules

## Health and Mana

* Health: You and the enemy start with 100 health. The game ends when either health reaches zero.
Mana: Used to perform special attacks. You start with 100 mana.

## Attacks

* Base Attack: A standard attack that deals damage to the enemy.

* Special Attack: Earned after landing 5 successful base attacks. Can be used to deal extra damage, heal yourself, or heal your group.

* Healing Potion: Restores health. You can use it once per game.

## Enemy Attacks
The enemy's damage is mostly consistent but can increase randomly during the battle.

# Character Classes

Choose from one of the following classes, each with unique abilities:

## 1. Paladin
Health: 200
Mana: 100
Skills:
Basic Attack: Deals 15 damage.
Healing Strike: Heals yourself for 5 health and deals 10 damage to the enemy.
Shield Block: Increases your defense by 20 for the next attack.

## 2. Mage
Health: 110
Mana: 150
Skills:
Basic Attack: Deals 25 damage.
Magic Missile: Deals 20 damage and heals your group by 5 health.
AOE Blanket Heal: Heals all party members by 45 health.

## 3. Rogue
Health: 140
Mana: 120
Skills:
Sneak Attack: Deals 167% of your base attack damage.
Backstab: Deals 220% of your base attack damage (available every 5 seconds).
Poison: Deals 3 damage to the enemy every 1.5 seconds and heals you for the same amount.

## 4. Ranger
Health: 150
Mana: 100
Skills:
Basic Attack: Deals 18 damage.
Energy Up: Increases your attack power by 160% for 6 seconds.
Poison Arrow: Deals 124% of your base attack damage and heals you for the same amount.

# Enemies

## Level 1: Goblin
Health: 100
Attack: 10
Defense: 5
Abilities:
Basic Attack: Deals 10 damage.
Random Proc: Occasionally increases attack damage by 5.

## Level 2: Orc
Health: 150
Attack: 15
Defense: 10
Abilities:
Basic Attack: Deals 15 damage.
Random Proc: Occasionally increases attack damage by 10.

## Level 3: Dragon
Health: 200
Attack: 20
Defense: 15
Abilities:
Basic Attack: Deals 20 damage.
Fire Breath: Deals 25 damage to all players.

# Commands

* During gameplay, you can use the following commands:

* Attack: Deal damage to the enemy.

* Heal: Heal yourself or a party member.

* Use Skill: Activate a special ability (e.g., Healing Strike, Shield Block).

* Use Health Potion: Restore health (limited to one use per game).

* Run: Escape from the battle (ends the game).

## Tips for Success

* Use special attacks strategically to maximize damage or heal yourself.

* Save your healing potion for critical moments.

Pay attention to the enemy's attack patterns and adjust your strategy accordingly.

* Troubleshooting

If the game doesn't start, ensure you have Python installed and are running the correct file (main.py).

If you encounter errors, check your inputs and try again.

# Enjoy the Game!

* Dive into the world of PDX Underground and test your skills against challenging enemies. Good luck, and may your health never reach zero!
---
