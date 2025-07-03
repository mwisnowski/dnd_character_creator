"""
Druid class data for D&D character creator.
Contains class definition, level progression, features, wild shape table, and subclasses.
"""

from __future__ import annotations

from typing import Any, Dict, List, Union

DRUID_CLASS: Dict[str, Any] = {
    'name': 'Druid',
    'hit_die': 8,
    'primary_ability': 'Wisdom',
    'saving_throws': ['Intelligence', 'Wisdom'],
    'proficiencies': {
        'armor': ['Light Armor', 'Shields'],
        'weapons': ['Simple Weapons'],
        'tools': ['Herbalism Kit'],
        'skills': [
            'Arcana', 'Animal Handling', 'Insight', 'Medicine',
            'Nature', 'Perception', 'Religion', 'Survival',
        ],
    },
    'starting_equipment': [
        [
            'Leather Armor', 'Shield', 'Sickle', 'Quarterstaff',
            'Druidic Focus (Quarterstaff)', "Explorer's Pack", 'Herbalism Kit', '9 GP',
        ],
        ['50 GP'],
    ],
}

DRUID_LEVELS: Dict[int, Dict[str, Any]] = {
    1: {
        'proficiency_bonus': 2,
        'features': ['Spellcasting', 'Druidic', 'Primal Order'],
        'wild_shape': None,
        'spellcasting': {
            'cantrips_known': 2,
            'spells_prepared': 4,
            'spells_known': 4,
            'spell_slots': {'Level 1': 2},
        },
    },
    2: {
        'proficiency_bonus': 2,
        'features': ['Wild Shape', 'Wild Companion'],
        'wild_shape': 2,
        'spellcasting': {
            'cantrips_known': 2,
            'spells_prepared': 5,
            'spells_known': 5,
            'spell_slots': {'Level 1': 3},
        },
    },
    3: {
        'proficiency_bonus': 2,
        'features': ['Druid Subclass'],
        'wild_shape': 2,
        'spellcasting': {
            'cantrips_known': 2,
            'spells_prepared': 6,
            'spells_known': 6,
            'spell_slots': {'Level 1': 4, 'Level 2': 2},
        },
    },
    4: {
        'proficiency_bonus': 2,
        'features': ['Ability Score Improvement'],
        'wild_shape': 2,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 7,
            'spells_known': 7,
            'spell_slots': {'Level 1': 4, 'Level 2': 3},
        },
    },
    5: {
        'proficiency_bonus': 3,
        'features': ['Wild Resurgence'],
        'wild_shape': 2,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 9,
            'spells_known': 9,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 2},
        },
    },
    6: {
        'proficiency_bonus': 3,
        'features': ['Subclass Feature'],
        'wild_shape': 3,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 10,
            'spells_known': 10,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3},
        },
    },
    7: {
        'proficiency_bonus': 3,
        'features': ['Elemental Fury'],
        'wild_shape': 3,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 11,
            'spells_known': 11,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 1},
        },
    },
    8: {
        'proficiency_bonus': 3,
        'features': ['Ability Score Improvement'],
        'wild_shape': 3,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 12,
            'spells_known': 12,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 2},
        },
    },
    9: {
        'proficiency_bonus': 4,
        'features': [],
        'wild_shape': 3,
        'spellcasting': {
            'cantrips_known': 3,
            'spells_prepared': 14,
            'spells_known': 14,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 1},
        },
    },
    10: {
        'proficiency_bonus': 4,
        'features': ['Subclass Feature'],
        'wild_shape': 3,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 15,
            'spells_known': 15,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2},
        },
    },
    11: {
        'proficiency_bonus': 4,
        'features': [],
        'wild_shape': 3,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 16,
            'spells_known': 16,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1},
        },
    },
    12: {
        'proficiency_bonus': 4,
        'features': ['Ability Score Improvement'],
        'wild_shape': 3,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 16,
            'spells_known': 16,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1},
        },
    },
    13: {
        'proficiency_bonus': 5,
        'features': [],
        'wild_shape': 3,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 17,
            'spells_known': 17,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1},
        },
    },
    14: {
        'proficiency_bonus': 5,
        'features': ['Subclass Feature'],
        'wild_shape': 3,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 17,
            'spells_known': 17,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1},
        },
    },
    15: {
        'proficiency_bonus': 5,
        'features': ['Improved Elemental Fury'],
        'wild_shape': 3,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 18,
            'spells_known': 18,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1, 'Level 8': 1},
        },
    },
    16: {
        'proficiency_bonus': 5,
        'features': ['Ability Score Improvement'],
        'wild_shape': 3,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 18,
            'spells_known': 18,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1, 'Level 8': 1},
        },
    },
    17: {
        'proficiency_bonus': 6,
        'features': [],
        'wild_shape': 4,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 19,
            'spells_known': 19,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 2, 'Level 6': 1, 'Level 7': 1, 'Level 8': 1, 'Level 9': 1},
        },
    },
    18: {
        'proficiency_bonus': 6,
        'features': ['Beast Spells'],
        'wild_shape': 4,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 20,
            'spells_known': 20,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 3, 'Level 6': 1, 'Level 7': 1, 'Level 8': 1, 'Level 9': 1},
        },
    },
    19: {
        'proficiency_bonus': 6,
        'features': ['Epic Boon'],
        'wild_shape': 4,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 21,
            'spells_known': 21,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 3, 'Level 6': 2, 'Level 7': 1, 'Level 8': 1, 'Level 9': 1},
        },
    },
    20: {
        'proficiency_bonus': 6,
        'features': ['Archdruid'],
        'wild_shape': 4,
        'spellcasting': {
            'cantrips_known': 4,
            'spells_prepared': 22,
            'spells_known': 22,
            'spell_slots': {'Level 1': 4, 'Level 2': 3, 'Level 3': 3, 'Level 4': 3, 'Level 5': 3, 'Level 6': 2, 'Level 7': 2, 'Level 8': 1, 'Level 9': 1},
        },
    },
}

WILD_SHAPE: Dict[int, Dict[str, Union[int, str, bool]]] = {
    2: {
        'known_forms': 4,
        'max_cr': '1/4',
        'fly_speed': False,
    },
    4: {
        'known_forms': 6,
        'max_cr': '1/2',
        'fly_speed': False,
    },
    8: {
        'known_forms': 8,
        'max_cr': '1',
        'fly_speed': True,
    },
}

DRUID_FEATURES: Dict[str, Union[str, List[Union[str, Dict[int, Dict[str, Union[int, str, bool]]]]]]] = {
    'Spellcasting': (
        "You have learned to cast spells through studying the mystical forces of nature. See chapter 7 for the rules on spellcasting. The information below details how you use those rules with Druid spells, which appear on the Druid spell list later in the class's description.\n\n"
        "  - Cantrips. You know two cantrips of your choice from the Druid spell list. Druidcraft and Produce Flame are recommended.\n"
        "    Whenever you gain a Druid level, you can replace one of your cantrips with another cantrip of your choice from the Druid spell list.\n"
        "    When you reach Druid levels 4 and 10, you learn another cantrip of your choice from the Druid spell list, as shown in the Cantrips column of the Druid Features table.\n\n"
        "  - Spell Slots. The Druid Features table shows how many spell slots you have to cast your level 1+ spells. You regain all expended slots when you finish a Long Rest.\n\n"
        "  - Prepared Spells of Level 1+. You prepare the list of level 1+ spells that are available for you to cast with this feature. To start, choose four level 1 spells from the Druid spell list. Animal Friendship, Cure Wounds, Faerie Fire, and Thunderwave are recommended.\n"
        "    The number of spells on your list increases as you gain Druid levels, as shown in the Prepared Spells column of the Druid Features table. Whenever that number increases, choose additional spells from the Druid spell list until the number of spells on your list matches the number on the table. The chosen spells must be of a level for which you have spell slots. For example, if you're a level 3 Druid, your list of prepared spells can include six spells of levels 1 and 2 in any combination.\n"
        "    If another Druid feature gives you spells that you always have prepared, those spells don't count against the number of spells you can prepare with this feature, but those spells otherwise count as Druid spells for you.\n\n"
        "  - Changing Your Prepared Spells. Whenever you finish a Long Rest, you can change your list of prepared spells, replacing any of the spells with other Druid spells for which you have spell slots.\n\n"
        "  - Spellcasting Ability. Wisdom is your spellcasting ability for your Druid spells.\n\n"
        "  - Spellcasting Focus. You can use a Druidic Focus as a Spellcasting Focus for your Druid spells."
    ),
    'Druidic': (
        "You know Druidic, the secret language of Druids. While learning this ancient tongue, you also unlocked the magic of communicating with animals; you always have the Speak with Animals spell prepared.\n\n"
        "You can use Druidic to leave hidden messages. You and others who know Druidic automatically spot such a message. Others spot the message's presence with a successful DC 15 Intelligence (Investigation) check but can't decipher it without magic."
    ),
    'Primal Order': (
        "You have dedicated yourself to one of the following sacred roles of your choice.\n\n"
        "  - Magician. You know one extra cantrip from the Druid spell list. In addition, your mystical connection to nature gives you a bonus to your Intelligence (Arcana or Nature) checks. The bonus equals your Wisdom modifier (minimum bonus of +1).\n\n"
        "  - Warden. Trained for battle, you gain proficiency with Martial weapons and training with Medium armor."
    ),
    'Wild Shape': [
        "The power of nature allows you to assume the form of an animal. As a Bonus Action, you shape-shift into a Beast form that you have learned for this feature (see 'Known Forms' below). You stay in that form for a number of hours equal to half your Druid level or until you use Wild Shape again, have the Incapacitated condition, or die. You can also leave the form early as a Bonus Action.\n\n"
        "  - Number of Uses. You can use Wild Shape twice. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.\n"
        "    You gain additional uses when you reach certain Druid levels, as shown in the Wild Shape column of the Druid Features table.\n\n"
        "  - Known Forms. You know four Beast forms for this feature, chosen from among Beast stat blocks that have a maximum Challenge Rating of 1/4 and that lack a Fly Speed (see appendix B for stat block options). The Rat, Riding Horse, Spider, and Wolf are recommended. Whenever you finish a Long Rest, you can replace one of your known forms with another eligible form.\n"
        "    When you reach certain Druid levels, your number of known forms and the maximum Challenge Rating for those forms increases, as shown in the Beast Shapes table. In addition, starting at level 8, you can adopt a form that has a Fly Speed.\n\n"
        "  - Rules While Shape-Shifted. While in a form, you retain your personality, memories, and ability to speak, and the following rules apply:\n"
        "    * Temporary Hit Points. When you assume a Wild Shape form, you gain a number of Temporary Hit Points equal to your Druid level.\n"
        "    * Game Statistics. Your game statistics are replaced by the Beast's stat block, but you retain your creature type; Hit Points; Hit Point Dice; Intelligence, Wisdom, and Charisma scores; class features; languages; and feats. You also retain your skill and saving throw proficiencies and use your Proficiency Bonus for them, in addition to gaining the proficiencies of the creature. If a skill or saving throw modifier in the Beast's stat block is higher than yours, use the one in the stat block.\n"
        "    * No Spellcasting. You can't cast spells, but shape-shifting doesn't break your Concentration or otherwise interfere with a spell you've already cast.\n"
        "    * Objects. Your ability to handle objects is determined by the form's limbs rather than your own. In addition, you choose whether your equipment falls in your space, merges into your new form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it's practical for the new form to wear a piece of equipment based on the creature's size and shape. Your equipment doesn't change size or shape to match the new form, and any equipment that the new form can't wear must either fall to the ground or merge with the form. Equipment that merges with the form has no effect while you're in that form.",
        WILD_SHAPE
    ],
    'Wild Companion': (
        "You can summon a nature spirit that assumes an animal form to aid you. As a Magic action, you can expend a spell slot or a use of Wild Shape to cast the Find Familiar spell without Material components.\n\n"
        "When you cast the spell in this way, the familiar is Fey and disappears when you finish a Long Rest."
    ),
    'Druid Subclass': (
        "You gain a Druid subclass of your choice. The Circle of the Land, Circle of the Moon, Circle of the Sea, and Circle of the Stars subclasses are detailed after this class's description. A subclass is a specialization that grants you features at certain Druid levels. For the rest of your career, you gain each of your subclass's features that are of your Druid level or lower."
    ),
    'Ability Score Improvement': (
        "You gain the Ability Score Improvement feat or another feat of your choice for which you qualify. You gain this feature again at Druid levels 8, 12, and 16."
    ),
    'Wild Resurgence': (
        "Once on each of your turns, if you have no uses of Wild Shape left, you can give yourself one use by expending a spell slot (no action required).\n\n"
        "In addition, you can expend one use of Wild Shape (no action required) to give yourself a level 1 spell slot, but you can't do so again until you finish a Long Rest."
    ),
    'Elemental Fury': (
        "The might of the elements flows through you. You gain one of the following options of your choice.\n\n"
        "  - Potent Spellcasting. Add your Wisdom modifier to the damage you deal with any Druid cantrip.\n\n"
        "  - Primal Strike. Once on each of your turns when you hit a creature with an attack roll using a weapon or a Beast form's attack in Wild Shape, you can cause the target to take an extra 1d8 Cold, Fire, Lightning, or Thunder damage (choose when you hit)."
    ),
    'Improved Elemental Fury': (
        "The option you chose for Elemental Fury grows more powerful, as detailed below.\n\n"
        "  - Potent Spellcasting. When you cast a Druid cantrip with a range of 10 feet or greater, the spell's range increases by 300 feet.\n\n"
        "  - Primal Strike. The extra damage of your Primal Strike increases to 2d8."
    ),
    'Beast Spells': (
        "While using Wild Shape, you can cast spells in Beast form, except for any spell that has a Material component with a cost specified or that consumes its Material component."
    ),
    'Epic Boon': (
        "You gain an Epic Boon feat or another feat of your choice for which you qualify. Boon of Dimensional Travel is recommended."
    ),
    'Archdruid': (
        "The vitality of nature constantly blooms within you, granting you the following benefits.\n\n"
        "  - Evergreen Wild Shape. Whenever you roll Initiative and have no uses of Wild Shape left, you regain one expended use of it.\n\n"
        "  - Nature Magician. You can convert uses of Wild Shape into a spell slot (no action required). Choose a number of your unexpended uses of Wild Shape and convert them into a single spell slot, with each use contributing 2 spell levels. For example, if you convert two uses of Wild Shape, you produce a level 4 spell slot. Once you use this benefit, you can't do so again until you finish a Long Rest.\n\n"
        "  - Longevity. The primal magic that you wield causes you to age more slowly. For every ten years that pass, your body ages only one year."
    ),
}

CIRCLE_OF_THE_LAND: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        "Celebrate Connection to the Natural World\n\n"
        "The Circle of the Land comprises mystics and sages who safeguard ancient knowledge and rites. These Druids meet within sacred circles of trees or standing stones to whisper primal secrets in Druidic. The circle’s wisest members preside as the chief priests of their communities."
    ),
    3: {
        'Circle of the Land Spells': (
            "Whenever you finish a Long Rest, choose one type of land: arid, polar, temperate, or tropical. Consult the table below that corresponds to the chosen type; you have the spells listed for your Druid level and lower prepared.\n\n"
            "Arid Land\n3: Blur, Burning Hands, Fire Bolt\n5: Fireball\n7: Blight\n9: Wall of Stone\n\n"
            "Polar Land\n3: Fog Cloud, Hold Person, Ray of Frost\n5: Sleet Storm\n7: Ice Storm\n9: Cone of Cold\n\n"
            "Temperate Land\n3: Misty Step, Shocking Grasp, Sleep\n5: Lightning Bolt\n7: Freedom of Movement\n9: Tree Stride\n\n"
            "Tropical Land\n3: Acid Splash, Ray of Sickness, Web\n5: Stinking Cloud\n7: Polymorph\n9: Insect Plague"
        ),
        "Land's Aid": (
            "As a Magic action, you can expend a use of your Wild Shape and choose a point within 60 feet of yourself. Vitality-giving flowers and life-draining thorns appear for a moment in a 10-foot-radius Sphere centered on that point. Each creature of your choice in the Sphere must make a Constitution saving throw against your spell save DC, taking 2d6 Necrotic damage on a failed save or half as much damage on a successful one. One creature of your choice in that area regains 2d6 Hit Points.\n\nThe damage and healing increase by 1d6 when you reach Druid levels 10 (3d6) and 14 (4d6)."
        ),
    },
    6: {
        'Natural Recovery': (
            "You can cast one of the level 1+ spells that you have prepared from your Circle Spells feature without expending a spell slot, and you must finish a Long Rest before you do so again.\n\n"
            "In addition, when you finish a Short Rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your Druid level (round up), and none of them can be level 6+. For example, if you’re a level 6 Druid, you can recover up to three levels’ worth of spell slots. You can recover a level 3 spell slot, a level 2 and a level 1 spell slot, or three level 1 spell slots. Once you recover spell slots with this feature, you can’t do so again until you finish a Long Rest."
        ),
    },
    10: {
        "Nature's Ward": (
            "You are immune to the Poisoned condition, and you have Resistance to a damage type associated with your current land choice in the Circle Spells feature, as shown in the Nature’s Ward table.\n\nArid: Fire\nPolar: Cold\nTemperate: Lightning\nTropical: Poison"
        ),
    },
    14: {
        "Nature's Sanctuary": (
            "As a Magic action, you can expend a use of your Wild Shape and cause spectral trees and vines to appear in a 15-foot Cube on the ground within 120 feet of yourself. They last there for 1 minute or until you have the Incapacitated condition or die. You and your allies have Half Cover while in that area, and your allies gain the current Resistance of your Nature’s Ward while there.\n\nAs a Bonus Action, you can move the Cube up to 60 feet to ground within 120 feet of yourself."
        ),
    },
}

CIRCLE_OF_THE_MOON: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        "Adopt Animal Forms to Guard the Wilds\n\n"
        "Druids of the Circle of the Moon draw on lunar magic to transform themselves. Their order gathers under the moon to share news and perform rituals.\n\nChangeable as the moon, a Druid of this circle might prowl as a great cat one night, soar over the treetops as an eagle the next day, and then crash through undergrowth as a bear to drive off a trespassing monster. The wild is in the Druid’s blood."
    ),
    3: {
        'Circle Forms': (
            "You can channel lunar magic when you assume a Wild Shape form, granting you the benefits below.\n\n"
            "  - Challenge Rating. The maximum Challenge Rating for the form equals your Druid level divided by 3 (round down).\n"
            "  - Armor Class. Until you leave the form, your AC equals 13 plus your Wisdom modifier if that total is higher than the Beast’s AC.\n"
            "  - Temporary Hit Points. You gain a number of Temporary Hit Points equal to three times your Druid level."
        ),
        'Circle of the Moon Spells': (
            "When you reach a Druid level specified in the Circle of the Moon Spells table, you thereafter always have the listed spells prepared.\n\nIn addition, you can cast the spells from this feature while you’re in a Wild Shape form.\n\n3: Cure Wounds, Moonbeam, Starry Wisp\n5: Conjure Animals\n7: Fount of Moonlight\n9: Mass Cure Wounds"
        ),
    },
    6: {
        'Improved Circle Forms': (
            "While in a Wild Shape form, you gain the following benefits.\n\nLunar Radiance. Each of your attacks in a Wild Shape form can deal its normal damage type or Radiant damage. You make this choice each time you hit with those attacks.\n\nIncreased Toughness. You can add your Wisdom modifier to your Constitution saving throws."
        ),
    },
    10: {
        'Moonlight Step': (
            "You magically transport yourself, reappearing amid a burst of moonlight. As a Bonus Action, you teleport up to 30 feet to an unoccupied space you can see, and you have Advantage on the next attack roll you make before the end of this turn.\n\nYou can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest. You can also regain uses by expending a level 2+ spell slot for each use you want to restore (no action required)."
        ),
    },
    14: {
        'Lunar Form': (
            "The power of the moon suffuses you, granting you the following benefits.\n\nImproved Lunar Radiance. Once per turn, you can deal an extra 2d10 Radiant damage to a target you hit with a Wild Shape form’s attack.\n\nShared Moonlight. Whenever you use Moonlight Step, you can also teleport one willing creature. That creature must be within 10 feet of you, and you teleport it to an unoccupied space you can see within 10 feet of your destination space."
        ),
    },
}

CIRCLE_OF_THE_SEA: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        "Become One with Tides and Storms\n\n"
        "Druids of the Circle of the Sea draw on the tempestuous forces of oceans and storms. Some view themselves as embodiments of nature’s wrath, seeking vengeance against those who despoil nature. Others seek mystical unity with nature by attuning themselves to the ebb and flow of the tides, following the rush of currents and waves and listening to the inscrutable whispers and roars of the winds."
    ),
    3: {
        'Circle of the Sea Spells': (
            "When you reach a Druid level specified in the Circle of the Sea Spells table, you thereafter always have the listed spells prepared.\n\n3: Fog Cloud, Gust of Wind, Ray of Frost, Thunderwave\n5: Lightning Bolt, Water Breathing\n7: Control Water, Ice Storm\n9: Conjure Elemental, Hold Monster"
        ),
        'Wrath of the Sea': (
            "As a Bonus Action, you can expend a use of your Wild Shape to manifest a 5-foot Emanation that takes the form of ocean spray that surrounds you for 10 minutes. It ends early if you dismiss it (no action required), manifest it again, or have the Incapacitated condition.\n\nWhen you manifest the Emanation and as a Bonus Action on your subsequent turns, you can choose another creature you can see in the Emanation. The target must succeed on a Constitution saving throw against your spell save DC or take Cold damage and, if the creature is Large or smaller, be pushed up to 15 feet away from you. To determine this damage, roll a number of d6s equal to your Wisdom modifier (minimum of one die)."
        ),
    },
    6: {
        'Aquatic Affinity': (
            "The size of the Emanation created by your Wrath of the Sea increases to 10 feet.\n\nIn addition, you gain a Swim Speed equal to your Speed."
        ),
    },
    10: {
        'Stormborn': (
            "Your Wrath of the Sea confers two more benefits while active, as detailed below.\n\nFlight. You gain a Fly Speed equal to your Speed.\n\nResistance. You have Resistance to Cold, Lightning, and Thunder damage."
        ),
    },
    14: {
        'Oceanic Gift': (
            "Instead of manifesting the Emanation of Wrath of the Sea around yourself, you can manifest it around one willing creature within 60 feet of yourself. That creature gains all the benefits of the Emanation and uses your spell save DC and Wisdom modifier for it.\n\nIn addition, you can manifest the Emanation around both the other creature and yourself if you expend two uses of your Wild Shape instead of one when manifesting it."
        ),
    },
}

CIRCLE_OF_THE_STARS: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        "Harness Secrets Hidden in Constellations\n\n"
        "The Circle of the Stars has tracked heavenly patterns since time immemorial, discovering secrets hidden amid the constellations. By understanding these secrets, the Druids of this circle seek to harness the powers of the cosmos."
    ),
    3: {
        'Star Map': (
            "You’ve created a star chart as part of your heavenly studies. It is a Tiny object, and you can use it as a Spellcasting Focus for your Druid spells. You determine its form by rolling on the Star Map table or by choosing one.\n\nWhile holding the map, you have the Guidance and Guiding Bolt spells prepared, and you can cast Guiding Bolt without expending a spell slot. You can cast it in that way a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.\n\nIf you lose the map, you can perform a 1-hour ceremony to magically create a replacement. This ceremony can be performed during a Short or Long Rest, and it destroys the previous map.\n\nStar Map\n1d6  Map Form\n1  A scroll bearing depictions of constellations\n2  A stone tablet with fine holes drilled through it\n3  An owlbear hide tooled with stellar symbols\n4  A collection of maps bound in an ebony cover\n5  A crystal engraved with starry patterns\n6  A glass disk etched with constellations"
        ),
        'Starry Form': (
            "As a Bonus Action, you can expend a use of your Wild Shape feature to take on a starry form rather than shape-shifting.\n\nWhile in your starry form, you retain your game statistics, but your body becomes luminous, your joints glimmer like stars, and glowing lines connect them as on a star chart. This form sheds Bright Light in a 10-foot radius and Dim Light for an additional 10 feet. The form lasts for 10 minutes. It ends early if you dismiss it (no action required), have the Incapacitated condition, or use this feature again.\n\nWhenever you assume your starry form, choose which of the following constellations glimmers on your body; your choice gives you certain benefits while in the form.\n\nArcher. A constellation of an archer appears on you. When you activate this form and as a Bonus Action on your subsequent turns while it lasts, you can make a ranged spell attack, hurling a luminous arrow that targets one creature within 60 feet of yourself. On a hit, the attack deals Radiant damage equal to 1d8 plus your Wisdom modifier.\n\nChalice. A constellation of a life-giving goblet appears on you. Whenever you cast a spell using a spell slot that restores Hit Points to a creature, you or another creature within 30 feet of you can regain Hit Points equal to 1d8 plus your Wisdom modifier.\n\nDragon. A constellation of a wise dragon appears on you. When you make an Intelligence or a Wisdom check or a Constitution saving throw to maintain Concentration, you can treat a roll of 9 or lower on the d20 as a 10."
        ),
    },
    6: {
        'Cosmic Omen': (
            "Whenever you finish a Long Rest, you can consult your Star Map for omens and roll a die. Until you finish your next Long Rest, you gain access to a special Reaction based on whether you rolled an even or an odd number on the die:\n\nWeal (Even). Whenever a creature you can see within 30 feet of you is about to make a D20 Test, you can take a Reaction to roll 1d6 and add the number rolled to the total.\n\nWoe (Odd). Whenever a creature you can see within 30 feet of you is about to make a D20 Test, you can take a Reaction to roll 1d6 and subtract the number rolled from the total.\n\nYou can use this Reaction a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."
        ),
    },
    10: {
        'Twinkling Constellations': (
            "The constellations of your Starry Form improve. The 1d8 of the Archer and the Chalice becomes 2d8, and while the Dragon is active, you have a Fly Speed of 20 feet and can hover.\n\nMoreover, at the start of each of your turns while in your Starry Form, you can change which constellation glimmers on your body."
        ),
    },
    14: {
        'Full of Stars': (
            "While in your Starry Form, you become partially incorporeal, giving you Resistance to Bludgeoning, Piercing, and Slashing damage."
        ),
    },
}

