** python_final_project **

######

# Game Details/Objective

    Defeat the enemy using base or advanced attacks.
    The game will end when the player's/ enemy's health reaches zero.
    The player will start with 100 health and the enemy will start with 100 health.
    Players `special attacks` can be used to defeat the enemy as well as, in certain scenarios, heal the player and/or group. 
    The player will have the option to use a `healing potion` to restore health.
    The Enemy's attack damage will be, mostly, stagnant, but can/ will increase upon random `proc` events.


# Rules

    `tick` = 1 second
    `proc` = between 1-5 seconds... results are random
    `healing potion` = 1 use per game
    `special attack` = can be used as attained... special attack possibilities are as follows:
        -- for every 5 successfully landed base attacks, the player will gain a ** special attack **
        -- special attacks can be used to defeat the enemy, heal the player, or heal the group (this ability is shared amongst players/enemies alike...)
        -- special attacks can be used in conjunction with base attacks to increase damage output or, in kind, can be fired to provide a certain amount of hp back to all remaining (alive) players.

# Classes

    

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