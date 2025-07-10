"""
Warlock class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

WARLOCK_CLASS: Dict[str, Any] = {
    'name': 'Warlock',
    'hit_die': 8,
    'primary_ability': 'Charisma',
    'saving_throws': ['Wisdom', 'Charisma'],
    'proficiencies': {
        'armor': ['Light Armor'],
        'weapons': ['Simple Weapons'],
        'tools': [],
        'skills': [
            'Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Nature', 'Religion'
        ],
        'skills_choose': 2
    },
    'starting_equipment': [
        [
            'Leather Armor', 'Sickle', 'Dagger', 'Dagger', 'Arcane Focus (orb)', 'Book (occult lore)', "Scholar's Pack", '15 GP'
        ],
        ['100 GP']
    ]
}

WARLOCK_LEVELS: Dict[int, Dict[str, Any]] = {
    1: {
        'proficiency_bonus': 2,
        'features': ['Eldritch Invocations', 'Pact Magic'],
        'eldritch_invocations': 2,
        'spellcasting': {
            'cantrips_known': 2,
            'spells_prepared': 2,
            'spells_known': 2,
            'spell_slots': 1,
            'slot_level': 1
        }
    },
    2: {
        'proficiency_bonus': 2,
        'features': ['Magical Cunning'],
        'eldritch_invocations': 3,
        'spellcasting': {
            'cantrips_known': 2,
            'spells_prepared': 3,
            'spells_known': 3,
            'spell_slots': 2,
            'slot_level': 1
        }
    },
    3: {
        'proficiency_bonus': 2,
        'features': ['Warlock Subclass'],
        'eldritch_invocations': 3,
        'spellcasting': {
            'cantrips_known': 2,
            'spells_prepared': 4,
            'spells_known': 4,
            'spell_slots': 2,
            'slot_level': 2
        }
    },
    4: {
        'proficiency_bonus': 2,
        'features': ['Ability Score Improvement'],
        'eldritch_invocations': 3,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 5,
            'spells_known': 5,
            'spell_slots': 2,
            'slot_level': 2
        }
    },
    5: {
        'proficiency_bonus': 3,
        'features': [],
        'eldritch_invocations': 5,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 6,
            'spells_known': 6,
            'spell_slots': 2,
            'slot_level': 3
        }
    },
    6: {
        'proficiency_bonus': 3,
        'features': ['Subclass Feature'],
        'eldritch_invocations': 5,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 7,
            'spells_known': 7,
            'spell_slots': 2,
            'slot_level': 3
        }
    },
    7: {
        'proficiency_bonus': 3,
        'features': [],
        'eldritch_invocations': 6,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 8,
            'spells_known': 8,
            'spell_slots': 2,
            'slot_level': 4
        }
    },
    8: {
        'proficiency_bonus': 3,
        'features': ['Ability Score Improvement'],
        'eldritch_invocations': 6,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 9,
            'spells_known': 9,
            'spell_slots': 2,
            'slot_level': 4
        }
    },
    9: {
        'proficiency_bonus': 4,
        'features': ['Contact Patron'],
        'eldritch_invocations': 7,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 10,
            'spells_known': 10,
            'spell_slots': 2,
            'slot_level': 5
        }
    },
    10: {
        'proficiency_bonus': 4,
        'features': ['Subclass Feature'],
        'eldritch_invocations': 7,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 10,
            'spells_known': 10,
            'spell_slots': 2,
            'slot_level': 5
        }
    },
    11: {
        'proficiency_bonus': 4,
        'features': ['Mystic Arcanum (Level 6 Spell)'],
        'eldritch_invocations': 7,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 11,
            'spells_known': 11,
            'spell_slots': 3,
            'slot_level': 5
        }
    },
    12: {
        'proficiency_bonus': 4,
        'features': ['Ability Score Improvement'],
        'eldritch_invocations': 8,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 11,
            'spells_known': 11,
            'spell_slots': 3,
            'slot_level': 5
        }
    },
    13: {
        'proficiency_bonus': 5,
        'features': ['Mystic Arcanum (Level 7 Spell)'],
        'eldritch_invocations': 8,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 12,
            'spells_known': 12,
            'spell_slots': 3,
            'slot_level': 5
        }
    },
    14: {
        'proficiency_bonus': 5,
        'features': ['Subclass Feature'],
        'eldritch_invocations': 8,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 12,
            'spells_known': 12,
            'spell_slots': 3,
            'slot_level': 5
        }
    },
    15: {
        'proficiency_bonus': 5,
        'features': ['Mystic Arcanum (Level 8 Spell)'],
        'eldritch_invocations': 9,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 13,
            'spells_known': 13,
            'spell_slots': 3,
            'slot_level': 5
        }
    },
    16: {
        'proficiency_bonus': 5,
        'features': ['Ability Score Improvement'],
        'eldritch_invocations': 9,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 13,
            'spells_known': 13,
            'spell_slots': 3,
            'slot_level': 5
        }
    },
    17: {
        'proficiency_bonus': 6,
        'features': ['Mystic Arcanum (Level 9 Spell)'],
        'eldritch_invocations': 9,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 14,
            'spells_known': 14,
            'spell_slots': 4,
            'slot_level': 5
        }
    },
    18: {
        'proficiency_bonus': 6,
        'features': [],
        'eldritch_invocations': 10,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 14,
            'spells_known': 14,
            'spell_slots': 4,
            'slot_level': 5
        }
    },
    19: {
        'proficiency_bonus': 6,
        'features': ['Epic Boon'],
        'eldritch_invocations': 10,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 15,
            'spells_known': 15,
            'spell_slots': 4,
            'slot_level': 5
        }
    },
    20: {
        'proficiency_bonus': 6,
        'features': ['Eldritch Master'],
        'eldritch_invocations': 10,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 15,
            'spells_known': 15,
            'spell_slots': 4,
            'slot_level': '5 (see Mystic Arcanum)'
        }
    }
}

WARLOCK_FEATURES: Dict[str, Any] = {
    'Eldritch Invocations': (
        "You have unearthed Eldritch Invocations, pieces of forbidden knowledge that imbue you with an abiding magical ability or other lessons. "
        "You gain one invocation of your choice, such as Pact of the Tome. Invocations are described in the ‘Eldritch Invocation Options’ section later in this class’s description.\n\n"
        "  - Prerequisites. If an invocation has a prerequisite, you must meet it to learn that invocation. For example, if an invocation requires you to be a level 5+ Warlock, you can select the invocation once you reach Warlock level 5.\n\n"
        "  - Replacing and Gaining Invocations. Whenever you gain a Warlock level, you can replace one of your invocations with another one for which you qualify. You can’t replace an invocation if it’s a prerequisite for another invocation that you have.\n\n"
        "    When you gain certain Warlock levels, you gain more invocations of your choice, as shown in the Invocations column of the Warlock Features table.\n\n"
        "    You can’t pick the same invocation more than once unless its description says otherwise."
    ),
    'Pact Magic': (
        "Through occult ceremony, you have formed a pact with a mysterious entity to gain magical powers. The entity is a voice in the shadows—its identity unclear—but its boon to you is concrete: the ability to cast spells. See chapter 7 for the rules on spellcasting. The information below details how you use those rules with Warlock spells, which appear in the Warlock spell list later in the class’s description.\n\n"
        "  - Cantrips. You know two Warlock cantrips of your choice. Eldritch Blast and Prestidigitation are recommended. Whenever you gain a Warlock level, you can replace one of your cantrips from this feature with another Warlock cantrip of your choice.\n\n"
        "    When you reach Warlock levels 4 and 10, you learn another Warlock cantrip of your choice, as shown in the Cantrips column of the Warlock Features table.\n\n"
        "  - Spell Slots. The Warlock Features table shows how many spell slots you have to cast your Warlock spells of levels 1–5. The table also shows the level of those slots, all of which are the same level. You regain all expended Pact Magic spell slots when you finish a Short or Long Rest.\n\n"
        "    For example, when you’re a level 5 Warlock, you have two level 3 spell slots. To cast the level 1 spell Witch Bolt, you must spend one of those slots, and you cast it as a level 3 spell.\n\n"
        "  - Prepared Spells of Level 1+. You prepare the list of level 1+ spells that are available for you to cast with this feature. To start, choose two level 1 Warlock spells. Charm Person and Hex are recommended.\n\n"
        "    The number of spells on your list increases as you gain Warlock levels, as shown in the Prepared Spells column of the Warlock Features table. Whenever that number increases, choose additional Warlock spells until the number of spells on your list matches the number in the table. The chosen spells must be of a level no higher than what’s shown in the table’s Slot Level column for your level. When you reach level 6, for example, you learn a new Warlock spell, which can be of levels 1–3.\n\n"
        "    If another Warlock feature gives you spells that you always have prepared, those spells don’t count against the number of spells you can prepare with this feature, but those spells otherwise count as Warlock spells for you.\n\n"
        "  - Changing Your Prepared Spells. Whenever you gain a Warlock level, you can replace one spell on your list with another Warlock spell of an eligible level.\n\n"
        "  - Spellcasting Ability. Charisma is the spellcasting ability for your Warlock spells.\n\n"
        "  - Spellcasting Focus. You can use an Arcane Focus as a Spellcasting Focus for your Warlock spells."
    ),
    'Magical Cunning': (
        "You can perform an esoteric rite for 1 minute. At the end of it, you regain expended Pact Magic spell slots but no more than a number equal to half your maximum (round up). Once you use this feature, you can’t do so again until you finish a Long Rest."
    ),
    'Warlock Subclass': (
        "You gain a Warlock subclass of your choice. The Archfey Patron, Celestial Patron, Fiend Patron, and Great Old One Patron subclasses are detailed after this class’s description. A subclass is a specialization that grants you features at certain Warlock levels. For the rest of your career, you gain each of your subclass’s features that are of your Warlock level or lower."
    ),
    'Ability Score Improvement': (
        "You gain the Ability Score Improvement feat or another feat of your choice for which you qualify. You gain this feature again at Warlock levels 8, 12, and 16."
    ),
    'Contact Patron': (
        "In the past, you usually contacted your patron through intermediaries. Now you can communicate directly; you always have the Contact Other Plane spell prepared. With this feature, you can cast the spell without expending a spell slot to contact your patron, and you automatically succeed on the spell’s saving throw.\n\n"
        "Once you cast the spell with this feature, you can’t do so in this way again until you finish a Long Rest."
    ),
    'Mystic Arcanum': (
        "Your patron grants you a magical secret called an arcanum. Choose one level 6 Warlock spell as this arcanum.\n\n"
        "You can cast your arcanum spell once without expending a spell slot, and you must finish a Long Rest before you can cast it in this way again.\n\n"
        "As shown in the Warlock Features table, you gain another Warlock spell of your choice that can be cast in this way when you reach Warlock levels 13 (level 7 spell), 15 (level 8 spell), and 17 (level 9 spell). You regain all uses of your Mystic Arcanum when you finish a Long Rest.\n\n"
        "Whenever you gain a Warlock level, you can replace one of your arcanum spells with another Warlock spell of the same level."
    ),
    'Epic Boon': (
        "You gain an Epic Boon feat or another feat of your choice for which you qualify. Boon of Fate is recommended."
    ),
    'Eldritch Master': (
        "When you use your Magical Cunning feature, you regain all your expended Pact Magic spell slots."
    )
}

ARCHFEY_PATRON = {
    'description': (
        "Bargain with Whimsical Fey\n\n"
        "Your pact draws on the power of the Feywild. When you choose this subclass, you might make a deal with an archfey, such as the Prince of Frost; the Queen of Air and Darkness, ruler of the Gloaming Court; Titania of the Summer Court; or an ancient hag. Or you might call on a spectrum of Fey, weaving a web of favors and debts. Whoever they are, your patron is often inscrutable and whimsical."
    ),
    3: {
        'Archfey Spells': (
            "The magic of your patron ensures you always have certain spells ready; when you reach a Warlock level specified in the Archfey Spells table, you thereafter always have the listed spells prepared.\n\n"
            "Archfey Spells\nWarlock Level\tSpells\n3\tCalm Emotions, Faerie Fire, Misty Step, Phantasmal Force, Sleep\n5\tBlink, Plant Growth\n7\tDominate Beast, Greater Invisibility\n9\tDominate Person, Seeming"
        ),
        'Steps of the Fey': (
            "Your patron grants you the ability to move between the boundaries of the planes. You can cast Misty Step without expending a spell slot a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.\n\nIn addition, whenever you cast that spell, you can choose one of the following additional effects.\n\nRefreshing Step. Immediately after you teleport, you or one creature you can see within 10 feet of yourself gains 1d10 Temporary Hit Points.\n\nTaunting Step. Creatures within 5 feet of the space you left must succeed on a Wisdom saving throw against your spell save DC or have Disadvantage on attack rolls against creatures other than you until the start of your next turn."
        )
    },
    6: {
        'Misty Escape': (
            "You can cast Misty Step as a Reaction in response to taking damage.\n\nIn addition, the following effects are now among your Steps of the Fey options.\n\nDisappearing Step. You have the Invisible condition until the start of your next turn or until immediately after you make an attack roll, deal damage, or cast a spell.\n\nDreadful Step. Creatures within 5 feet of the space you left or the space you appear in (your choice) must succeed on a Wisdom saving throw against your spell save DC or take 2d10 Psychic damage."
        )
    },
    10: {
        'Beguiling Defenses': (
            "Your patron teaches you how to guard your mind and body. You are immune to the Charmed condition.\n\nIn addition, immediately after a creature you can see hits you with an attack roll, you can take a Reaction to reduce the damage you take by half (round down), and you can force the attacker to make a Wisdom saving throw against your spell save DC. On a failed save, the attacker takes Psychic damage equal to the damage you take. Once you use this Reaction, you can’t use it again until you finish a Long Rest unless you expend a Pact Magic spell slot (no action required) to restore your use of it."
        )
    },
    14: {
        'Bewitching Magic': (
            "Your patron grants you the ability to weave your magic with teleportation. Immediately after you cast an Enchantment or Illusion spell using an action and a spell slot, you can cast Misty Step as part of the same action and without expending a spell slot."
        )
    }
}

CELESTIAL_PATRON = {
    'description': (
        "Call on the Power of the Heavens\n\n"
        "Your pact draws on the Upper Planes, the realms of everlasting bliss. You might enter an agreement with an empyrean, a couatl, a sphinx, a unicorn, or another heavenly entity. Or you might call on numerous such beings as you pursue goals aligned with theirs. Your pact allows you to experience a hint of the holy light that illuminates the multiverse."
    ),
    3: {
        'Celestial Spells': (
            "The magic of your patron ensures you always have certain spells ready; when you reach a Warlock level specified in the Celestial Spells table, you thereafter always have the listed spells prepared.\n\nCelestial Spells\nWarlock Level\tSpells\n3\tAid, Cure Wounds, Guiding Bolt, Lesser Restoration, Light, Sacred Flame\n5\tDaylight, Revivify\n7\tGuardian of Faith, Wall of Fire\n9\tGreater Restoration, Summon Celestial"
        ),
        'Healing Light': (
            "You gain the ability to channel celestial energy to heal wounds. You have a pool of d6s to fuel this healing. The number of dice in the pool equals 1 plus your Warlock level.\n\nAs a Bonus Action, you can heal yourself or one creature you can see within 60 feet of yourself, expending dice from the pool. The maximum number of dice you can expend at once equals your Charisma modifier (minimum of one die). Roll the dice you expend, and restore a number of Hit Points equal to the roll’s total. Your pool regains all expended dice when you finish a Long Rest."
        )
    },
    6: {
        'Radiant Soul': (
            "Your link to your patron allows you to serve as a conduit for radiant energy. You have Resistance to Radiant damage. Once per turn, when a spell you cast deals Radiant or Fire damage, you can add your Charisma modifier to that spell’s damage against one of the spell’s targets."
        )
    },
    10: {
        'Celestial Resilience': (
            "You gain Temporary Hit Points whenever you use your Magical Cunning feature or finish a Short or Long Rest. These Temporary Hit Points equal your Warlock level plus your Charisma modifier. Additionally, choose up to five creatures you can see when you gain the points. Those creatures each gain Temporary Hit Points equal to half your Warlock level plus your Charisma modifier."
        )
    },
    14: {
        'Searing Vengeance': (
            "When you or an ally within 60 feet of you is about to make a Death Saving Throw, you can unleash radiant energy to save the creature. The creature regains Hit Points equal to half its Hit Point maximum and can end the Prone condition on itself. Each creature of your choice that is within 30 feet of the creature takes Radiant damage equal to 2d8 plus your Charisma modifier, and each has the Blinded condition until the end of the current turn.\n\nOnce you use this feature, you can’t use it again until you finish a Long Rest."
        )
    }
}

FIEND_PATRON = {
    'description': (
        "Make a Deal with the Lower Planes\n\n"
        "Your pact draws on the Lower Planes, the realms of perdition. You might forge a bargain with a demon lord such as Demogorgon or Orcus; an archdevil such as Asmodeus; or a pit fiend, balor, yugoloth, or night hag that is especially mighty. That patron’s aims are evil—the corruption or destruction of all things, ultimately including you—and your path is defined by the extent to which you strive against those aims."
    ),
    3: {
        'Dark One’s Blessing': (
            "When you reduce an enemy to 0 Hit Points, you gain Temporary Hit Points equal to your Charisma modifier plus your Warlock level (minimum of 1 Temporary Hit Point). You also gain this benefit if someone else reduces an enemy within 10 feet of you to 0 Hit Points."
        ),
        'Fiend Spells': (
            "The magic of your patron ensures you always have certain spells ready; when you reach a Warlock level specified in the Fiend Spells table, you thereafter always have the listed spells prepared.\n\nFiend Spells\nWarlock Level\tSpells\n3\tBurning Hands, Command, Scorching Ray, Suggestion\n5\tFireball, Stinking Cloud\n7\tFire Shield, Wall of Fire\n9\tGeas, Insect Plague"
        )
    },
    6: {
        'Dark One’s Own Luck': (
            "You can call on your fiendish patron to alter fate in your favor. When you make an ability check or a saving throw, you can use this feature to add 1d10 to your roll. You can do so after seeing the roll but before any of the roll’s effects occur.\n\nYou can use this feature a number of times equal to your Charisma modifier (minimum of once), but you can use it no more than once per roll. You regain all expended uses when you finish a Long Rest."
        )
    },
    10: {
        'Fiendish Resilience': (
            "Choose one damage type, other than Force, whenever you finish a Short or Long Rest. You have Resistance to that damage type until you choose a different one with this feature."
        )
    },
    14: {
        'Hurl Through Hell': (
            "Once per turn when you hit a creature with an attack roll, you can try to instantly transport the target through the Lower Planes. The target must succeed on a Charisma saving throw against your spell save DC, or the target disappears and hurtles through a nightmare landscape. The target takes 8d10 Psychic damage if it isn’t a Fiend, and it has the Incapacitated condition until the end of your next turn, when it returns to the space it previously occupied or the nearest unoccupied space.\n\nOnce you use this feature, you can’t use it again until you finish a Long Rest unless you expend a Pact Magic spell slot (no action required) to restore your use of it."
        )
    }
}

GREAT_OLD_ONE_PATRON = {
    'description': (
        "Unearth Forbidden Lore of Ineffable Beings\n\n"
        "When you choose this subclass, you might bind yourself to an unspeakable being from the Far Realm or an elder god—a being such as Tharizdun, the Chained God; Zargon, the Returner; Hadar, the Dark Hunger; or Great Cthulhu. Or you might invoke several entities without yoking yourself to one. The motives of these beings are incomprehensible, and the Great Old One might be indifferent to your existence. But the secrets you’ve learned nevertheless allow you to draw strange magic from it."
    ),
    3: {
        'Awakened Mind': (
            "You can form a telepathic connection between your mind and the mind of another. As a Bonus Action, choose one creature you can see within 30 feet of yourself. You and the chosen creature can communicate telepathically with each other while the two of you are within a number of miles of each other equal to your Charisma modifier (minimum of 1 mile). To understand each other, you each must mentally use a language the other knows.\n\nThe telepathic connection lasts for a number of minutes equal to your Warlock level. It ends early if you use this feature to connect with a different creature."
        ),
        'Great Old One Spells': (
            "The magic of your patron ensures you always have certain spells ready; when you reach a Warlock level specified in the Great Old One Spells table, you thereafter always have the listed spells prepared.\n\nGreat Old One Spells\nWarlock Level\tSpells\n3\tDetect Thoughts, Dissonant Whispers, Phantasmal Force, Tasha's Hideous Laughter\n5\tClairvoyance, Hunger of Hadar\n7\tConfusion, Summon Aberration\n9\tModify Memory, Telekinesis"
        ),
        'Psychic Spells': (
            "When you cast a Warlock spell that deals damage, you can change its damage type to Psychic. In addition, when you cast a Warlock spell that is an Enchantment or Illusion, you can do so without Verbal or Somatic components."
        )
    },
    6: {
        'Clairvoyant Combatant': (
            "When you form a telepathic bond with a creature using your Awakened Mind, you can force that creature to make a Wisdom saving throw against your spell save DC. On a failed save, the creature has Disadvantage on attack rolls against you, and you have Advantage on attack rolls against that creature for the duration of the bond.\n\nOnce you use this feature, you can’t use it again until you finish a Short or Long Rest unless you expend a Pact Magic spell slot (no action required) to restore your use of it."
        )
    },
    10: {
        'Eldritch Hex': (
            "Your alien patron grants you a powerful curse. You always have the Hex spell prepared. When you cast Hex and choose an ability, the target also has Disadvantage on saving throws of the chosen ability for the duration of the spell."
        ),
        'Thought Shield': (
            "Your thoughts can’t be read by telepathy or other means unless you allow it. You also have Resistance to Psychic damage, and whenever a creature deals Psychic damage to you, that creature takes the same amount of damage that you take."
        )
    },
    14: {
        'Create Thrall': (
            "When you cast Summon Aberration, you can modify it so that it doesn’t require Concentration. If you do so, the spell’s duration becomes 1 minute for that casting, and when summoned, the Aberration has a number of Temporary Hit Points equal to your Warlock level plus your Charisma modifier.\n\nIn addition, the first time each turn the Aberration hits a creature under the effect of your Hex, the Aberration deals extra Psychic damage to the target equal to the bonus damage of that spell."
        )
    }
}
