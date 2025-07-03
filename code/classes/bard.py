"""
Bard class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

BARD_CLASS: Dict[str, Any] = {
    'name': 'Bard',
    'hit_die': 8,
    'primary_ability': 'Charisma',
    'saving_throws': ['Dexterity', 'Charisma'],
    'proficiencies': {
        'armor': ['Light Armor'],
        'weapons': ['Simple Weapons'],
        'tools': ['Choose 3 Musical Instruments'],
        'skills': ['Choose any 3 skills']
    },
    'starting_equipment': [
        ['Leather Armor', '2 Daggers', 'Musical Instrument of your choice', "Entertainer's Pack", '19 GP'],
        ['90 GP']
    ]
}

BARD_LEVELS: Dict[int, Dict[str, Any]] = {
    1: {
        'features': ['Bardic Inspiration', 'Spellcasting'],
        'bardic_inspiration_die': 'd6',
        'spellcasting': {
            'cantrips_known': 2,
            'spells_prepared': 4,
            'spells_known': 4,
            'spell_slots': {'Level 1': 2}
        }
    },
    2: {
        'features': ['Expertise', 'Jack of all Trades'],
        'bardic_inspiration_die': 'd6',
        'spellcasting': {
            'cantrips_known': 2,
            'spells_prepared': 5,
            'spells_known': 5,
            'spell_slots': {'Level 1': 3}
        }
    },
    3: {
        'features': ['Bard Subclass'],
        'bardic_inspiration_die': 'd6',
        'spellcasting': {
            'cantrips_known': 2,
            'spells_prepared': 6,
            'spells_known': 6,
            'spell_slots': {'Level 1': 4, 'Level 2': 2}
        }
    },
    4: {
        'features': ['Ability Score Improvement'],
        'bardic_inspiration_die': 'd6',
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 7,
            'spells_known': 7,
            'spell_slots': {'Level 1': 4, 'Level 2': 3}
        }
    },
    5: {
        'features': ['Font of Inspiration'],
        'bardic_inspiration_die': 'd8',
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 9,
            'spells_known': 9,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 2}
        }
    },
    6: {
        'features': ['Subclass Feature'],
        'bardic_inspiration_die': 'd8',
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 10,
            'spells_known': 10,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3}
        }
    },
    7: {
        'features': ['Countercharm'],
        'bardic_inspiration_die': 'd8',
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 11,
            'spells_known': 11,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 1}
        }
    },
    8: {
        'features': ['Ability Score Improvement'],
        'bardic_inspiration_die': 'd8',
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 12,
            'spells_known': 12,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 2}
        }
    },
    9: {
        'features': ['Expertise'],
        'bardic_inspiration_die': 'd8',
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 14,
            'spells_known': 14,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 1}
        }
    },
    10: {
        'features': ['Magical Secrets'],
        'bardic_inspiration_die': 'd10',
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 15,
            'spells_known': 15,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2}
        }
    },
    11: {
        'features': [],
        'bardic_inspiration_die': 'd10',
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 16,
            'spells_known': 16,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1}
        }
    },
    12: {
        'features': ['Ability Score Improvement'],
        'bardic_inspiration_die': 'd10',
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 16,
            'spells_known': 16,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1}
        }
    },
    13: {
        'features': [],
        'bardic_inspiration_die': 'd10',
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 17,
            'spells_known': 17,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1}
        }
    },
    14: {
        'features': ['Subclass Feature'],
        'bardic_inspiration_die': 'd10',
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 17,
            'spells_known': 17,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1}
        }
    },
    15: {
        'features': [],
        'bardic_inspiration_die': 'd12',
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 18,
            'spells_known': 18,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1, 'Level 8': 1}
        }
    },
    16: {
        'features': ['Ability Score Improvement'],
        'bardic_inspiration_die': 'd12',
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 18,
            'spells_known': 18,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1, 'Level 8': 1}
        }
    },
    17: {
        'features': [],
        'bardic_inspiration_die': 'd12',
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 19,
            'spells_known': 19,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1, 'Level 8': 1, 'Level 9': 1}
        }
    },
    18: {
        'features': ['Superior Inspiration'],
        'bardic_inspiration_die': 'd12',
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 20,
            'spells_known': 20,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1, 'Level 8': 1, 'Level 9': 1}
        }
    },
    19: {
        'features': ['Epic Boon'],
        'bardic_inspiration_die': 'd12',
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 21,
            'spells_known': 21,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 2, 'Level 7': 1, 'Level 8': 1, 'Level 9': 1}
        }
    },
    20: {
        'features': ['Words of Creation'],
        'bardic_inspiration_die': 'd12',
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 22,
            'spells_known': 22,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 2, 'Level 7': 2, 'Level 8': 1, 'Level 9': 1}
        }
    }
}

COLLEGE_OF_DANCE: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        'Move in Harmony with the Cosmos\n\n'
        'Bards of the College of Dance know that the Words of Creation can\'t be contained within speech or song; the words are uttered by the '
        'movements of celestial bodies and flow through the motions of the smallest creatures.\n'
        'These Bards practice a way of being in harmony with the whirling cosmos that emphasizes agility, speed, and grace.'
    ),
    3: {
        'Dazzling Footwork': (
            'While you aren\'t wearing armor or wielding a Shield, you gain the following benefits.\n\n'
            '  - Dance Virtuoso: You have Advantage on any Charisma (Performance) check you make that involves you dancing.\n'
            '  - Unarmored Defense: Your base Armor Class equals 10 plus your Dexterity and Charisma modifiers.\n'
            '  - Agile Strikes: When you expend a use of your Bardic Inspiration as part of an action, a Bonus Action, or a Reaction, you can '
            'make one Unarmed Strike as part of that action, Bonus Action, or Reaction.\n'
            '  - Bardic Damage: You can use Dexterity instead of Strength for the attack rolls of your Unarmed Strikes. When you deal damage with '
            'an Unarmed Strike, you can deal Bludgeoning damage equal to a roll of your Bardic Inspiration die plus your Dexterity modifier, '
            'instead of the strike\'s normal damage. This roll doesn\'t expend the die.'
        )
    },
    6: {
        'Inspiring Movement': (
            'When an enemy you can see ends its turn within 5 feet of you, you can take a Reaction and expend one use of your Bardic Inspiration to '
            'move up to half your Speed. Then one ally of your choice within 30 feet of you can also move up to half their Speed using their '
            'Reaction.\n\n'
            'None of this feature\'s movement provokes Opportunity Attacks.'
        ),
        'Tandem Footwork': (
            'When you roll Initiative, you can expend one use of your Bardic Inspiration if you don\'t have the Incapacitated condition. When you do '
            'so, roll your Bardic Inspiration die; you and each ally within 30 feet of you who can see or hear you gains a bonus to Initiative equal '
            'to the number rolled.'
        )
    },
    14: {
        'Leading Evasion': (
            'When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage '
            'if you succeed on the saving throw and only half damage if you fail. If any creatures within 5 feet of you are making the same Dexterity '
            'saving throw, you can share this benefit with them for that save.\n\n'
            'You can\'t use this feature if you have the Incapacitated condition.'
        )
    }
}

COLLEGE_OF_GLAMOUR: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        'Weave Beguiling Fey Magic\n\n'
        'The College of Glamour traces its origins to the beguiling magic of the Feywild.\n'
        'Bards who study this magic weave threads of beauty and terror into their songs and stories, and the mightiest among them can cloak themselves '
        'in otherworldly majesty. Their performances stir up wistful longing for forgotten innocence, evoke unconscious memories of longheld fears, and '
        'tug at the emotions of  even the most hard-hearted listeners.'
    ),
    3: {
        'Beguiling Magic': (
            'You always have the Charm Person and Mirror Image spells prepared.\n\n'
            'In addition, immediately after you cast an Enchantment or Illusion spell using a spell slot, you can cause a creature you can see within 60 '
            'feet of yourself to make a Wisdom saving throw against your spell save DC. On a failed save, the target has the Charmed or Frightened '
            'condition (your choice) for 1 minute. The target repeats the save at the end of each of its turns, ending the effect on itself on a success.\n\n'
            'Once you use this benefit, you can\'t use it again until you finish a Long Rest. You can also restore your use of it by expending one use of your '
            'Bardic Inspiration (no action required).'
        ),
        'Mantle of Inspiration': (
            'You can weave fey magic into a song or dance to fill others with vigor. As a Bonus Action, you can expend a use of Bardic Inspiration, rolling a'
            'Bardic Inspiration die. When you do so, choose a number of other creatures within 60 feet of yourself, up to a number equal to your Charisma '
            'modifier (minimum of one creature). Each of those creatures gains a number of Temporary Hit Points equal to two times the number rolled on the '
            'Bardic Inspiration die, and then each can use its Reaction to move up to its Speed without provoking Opportunity Attacks.'
        )
    },
    6: {
        'Mantle of Majesty': (
            'You always have the Command spell prepared.\n\n'
            'As a Bonus Action, you cast Command (no spell slot required), and you take on an unearthly appearance for 1 minute or until your Concentration '
            'ends. During this time, you can cast Command as a Bonus Action without expending a spell slot.\n\n'
            'Any creature Charmed by you automatically fails its saving throw against the Command you cast with this feature.\n\n'
            'Once you use this feature, you can\'t use it again until you finish a Long Rest. You can also restore your use of it by expending a level 3+'
            'spell slot (no action required).'
        )
    },
    14: {
        'Unbreakable Majesty': (
            'As a Bonus Action, you can assume a magically majestic presence for 1 minute or until you have the Incapacitated condition. For the duration, '
            'whenever any creature hits you with an attack roll for the first time on a turn, the attacker must succeed on a Charisma saving throw against '
            'your spell save DC, or the attack misses instead, as the creature recoils from your majesty.\n\n'
            'Once you assume this majestic presence, you can\'t do so again until you finish a Short or Long Rest.'
        )
    }
}

COLLEGE_OF_LORE: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        'Plumb the Depths of Magical Knowledge\n\n'
        'Bards of the College of Lore collect spells and secrets from diverse sources, such as scholarly tomes, mystical rites, and peasant tales.\n'
        'The college\'s members gather in libraries and universities to share their lore with one another. They also meet at festivals or affairs of '
        'state, where they can expose corruption, unravel lies, and poke fun at self-important figures of authority.'
    ),
    3: {
        'Bonus Proficiencies': (
            'You gain proficiency with three skills of your choice.'
        ),
        'Cutting Words': (
            'You learn to use your wit to supernaturally distract, confuse, and otherwise sap the confidence and competence of others. When a creature '
            'that you can see within 60 feet of yourself makes a damage roll or succeeds on an ability check or attack roll, you can take a Reaction '
            'to expend one use of your Bardic Inspiration; roll your Bardic Inspiration die, and subtract the number rolled from the creature\'s roll, '
            'reducing the damage or potentially turning the success into a failure.'
        )
    },
    6: {
        'Magical Discoveries': (
            'You learn two spells of your choice. These spells can come from the Cleric, Druid, or Wizard spell list or any combination thereof.\n\n'
            'A spell you choose must be a cantrip or a spell for which you have spell slots, as shown in the Bard Features table.\n\n'
            'You always have the chosen spells prepared, and whenever you gain a Bard level, you can replace one of the spells with another spell '
            'that meets these requirements.'
        )
    },
    14: {
        'Peerless Skill': (
            'When you make an ability check or attack roll and fail, you can expend one use of Bardic Inspiration; roll the Bardic Inspiration die, '
            'and add the number rolled to the d20, potentially turning a failure into a success. On a failure, the Bardic Inspiration isn\'t expended.'
        )
    }
}

COLLEGE_OF_VALOR: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        'Sing the Deeds of Ancient Heroes\n\n'
        'Bards of the College of Valor are daring storytellers whose tales preserve the memory of the great heroes of the past.\n'
        'These Bards sing the deeds of the mighty in vaulted halls or to crowds gathered around great bonfires. They travel to witness great events '
        'firsthand and to ensure that the memory of these events doesn\'t pass away. With their songs, they inspire new generations to reach the '
        'same heights of accomplishment as the heroes of old.'
    ),
    3: {
        'Combat Inspiration': (
            'You can use your wit to turn the tide of battle. A creature that has a Bardic Inspiration die from you can use it for one of the '
            'following effects.\n\n'
            '  - Defense: When the creature is hit by an attack roll, that creature can use its Reaction to roll the Bardic Inspiration die and add '
            'the number rolled to its AC against that attack, potentially causing the attack to miss.\n\n'
            '  - Offense: Immediately after the creature hits a target with an attack roll, the creature can roll the Bardic Inspiration die and add '
            'the number rolled to the attack\'s damage against the target.'
        ),
        'Martial Training': (
            'You gain proficiency with Martial weapons and training with Medium armor and Shields.\n\n'
            'In addition, you can use a Simple or Martial weapon as a Spellcasting Focus to cast spells from your Bard spell list.'
        )
    },
    6: {
        'Extra Attack': (
            'You can attack twice instead of once whenever you take the Attack action on your turn.\n\n'
            'In addition, you can cast one of your cantrips that has a casting time of an action in place of one of those attacks.'
        )
    },
    14: {
        'Battle Magic': (
            'After you cast a spell that has a casting time of an action, you can make one attack with a weapon as a Bonus Action.'
        )
    }
}


BARD_FEATURES: Dict[Union[str, int], Any] = {
    'Bardic Inspiration': {
        'You can supernaturally inspire others through words, music, or dance. This inspiration is represented by your Bardic Inspiration die, '
        'which is a d6.\n\n'
        '  - Using Bardic Inspiration. As a Bonus Action, you can inspire another creature within 60 feet of yourself who can see or hear you. '
        'That creature gains one of your Bardic Inspiration dice. A creature can have only one Bardic Inspiration die at a time.\n\n'
        '    Once within the next hour when the creature fails a D20 Test, the creature can roll the Bardic Inspiration die and add the number '
        'rolled to the d20, potentially turning the failure into a success. A Bardic Inspiration die is expended when it\'s rolled.\n\n'
        '  - Number of Uses. You can confer a Bardic Inspiration die a number of times equal to your Charisma modifier (minimum of once), and '
        'you regain all expended uses when you finish a Long Rest.\n\n'
        '  - At Higher Levels. Your Bardic Inspiration die changes when you reach certain Bard levels, as shown in the Bardic Die column of '
        'the Bard Features table. The die becomes a d8 at level 5, a d10 at level 10, and a d12 at level 15.'
    },
    'Spellcasting': {
        'You have learned to cast spells through your bardic arts. See chapter 7 for the rules on spellcasting. The information below details '
        'how you use those rules with Bard spells, which appear in the Bard spell list later in the class\'s description.\n\n'
        '  - Cantrips. You know two cantrips of your choice from the Bard spell list. Dancing Lights and Vicious Mockery are recommended.\n'
        '    Whenever you gain a Bard level, you can replace one of your cantrips with another cantrip of your choice from the Bard spell list.\n'
        '    When you reach Bard levels 4 and 10, you learn another cantrip of your choice from the Bard spell list, as shown in the Cantrips '
        'column of the Bard Features table.\n\n'
        '  - Spell Slots. The Bard Features table shows how many spell slots you have to cast your level 1+ spells. You regain all expended '
        'slots when you finish a Long Rest.'
        '  - Prepared Spells of Level 1+. You prepare the list of level 1+ spells that are available for you to cast with this feature. To '
        'start, choose four level 1 spells from the Bard spell list. Charm Person, Color Spray, Dissonant Whispers, and Healing Word are '
        'recommended.\n'
        '    The number of spells on your list increases as you gain Bard levels, as shown in the Prepared Spells column of the Bard Features '
        'table. Whenever that number increases, choose additional spells from the Bard spell list until the number of spells on your list '
        'matches the number on the table. The chosen spells must be of a level for which you have spell slots. For example, if you\'re a level '
        '3 Bard, your list of prepared spells can include six spells of levels 1 and 2 in any combination.\n'
        'If another Bard feature gives you spells that you always have prepared, those spells don\'t count against the number of spells you '
        'can prepare with this feature, but those spells otherwise count as Bard spells for you.\n\n'
        '  - Changing Your Prepared Spells. Whenever you gain a Bard level, you can replace one spell on your list with another Bard spell '
        'for which you have spell slots.\n\n'
        'Spellcasting Ability. Charisma is your spellcasting ability for your Bard spells.\n\n'
        'Spellcasting Focus. You can use a Musical Instrument as a Spellcasting Focus for your Bard spells.'
    },
    'Expertise': {
        'You gain Expertise (see the rules glossary) in two of your skill proficiencies of your choice. Performance and Persuasion are '
        'recommended if you have proficiency in them.\n\n'
        'At Bard level 9, you gain Expertise in two more of your skill proficiencies of your choice.'
    },
    'Jack of all Trades': {
        'You can add half your Proficiency Bonus (round down) to any ability check you make that uses a skill proficiency you lack and that doesn\'t '
        'otherwise use your Proficiency Bonus. For example, if you make a Strength (Athletics) check and lack Athletics proficiency, you can add '
        'half your Proficiency Bonus to the check.'
    },
    'Bard Subclass': {
        'You gain a Bard subclass of your choice. The College of Dance, College of Glamour, College of Lore, and College of Valor subclasses are '
        'detailed after this class\'s description. A subclass is a specialization that grants you features at certain Bard levels. For the rest of '
        'your career, you gain each of your subclass\'s features that are of your Bard level or lower.'
        },
    4: {
        'Ability Score Improvement': (
            "Increase one ability score by 2, or two by 1 each, or take a feat. Repeat at levels 8, 12, 16."
        )
    },
    5: {
        'Font of Inspiration': (
            "Regain all Bardic Inspiration uses on a Short or Long Rest. Spend a spell slot to regain one use."
        )
    },
    6: {
        'Subclass Feature': (
            "Gain a feature from your Bard subclass."
        )
    },
    7: {
        'Countercharm': (
            "As a Reaction, if you or a creature within 30 feet fails a save vs Charmed or Frightened, reroll with Advantage."
        )
    },
    8: {
        'Ability Score Improvement': (
            "Increase one ability score by 2, or two by 1 each, or take a feat."
        )
    },
    9: {
        'Expertise': (
            "Choose 2 more skill proficiencies for Expertise."
        )
    },
    10: {
        'Magical Secrets': (
            "When your prepared spells increase, you can choose new spells from the Bard, Cleric, Druid, or Wizard lists. "
            "When you replace a spell, you can choose from those lists."
        )
    },
    11: {},
    12: {
        'Ability Score Improvement': (
            "Increase one ability score by 2, or two by 1 each, or take a feat."
        )
    },
    13: {},
    14: {
        'Subclass Feature': (
            "Gain a feature from your Bard subclass."
        )
    },
    15: {},
    16: {
        'Ability Score Improvement': (
            "Increase one ability score by 2, or two by 1 each, or take a feat."
        )
    },
    17: {},
    18: {
        'Superior Inspiration': (
            "When you roll Initiative, regain Bardic Inspiration uses until you have at least two."
        )
    },
    19: {
        'Epic Boon': (
            "Gain an Epic Boon feat or another feat of your choice."
        )
    },
    20: {
        'Words of Creation': (
            "Always have Power Word: Heal and Power Word: Kill prepared. When you cast either, you can target a second creature within 10 feet."
        )
    }
}
