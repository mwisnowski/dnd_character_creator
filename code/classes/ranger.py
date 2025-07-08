"""
Ranger class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

RANGER_CLASS: Dict[str, Any] = {
    'name': 'Ranger',
    'hit_die': 10,
    'primary_ability': ['Dexterity', 'Wisdom'],
    'saving_throws': ['Strength', 'Dexterity'],
    'proficiencies': {
        'armor': ['Light Armor', 'Medium Armor', 'Shields'],
        'weapons': ['Simple Weapons', 'Martial Weapons'],
        'tools': [],
        'skills': [
            'Animal Handling', 'Athletics', 'Insight', 'Investigation',
            'Nature', 'Perception', 'Stealth', 'Survival'
        ]
    },
    'starting_equipment': [
        [
            'Studded Leather Armor', 'Scimitar', 'Shortsword', 'Longbow',
            '20 Arrows', 'Quiver', 'Druidic Focus (sprig of mistletoe)',
            
            "Explorer's Pack", '7 GP'
        ],
        ['150 GP']
    ]
}

RANGER_LEVELS: Dict[int, Dict[str, Any]] = {
    1: {
        'proficiency_bonus': 2,
        'features': ['Spellcasting', 'Favored Enemy', 'Weapon Mastery'],
        'spellcasting': {
            'favored_enemy': 2,
            'prepared_spells': 2,
            'spells_known': 2,
            'spell_slots': {'Level 1': 2}
        }
    },
    2: {
        'proficiency_bonus': 2,
        'features': ['Deft Explorer', 'Fighting Style'],
        'spellcasting': {
            'favored_enemy': 2,
            'prepared_spells': 3,
            'spells_known': 3,
            'spell_slots': {'Level 1': 2}
        }
    },
    3: {
        'proficiency_bonus': 2,
        'features': ['Ranger Subclass'],
        'spellcasting': {
            'favored_enemy': 2,
            'prepared_spells': 4,
            'spells_known': 4,
            'spell_slots': {'Level 1': 3}
        }
    },
    4: {
        'proficiency_bonus': 2,
        'features': ['Ability Score Improvement'],
        'spellcasting': {
            'favored_enemy': 2,
            'prepared_spells': 5,
            'spells_known': 5,
            'spell_slots': {'Level 1': 3}
        }
    },
    5: {
        'proficiency_bonus': 3,
        'features': ['Extra Attack'],
        'spellcasting': {
            'favored_enemy': 3,
            'prepared_spells': 6,
            'spells_known': 6,
            'spell_slots': {'Level 1': 4, 'Level 2': 2}
        }
    },
    6: {
        'proficiency_bonus': 3,
        'features': ['Roving'],
        'spellcasting': {
            'favored_enemy': 3,
            'prepared_spells': 6,
            'spells_known': 6,
            'spell_slots': {'Level 1': 4, 'Level 2': 2}
        }
    },
    7: {
        'proficiency_bonus': 3,
        'features': ['Subclass Feature'],
        'spellcasting': {
            'favored_enemy': 3,
            'prepared_spells': 7,
            'spells_known': 7,
            'spell_slots': {'Level 1': 4, 'Level 2': 3}
        }
    },
    8: {
        'proficiency_bonus': 3,
        'features': ['Ability Score Improvement'],
        'spellcasting': {
            'favored_enemy': 3,
            'prepared_spells': 7,
            'spells_known': 7,
            'spell_slots': {'Level 1': 4, 'Level 2': 3}
        }
    },
    9: {
        'proficiency_bonus': 4,
        'features': ['Expertise'],
        'spellcasting': {
            'favored_enemy': 4,
            'prepared_spells': 9,
            'spells_known': 9,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 2}
        }
    },
    10: {
        'proficiency_bonus': 4,
        'features': ['Tireless'],
        'spellcasting': {
            'favored_enemy': 4,
            'prepared_spells': 9,
            'spells_known': 9,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 2}
        }
    },
    11: {
        'proficiency_bonus': 4,
        'features': ['Subclass Feature'],
        'spellcasting': {
            'favored_enemy': 4,
            'prepared_spells': 10,
            'spells_known': 10,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3}
        }
    },
    12: {
        'proficiency_bonus': 4,
        'features': ['Ability Score Improvement'],
        'spellcasting': {
            'favored_enemy': 4,
            'prepared_spells': 10,
            'spells_known': 10,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3}
        }
    },
    13: {
        'proficiency_bonus': 5,
        'features': ['Relentless Hunter'],
        'spellcasting': {
            'favored_enemy': 5,
            'prepared_spells': 11,
            'spells_known': 11,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 1}
        }
    },
    14: {
        'proficiency_bonus': 5,
        'features': ["Nature's Veil"],
        'spellcasting': {
            'favored_enemy': 5,
            'prepared_spells': 11,
            'spells_known': 11,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 1}
        }
    },
    15: {
        'proficiency_bonus': 5,
        'features': ['Subclass Feature'],
        'spellcasting': {
            'favored_enemy': 5,
            'prepared_spells': 12,
            'spells_known': 12,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 2}
        }
    },
    16: {
        'proficiency_bonus': 5,
        'features': ['Ability Score Improvement'],
        'spellcasting': {
            'favored_enemy': 5,
            'prepared_spells': 12,
            'spells_known': 12,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 2}
        }
    },
    17: {
        'proficiency_bonus': 6,
        'features': ['Precise Hunter'],
        'spellcasting': {
            'favored_enemy': 6,
            'prepared_spells': 14,
            'spells_known': 14,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 1}
        }
    },
    18: {
        'proficiency_bonus': 6,
        'features': ['Feral Senses'],
        'spellcasting': {
            'favored_enemy': 6,
            'prepared_spells': 14,
            'spells_known': 14,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 1}
        }
    },
    19: {
        'proficiency_bonus': 6,
        'features': ['Epic Boon'],
        'spellcasting': {
            'favored_enemy': 6,
            'prepared_spells': 15,
            'spells_known': 15,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2}
        }
    },
    20: {
        'proficiency_bonus': 6,
        'features': ['Foe Slayer'],
        'spellcasting': {
            'favored_enemy': 6,
            'prepared_spells': 15,
            'spells_known': 15,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2}
        }
    }
}

RANGER_FEATURES: Dict[str, Any] = {
    'Spellcasting': (
        "You have learned to channel the magical essence of nature to cast spells. See Chapter 7 for the rules on Spellcasting. The Information below details how you use those rules with Ranger spells, which appear in the Ranger spell list later in the class's description.\n\n"
        "  - Spell Slots. The Ranger Features table shows how many spell slots you have to cast your level 1+ spells. You regain all expended slots when you finish a Long Rest.\n\n"
        "  - Prepared Spells of Level 1+. You prepare the list of level 1+ spells that are available for you to cast with this feature. To start, choose two level 1 Ranger spells Cure Wounds and Ensnaring Strike are recommended.\n\n"
        "The number of spells on your list increases as you gain Ranger levels, as shown in the Prepared Spells column of the Ranger Features table. Whenever that number increases, choose additional spells from the Ranger spell list until the number of spells on your list matches the number on the table. The chosen spells must be of a level for which you have spell slots. For example, if you're a level 5 Ranger, your list of prepared spells can include six spells of levels 1 and 2 in any combination.\n\n"
        "If another Ranger feature gives you spells that you always have prepared, those spells don’t count against the number of spells you can prepare with this feature, but those spells otherwise count as Ranger spells for you.\n\n"
        "  - Changing Your Prepared Spells. Whenever you finish a Long Rest, you can replace one spell on your list with another Ranger spell for which you have spell slots.\n\n"
        "  - Spellcasting Ability. Wisdom is your spellcasting ability for your Ranger spells.\n\n"
        "  - Spellcasting Focus. You can use a Druidic Focus as a Spellcasting Focus for your Ranger spells."
    ),
    'Favored Enemy': (
        "You always have the Hunter's Mark spell prepared.\n"
        "You can cast it twice without expending a spell slot, and you regain all expended uses of this ability when you finish a Long Rest.\n\n"
        "The number of times you can cast the spell without a spell slot increases when you reach certain Ranger Levels, as shown in the Favored Enemy column of the Ranger Features table."
    ),
    'Weapon Mastery': (
        "Your training with weapons allows you to use the mastery properties of two kinds of weapons of your choice with which you have proficiency, such as Longbows and Shortswords.\n\n"
        "Whenever you finish a Long Rest, you can change the kinds of weapons you chose. For Example, you could switch to using the mastery properties of Scimitars and Longswords."
    ),
    'Deft Explorer': (
        "Thanks to your travels, you gain the following benefits.\n\n"
        "  - Expertise.: Choose one of your skill proficiencies with which you lack Expertise. You gain Expertise in that skill.\n\n"
        "  - Languages.: You know two languages of your choice from the language tables in chapter 2."
    ),
    'Fighting Style': (
        "You gain a Fighting Style feat of your choice (see chapter 5). Instead of choosing one of those feats, you can choose the option below.\n\n"
        "  - Druidic Warrior. You learn two Druid cantrips of your choice (See the Druid class's section for a list of Druid spells). Guidance and Starry Wisp are recommended. The chosen cantrips count as Ranger spells for you, and Wisdom is your spellcasting ability for them. Whenever you gain a Ranger level, you can replace one of these cantrips with another Druid cantrip."
    ),
    'Ranger Subclass': (
        "You gain a Ranger Subclass of your choice. The Beast Master, Fey Wanderer, Gloom Stalker and Hunter subclasses are detailed after this class's description. A Subclass is a specialization that grants you features at certain Ranger levels. For the rest of your career, you gain each of your subclass’s features that are of your Ranger level or lower.\n\n"
        "Ranger Subclasses\nName\nBeast Master\nFey Wanderer\nGloom Stalker\nHunter"
    ),
    'Ability Score Improvement': (
        "You gain the Ability Score Improvement feat or another feat of your choice for which you qualify. You gain this feature again at Ranger levels 8, 12, and 16."
    ),
    'Extra Attack': (
        "You can attack twice instead of once whenever you take the Attack action on your turn."
    ),
    'Roving': (
        "Your speed increases by 10 feet while you aren't wearing Heavy Armor. You also have a Climb speed and a Swim Speed equal to your Speed."
    ),
    'Expertise': (
        "Choose two of your skill proficiencies with which you lack Expertise. You gain Expertise in those skills."
    ),
    'Tireless': (
        "Primal forces now help fuel you on your journeys, granting you the following benefits.\n\n"
        "  - Temporary Hit Points. As a Magic Action, you can give yourself a number of Temporary Hit Points equal to 1d8 plus your Wisdom modifier (minimum of 1). You can use this action a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.\n\n"
        "  - Decrease Exhaustion. Whenever you finish a Short Rest, your Exhaustion level, if any, decreases by 1."
    ),
    'Relentless Hunter': (
        "Taking damage can't break your Concentration on Hunter's Mark."
    ),
    "Nature's Veil": (
        "You invoke spirits of nature to magically hide yourself. As a Bonus Action you can give yourself the Invisible condition until the end of your next turn.\n\n"
        "You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."
    ),
    'Precise Hunter': (
        "You have Advantage on attack rolls against the creature currently marked by your Hunter's Mark."
    ),
    'Feral Senses': (
        "Your connection to the forces of nature grants you Blindsight with a range of 30 feet."
    ),
    'Epic Boon': (
        "You gain an Epic Boon feat or another feat of your choice for which you qualify. Boon of Dimensional Travel is recommended."
    ),
    'Foe Slayer': (
        "The damage die of your Hunter's Mark is a d10 rather than a d6."
    ),
}

BEAST_OF_THE_LAND: Dict[str, Any] = {
    'name': 'Beast of the Land',
    'size': 'Medium',
    'type': 'Beast',
    'alignment': 'Neutral',
    'armor_class': '13 + Wisdom modifier',
    'hit_points': '5 + (5 * Ranger Level)',
    'hit_dice': 'Ranger Level (d8)',
    'speed': {'walk': 40, 'climb': 40},
    'stats': {
        'STR': {'score': 14, 'mod': 2, 'save': 2},
        'DEX': {'score': 14, 'mod': 2, 'save': 2},
        'CON': {'score': 15, 'mod': 2, 'save': 2},
        'INT': {'score': 8, 'mod': -1, 'save': -1},
        'WIS': {'score': 14, 'mod': 2, 'save': 2},
        'CHA': {'score': 11, 'mod': 0, 'save': 0},
    },
    'senses': {'darkvision': 60, 'passive_perception': 12},
    'languages': 'Understands the languages that you know',
    'challenge_rating': None,
    'proficiency_bonus': 'Equals your Proficiency Bonus',
    'traits': [
        'Primal Bond: Add your Proficiency Bonus to any ability check or saving throw the beast makes.'
    ],
    'actions': [
        {
            'name': "Beast's Strike",
            'type': 'Melee Weapon Attack',
            'attack_bonus': 'Equals your spell attack modifier',
            'reach': 5,
            'hit': '1d8 + 2 + Wisdom modifier bludgeoning, piercing, or slashing damage (your choice when you summon the beast).',
            'special': 'If the beast moved at least 20 feet straight toward the target before the hit, the target takes an extra 1d6 damage of the same type, and the target has the Prone condition if it is a Large or smaller creature.'
        }
    ]
}

BEAST_OF_THE_SKY: Dict[str, Any] = {
    'name': 'Beast of the Sky',
    'size': 'Small',
    'type': 'Beast',
    'alignment': 'Neutral',
    'armor_class': '13 + Wisdom modifier',
    'hit_points': '4 + (4 * Ranger Level)',
    'hit_dice': 'Ranger Level (d6)',
    'speed': {'walk': 10, 'fly': 60},
    'stats': {
        'STR': {'score': 6, 'mod': -2, 'save': -2},
        'DEX': {'score': 16, 'mod': 3, 'save': 3},
        'CON': {'score': 13, 'mod': 1, 'save': 1},
        'INT': {'score': 8, 'mod': -1, 'save': -1},
        'WIS': {'score': 14, 'mod': 2, 'save': 2},
        'CHA': {'score': 11, 'mod': 0, 'save': 0},
    },
    'senses': {'darkvision': 60, 'passive_perception': 12},
    'languages': 'Understands the languages that you know',
    'challenge_rating': None,
    'proficiency_bonus': 'Equals your Proficiency Bonus',
    'traits': [
        "Flyby: The beast doesn't provoke Opportunity Attacks when it flies out of an enemy's reach.",
        'Primal Bond: Add your Proficiency Bonus to any ability check or saving throw the beast makes.'
    ],
    'actions': [
        {
            'name': "Beast's Strike",
            'type': 'Melee Weapon Attack',
            'attack_bonus': 'Equals your spell attack modifier',
            'reach': 5,
            'hit': '1d4 + 3 + Wisdom modifier slashing damage.'
        }
    ]
}

BEAST_OF_THE_SEA: Dict[str, Any] = {
    'name': 'Beast of the Sea',
    'size': 'Medium',
    'type': 'Beast',
    'alignment': 'Neutral',
    'armor_class': '13 + Wisdom modifier',
    'hit_points': '5 + (5 * Ranger Level)',
    'hit_dice': 'Ranger Level (d8)',
    'speed': {'walk': 5, 'swim': 60},
    'stats': {
        'STR': {'score': 14, 'mod': 2, 'save': 2},
        'DEX': {'score': 14, 'mod': 2, 'save': 2},
        'CON': {'score': 15, 'mod': 2, 'save': 2},
        'INT': {'score': 8, 'mod': -1, 'save': -1},
        'WIS': {'score': 14, 'mod': 2, 'save': 2},
        'CHA': {'score': 11, 'mod': 0, 'save': 0},
    },
    'senses': {'darkvision': 90, 'passive_perception': 12},
    'languages': 'Understands the languages that you know',
    'challenge_rating': None,
    'proficiency_bonus': 'Equals your Proficiency Bonus',
    'traits': [
        'Amphibious: The beast can breathe air and water.',
        'Primal Bond: Add your Proficiency Bonus to any ability check or saving throw the beast makes.'
    ],
    'actions': [
        {
            'name': "Beast's Strike",
            'type': 'Melee Weapon Attack',
            'attack_bonus': 'Equals your spell attack modifier',
            'reach': 5,
            'hit': '1d6 + 2 + Wisdom modifier bludgeoning or piercing damage (your choice when you summon the beast).',
            'special': 'The target has the Grappled condition (escape DC equals your spell save DC).'
        }
    ]
}

BEAST_MASTER: Dict[Union[str, int], Any] = {
    'description': (
        "Bond with a Primal Beast\n\n"
        "A Beast Master forms a mystical bond with a special animal, drawing on primal magic and a deep connection to the natural world."
    ),
    3: {
        'Primal Companion': [
            "You magically summon a primal beast, which draws strength from your bond with nature. Choose its stat block: Beast of the Land, Beast of the Sea or Beast of the Sky. You also determine the kind of animal it is, choosing a kind appropriate for the stat block. Whatever beast you choose, it bears primal markings indicating its supernatural origin.\n\n"
            "  - The Beast in Combat. In combat, the beast acts during your turn. It can move and use its Reaction on its own, but the only action it takes is the Dodge action unless you take a Bonus Action to command it to take an action in its stat block or some other action. You can also sacrifice one of your attacks when you take the Attack action to command the beast to take the Beast's Strike action. If you have the Incapacitated condition, the beast acts on its own and isn't limited to the Dodge action.\n\n"
            "  - Restoring or Replacing the Beast. If the beast has died within the last hour, you can take a Magic action to touch it and expend a spell slot. The beast returns to life after 1 minute with all its Hit Points restored.\n\n"
            "Whenever you finish a Long Rest, you can summon a different primal beast, which appears in an unoccupied space within 5 feet of you. You choose its stat block and appearance. If you already have a beast from this feature, the old one vanishes when the new one appears.",
            BEAST_OF_THE_LAND,
            BEAST_OF_THE_SEA,
            BEAST_OF_THE_SKY
            ]
        },
    7: {
        'Exceptional Training': (
            "When you take a Bonus Action to command your Primal Companion beast to take an action, you can also command it to take the Dash, Disengage, Dodge, or Help action using its Bonus Action.\n\n"
            "In addition, whenever it hits with an attack roll and deals damage, it can deal your choice of Force damage or its normal damage type."
        )
    },
    11: {
        'Bestial Fury': (
            "When you command your Primal Companion beast to take the Beast's Strike action, the beast can use it twice.\n\n"
            "In addition, the first time each turn it hits a creature under the effect of your Hunter's Mark spell, the beast deals extra Force damage equal to the bonus damage of that spell."
        )
    },
    15: {
        'Share Spells': (
            "When you cast a spell targeting yourself, you can also affect your Primal Companion beast with the spell if the beast is within 30 feet of you."
        )
    }
}

FEYWILD_GIFTS: Dict[int, str] = {
    1: "Illusory butterflies flutter around you while you take a Short or Long Rest.",
    2: "Flowers bloom from your hair each dawn.",
    3: "You faintly smell of cinnamon, lavender, nutmeg, or another comforting herb or spice.",
    4: "Your shadow dances while no one is looking directly at it.",
    5: "Horns or antlers sprout from your head.",
    6: "Your skin and hair change color each dawn."
}

FEY_WANDERER: Dict[Union[str, int], Any] = {
    'description': (
        "Wield Fey Mirth and Fury\n\n"
        "A fey mystique surrounds you, thanks to the boon of an archfey or a location in the Feywild that transformed you. However you gained fey magic, you are now a Fey Wanderer. Your joyful laughter brightens the hearts of the downtrodden, and your martial prowess strikes terror in your foes, for great is the mirth of the fey and dreadful is their fury."
    ),
    3: {
        'Dreadful Strikes': (
            "You can augment your weapon strikes with mind-scarring magic drawn from the murky hollows of the Feywild. When you hit a creature with a weapon, you can deal an extra 1d4 Psychic damage to the target, which can take this extra damage only once per turn. The extra damage increases to 1d6 when you reach Ranger level 11."
        ),
        'Fey Wanderer Spells': (
            "When you reach a Ranger level specified in the Fey Wanderer spells table, you thereafter always have the listed spells prepared.\n\n"
            "Fey Wanderer Spells\nRanger Level  Spell\n3  Charm Person\n5  Misty Step\n9  Summon Fey\n13 Dimension Door\n17 Mislead"
        ),
        'Feywild Gift': [
            "You also possess a fey blessing. Choose it from the Feywild Gifts table or determine it randomly.",
            FEYWILD_GIFTS
        ],
        'Otherworldly Glamour': (
            "Whenever you make a Charisma check, you gain a bonus to the check equal to your Wisdom modifier (Minimum of +1).\n\n"
            "You also gain proficiency in one of these skills of your choice: Deception, Performance, or Persuasion."
        )
    },
    7: {
        'Beguiling Twist': (
            "The magic of the Feywild guards your mind. You have advantage on saving throws to avoid or end the Charmed or Frightened condition.\n\n"
            "In addition, whenever you or a creature you can see within 120 feet of you succeeds on a saving throw to avoid or end the Charmed or Frightened condition, you can take a Reaction to force a different creature you can see within 120 feet of yourself to make a Wisdom save against your spell save DC. On a failed save, the target is charmed or frightened (your choice) for 1 minute. The target repeats the save at the end of each of its turns, ending the effect on itself on a success."
        )
    },
    11: {
        'Fey Reinforcements': (
            "You can cast Summon Fey without a Material component. You can also cast it once without a spell slot, and you regain the ability to cast it in this way when you finish a Long Rest.\n\n"
            "Whenever you start casting the spell, you can modify it so that it doesn't require Concentration. If you do so, the spell's duration becomes 1 minute for the casting."
        )
    },
    15: {
        'Misty Wanderer': (
            "You can cast Misty Step without expending a spell slot. You can do so a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.\n\n"
            "In addition, whenever you cast Misty Step, you can bring along one willing creature you can see within 5 feet of yourself. That creature teleports to an unoccupied space of your choice within 5 feet of your destination space."
        )
    }
}

GLOOM_STALKER: Dict[Union[str, int], Any] = {
    'description': (
        "Draw on Shadow Magic to Fight Your Foes\n\n"
        "Gloom Stalkers are at home in the darkest places, wielding magic drawn from the Shadowfell to combat enemies that lurk in darkness."
    ),
    3: {
        'Dread Ambusher': (
            "You have mastered the art of creating fearsome ambushes, granting you the following benefits.\n\n"
            "Ambusher's Leap. At the start of your first turn of each combat, your speed increases by 10 feet until the end of that turn.\n\n"
            "Dreadful Strike. When you attack a creature and hit it with a weapon, you can deal an extra 2d6 Psychic damage. You can use this benefit only once per turn, you can use it a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.\n\n"
            "Initiative Bonus. When you roll Initiative, you can add your Wisdom modifier to the roll."
        ),
        'Gloom Stalker Spells': (
            "When you reach a Ranger level specified in the Gloom Stalker spells table, you thereafter always have the listed spells prepared.\n\n"
            "Gloom Stalker Spells\nRanger Level  Spells\n3  Disguise Self\n5  Rope Trick\n9  Fear\n13 Greater Invisibility\n17 Seeming"
        ),
        'Umbral Sight': (
            "You gain Darkvision with a range of 60 feet. If you already have Darkvision when you gain this feature, its range increases by 60 feet.\n\n"
            "You are also adept at evading creatures that rely on Darkvision. While entirely in Darkness, you have the Invisible condition to any creature that relies on Darkvision to see you in that Darkness."
        )
    },
    7: {
        'Iron Mind': (
            "You have honed your ability to resist mind-altering powers. You gain proficiency in Wisdom saving throws. If you already have this proficiency, you instead gain proficiency in Intelligence or Charisma saving throws (your choice)."
        )
    },
    11: {
        "Stalker's Flurry": (
            "The Psychic damage of your Dreadful Strike becomes 2d8. In addition, when you use the Dreadful Strike effect of your Dread Ambusher feature, you can use one of the following additional effects.\n\n"
            "Sudden Strike. You can make another attack with the same weapon against a different creature that is within 5 feet of the original target and that is within the weapon's range.\n\n"
            "Mass Fear. The target and each creature within 10 feet of it must make a wisdom saving throw against your spell save DC. On a failed save, a creature has the Frightened condition until the start of your next turn."
        )
    },
    15: {
        'Shadowy Dodge': (
            "When a creature makes an attack roll against you, you can take a Reaction to impose Disadvantage on that roll. Whether the attack hits or misses, you can teleport up to 30 feet to an unoccupied space that you can see."
        )
    }
}

HUNTER: Dict[Union[str, int], Any] = {
    'description': (
        "Protect Nature and People from Destruction\n\n"
        "You stalk prey in the wilds and elsewhere, using your abilities as a Hunter to protect nature and people everywhere from forces that would destroy them."
    ),
    3: {
        "Hunter's Lore": (
            "You can call upon the forces of nature to reveal certain strengths and weaknesses of your prey. While a creature is marked by your Hunter's Mark, you know whether the creature has any Immunities, Resistances, or Vulnerabilities, and if the creature has any, you know what they are."
        ),
        "Hunter's Prey": (
            "You gain one of the following feature options of your choice. Whenever you finish a Short or Long Rest, you can replace the chosen option with the other one.\n\n"
            "Colossus Slayer. Your tenacity can wear down even the most resilient foes. When you hit a creature with a weapon, the weapon deals an extra 1d8 damage to the target if it's missing any of its Hit Points. You can deal this extra damage only once per turn.\n\n"
            "Horde Breaker. Once on each of your turns when you make an attack with a weapon, you can make another attack with the same weapon against a different creature that is within 5 feet of the original target, that is within the weapon's range, and that you haven't attacked this turn."
        )
    },
    7: {
        "Defensive Tactics": (
            "You gain one of the following feature options of your choice. Whenever you finish a Short or Long Rest, you can replace the chosen option with the other one.\n\n"
            "Escape the Horde. Opportunity Attacks have Disadvantage against you.\n\n"
            "Multiattack Defense. When a creature hits you with an attack roll, that creature has Disadvantage on all other attack rolls against you this turn."
        )
    },
    11: {
        "Superior Hunter's Prey": (
            "Once per turn when you deal damage to a creature marked by your Hunter's Mark, you can also deal that spell's extra damage to a different creature that you can see within 30 feet of the first creature."
        )
    },
    15: {
        "Superior Hunter's Defense": (
            "When you take damage, you can take a Reaction to give yourself Resistance to that damage and any other damage of the same type until the end of the current turn."
        )
    }
}
