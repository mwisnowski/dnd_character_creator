"""
Monk class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

MONK_CLASS: Dict[str, Any] = {
    "primary_ability": ["Dexterity", "Wisdom"],
    "hit_die": "d8",
    "saving_throws": ["Strength", "Dexterity"],
    "proficiencies": {
        "skills": [
            "Choose 2: Acrobatics, Athletics, History, Insight, Religion, or Stealth"
        ],
        "tools": ["Choose one type of Artisan's Tools or Musical Instrument"],
        "weapons": [
            "Simple Weapons",
            "Martial weapons with the Light property"
        ],
        "armor": [],
    },
    "starting_equipment": [
        [
            "Spear", "5 Daggers", "Artisan's Tools or Musical Instrument (chosen above)", "Explorer's Pack", "11 GP"
        ],
        [
            "50 GP"
        ]
    ],
}

MONK_LEVELS: Dict[int, Dict[str, Any]] = {
    1:  {"proficiency_bonus": 2, "features": ["Martial Arts", "Unarmored Defense"]},
    2:  {"proficiency_bonus": 2, "features": ["Monk's Focus", "Unarmored Movement", "Uncanny Metabolism"]},
    3:  {"proficiency_bonus": 2, "features": ["Deflect Attacks", "Monk Subclass"]},
    4:  {"proficiency_bonus": 2, "features": ["Ability Score Improvement", "Slow Fall"]},
    5:  {"proficiency_bonus": 3, "features": ["Extra Attack", "Stunning Strike"]},
    6:  {"proficiency_bonus": 3, "features": ["Empowered Strikes", "Subclass Feature"]},
    7:  {"proficiency_bonus": 3, "features": ["Evasion"]},
    8:  {"proficiency_bonus": 3, "features": ["Ability Score Improvement"]},
    9:  {"proficiency_bonus": 4, "features": ["Acrobatic Movement"]},
    10: {"proficiency_bonus": 4, "features": ["Heightened Focus", "Self-Restoration"]},
    11: {"proficiency_bonus": 4, "features": ["Subclass Feature"]},
    12: {"proficiency_bonus": 4, "features": ["Ability Score Improvement"]},
    13: {"proficiency_bonus": 5, "features": ["Deflect Energy"]},
    14: {"proficiency_bonus": 5, "features": ["Disciplined Survivor"]},
    15: {"proficiency_bonus": 5, "features": ["Perfect Focus"]},
    16: {"proficiency_bonus": 5, "features": ["Ability Score Improvement"]},
    17: {"proficiency_bonus": 6, "features": ["Subclass Feature"]},
    18: {"proficiency_bonus": 6, "features": ["Superior Defense"]},
    19: {"proficiency_bonus": 6, "features": ["Epic Boon"]},
    20: {"proficiency_bonus": 6, "features": ["Body and Mind"]},
    # Martial Arts/Focus/Unarmored Movement table is separate
}

# Martial Arts/Focus/Unarmored Movement progression table
MARTIAL_ARTS: Dict[int, Dict[str, Any]] = {
    1:  {"martial_arts_die": "1d6",  "focus_points": None,  "unarmored_movement": None},
    2:  {"martial_arts_die": "1d6",  "focus_points": 2,     "unarmored_movement": "+10 ft"},
    3:  {"martial_arts_die": "1d6",  "focus_points": 3,     "unarmored_movement": "+10 ft"},
    4:  {"martial_arts_die": "1d6",  "focus_points": 4,     "unarmored_movement": "+10 ft"},
    5:  {"martial_arts_die": "1d8",  "focus_points": 5,     "unarmored_movement": "+10 ft"},
    6:  {"martial_arts_die": "1d8",  "focus_points": 6,     "unarmored_movement": "+15 ft"},
    7:  {"martial_arts_die": "1d8",  "focus_points": 7,     "unarmored_movement": "+15 ft"},
    8:  {"martial_arts_die": "1d8",  "focus_points": 8,     "unarmored_movement": "+15 ft"},
    9:  {"martial_arts_die": "1d8",  "focus_points": 9,     "unarmored_movement": "+15 ft"},
    10: {"martial_arts_die": "1d8",  "focus_points": 10,    "unarmored_movement": "+20 ft"},
    11: {"martial_arts_die": "1d10", "focus_points": 11,    "unarmored_movement": "+20 ft"},
    12: {"martial_arts_die": "1d10", "focus_points": 12,    "unarmored_movement": "+20 ft"},
    13: {"martial_arts_die": "1d10", "focus_points": 13,    "unarmored_movement": "+20 ft"},
    14: {"martial_arts_die": "1d10", "focus_points": 14,    "unarmored_movement": "+25 ft"},
    15: {"martial_arts_die": "1d10", "focus_points": 15,    "unarmored_movement": "+25 ft"},
    16: {"martial_arts_die": "1d10", "focus_points": 16,    "unarmored_movement": "+25 ft"},
    17: {"martial_arts_die": "1d12", "focus_points": 17,    "unarmored_movement": "+25 ft"},
    18: {"martial_arts_die": "1d12", "focus_points": 18,    "unarmored_movement": "+30 ft"},
    19: {"martial_arts_die": "1d12", "focus_points": 19,    "unarmored_movement": "+30 ft"},
    20: {"martial_arts_die": "1d12", "focus_points": 20,    "unarmored_movement": "+30 ft"},
}





# Monk Subclasses (features as level: {feature: description}, like cleric.py.LIFE_DOMAIN)
WARRIOR_OF_MERCY = {
    'description': (
        'Manipulate Forces of Life and Death\n\n'
        'Warriors of Mercy manipulate the life force of others. These Monks are wandering physicians, but they bring a swift end to their enemies. '
        'They often wear masks, presenting themselves as faceless bringers of life and death.'
    ),
    3: {
        'Hand of Harm': (
            'Once per turn when you hit a creature with an Unarmed Strike and deal damage, you can expend 1 Focus Point to deal extra Necrotic damage equal to one roll of your Martial Arts die plus your Wisdom modifier.'
        ),
        'Hand of Healing': (
            'As a Magic action, you can expend 1 Focus Point to touch a creature and restore a number of Hit Points equal to a roll of your Martial Arts die plus your Wisdom modifier. When you use your Flurry of Blows, you can replace one of the Unarmed Strikes with a use of this feature without expending a Focus Point for the healing.'
        ),
        'Implements of Mercy': (
            'You gain proficiency in the Insight and Medicine skills and proficiency with the Herbalism Kit.'
        )
    },
    6: {
        "Physician's Touch": (
            'Your Hand of Harm and Hand of Healing improve. Hand of Harm can also Poison, and Hand of Healing can end certain conditions.'
        )
    },
    11: {
        'Flurry of Healing and Harm': (
            'When you use Flurry of Blows, you can replace each Unarmed Strike with Hand of Healing without expending Focus Points. You can also use Hand of Harm with Flurry of Blows without expending a Focus Point, a number of times per long rest equal to your Wisdom modifier.'
        )
    },
    17: {
        'Hand of Ultimate Mercy': (
            'As a Magic action, you can touch the corpse of a creature that died within the past 24 hours and expend 5 Focus Points to return it to life with 4d10+Wisdom HP, removing certain conditions. Once per long rest.'
        )
    }
}

WAY_OF_SHADOW = {
    'description': (
        'Harness Shadow Power for Stealth and Subterfuge\n\n'
        'Warriors of Shadow practice stealth and subterfuge, harnessing the power of the Shadowfell. They are at home in darkness, able to draw gloom around themselves to hide, leap from shadow to shadow, and take on a wraithlike form.'
    ),
    3: {
        'Shadow Arts': (
            'Cast Darkness (1 Focus Point), see in magical darkness, move the area, gain Darkvision +60 ft, know Minor Illusion (Wisdom as spellcasting).'
        )
    },
    6: {
        'Shadow Step': (
            'Teleport in dim light/darkness as a bonus action, then gain advantage on next melee attack.'
        )
    },
    11: {
        'Improved Shadow Step': (
            'Spend 1 Focus Point to teleport regardless of light, and make an Unarmed Strike after teleporting.'
        )
    },
    17: {
        'Cloak of Shadows': (
            'As a Magic action in dim light/darkness, spend 3 Focus Points to become invisible and partially incorporeal for 1 minute, and use Flurry of Blows for free.'
        )
    }
}

WAY_OF_THE_ELEMENTS = {
    'description': (
        'Wield Strikes and Bursts of Elemental Power\n\n'
        'Warriors of the Elements tap into the power of the Elemental Planes. Harnessing their supernatural focus, these Monks momentarily tame the energy of the Elemental Chaos to empower themselves in and out of battle.'
    ),
    3: {
        'Elemental Attunement': (
            'Spend 1 Focus Point to gain reach, change Unarmed Strike damage type, and move targets.'
        ),
        'Manipulate Elements': (
            'Know the Elementalism spell (Wisdom as spellcasting).'
        )
    },
    6: {
        'Elemental Burst': (
            'Spend 2 Focus Points to deal AoE damage (choose type) in a 20-ft sphere.'
        )
    },
    11: {
        'Stride of the Elements': (
            'While attuned, gain fly and swim speed equal to your speed.'
        )
    },
    17: {
        'Elemental Epitome': (
            'While attuned, gain resistance to a chosen element, destructive stride, and empowered strikes.'
        )
    }
}

WAY_OF_THE_OPEN_HAND = {
    'description': (
        'Master Unarmed Combat Techniques\n\n'
        'Warriors of the Open Hand are masters of unarmed combat. They learn techniques to push and trip their opponents and manipulate their own energy to protect themselves from harm.'
    ),
    3: {
        'Open Hand Technique': (
            'Flurry of Blows can addle, push, or topple targets.'
        )
    },
    6: {
        'Wholeness of Body': (
            'Bonus action to heal yourself (Martial Arts die + Wisdom, uses/long rest = Wisdom modifier).'
        )
    },
    11: {
        'Fleet Step': (
            'Take Step of the Wind as a bonus action after another bonus action.'
        )
    },
    17: {
        'Quivering Palm': (
            'Expend 4 Focus Points to set up lethal vibrations, then end them for 10d12 force damage (Con save for half). Only one creature at a time.'
        )
    }
}

MONK_FEATURES: Dict[str, str] = {
    'Martial Arts':
        'Your practice of martial arts gives you mastery of combat styles that use your Unarmed Strike and Monk weapons, which are the following:\n\n'
        '  - Simple Melee weapons\n'
        '  - Martial Melee weapons that have the Light property\n\n'
        'You gain the following benefits while you are unarmed or wielding only Monk weapons and you aren\'t wearing armor or wielding a Shield.\n\n'
        '  - Bonus Unarmed Strike. You can make an Unarmed Strike as a Bonus Action.\n\n'
        '  - Martial Arts Die. You can roll 1d6 in place of the normal damage of your Unarmed Strike or Monk weapons. This die changes as you gain Monk levels, as shown in the Martial Arts column of the Monk Features table.\n\n'
        '  - Dexterous Attacks. You can use your Dexterity modifier instead of your Strength modifier for the attack and damage rolls of your Unarmed Strikes and Monk weapons. In addition, when you use the Grapple or Shove option of your Unarmed Strike, you can use your Dexterity modifier instead of your Strength modifier to determine the save DC.',
    'Unarmored Defense':
        'While you aren\'t wearing armor or wielding a Shield, your base Armor Class equals 10 plus your Dexterity and Wisdom modifiers.',
    'Monk\'s Focus':
        'Your focus and martial training allow you to harness a well of extraordinary energy within yourself. This energy is represented by Focus Points. Your Monk level determines the number of points you have, as shown in the Focus Points column of the Monk Features table.\n\n'
        'You can expend these points to enhance or fuel certain Monk features. You start knowing three such features: Flurry of Blows, Patient Defense, and Step of the Wind, each of which is detailed below.\n\n'
        'When you expend a Focus Point, it is unavailable until you finish a Short or Long Rest, at the end of which you regain all your expended points.\n\n'
        'Some features that use Focus Points require your target to make a saving throw. The save DC equals 8 plus your Wisdom modifier and Proficiency Bonus.\n\n'
        '  - Flurry of Blows. You can expend 1 Focus Point to make two Unarmed Strikes as a Bonus Action.\n\n'
        '  - Patient Defense. You can take the Disengage action as a Bonus Action. Alternatively, you can expend 1 Focus Point to take both the Disengage and the Dodge actions as a Bonus Action.\n\n'
        '  - Step of the Wind. You can take the Dash action as a Bonus Action. Alternatively, you can expend 1 Focus Point to take both the Disengage and Dash actions as a Bonus Action, and your jump distance is doubled for the turn.',
    'Unarmored Movement':
        'Your speed increases by 10 feet while you aren\'t wearing armor or wielding a Shield. This bonus increases when you reach certain Monk levels, as shown on the Monk Features table.',
    'Uncanny Metabolism':
        'When you roll Initiative, you can regain all expended Focus Points. When you do so, roll your Martial Arts die, and regain a number of Hit Points equal to your Monk level plus the number rolled.\n\n'
        'Once you use this feature, you can\'t use it again until you finish a Long Rest.',
    'Deflect Attacks':
        'When an attack roll hits you and its damage includes Bludgeoning, Piercing, or Slashing damage, you can take a Reaction to reduce the attack\'s total damage against you. The reduction equals 1d10 plus your Dexterity modifier and Monk level.\n\n'
        'If you reduce the damage to 0, you can expend 1 Focus Point to redirect some of the attack\'s force. If you do so, choose a creature you can see within 5 feet of yourself if the attack was a melee attack or a creature you can see within 60 feet of yourself that isn\'t behind Total Cover if the attack was a ranged attack. That creature must succeed on a Dexterity saving throw or take damage equal to two rolls of your Martial Arts die plus your Dexterity modifier. The damage is the same type dealt by the attack.',
    'Monk Subclass':
        'You gain a Monk subclass of your choice. The Warrior of Mercy, Warrior of Shadow, Warrior of the Elements, and Warrior of the Open Hand subclasses are detailed after this class\'s description. A subclass is a specialization that grants you features at certain Monk levels. For the rest of your career, you gain each of your subclass\'s features that are of your Monk level or lower.\n\n'
        'Monk Subclasses\nName\nWarrior of Mercy\nWarrior of Shadow\nWarrior of the Elements\nWarrior of the Open Hand',
    'Ability Score Improvement':
        'You gain the Ability Score Improvement feat or another feat of your choice for which you qualify. You gain this feature again at Monk levels 8, 12, and 16.',
    'Slow Fall':
        'You can take a Reaction when you fall to reduce any damage you take from the fall by an amount equal to five times your Monk level.',
    'Extra Attack':
        'You can attack twice instead of once whenever you take the Attack action on your turn.',
    'Stunning Strike':
        'Once per turn when you hit a creature with a Monk weapon or an Unarmed Strike, you can expend 1 Focus Point to attempt a stunning strike. The target must make a Constitution saving throw. On a failed save, the target has the Stunned condition until the start of your next turn. On a successful save, the target\'s Speed is halved until the start of your next turn, and the next attack roll made against the target before then has Advantage.',
    'Empowered Strikes':
        'Whenever you deal damage with your Unarmed Strike, it can deal your choice of Force damage or its normal damage type.',
    'Evasion':
        'When you\'re subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw and only half damage if you fail.\n\n'
        'You don\'t benefit from this feature if you have the Incapacitated condition.',
    'Acrobatic Movement':
        'While you aren\'t wearing armor or wielding a Shield, you gain the ability to move along vertical surfaces and across liquids on your turn without falling during the movement.',
    'Heightened Focus':
        'Your Flurry of Blows, Patient Defense, and Step of the Wind gain the following benefits.\n\n'
        'Flurry of Blows. You can expend 1 Focus Point to use Flurry of Blows and make three Unarmed Strikes with it instead of two.\n\n'
        'Patient Defense. When you expend a Focus Point to use Patient Defense, you gain a number of Temporary Hit Points equal to two rolls of your Martial Arts die.\n\n'
        'Step of the Wind. When you expend a Focus Point to use Step of the Wind, you can choose a willing creature within 5 feet of yourself that is Large or smaller. You move the creature with you until the end of your turn. The creature\'s movement doesn\'t provoke Opportunity Attacks.',
    'Self-Restoration':
        'Through sheer force of will, you can remove one of the following conditions from yourself at the end of each of your turns: Charmed, Frightened, or Poisoned.\n\n'
        'In addition, forgoing food and drink doesn\'t give you levels of Exhaustion.',
    'Deflect Energy':
        'You can now use your Deflect Attacks feature against attacks that deal any damage type, not just Bludgeoning, Piercing, or Slashing.',
    'Disciplined Survivor':
        'Your physical and mental discipline grant you proficiency in all saving throws.\n\n'
        'Additionally, whenever you make a saving throw and fail, you can expend 1 Focus Point to reroll it, and you must use the new roll.',
    'Perfect Focus':
        'When you roll Initiative and don\'t use Uncanny Metabolism, you regain expended Focus Points until you have 4 if you have 3 or fewer.',
    'Superior Defense':
        'At the start of your turn, you can expend 3 Focus Points to bolster yourself against harm for 1 minute or until you have the Incapacitated condition. During that time, you have Resistance to all damage except Force damage.',
    'Epic Boon':
        'You gain an Epic Boon feat or another feat of your choice for which you qualify. Boon of Irresistible Offense is recommended.',
    'Body and Mind':
        'You have developed your body and mind to new heights. Your Dexterity and Wisdom scores increase by 4, to a maximum of 25.'
}
