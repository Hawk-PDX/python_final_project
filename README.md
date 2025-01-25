# PDX Underground - CLI Game

## Game Overview

PDX Underground is a text-based role-playing game (RPG) that offers a captivating narrative, character customization, dynamic combat system, and exploration.

## Game Rules

* Health: You and the enemy start with 100 health. The game ends when either health reaches zero.
* Attacks:
	+ Base Attack: A standard attack that deals damage to the enemy.
	+ Special Attack: Earned after landing 5 successful base attacks. Can be used to deal extra damage, heal yourself, or heal your group.
	+ Healing Potion: Restores health. You can use it once per game.
* Enemy Attacks:
	+ The enemy's damage is mostly consistent but can increase randomly during the battle.

## Character Classes

Choose from one of the following classes, each with unique abilities:

* Paladin
	+ Health: 200
	+ Mana: 100
	+ Skills:
		- Basic Attack: Deals 15 damage.
		- Healing Strike: Heals yourself for 5 health and deals 10 damage to the enemy.
		- Shield Block: Increases your defense by 20 for the next attack.
* Mage
	+ Health: 110
	+ Mana: 150
	+ Skills:
		- Basic Attack: Deals 25 damage.
		- Magic Missile: Deals 20 damage and heals your group by 5 health.
		- AOE Blanket Heal: Heals all party members by 45 health.
* Rogue
	+ Health: 140
	+ Mana: 120
	+ Skills:
		- Sneak Attack: Deals 167% of your base attack damage.
		- Backstab: Deals 220% of your base attack damage (available every 5 seconds).
		- Poison: Deals 3 damage to the enemy every 1.5 seconds and heals you for the same amount.
* Ranger
	+ Health: 150
	+ Mana: 100
	+ Skills:
		- Basic Attack: Deals 18 damage.
		- Energy Up: Increases your attack power by 160% for 6 seconds.
		- Poison Arrow: Deals 124% of your base attack damage and heals you for the same amount.

## Enemies

* Level 1: Goblin
	+ Health: 100
	+ Attack: 10
	+ Defense: 5
	+ Abilities:
		- Basic Attack: Deals 10 damage.
		- Random Proc: Occasionally increases attack damage by 5.
* Level 2: Orc
	+ Health: 150
	+ Attack: 15
	+ Defense: 10
	+ Abilities:
		- Basic Attack: Deals 15 damage.
		- Random Proc: Occasionally increases attack damage by 10.
* Level 3: Dragon
	+ Health: 200
	+ Attack: 20
	+ Defense: 15
	+ Abilities:
		- Basic Attack: Deals 20 damage.
		- Fire Breath: Deals 25 damage to all players.

## Commands

* During gameplay, you can use the following commands:
	+ Attack: Deal damage to the enemy.
	+ Heal: Heal yourself or a party member.
	+ Use Skill: Activate a special ability (e.g., Healing Strike, Shield Block).
	+ Use Health Potion: Restore health (limited to one use per game).
	+ Run: Escape from the battle (ends the game).

## Tips for Success

* Use special attacks strategically to maximize damage or heal yourself.
* Save your healing potion for critical moments.
* Pay attention to the enemy's attack patterns and adjust your strategy accordingly.

## Troubleshooting

* If the game doesn't start, ensure you have Python installed and are running the correct file (main.py).
* If you encounter errors, check your inputs and try again.

## Installation

1. Clone the repository using `git clone https://github.com/your-username/pdx-underground.git`
2. Install the required dependencies using `pip install -r requirements.txt`
3. Run the game using `python main.py`

## Contribution Guidelines

1. Fork the repository using `git fork https://github.com/your-username/pdx-underground.git`
2. Create a new branch using `git branch feature/new-feature`
3. Commit your changes using `git commit -m "Added new feature"`
4. Push your changes using `git push origin feature/new-feature`
5. Submit a pull request to the main repository