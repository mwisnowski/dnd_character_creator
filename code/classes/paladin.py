"""
Paladin class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

PALADIN_CLASS: Dict[str, Any] = {
    'name': 'Paladin',
    'hit_die': 10,
    'primary_ability': ['Strength', 'Charisma'],
    'saving_throws': ['Wisdom', 'Charisma'],
    'proficiencies': {
        'armor': ['Light Armor', 'Medium Armor', 'Heavy Armor', 'Shields'],
        'weapons': ['Simple Weapons', 'Martial Weapons'],
        'tools': [],
        'skills': [
            'Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion'
        ]
    },
    'starting_equipment': [
        [
            'Chain Mail', 'Shield', 'Longsword', '6 Javelins', 'Holy Symbol', \
            "Priest's Pack", '9 GP'
        ],
        ['150 GP']
    ]
}
PALADIN_LEVELS: Dict[int, Dict[str, Any]] = {
    1: {
        'proficiency_bonus': 2,
        'features': ['Lay On Hands', 'Spellcasting', 'Weapon Mastery'],
        'channel_divinity': None,
        'spellcasting': {
            'prepared_spells': 2,
            'spells_known': 2,
            'spell_slots': {'Level 1': 2}
        }
    },
    2: {
        'proficiency_bonus': 2,
        'features': ["Fighting Style", "Paladin's Smite"],
        'channel_divinity': None,
        'spellcasting': {
            'prepared_spells': 3,
            'spells_known': 3,
            'spell_slots': {'Level 1': 2}
        }
    },
    3: {
        'proficiency_bonus': 2,
        'features': ['Channel Divinity', 'Paladin Subclass'],
        'channel_divinity': 2,
        'spellcasting': {
            'prepared_spells': 4,
            'spells_known': 4,
            'spell_slots': {'Level 1': 3}
        }
    },
    4: {
        'proficiency_bonus': 2,
        'features': ['Ability Score Improvement'],
        'channel_divinity': 2,
        'spellcasting': {
            'prepared_spells': 5,
            'spells_known': 5,
            'spell_slots': {'Level 1': 3}
        }
    },
    5: {
        'proficiency_bonus': 3,
        'features': ['Extra Attack', 'Faithful Steed'],
        'channel_divinity': 2,
        'spellcasting': {
            'prepared_spells': 6,
            'spells_known': 6,
            'spell_slots': {'Level 1': 4, 'Level 2': 2}
        }
    },
    6: {
        'proficiency_bonus': 3,
        'features': ['Aura of Protection'],
        'channel_divinity': 2,
        'spellcasting': {
            'prepared_spells': 6,
            'spells_known': 6,
            'spell_slots': {'Level 1': 4, 'Level 2': 2}
        }
    },
    7: {
        'proficiency_bonus': 3,
        'features': ['Subclass Feature'],
        'channel_divinity': 2,
        'spellcasting': {
            'prepared_spells': 7,
            'spells_known': 7,
            'spell_slots': {'Level 1': 4, 'Level 2': 3}
        }
    },
    8: {
        'proficiency_bonus': 3,
        'features': ['Ability Score Improvement'],
        'channel_divinity': 2,
        'spellcasting': {
            'prepared_spells': 7,
            'spells_known': 7,
            'spell_slots': {'Level 1': 4, 'Level 2': 3}
        }
    },
    9: {
        'proficiency_bonus': 4,
        'features': ['Abjure Foes'],
        'channel_divinity': 2,
        'spellcasting': {
            'prepared_spells': 9,
            'spells_known': 9,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 2}
        }
    },
    10: {
        'proficiency_bonus': 4,
        'features': ['Aura of Courage'],
        'channel_divinity': 2,
        'spellcasting': {
            'prepared_spells': 9,
            'spells_known': 9,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 2}
        }
    },
    11: {
        'proficiency_bonus': 4,
        'features': ['Radiant Strikes'],
        'channel_divinity': 3,
        'spellcasting': {
            'prepared_spells': 10,
            'spells_known': 10,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3}
        }
    },
    12: {
        'proficiency_bonus': 4,
        'features': ['Ability Score Improvement'],
        'channel_divinity': 3,
        'spellcasting': {
            'prepared_spells': 10,
            'spells_known': 10,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3}
        }
    },
    13: {
        'proficiency_bonus': 5,
        'features': [],
        'channel_divinity': 3,
        'spellcasting': {
            'prepared_spells': 11,
            'spells_known': 11,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 1}
        }
    },
    14: {
        'proficiency_bonus': 5,
        'features': ['Restoring Touch'],
        'channel_divinity': 3,
        'spellcasting': {
            'prepared_spells': 11,
            'spells_known': 11,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 1}
        }
    },
    15: {
        'proficiency_bonus': 5,
        'features': ['Subclass Feature'],
        'channel_divinity': 3,
        'spellcasting': {
            'prepared_spells': 12,
            'spells_known': 12,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 2}
        }
    },
    16: {
        'proficiency_bonus': 5,
        'features': ['Ability Score Improvement'],
        'channel_divinity': 3,
        'spellcasting': {
            'prepared_spells': 12,
            'spells_known': 12,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 2}
        }
    },
    17: {
        'proficiency_bonus': 6,
        'features': [],
        'channel_divinity': 3,
        'spellcasting': {
            'prepared_spells': 14,
            'spells_known': 14,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 1}
        }
    },
    18: {
        'proficiency_bonus': 6,
        'features': ['Aura Expansion'],
        'channel_divinity': 3,
        'spellcasting': {
            'prepared_spells': 14,
            'spells_known': 14,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 1}
        }
    },
    19: {
        'proficiency_bonus': 6,
        'features': ['Epic Boon'],
        'channel_divinity': 3,
        'spellcasting': {
            'prepared_spells': 15,
            'spells_known': 15,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2}
        }
    },
    20: {
        'proficiency_bonus': 6,
        'features': ['Subclass Feature'],
        'channel_divinity': 3,
        'spellcasting': {
            'prepared_spells': 15,
            'spells_known': 15,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2}
        }
    }
}
PALADIN_FEATURES: Dict[str, Any] = {
    'Lay On Hands': (
        "Your blessed touch can heal wounds. You have a pool of healing power that replenishes when you finish a Long Rest. With that pool, you can restore a total number of Hit Points equal to five times your Paladin level.\n\n"
        "As a Bonus Action, you can touch a creature (which could be yourself) and draw power from the pool of healing to restore a number of Hit Points to that creature, up to the maximum amount remaining in the pool.\n\n"
        "You can also expend 5 Hit Points from the pool of healing power to remove the Poisoned condition from the creature; those points don't also restore Hit Points to the creature."
    ),
    'Spellcasting': (
        "You have learned to cast spells through prayer and meditation. See Chapter 7 for the rules on Spellcasting. The Information below details how you use those rules with Paladin spells, which appear in the Paladin spell list later in the class's description.\n\n"
        "  - Spell Slots. The Paladin Features table shows how many spell slots you have to cast your level 1+ spells. You regain all expended slots when you finish a Long Rest.\n\n"
        "  - Prepared Spells of Level 1+. You prepare the list of level 1+ spells that are available for you to cast with this feature. To start, choose two level 1 Paladin spells Heroism and Searing Smite are recommended.\n\n"
        "    The number of spells on your list increases as you gain Paladin levels, as shown in the Prepared Spells column of the Paladin Features table. Whenever that number increases, choose additional spells from the Paladin spell list until the number of spells on your list matches the number on the table. The chosen spells must be of a level for which you have spell slots. For example, if you're a level 5 Paladin, your list of prepared spells can include six spells of levels 1 and 2 in any combination.\n\n"
        "    If another Paladin feature gives you spells that you always have prepared, those spells don’t count against the number of spells you can prepare with this feature, but those spells otherwise count as Paladin spells for you.\n\n"
        "  - Changing Your Prepared Spells. Whenever you finish a Long Rest, you can replace one spell on your list with another Paladin spell for which you have spell slots.\n\n"
        "  - Spellcasting Ability. Charisma is your spellcasting ability for your Paladin spells.\n\n"
        "  - Spellcasting Focus. You can use a Holy Symbol as a Spellcasting Focus for your Paladin spells."
    ),
    'Weapon Mastery': (
        "Your training with weapons allows you to use the mastery properties of two kinds of weapons of your choice with which you have proficiency, such as Longswords and Javelins.\n\n"
        "Whenever you finish a Long Rest, you can change the kinds of weapons you chose. For Example, you could switch to using the mastery properties of Halberds and Flails."
    ),
    'Fighting Style': (
        "You gain a Fighting Style feat of your choice (see chapter 5). Instead of choosing one of those feats, you can choose the option below.\n\n"
        "  - Blessed Warrior. You learn two Cleric cantrips of your choice (See the Cleric class's section for a list of Cleric spells). Guidance and Sacred Flame are recommended. The chosen cantrips count as Paladin spells for you, and Charisma is your spellcasting ability for them. Whenever you gain a Paladin level, you can replace one of these cantrips with another Cleric cantrip."
    ),
    "Paladin's Smite": (
        "You always have the Divine Smite spell prepared.\nYou can cast it without expending a spell slot, but you must finish a Long Rest before you can cast it this way again."
    ),
    'Channel Divinity': (
        "You can channel divine energy directly from the Outer Planes, using it to fuel magical effects. You start with one such effect: Divine Sense, which is described below. Other Paladin features give additional Channel Divinity effect options. Each time you use this class's Channel Divinity, you choose which effect from this class to create.\n\n"
        "You can use this class's Channel Divinity twice. You regain one of its expended uses when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest. You gain an additional use when you reach Paladin level 11.\n\n"
        "If a Channel Divinity effect requires a saving throw, the DC equals the spell save DC from this class's Spellcasting Feature.\n\n"
        "  - Divine Sense. As a Bonus Action, you can open your awareness to detect Celestials, Fiends, and Undead. For the next 10 minutes or until you have the Incapacitated condition, you know the location of any creature of those types within 60 feet of yourself, and you know its creature type. Within the same radius, you also detect the presence of any place or object that has been consecrated or desecrated, as with the Hallow spell."
    ),
    'Paladin Subclass': (
        "You gain a Paladin Subclass of your choice. The Oath of Devotion, Oath of Glory, Oath of the Ancients and Oath of Vengeance subclasses are detailed after this class's description. A Subclass is a specialization that grants you features at certain Paladin levels. For the rest of your career, you gain each of your subclass’s features that are of your Paladin level or lower.\n\n"
        "Paladin Subclasses\nName\nOath of Devotion\nOath of Glory\nOath of the Ancients\nOath of Vengeance\n\n"
        "Breaking Your Oath. A Paladin tries to hold to the highest standards of conduct, but even the most dedicated are fallible. Sometimes a Paladin transgresses on their oath.\n\n"
        "A Paladin who has broken a vow typically seeks absolution, spending an all-night vigil as a sign of penitence or undertaking a fast. After a rite of forgiveness, the Paladin starts fresh.\n\n"
        "If your Paladin unrepentantly violates their oath, talk to your DM. Your Paladin should probably take a more appropriate subclass or even abandon the class and adopt another one."
    ),
    'Ability Score Improvement': (
        "You gain the Ability Score Improvement feat or another feat of your choice for which you qualify. You gain this feature again at Paladin levels 8, 12, and 16."
    ),
    'Extra Attack': (
        "You can attack twice instead of once whenever you take the Attack action on your turn."
    ),
    'Faithful Steed': (
        "You can call on the aid of an otherworldly steed.\nYou always have the Find Steed spell prepared.\n\n"
        "You can also cast the spell once without expending a spell slot, and you regain your ability to do so when you finish a Long Rest."
    ),
    'Aura of Protection': (
        "You radiate a protective, unseeable aura in a 10-foot Emanation that originates from you. The aura is inactive while you have the Incapacitated condition.\n\n"
        "You and your allies in the aura gain a bonus to saving throws equal to your Charisma modifier (minimum bonus of +1).\n\n"
        "If another Paladin is present, a creature can benefit from only one Aura of Protection at a time; the creature chooses which aura while in them."
    ),
    'Abjure Foes': (
        "As a Magic action, you can expend one use of this class's Channel Divinity to overwhelm foes with awe. As you present your Holy Symbol or weapon, you can target a number of creatures equal to your Charisma modifier (minimum of one creature) that you can see within 60 feet of yourself. Each target must succeed on a Wisdom saving throw or have the Frightened condition for 1 minute or until it takes any damage. While Frightened in this way, a target can only do one of the following on its turns: move, take an action or take a Bonus Action."
    ),
    'Aura of Courage': (
        "You and your allies have Immunity to the Frightened condition while in your Aura of Protection. If a Frightened ally enters the aura, that condition has no effect on that ally while there."
    ),
    'Radiant Strikes': (
        "Your strikes now carry supernatural power. When you hit a target with an attack roll using a Melee weapon or an Unarmed Strike, the target takes an extra 1d8 Radiant damage."
    ),
    'Restoring Touch': (
        "When you use Lay On Hands on a creature, you can also remove one or more of the following conditions from the creature: Blinded, Charmed, Deafened, Frightened, Paralyzed, or Stunned. You must expend 5 Hit Points from the healing pool of Lay On Hands for each of these conditions you remove; those points don't also restore Hit Points to the creature."
    ),
    'Aura Expansion': (
        "Your Aura of Protection is now a 30-foot Emanation."
    ),
    'Epic Boon': (
        "You gain an Epic Boon feat or another feat of your choice for which you qualify. Boon of Truesight is recommended."
    ),
}

OATH_OF_DEVOTION: Dict[Union[str, int], Any] = {
    'description': (
        "Uphold the Ideals of Justice and Order\n\n"
        "The Oath of Devotion binds Paladins to the ideals of Justice and Order. These Paladins meet the archetype of the knight in shining armor. They hold themselves to the highest standards of conduct, and some - for better or worse - hold the rest of the world to the same standards.\n\n"
        "Many who swear this oath are devoted to gods of law and good and use their gods' tenets as the measure of personal devotion. Others holed angels as their ideals and incorporate images of angelic wings into their helmets or coats of arms.\n\n"
        "These Paladins share the following tenets:\n\n"
        "  - Let your word be your promise.\n"
        "  - Protect the weak and never fear to act.\n"
        "  - Let your honorable deeds be an example."
    ),
    3: {
        'Oath of Devotion Spells': (
            "The magic of your oath ensures you always have certain spells ready; when you reach a Paladin level specified in the Oath of Devotion Spells table, you thereafter always have the listed spells prepared.\n\n"
            "Oath of Devotion Spells\nPaladin Level  Spells\n"
            "3  Protection from Evil and Good, Shield of Faith\n"
            "5  Aid, Zone of Truth\n"
            "9  Beacon of Hope, Dispel Magic\n"
            "13 Freedom of Movement, Guardian of Faith\n"
            "17 Commune, Flame Strike"
        ),
        'Sacred Weapon': (
            "When you take the Attack action, you can expend one use of your Channel Divinity to imbue one Melee weapon that you are holding with positive energy. For 10 minutes or until you use this feature again, you add your Charisma modifier to attack rolls you make with that weapon (minimum bonus of +1), and each time you hit with it, you cause it to deal its normal damage type or Radiant Damage.\n\n"
            "The weapon also emits Bright Light in a 20-foot radius and Dim Light 20 feet beyond that.\n\n"
            "You can end this effect early (no action required). This effect also ends if you aren't carrying the weapon."
        )
    },
    7: {
        'Aura of Devotion': (
            "You and your allies have Immunity to the Charmed condition while in your Aura of Protection. If a Charmed ally enters the aura, that condition has no effect on that ally while there."
        )
    },
    15: {
        'Smite of Protection': (
            "Your magical smite now radiates protective energy. Whenever you cast Divine Smite, you and your allies have Half Cover while in your Aura of Protection.\n\n"
            "The aura has this benefit until the start of your next turn."
        )
    },
    20: {
        'Holy Nimbus': (
            "As a Bonus Action, you can imbue your Aura of Protection with holy power, granting the benefits below for 10 minutes or until you end them (no action required). Once you use this feature, you can't use it again until you finish a Long Rest. You can also restore your use of it by expending a level 5 spell slot (no action required).\n\n"
            "  - Holy Ward. You have Advantage on any saving throw you are forced to make by a Fiend or an Undead.\n\n"
            "  - Radiant Damage. Whenever an enemy starts its turn in the aura, that creature takes Radiant damage equal to your Charisma modifier plus your Proficiency Bonus.\n\n"
            "  - Sunlight. The aura is filled with Bright Light that is sunlight."
        )
    }
}

OATH_OF_GLORY: Dict[Union[str, int], Any] = {
    'description': (
        "Strive for the Heights of Heroism\n\n"
        "Paladins who take the Oath of Glory believe they and their companions are destined to achieve glory through deeds of heroism. They train diligently and encourage their companions, so that they're all ready when destiny calls.\n\n"
        "These Paladins share the following tenets:\n\n"
        "  - Endeavor to be known by your deeds.\n"
        "  - Face hardships with courage.\n"
        "  - Inspire others to strive for glory."
    ),
    3: {
        'Inspiring Smite': (
            "Immediately after you cast Divine Smite, you can expend one use of your Channel Divinity and distribute Temporary Hit Points to creatures of your choice within 30 feet of yourself, which can include you. The total number of Temporary Hit Points equals 2d8 plus your Paladin level, divided among the chosen creatures however you like."
        ),
        'Oath of Glory Spells': (
            "The magic of your oath ensures you always have certain spells ready; when you reach a Paladin level specified in the Oath of Glory Spells table, you thereafter always have the listed spells prepared.\n\n"
            "Oath of Glory Spells\nPaladin Level  Spells\n"
            "3  Guiding Bolt, Heroism\n"
            "5  Enhance Ability, Magic Weapon\n"
            "9  Haste, Protection from Energy\n"
            "13 Compulsion, Freedom of Movement\n"
            "17 Legend Lore, Yolande's Regal Presence"
        ),
        'Peerless Athlete': (
            "As a Bonus Action, you can expend one use of your Channel Divinity to augment your athleticism. For 1 hour, you have Advantage on Strength (Athletics) and Dexterity (Acrobatics) checks, and the distance of your Long and High Jumps increases by 10 feet (this extra distance costs movement as normal)."
        )
    },
    7: {
        'Aura of Alacrity': (
            "Your Speed increases by 10 feet.\n\n"
            "In addition, whenever an ally enters your Aura of Protection for the first time on a turn or starts their turn there, the ally's Speed increases by 10 feet until the end of their next turn."
        )
    },
    15: {
        'Glorious Defense': (
            "You can turn defense into a sudden strike. When you or another creature you can see within 10 feet of you is hit by an attack roll, you can take a Reaction to grant a bonus to the target's AC against that attack, potentially causing it to miss. The bonus equals your Charisma modifier (minimum of +1). If the attack misses, you can make one attack with a weapon against the attacker as part of this Reaction if the attacker is within your weapon's range.\n\n"
            "You can use this feature a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."
        )
    },
    20: {
        'Living Legend': (
            "You can empower yourself with the legends - whether true or exaggerated - of your great deeds. As a Bonus Action, you gain the benefits below for 10 minutes. Once you use this feature, you can't use it again until you finish a Long Rest. You can also restore your use of it by expending a level 5 spell slot (no action required).\n\n"
            "  - Charismatic. You are blessed with an otherworldly presence and have Advantage on all Charisma checks.\n\n"
            "  - Saving Throw Reroll. If you fail a saving throw, you can take a Reaction to reroll it. You must use this new roll.\n\n"
            "  - Unerring Strike. Once on each of your turns when you make an attack roll with a weapon and miss, you can cause that attack to hit instead."
        )
    }
}

OATH_OF_THE_ANCIENTS: Dict[Union[str, int], Any] = {
    'description': (
        "Preserve Life and Light in the World\n\n"
        "The Oath of the Ancients is as old as the first elves.\n"
        "Paladins who swear this oath cherish the light; they love the beautiful and life-giving things of the world more than any principles of honor, courage and justice. They often adorn their armor and clothing with images of growing things - leaves, antlers, or flowers - to reflect their commitment to preserving life and light.\n\n"
        "These Paladins share the following tenets:\n\n"
        "  - Kindle the light of hope.\n"
        "  - Shelter life.\n"
        "  - Delight in art and laughter."
    ),
    3: {
        "Nature's Wrath": (
            "As a Magic action, you can expend one of your uses of Channel Divinity to conjure spectral vines around nearby creatures. Each creature of your choice that you can see within 15 feet of yourself must succeed on a Strength saving throw or have the Restrained condition for 1 minute. A Restrained creature repeats the save at the end of each of its turns, ending the effect on a success."
        ),
        'Oath of the Ancients Spells': (
            "The magic of your oath ensures you always have certain spells ready; when you reach a Paladin level specified in the Oath of the Ancients Spells table, you thereafter always have the listed spells prepared.\n\n"
            "Oath of the Ancients Spells\nPaladin Level  Spells\n"
            "3  Ensnaring Strike, Speak with Animals\n"
            "5  Misty Step, Moonbeam\n"
            "9  Plant Growth, Protection from Energy\n"
            "13 Ice Storm, Stoneskin\n"
            "17 Commune with Nature, Tree Stride"
        )
    },
    7: {
        'Aura of Warding': (
            "Ancient magic lies so heavily upon you that it forms an eldritch ward, blunting energy from beyond the Material Plane; you and your allies have Resistance to Necrotic, Psychic and Radiant damage while in your Aura of Protection."
        )
    },
    15: {
        'Undying Sentinel': (
            "When you are reduced to 0 Hit Points and not killed outright, you can drop to 1 Hit Point instead, and regain a number of Hit Points equal to three times your Paladin level. Once you use this feature, you can't do so again until you finish a Long Rest.\n\n"
            "Additionally, you can't be aged magically, and you cease visibly aging."
        )
    },
    20: {
        'Elder Champion': (
            "As a Bonus Action, you can imbue your Aura of Protection with primal power, granting the benefits below for 1 minute or until you end them (no action required). Once you use this feature, you can't use it again until you finish a Long Rest. You can also restore your use of it by expending a level 5 spell slot (no action required).\n\n"
            "  - Diminish Defiance. Enemies in the aura have Disadvantage on saving throws against your spells and Channel Divinity options.\n\n"
            "  - Regeneration. At the start of each of your turns, you regain 10 Hit Points.\n\n"
            "  - Swift Spells. Whenever you cast a spell that has a casting time of an action, you can cast it using a Bonus Action instead."
        )
    }
}

OATH_OF_VENGEANCE: Dict[Union[str, int], Any] = {
    'description': (
        "Punish Evildoers at Any Cost\n\n"
        "The Oath of Vengeance is a solemn commitment to punish those who have committed grievously evil acts. When evil armies slaughter helpless villagers, when a tyrant defies the will of the gods, when a thieves' guild grows too violent, when a dragon rampages though the countryside - at times like these, Paladins arise and swear the Oath of Vengeance to set right what has gone wrong.\n\n"
        "These Paladins share the following tenets:\n\n"
        "  - Show the wicked no mercy.\n"
        "  - Fight injustice and its causes.\n"
        "  - Aid those harmed by injustice."
    ),
    3: {
        'Oath of Vengeance Spells': (
            "The magic of your oath ensures you always have certain spells ready; when you reach a Paladin level specified in the Oath of Vengeance Spells table, you thereafter always have the listed spells prepared.\n\n"
            "Oath of Vengeance Spells\nPaladin Level  Spells\n"
            "3  Bane, Hunter's Mark\n"
            "5  Hold Person, Misty Step\n"
            "9  Haste, Protection from Energy\n"
            "13 Banishment, Dimension Door\n"
            "17 Hold Monster, Scrying"
        ),
        'Vow of Enmity': (
            "When you take the Attack action, you can expend one use of your Channel Divinity to utter a vow of enmity against a creature you can see within 30 feet of yourself. You have Advantage on attack rolls against the creature for 1 minute or until you use this feature again.\n\n"
            "If the creature drops to 0 Hit Points before the vow ends, you can transfer the vow to a different creature within 30 feet of yourself (no action required)."
        )
    },
    7: {
        'Relentless Avenger': (
            "Your supernatural focus helps you close off a foe's retreat. When you hit a creature with an Opportunity Attack, you can reduce the creature's Speed to 0 until the end of the current turn. You can then move up to half your Speed as part of the same Reaction. This movement doesn't provoke Opportunity Attacks."
        )
    },
    15: {
        'Soul of Vengeance': (
            "Immediately after a creature under the effect of your Vow of Enmity hits or misses with an attack roll, you can take a Reaction to make a melee attack against that creature if it's within range."
        )
    },
    20: {
        'Avenging Angel': (
            "As a Bonus Action, you gain the benefits below for 10 minutes or until you end them (no action required). Once you use this feature, you can't use it again until you finish a Long Rest. You can also restore your use of it by expending a level 5 spell slot (no action required).\n\n"
            "  - Flight. You sprout spectral wings on your back and have a Fly Speed of 60 feet, and can hover.\n\n"
            "  - Frightful Aura. Whenever an enemy starts its turn in your Aura of Protection, that creature must succeed on a Wisdom saving throw or have the Frightened condition for 1 minute or until it takes any damage. Attack rolls against the Frightened creature have Advantage."
        )
    }
}
