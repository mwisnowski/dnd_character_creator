"""
Cleric class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

CLERIC_CLASS: Dict[str, Any] = {
    'name': 'Cleric',
    'hit_die': 8,
    'primary_ability': 'Wisdom',
    'saving_throws': ['Wisdom', 'Charisma'],
    'proficiencies': {
        'armor': ['Light Armor', 'Medium Armor', 'Shields'],
        'weapons': ['Simple Weapons'],
        'tools': [],
        'skills': ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion'],
        "skills_choose": 2
    },
    'starting_equipment': [
        ['Chain Shirt', 'Shield', 'Mace', 'Holy Symbol', "Priest's Pack", '7 GP'],
        ['110 GP']
    ]
}

CLERIC_LEVELS: Dict[int, Dict[str, Any]] = {
    1: {
        'features': ['Spellcasting', 'Divine Order'],
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 4,
            'spells_known': 4,
            'spell_slots': {'Level 1': 2}
        }
    },
    2: {
        'features': ['Channel Divinity'],
        'channel_divinity': 2,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 5,
            'spells_known': 5,
            'spell_slots': {'Level 1': 3}
        }
    },
    3: {
        'features': ['Cleric Subclass'],
        'channel_divinity': 2,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 6,
            'spells_known': 6,
            'spell_slots': {'Level 1': 4, 'Level 2': 2}
        }
    },
    4: {
        'features': ['Ability Score Improvement'],
        'channel_divinity': 2,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 7,
            'spells_known': 7,
            'spell_slots': {'Level 1': 4, 'Level 2': 3}
        }
    },
    5: {
        'features': ['Sear Undead'],
        'channel_divinity': 2,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 9,
            'spells_known': 9,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 2}
        }
    },
    6: {
        'features': ['Subclass Feature'],
        'channel_divinity': 3,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 10,
            'spells_known': 10,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3}
        }
    },
    7: {
        'features': ['Blessed Strikes'],
        'channel_divinity': 3,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 11,
            'spells_known': 11,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 1}
        }
    },
    8: {
        'features': ['Ability Score Improvement'],
        'channel_divinity': 3,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 12,
            'spells_known': 12,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 2}
        }
    },
    9: {
        'features': [],
        'channel_divinity': 3,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 14,
            'spells_known': 14,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 1}
        }
    },
    10: {
        'features': ['Divine Intervention'],
        'channel_divinity': 3,
        'spellcasting': {
            'cantrips_known': 5,
            'spells_prepared': 15,
            'spells_known': 15,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2}
        }
    },
    11: {
        'features': [],
        'channel_divinity': 3,
        'spellcasting': {
            'cantrips_known': 5,
            'spells_prepared': 16,
            'spells_known': 16,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1}
        }
    },
    12: {
        'features': ['Ability Score Improvement'],
        'channel_divinity': 3,
        'spellcasting': {
            'cantrips_known': 5,
            'spells_prepared': 16,
            'spells_known': 16,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1}
        }
    },
    13: {
        'features': [],
        'channel_divinity': 3,
        'spellcasting': {
            'cantrips_known': 5,
            'spells_prepared': 17,
            'spells_known': 17,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1}
        }
    },
    14: {
        'features': ['Improved Blessed Strikes'],
        'channel_divinity': 3,
        'spellcasting': {
            'cantrips_known': 5,
            'spells_prepared': 17,
            'spells_known': 17,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1}
        }
    },
    15: {
        'features': [],
        'channel_divinity': 3,
        'spellcasting': {
            'cantrips_known': 5,
            'spells_prepared': 18,
            'spells_known': 18,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1, 'Level 8': 1}
        }
    },
    16: {
        'features': ['Ability Score Improvement'],
        'channel_divinity': 3,
        'spellcasting': {
            'cantrips_known': 5,
            'spells_prepared': 18,
            'spells_known': 18,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1, 'Level 8': 1}
        }
    },
    17: {
        'features': ['Subclass Feature'],
        'channel_divinity': 3,
        'spellcasting': {
            'cantrips_known': 5,
            'spells_prepared': 19,
            'spells_known': 19,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1, 'Level 8': 1, 'Level 9': 1}
        }
    },
    18: {
        'features': [],
        'channel_divinity': 4,
        'spellcasting': {
            'cantrips_known': 5,
            'spells_prepared': 20,
            'spells_known': 20,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 3, 'Level 7': 1, 'Level 8': 1, 'Level 9': 1}
        }
    },
    19: {
        'features': ['Epic Boon'],
        'channel_divinity': 4,
        'spellcasting': {
            'cantrips_known': 5,
            'spells_prepared': 21,
            'spells_known': 21,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 3, 'Level 7': 2, 'Level 8': 1, 'Level 9': 1}
        }
    },
    20: {
        'features': ['Greater Divine Intervention'],
        'channel_divinity': 4,
        'spellcasting': {
            'cantrips_known': 5,
            'spells_prepared': 22,
            'spells_known': 22,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 3, 'Level 7': 2, 'Level 8': 2, 'Level 9': 1}
        }
    },
}

CLERIC_FEATURES: Dict[str, Any] = {
    'Spellcasting': (
        "You have learned to cast spells through prayer and meditation. See chapter 7 for the rules on spellcasting. "
        "The information below details how you use those rules with Cleric spells, which appear on the Cleric spell list later in the class's description.\n\n"
        "  - Cantrips. You know three cantrips of your choice from the Cleric spell list. Guidance, Sacred Flame, and Thaumaturgy are recommended.\n"
        "    Whenever you gain a Cleric level, you can replace one of your cantrips with another cantrip of your choice from the Cleric spell list.\n"
        "    When you reach Cleric levels 4 and 10, you learn another cantrip of your choice from the Cleric spell list, as shown in the Cantrips column of the "
        "Cleric Features table.\n\n"
        "  - Spell Slots. The Cleric Features table shows how many spell slots you have to cast your level 1+ spells. You regain all expended slots when you "
        "finish a Long Rest.\n\n"
        "  - Prepared Spells of Level 1+. You prepare the list of level 1+ spells that are available for you to cast with this feature. To start, choose four level "
        "1 spells from the Cleric spell list. Bless, Cure Wounds, Guiding Bolt, and Shield of Faith are recommended.\n"
        "    The number of spells on your list increases as you gain Cleric levels, as shown in the Prepared Spells column of the Cleric Features table. Whenever "
        "that number increases, choose additional spells from the Cleric spell list until the number of spells on your list matches the number on the table. The "
        "chosen spells must be of a level for which you have spell slots. For example, if you're a level 3 Cleric, your list of prepared spells can include six "
        "spells of levels 1 and 2 in any combination.\n"
        "    If another Cleric feature gives you spells that you always have prepared, those spells don't count against the number of spells you can prepare with "
        "this feature, but those spells otherwise count as Cleric spells for you.\n\n"
        "  - Changing Your Prepared Spells. Whenever you finish a Long Rest, you can change your list of prepared spells, replacing any of the spells there with "
        "other Cleric spells for which you have spell slots.\n\n"
        "  - Spellcasting Ability. Wisdom is your spellcasting ability for your Cleric spells.\n\n"
        "  - Spellcasting Focus. You can use a Holy Symbol as a Spellcasting Focus for your Cleric spells."
    ),
    'Divine Order': (
        "You have dedicated yourself to one of the following sacred roles of your choice.\n\n"
        "  - Protector. Trained for battle, you gain proficiency with Martial weapons and training with Heavy armor.\n\n"
        "  - Thaumaturge. You know one extra cantrip from the Cleric spell list. In addition, your mystical connection to the divine gives you a bonus to your "
        "Intelligence (Arcana or Religion) checks. The bonus equals your Wisdom modifier (minimum of +1)."
    ),
    'Channel Divinity': (
        "You can channel divine energy directly from the Outer Planes to fuel magical effects. You start with two such effects: Divine Spark and Turn Undead, each "
        "of which is described below. Each time you use this class's Channel Divinity, choose which Channel Divinity effect from this class to create. You gain "
        "additional effect options at higher Cleric levels.\n\n"
        "You can use this class's Channel Divinity twice. You regain one of its expended uses when you finish a Short Rest, and you regain all expended uses when you "
        "finish a Long Rest. You gain additional uses when you reach certain Cleric levels, as shown in the Channel Divinity column of the Cleric Features table.\n\n"
        "If a Channel Divinity effect requires a saving throw, the DC equals the spell save DC from this class's Spellcasting feature.\n\n"
        "  - Divine Spark. As a Magic action, you point your Holy Symbol at another creature you can see within 30 feet of yourself and focus divine energy at it. "
        "Roll 1d8 and add your Wisdom modifier. You either restore Hit Points to the creature equal to that total or force the creature to make a Constitution saving "
        "throw. On a failed save, the creature takes Necrotic or Radiant damage (your choice) equal to that total. On a successful save, the creature takes half as "
        "much damage (round down).\n\n"
        "    You roll an additional d8 when you reach Cleric levels 7 (2d8), 13 (3d8), and 18 (4d8).\n\n"
        "  - Turn Undead. As a Magic action, you present your Holy Symbol and censure Undead creatures. Each Undead of your choice within 30 feet of you must make a "
        "Wisdom saving throw. If the creature fails its save, it has the Frightened and Incapacitated conditions for 1 minute. For that duration, it tries to move as "
        "far from you as it can on its turns. This effect ends early on the creature if it takes any damage, if you have the Incapacitated condition, or if you die."
    ),
    'Cleric Subclass': (
        "You gain a Cleric subclass of your choice. The Life Domain, Light Domain, Trickery Domain, and War Domain subclasses are detailed after this class's "
        "description. A subclass is a specialization that grants you features at certain Cleric levels. For the rest of your career, you gain each of your subclass's "
        "features that are of your Cleric level or lower."
    ),
    'Ability Score Improvement': (
        "You gain the Ability Score Improvement feat or another feat of your choice for which you qualify. You gain this feature again at Cleric levels 8, 12, and 16."
    ),
    'Sear Undead': (
        "Whenever you use Turn Undead, you can roll a number of d8s equal to your Wisdom modifier (minimum of 1d8) and add the rolls together. Each Undead that fails "
        "its saving throw against that use of Turn Undead takes Radiant damage equal to the roll's total. This damage doesn't end the turn effect."
    ),
    'Blessed Strikes': (
        "Divine power infuses you in battle. You gain one of the following options of your choice (if you get either option from a Cleric subclass in an older book, "
        "use only the option you choose for this feature).\n\n"
        "  - Divine Strike. Once on each of your turns when you hit a creature with an attack roll using a weapon, you can cause the target to take an extra 1d8 "
        "Necrotic or Radiant damage (your choice).\n\n"
        "  - Potent Spellcasting. Add your Wisdom modifier to the damage you deal with any Cleric cantrip."
    ),
    'Divine Intervention': (
        "You can call on your deity or pantheon to intervene on your behalf. As a Magic action, choose any Cleric spell of level 5 or lower that doesn't require a "
        "Reaction to cast. As part of the same action, you cast that spell without expending a spell slot or needing Material components. You can't use this feature "
        "again until you finish a Long Rest."
    ),
    'Improved Blessed Strikes': (
        "The option you chose for Blessed Strikes grows more powerful.\n\n"
        "  - Divine Strike. The extra damage of your Divine Strike increases to 2d8.\n\n"
        "  - Potent Spellcasting. When you cast a Cleric cantrip and deal damage to a creature with it, you can give vitality to yourself or another creature within "
        "60 feet of yourself, granting a number of Temporary Hit Points equal to twice your Wisdom modifier."
    ),
    'Epic Boon': (
        "You gain an Epic Boon feat or another feat of your choice for which you qualify. Boon of Fate is recommended."
    ),
    'Greater Divine Intervention': (
        "You can call on even more powerful divine intervention. When you use your Divine Intervention feature, you can choose Wish when you select a spell. If you do "
        "so, you can't use Divine Intervention again until you finish 2d4 Long Rests."
    ),
}

LIFE_DOMAIN: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        "Soothe the Hurts of the World\n\n"
        "The Life Domain focuses on the positive energy that helps sustain all life in the multiverse. Clerics who tap into this domain are masters of healing, using that life force to cure many hurts.\n\n"
        "Existence itself relies on the positive energy associated with this domain, so a Cleric of almost any religious tradition might choose it. This domain is particularly associated with agricultural deities, gods of healing or endurance, and gods of home and community. Religious orders of healing also seek the magic of this domain."
    ),
    3: {
        'Disciple of Life': (
            "When a spell you cast with a spell slot restores Hit Points to a creature, that creature regains additional Hit Points on the turn you cast the spell. The additional Hit Points equal 2 plus the spell slot's level."
        ),
        'Life Domain Spells': (
            "Your connection to this divine domain ensures you always have certain spells ready. When you reach a Cleric level specified in the Life Domain Spells table, you thereafter always have the listed spells prepared.\n\n"
            "Life Domain Spells\nCleric Level  Prepared Spells\n3  Aid, Bless, Cure Wounds, Lesser Restoration\n5  Mass Healing Word, Revivify\n7  Aura of Life, Death Ward\n9  Greater Restoration, Mass Cure Wounds"
        ),
        'Preserve Life': (
            "As a Magic action, you present your Holy Symbol and expend a use of your Channel Divinity to evoke healing energy that can restore a number of Hit Points equal to five times your Cleric level. Choose Bloodied creatures within 30 feet of yourself (which can include you), and divide those Hit Points among them. This feature can restore a creature to no more than half its Hit Point maximum."
        )
    },
    6: {
        'Blessed Healer': (
            "The healing spells you cast on others heal you as well. Immediately after you cast a spell with a spell slot that restores Hit Points to one or more creatures other than yourself, you regain Hit Points equal to 2 plus the spell slot's level."
        )
    },
    17: {
        'Supreme Healing': (
            "When you would normally roll one or more dice to restore Hit Points to a creature with a spell or Channel Divinity, don't roll those dice for the healing; instead use the highest number possible for each die. For example, instead of restoring 2d6 Hit Points to a creature with a spell, you restore 12."
        )
    }
}

LIGHT_DOMAIN: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        "Bring Light to Banish Darkness\n\n"
        "The Light Domain emphasizes the divine power to bring about blazing fire and revelation. Clerics who wield this power are enlightened souls infused with radiance and the power of their deities' discerning vision, charged with chasing away lies and burning away darkness.\n\n"
        "The Light Domain is associated with gods of truth, vigilance, beauty, insight, and renewal. Some of these gods are identified with the sun or as charioteers who guide the sun across the sky. Others are sentinels who pierce deception. Some are deities of beauty and artistry who teach that art is a vehicle for the soul's improvement."
    ),
    3: {
        'Light Domain Spells': (
            "Your connection to this divine domain ensures you always have certain spells ready. When you reach a Cleric level specified in the Light Domain Spells table, you thereafter always have the listed spells prepared.\n\n"
            "Light Domain Spells\nCleric Level  Prepared Spells\n3  Burning Hands, Faerie Fire, Scorching Ray, See Invisibility\n5  Daylight, Fireball\n7  Arcane Eye, Wall of Fire\n9  Flame Strike, Scrying"
        ),
        'Radiance of the Dawn': (
            "As a Magic action, you present your Holy Symbol and expend a use of your Channel Divinity to emit a flash of light in a 30-foot Emanation originating from yourself. Any magical Darkness—such as that created by the Darkness spell—in that area is dispelled. Additionally, each creature of your choice in that area must make a Constitution saving throw, taking Radiant damage equal to 2d10 plus your Cleric level on a failed save or half as much damage on a successful one."
        ),
        'Warding Flare': (
            "When a creature that you can see within 30 feet of yourself makes an attack roll, you can take a Reaction to impose Disadvantage on the attack roll, causing light to flare before it hits or misses.\n\nYou can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you finish a Long Rest."
        )
    },
    6: {
        'Improved Warding Flare': (
            "You regain all expended uses of your Warding Flare when you finish a Short or Long Rest.\n\nIn addition, whenever you use Warding Flare, you can give the target of the triggering attack a number of Temporary Hit Points equal to 2d6 plus your Wisdom modifier."
        )
    },
    17: {
        'Corona of Light': (
            "As a Magic action, you cause yourself to emit an aura of sunlight that lasts for 1 minute or until you dismiss it (no action required). You emit Bright Light in a 60-foot radius and Dim Light for an additional 30 feet. Your enemies in the Bright Light have Disadvantage on saving throws against your Radiance of the Dawn and any spell that deals Fire or Radiant damage.\n\nYou can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."
        )
    }
}

TRICKSTER_DOMAIN: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        "Make Mischief and Challenge Authority\n\n"
        "The Trickery Domain offers magic of deception, illusion, and stealth. Clerics who wield this magic are a disruptive force in the world, puncturing pride, mocking tyrants, freeing captives, and flouting hollow traditions. They prefer subterfuge and pranks to direct confrontation.\n\n"
        "Gods of trickery are mischief-makers and instigators who stand as a constant challenge to the accepted order among both gods and mortals. They embody the forces of change and social upheaval, and they're patrons of thieves, scoundrels, gamblers, rebels, and liberators. Religious orders that operate in secret, especially those that seek to undermine oppressive governments or hierarchies, also draw on the power of the Trickery Domain."
    ),
    3: {
        'Blessing of the Trickster': (
            "As a Magic action, you can choose yourself or a willing creature within 30 feet of yourself to have Advantage on Dexterity (Stealth) checks. This blessing lasts until you finish a Long Rest or you use this feature again."
        ),
        'Trickery Domain Spells': (
            "Your connection to this divine domain ensures you always have certain spells ready. When you reach a Cleric level specified in the Trickery Domain Spells table, you thereafter always have the listed spells prepared.\n\n"
            "Trickery Domain Spells\nCleric Level  Prepared Spells\n3  Charm Person, Disguise Self, Invisibility, Pass without Trace\n5  Hypnotic Pattern, Nondetection\n7  Confusion, Dimension Door\n9  Dominate Person, Modify Memory"
        ),
        'Invoke Duplicity': (
            "As a Bonus Action, you can expend one use of your Channel Divinity to create a perfect visual illusion of yourself in an unoccupied space you can see within 30 feet of yourself. The illusion is intangible and doesn't occupy its space. It lasts for 1 minute, but it ends early if you dismiss it (no action required) or have the Incapacitated condition. The illusion is animated and mimics your expressions and gestures. While it persists, you gain the following benefits.\n\n"
            "Cast Spells. You can cast spells as though you were in the illusion's space, but you must use your own senses.\n\n"
            "Distract. When both you and your illusion are within 5 feet of a creature that can see the illusion, you have Advantage on attack rolls against that creature, given how distracting the illusion is to the target.\n\n"
            "Move. As a Bonus Action, you can move the illusion up to 30 feet to an unoccupied space you can see that is within 120 feet of yourself."
        )
    },
    6: {
        "Trickster's Transposition": (
            "Whenever you take the Bonus Action to create or move the illusion of your Invoke Duplicity, you can teleport, swapping places with the illusion."
        )
    },
    17: {
        "Improved Duplicity": (
            "The illusion of your Invoke Duplicity has grown more powerful in the following ways.\n\n"
            "Shared Distraction. When you and your allies make attack rolls against a creature within 5 feet of the illusion, the attack rolls have Advantage.\n\n"
            "Healing Illusion. When the illusion is present, you and your allies within 10 feet of it regain 1d6 hit points at the start of your turns."
        )
    }
}

WAR_DOMAIN: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        "Inspire Valor and Smite Foes\n\n"
        "War has many manifestations. It can make heroes of ordinary people. It can be desperate and horrific, with acts of cruelty and cowardice eclipsing instances of excellence and courage. Clerics who tap into the magic of the War Domain excel in battle, inspiring others to fight the good fight or offering acts of violence as prayers.\n\n"
        "Gods of the War Domain watch over warriors and reward them for their great deeds. They include champions of honor and chivalry as well as gods of destruction and pillage. Other war gods take a more neutral stance, promoting war in all its manifestations and supporting warriors in any circumstance."
    ),
    3: {
        'Guided Strike': (
            "When you or a creature within 30 feet of you misses with an attack roll, you can expend one use of your Channel Divinity and give that roll a +10 bonus, potentially causing it to hit. When you use this feature to benefit another creature's attack roll, you must take a Reaction to do so."
        ),
        'War Domain Spells': (
            "Your connection to this divine domain ensures you always have certain spells ready. When you reach a Cleric level specified in the War Domain Spells table, you thereafter always have the listed spells prepared.\n\n"
            "War Domain Spells\nCleric Level\tPrepared Spells\n3\tGuiding Bolt, Magic Weapon, Shield of Faith, Spiritual Weapon\n5\tCrusader's Mantle, Spirit Guardians\n7\tFire Shield, Freedom of Movement\n9\tHold Monster, Steel Wind Strike"
        ),
        'War Priest': (
            "As a Bonus Action, you can make one attack with a weapon or an Unarmed Strike. You can use this Bonus Action a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you finish a Short or Long Rest."
        )
    },
    6: {
        "War God's Blessing": (
            "You can expend a use of your Channel Divinity to cast Shield of Faith or Spiritual Weapon rather than expending a spell slot. When you cast either spell in this way, the spell doesn't require Concentration. Instead the spell lasts for 1 minute, but it ends early if you cast that spell again, have the Incapacitated condition, or die."
        )
    },
    17: {
        "Avatar of Battle": (
            "You gain Resistance to Bludgeoning, Piercing, and Slashing damage."
        )
    }
}
