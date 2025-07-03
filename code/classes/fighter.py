"""
Fighter class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

FIGHTER_CLASS: Dict[str, Any] = {
    'name': 'Fighter',
    'hit_die': 10,
    'primary_ability': ['Strength', 'Dexterity'],
    'saving_throws': ['Strength', 'Constitution'],
    'proficiencies': {
        'armor': ['Light Armor', 'Medium Armor', 'Heavy Armor', 'Shields'],
        'weapons': ['Simple Weapons', 'Martial Weapons'],
        'tools': [],
        'skills': [
            'Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Persuasion', 'Perception', 'Survival'
        ]
    },
    'starting_equipment': [
        [
            'Chain Mail', 'Greatsword', 'Flail', '8 Javelins', "Dungeoneer's Pack", '4 GP'
        ],
        [
            'Studded Leather Armor', 'Scimitar', 'Shortsword', 'Longbow', '20 Arrows', 'Quiver', "Dungeoneer's Pack", '11 GP'
        ],
        ['155 GP']
    ]
}

FIGHTER_LEVELS: Dict[int, Dict[str, Any]] = {
    1:  {"proficiency_bonus": 2, "features": ["Fighting Style", "Second Wind", "Weapon Mastery"], "second_wind": 2, "weapon_mastery": 3},
    2:  {"proficiency_bonus": 2, "features": ["Action Surge (One Use)", "Tactical Mind"], "second_wind": 2, "weapon_mastery": 3},
    3:  {"proficiency_bonus": 2, "features": ["Fighter Subclass"], "second_wind": 2, "weapon_mastery": 3},
    4:  {"proficiency_bonus": 2, "features": ["Ability Score Improvement"], "second_wind": 3, "weapon_mastery": 4},
    5:  {"proficiency_bonus": 3, "features": ["Extra Attack", "Tactical Shift"], "second_wind": 3, "weapon_mastery": 4},
    6:  {"proficiency_bonus": 3, "features": ["Ability Score Improvement"], "second_wind": 3, "weapon_mastery": 4},
    7:  {"proficiency_bonus": 3, "features": ["Subclass Feature"], "second_wind": 3, "weapon_mastery": 4},
    8:  {"proficiency_bonus": 3, "features": ["Ability Score Improvement"], "second_wind": 3, "weapon_mastery": 4},
    9:  {"proficiency_bonus": 4, "features": ["Indomitable (One Use)", "Tactical Master"], "second_wind": 3, "weapon_mastery": 4},
    10: {"proficiency_bonus": 4, "features": ["Subclass Feature"], "second_wind": 4, "weapon_mastery": 5},
    11: {"proficiency_bonus": 4, "features": ["Two Extra Attacks"], "second_wind": 4, "weapon_mastery": 5},
    12: {"proficiency_bonus": 4, "features": ["Ability Score Improvement"], "second_wind": 4, "weapon_mastery": 5},
    13: {"proficiency_bonus": 5, "features": ["Indomitable (Two Uses)", "Studied Attacks"], "second_wind": 4, "weapon_mastery": 5},
    14: {"proficiency_bonus": 5, "features": ["Ability Score Improvement"], "second_wind": 4, "weapon_mastery": 5},
    15: {"proficiency_bonus": 5, "features": ["Subclass Feature"], "second_wind": 4, "weapon_mastery": 5},
    16: {"proficiency_bonus": 5, "features": ["Ability Score Improvement"], "second_wind": 4, "weapon_mastery": 6},
    17: {"proficiency_bonus": 6, "features": ["Action Surge (Two Uses)", "Indomitable (Three Uses)"], "second_wind": 4, "weapon_mastery": 6},
    18: {"proficiency_bonus": 6, "features": ["Subclass Feature"], "second_wind": 4, "weapon_mastery": 6},
    19: {"proficiency_bonus": 6, "features": ["Epic Boon"], "second_wind": 4, "weapon_mastery": 6},
    20: {"proficiency_bonus": 6, "features": ["Three Extra Attacks"], "second_wind": 4, "weapon_mastery": 6},
}

FIGHTER_FEATURES: Dict[str, Any] = {
    "Fighting Style": (
        "You gain a Fighting Style feat of your choice (see chapter 5). Defense is recommended.\n\n"
        "Whenever you gain a Fighter level, you can replace the feat you chose with a different Fighting Style feat."
    ),
    "Second Wind": (
        "You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action, you can use it to regain Hit Points equal to 1d10 plus your Fighter level.\n\n"
        "You can use this feature twice. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.\n\n"
        "When you reach certain Fighter levels, you gain more uses of this feature, as shown in the Second Wind column of the Fighter Features table."
    ),
    "Weapon Mastery": (
        "Your training with weapons allows you to use the mastery properties of three kinds of Simple or Martial weapons of your choice. Whenever you finish a Long Rest, you can practice weapon drills and change one of those weapon choices.\n\n"
        "When you reach certain Fighter levels, you gain the ability to use the mastery properties of more kinds of weapons, as shown in the Weapon Mastery column of the Fighter Features table."
    ),
    "Action Surge": (
        "You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action, except the Magic action.\n\n"
        "Once you use this feature, you can't do so again until you finish a Short or Long Rest. Starting at level 17, you can use it twice before a rest but only once on a turn."
    ),
    "Tactical Mind": (
        "You have a mind for tactics on and off the battlefield. When you fail an ability check, you can expend a use of your Second Wind to push yourself toward success. Rather than regaining Hit Points, you roll 1d10 and add the number rolled to the ability check, potentially turning it into a success. If the check still fails, this use of Second Wind isn't expended."
    ),
    "Fighter Subclass": (
        "You gain a Fighter subclass of your choice. The Battle Master, Champion, Eldritch Knight, and Psi Warrior subclasses are detailed after this class's description. A subclass is a specialization that grants you features at certain Fighter levels. For the rest of your career, you gain each of your subclass's features that are of your Fighter level or lower.\n\n"
        "Fighter Subclasses: Battle Master, Champion, Eldritch Knight, Psi Warrior."
    ),
    "Ability Score Improvement": (
        "You gain the Ability Score Improvement feat or another feat of your choice for which you qualify. You gain this feature again at Fighter levels 6, 8, 12, 14, and 16."
    ),
    "Extra Attack": (
        "You can attack twice instead of once whenever you take the Attack action on your turn."
    ),
    "Tactical Shift": (
        "Whenever you activate your Second Wind with a Bonus Action, you can move up to half your Speed without provoking Opportunity Attacks."
    ),
    "Indomitable": (
        "If you fail a saving throw, you can reroll it with a bonus equal to your Fighter level. You must use the new roll, and you can't use this feature again until you finish a Long Rest.\n\n"
        "You can use this feature twice before a Long Rest starting at level 13 and three times before a Long Rest starting at level 17."
    ),
    "Tactical Master": (
        "When you attack with a weapon whose mastery property you can use, you can replace that property with the Push, Sap, or Slow property for that attack."
    ),
    "Two Extra Attacks": (
        "You can attack three times instead of once whenever you take the Attack action on your turn."
    ),
    "Studied Attacks": (
        "You study your opponents and learn from each attack you make. If you make an attack roll against a creature and miss, you have Advantage on your next attack roll against that creature before the end of your next turn."
    ),
    "Epic Boon": (
        "You gain an Epic Boon feat or another feat of your choice for which you qualify. Boon of Combat Prowess is recommended."
    ),
    "Three Extra Attacks": (
        "You can attack four times instead of once whenever you take the Attack action on your turn."
    ),
}

MANEUVER_OPTIONS: Dict[str, str] = {
    "Ambush": (
        "When you make a Dexterity (Stealth) check or an Initiative roll, you can expend one Superiority Die and add the die to the roll, unless you have the Incapacitated condition."
    ),
    "Bait and Switch": (
        "When you're within 5 feet of a creature on your turn, you can expend one Superiority Die and switch places with that creature, provided you spend at least 5 feet of movement and the creature is willing and doesn't have the Incapacitated condition. This movement doesn't provoke Opportunity Attacks.\n\n"
        "Roll the Superiority Die. Until the start of your next turn, you or the other creature (your choice) gains a bonus to AC equal to the number rolled."
    ),
    "Commander's Strike": (
        "When you take the Attack action on your turn, you can replace one of your attacks to direct one of your companions to strike. When you do so, choose a willing creature who can see or hear you and expend one Superiority Die. That creature can immediately use its Reaction to make one attack with a weapon or an Unarmed Strike, adding the Superiority Die to the attack's damage roll on a hit."
    ),
    "Commanding Presence": (
        "When you make a Charisma (Intimidation, Performance, or Persuasion) check, you can expend one Superiority Die and add that die to the roll."
    ),
    "Disarming Attack": (
        "When you hit a creature with an attack roll, you can expend one Superiority Die to attempt to disarm the target. Add the Superiority Die roll to the attack's damage roll. The target must succeed on a Strength saving throw or drop one object of your choice that it's holding, with the object landing in its space."
    ),
    "Distracting Strike": (
        "When you hit a creature with an attack roll, you can expend one Superiority Die to distract the target. Add the Superiority Die roll to the attack's damage roll. The next attack roll against the target by an attacker other than you has Advantage if the attack is made before the start of your next turn."
    ),
    "Evasive Footwork": (
        "As a Bonus Action, you can expend one Superiority Die and take the Disengage action. You also roll the die and add the number rolled to your AC until the start of your next turn."
    ),
    "Feinting Attack": (
        "As a Bonus Action, you can expend one Superiority Die to feint, choosing one creature within 5 feet of yourself as your target. You have Advantage on your next attack roll against that target this turn. If that attack hits, add the Superiority Die to the attack's damage roll."
    ),
    "Goading Attack": (
        "When you hit a creature with an attack roll, you can expend one Superiority Die to attempt to goad the target into attacking you. Add the Superiority Die to the attack's damage roll. The target must succeed on a Wisdom saving throw or have Disadvantage on attack rolls against targets other than you until the end of your next turn."
    ),
    "Lunging Attack": (
        "As a Bonus Action, you can expend one Superiority Die and take the Dash action. If you move at least 5 feet in a straight line immediately before hitting with a melee attack as part of the Attack action on this turn, you can add the Superiority Die to the attack's damage roll."
    ),
    "Maneuvering Attack": (
        "When you hit a creature with an attack roll, you can expend one Superiority Die to maneuver one of your comrades into another position. Add the Superiority Die roll to the attack's damage roll, and choose a willing creature who can see or hear you. That creature can use its Reaction to move up to half its Speed without provoking an Opportunity Attacks from the target of your attack."
    ),
    "Menacing Attack": (
        "When you hit a creature with an attack roll, you can expend one Superiority Die to attempt to frighten the target. Add the Superiority Die to the attack's damage roll. The target must succeed on a Wisdom saving throw or have the Frightened condition until the end of your next turn."
    ),
    "Parry": (
        "When another creature damages you with a melee attack roll, you can take a Reaction and expend one Superiority Die to reduce the damage by the number you roll on your Superiority Die plus your Strength or Dexterity modifier (your choice)."
    ),
    "Precision Attack": (
        "When you miss with an attack roll, you can expend one Superiority Die, roll that die, and add it to the attack roll, potentially causing the attack to hit."
    ),
    "Pushing Attack": (
        "When you hit a creature with an attack roll using a weapon or an Unarmed Strike, you can expend one Superiority Die to attempt to drive the target back. Add the Superiority Die to the attack's damage roll. If the target is Large or smaller, it must succeed on a Strength saving throw or be pushed up to 15 feet directly away from you."
    ),
    "Rally": (
        "As a Bonus Action, you can expend one Superiority Die to bolster the resolve of a companion. Choose an ally of yours within 30 feet of yourself who can see or hear you. That creature gains Temporary Hit Points equal to the Superiority Die roll plus half your Fighter level (round down)."
    ),
    "Riposte": (
        "When a creature misses you with a melee attack roll, you can take a Reaction and expend one Superiority Die to make a melee attack roll with a weapon or an Unarmed Strike against the creature. If you hit, add the Superiority Die to the attack's damage."
    ),
    "Sweeping Attack": (
        "When you hit a creature with a melee attack roll using a weapon or an Unarmed Strike, you can expend one Superiority Die to attempt to damage another creature. Choose another creature within 5 feet of the original target and within your reach. If the original attack roll would hit the second creature, it takes damage equal to the number you roll on your Superiority Die. The damage is of the same type dealt by the original attack."
    ),
    "Tactical Assessment": (
        "When you make an Intelligence (History or Investigation) check or a Wisdom (Insight) check, you can expend one Superiority Die and add that die to the ability check."
    ),
    "Trip Attack": (
        "When you hit a creature with an attack roll using a weapon or an Unarmed Strike, you can expend one Superiority Die and add the die to the attack's damage roll. If the target is Large or smaller, it must succeed on a Strength saving throw or have the Prone condition."
    ),
}

# Subclass dictionaries
BATTLE_MASTER: Dict[Union[str, int], Any] = {
    "description": "Master Sophisticated Battle Maneuvers. Battle Masters are students of the art of battle, learning martial techniques passed down through generations.",
    3: {
        "Combat Superiority": (
            "Your experience on the battlefield has refined your fighting techniques. You learn maneuvers that are fueled by special dice called Superiority Dice.\n\n"
            "Maneuvers. You learn three maneuvers of your choice from the 'Maneuver Options' section. You learn two additional maneuvers at levels 7, 10, and 15. Each time you learn new maneuvers, you can also replace one maneuver you know with a different one.\n\n"
            "Superiority Dice. You have four Superiority Dice, which are d8s. You gain an additional die at levels 7 (five dice) and 15 (six dice). You regain all expended dice on a Short or Long Rest.\n\n"
            "Saving Throws. If a maneuver requires a saving throw, the DC equals 8 + your Strength or Dexterity modifier (your choice) + Proficiency Bonus."
        ),
        "Student of War": (
            "You gain proficiency with one type of Artisan's Tools of your choice, and you gain proficiency in one skill of your choice from the skills available to Fighters at level 1."
        ),
    },
    7: {
        "Know Your Enemy": (
            "As a Bonus Action, you can discern certain strengths and weaknesses of a creature you can see within 30 feet of yourself; you know whether that creature has any Immunities, Resistances, or Vulnerabilities, and if the creature has any, you know what they are.\n\n"
            "Once you use this feature, you can't do so again until you finish a Long Rest. You can also restore a use of the feature by expending one Superiority Die (no action required)."
        ),
    },
    10: {
        "Improved Combat Superiority": (
            "Your Superiority Die becomes a d10."
        ),
    },
    15: {
        "Relentless": (
            "Once per turn, when you use a maneuver, you can roll 1d8 and use the number rolled instead of expending a Superiority Die."
        ),
    },
    18: {
        "Ultimate Combat Superiority": (
            "Your Superiority Die becomes a d12."
        ),
    },
}

CHAMPION: Dict[Union[str, int], Any] = {
    "description": "Pursue Physical Excellence in Combat. Champions combine rigorous training with physical excellence to deal devastating blows, withstand peril, and garner glory.",
    3: {
        "Improved Critical": (
            "Your attack rolls with weapons and Unarmed Strikes can score a Critical Hit on a roll of 19 or 20 on the d20."
        ),
        "Remarkable Athlete": (
            "Thanks to your athleticism, you have Advantage on Initiative rolls and Strength (Athletics) checks.\n\n"
            "In addition, immediately after you score a Critical Hit, you can move up to half your Speed without provoking Opportunity Attacks."
        ),
    },
    7: {
        "Additional Fighting Style": (
            "You gain another Fighting Style feat of your choice."
        ),
    },
    10: {
        "Heroic Warrior": (
            "During combat, you can give yourself Heroic Inspiration whenever you start your turn without it."
        ),
    },
    15: {
        "Superior Critical": (
            "Your attack rolls with weapons and Unarmed Strikes can now score a Critical Hit on a roll of 18-20 on the d20."
        ),
    },
    18: {
        "Survivor": (
            "Defy Death. You have Advantage on Death Saving Throws. Moreover, when you roll 18-20 on a Death Saving Throw, you gain the benefit of rolling a 20 on it.\n\n"
            "Heroic Rally. At the start of each of your turns, you regain Hit Points equal to 5 plus your Constitution modifier if you are Bloodied and have at least 1 Hit Point."
        ),
    },
}

ELDRITCH_KNIGHT: Dict[Union[str, int], Any] = {
    "description": "Support Combat Skills with Arcane Magic. Eldritch Knights combine martial mastery with a careful study of magic.",
    3: {
        "Spellcasting": (
            "You have learned to cast spells. See chapter 7 for the rules on spellcasting. The information below details how you use those rules as an Eldritch Knight.\n\n"
            "Cantrips. You know two cantrips of your choice from the Wizard spell list. Ray of Frost and Shocking Grasp are recommended. Whenever you gain a Fighter level, you can replace one of these cantrips with another cantrip of your choice from the Wizard spell list.\n\n"
            "When you reach Fighter level 10, you learn another Wizard cantrip of your choice.\n\n"
            "Spell Slots. The Eldritch Knight Spellcasting table shows how many spell slots you have to cast your level 1+ spells. You regain all expended slots when you finish a Long Rest.\n\n"
            "Prepared Spells of Level 1+. You prepare the list of level 1+ spells that are available for you to cast with this feature. To start, choose three level 1 spells from the Wizard spell list. Burning Hands, Jump, and Shield are recommended.\n\n"
            "The number of spells on your list increases as you gain Fighter levels, as shown in the Prepared Spells column of the Eldritch Knight Spellcasting table. Whenever that number increases, choose additional spells from the Wizard spell list until the number of spells on your list matches the number on the table. The chosen spells must be of a level for which you have spell slots.\n\n"
            "Changing Your Prepared Spells. Whenever you gain a Fighter level, you can replace one spell on your list with another Wizard spell for which you have spell slots.\n\n"
            "Spellcasting Ability. Intelligence is your spellcasting ability for your Wizard spells.\n\n"
            "Spellcasting Focus. You can use an Arcane Focus as a Spellcasting Focus for your Wizard spells."
        ),
        "War Bond": (
            "You learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual over the course of 1 hour, which can be done during a Short Rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond. The bond fails if another Fighter is bonded to the weapon or if the weapon is a magic item to which someone else is attuned.\n\n"
            "Once you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you have the Incapacitated condition. If it is on the same plane of existence, you can summon that weapon as a Bonus Action, causing it to teleport instantly to your hand.\n\n"
            "You can have up to two bonded weapons, but you can summon only one at a time with a Bonus Action. If you attempt to bond with a third weapon, you must break the bond with one of the other two."
        ),
    },
    7: {
        "War Magic": (
            "When you take the Attack action on your turn, you can replace one of the attacks with a casting of one of your Wizard cantrips that has a casting time of an action."
        ),
    },
    10: {
        "Eldritch Strike": (
            "You learn how to make your weapon strikes undercut a creature's ability to withstand your spells. When you hit a creature with an attack using a weapon, that creature has Disadvantage on the next saving throw it makes against a spell you cast before the end of your next turn."
        ),
    },
    15: {
        "Arcane Charge": (
            "When you use your Action Surge, you can teleport up to 30 feet to an unoccupied space you can see. You can teleport before or after the additional action."
        ),
    },
    18: {
        "Improved War Magic": (
            "When you take the Attack action on your turn, you can replace two of the attacks with a casting of one of your level 1 or level 2 Wizard spells that has a casting time of an action."
        ),
    },
}

ELDRITCH_KNIGHT_SPELLCASTING: Dict[int, Dict[str, Union[int, str]]] = {
    3:  {"spells_prepared": 3, "1st": 2, "2nd": 0, "3rd": 0, "4th": 0},
    4:  {"spells_prepared": 4, "1st": 3, "2nd": 0, "3rd": 0, "4th": 0},
    5:  {"spells_prepared": 4, "1st": 3, "2nd": 0, "3rd": 0, "4th": 0},
    6:  {"spells_prepared": 4, "1st": 3, "2nd": 0, "3rd": 0, "4th": 0},
    7:  {"spells_prepared": 5, "1st": 4, "2nd": 2, "3rd": 0, "4th": 0},
    8:  {"spells_prepared": 6, "1st": 4, "2nd": 2, "3rd": 0, "4th": 0},
    9:  {"spells_prepared": 6, "1st": 4, "2nd": 2, "3rd": 0, "4th": 0},
    10: {"spells_prepared": 7, "1st": 4, "2nd": 3, "3rd": 0, "4th": 0},
    11: {"spells_prepared": 8, "1st": 4, "2nd": 3, "3rd": 0, "4th": 0},
    12: {"spells_prepared": 8, "1st": 4, "2nd": 3, "3rd": 0, "4th": 0},
    13: {"spells_prepared": 9, "1st": 4, "2nd": 3, "3rd": 2, "4th": 0},
    14: {"spells_prepared": 10, "1st": 4, "2nd": 3, "3rd": 2, "4th": 0},
    15: {"spells_prepared": 10, "1st": 4, "2nd": 3, "3rd": 2, "4th": 0},
    16: {"spells_prepared": 11, "1st": 4, "2nd": 3, "3rd": 3, "4th": 0},
    17: {"spells_prepared": 11, "1st": 4, "2nd": 3, "3rd": 3, "4th": 0},
    18: {"spells_prepared": 11, "1st": 4, "2nd": 3, "3rd": 3, "4th": 0},
    19: {"spells_prepared": 12, "1st": 4, "2nd": 3, "3rd": 3, "4th": 1},
    20: {"spells_prepared": 13, "1st": 4, "2nd": 3, "3rd": 3, "4th": 1},
}

PSI_WARRIOR: Dict[Union[str, int], Any] = {
    "description": "Augment Physical Might with Psionic Power. Psi Warriors awaken the power of their minds to augment their physical might.",
    3: {
        "Psionic Power": (
            "You harbor a wellspring of psionic energy within yourself. It is represented by your Psionic Energy Dice, which fuel powers you have from this subclass. The Psi Warrior Energy Dice table shows the die size and number of these dice you have when you reach certain Fighter levels.\n\n"
            "Psi Warrior Energy Dice\nFighter Level\tDie Size\tNumber\n3\tD6\t4\n5\tD8\t6\n9\tD8\t8\n11\tD10\t8\n13\tD10\t10\n17\tD12\t12\n\nAny features in this subclass that use a Psionic Energy Die use only the dice from this subclass. Some of your powers expend the Psionic Energy Die, as specified in a power's description, and you can't use a power if it requires you to use a die when all your Psionic Energy Dice are expended.\n\n"
            "You regain one of your expended Psionic Energy Dice when you finish a Short Rest, and you regain all of them when you finish a Long Rest.\n\n"
            "Protective Field. When you or another creature you can see within 30 feet of you takes damage, you can take a Reaction to expend one Psionic Energy Die, roll the die, and reduce the damage taken by the number rolled plus your Intelligence modifier (minimum reduction of 1), as you create a momentary shield of telekinetic force.\n\n"
            "Psionic Strike. You can propel your weapons with psionic force. Once on each of your turns, immediately after you hit a target within 30 feet of yourself with an attack and deal damage to it with a weapon, you can expend one Psionic Energy Die, rolling it and dealing Force damage to the target equal to the number rolled plus your Intelligence modifier.\n\n"
            "Telekinetic Movement. You can move an object or a creature with your mind. As a Magic action, choose one target you can see within 30 feet of yourself; the target must be a loose object that is Large or smaller or one willing creature other than you. You transport the target up to 30 feet to an unoccupied space you can see. Alternatively, if the target is a Tiny object, you can transport it to or from your hand.\n\n"
            "Once you take this action, you can't do so again until you finish a Short or Long Rest unless you expend a Psionic Energy Die (no action required) to restore your use of it."
        ),
    },
    7: {
        "Telekinetic Adept": (
            "Psi-Powered Leap. As a Bonus Action, you gain a Fly Speed equal to twice your Speed until the end of the current turn. Once you take this Bonus Action, you can't do so again until you finish a Short or Long Rest unless you expend a Psionic Energy Die (no action required) to restore your use of it.\n\n"
            "Telekinetic Thrust. When you deal damage to a target with your Psionic Strike, you can force the target to make a Strength saving throw (DC 8 plus your Intelligence modifier and Proficiency Bonus). On a failed save, you can give the target the Prone condition or transport it up to 10 feet horizontally."
        ),
    },
    10: {
        "Guarded Mind": (
            "You have Resistance to Psychic damage. Moreover, if you start your turn with the Charmed or Frightened condition, you can expend a Psionic Energy Die (no action required) and end every effect on yourself giving you those conditions."
        ),
    },
    15: {
        "Bulwark of Force": (
            "You can shield yourself and others with telekinetic force. As a Bonus Action, you can choose creatures, including yourself, within 30 feet of yourself, up to a number of creatures equal to your Intelligence modifier (minimum of one creature). Each of the chosen creatures has Half Cover for 1 minute or until you have the Incapacitated condition.\n\n"
            "Once you use this feature, you can't do so again until you finish a Long Rest unless you expend a Psionic Energy Die (no action required) to restore your use of it."
        ),
    },
    18: {
        "Telekinetic Master": (
            "You always have the telekinesis spell prepared. With this feature, you can cast it without a spell slot or components, and your spellcasting ability for it is Intelligence. On each of your turns while you maintain Concentration on it, including the turn when you cast it, you can make one attack with a weapon as a Bonus Action.\n\n"
            "Once you cast the spell with this feature, you can't do so in this way again until you finish a Long Rest unless you expend a Psionic Energy Die (no action required) to restore your use of it."
        ),
    },
}
