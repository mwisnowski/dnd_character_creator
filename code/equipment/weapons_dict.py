from __future__ import annotations

MASTERY_DICT: dict[str, str] = {
    'Cleave': 'If you hit a creature with a melee attack roll using this weapon, you can make a melee attack roll with the weapon against a second creature '
    'within 5 feet of the first that is also within your reach. On a hit, the second creature takes the weapon\'s damage, but don\'t add your ability modifier '
    'to that damage unless that modifier is negative. You can make this extra attack only once per turn.',
    'Graze': 'If your attack roll with this weapon misses a creature, you can deal damage to that creature equal to the ability modifier you used to make the '
    'attack roll. This damage is the same type dealt by the weapon, and the damage can be increased only by increasing the ability modifier.',
    'Nick': 'When you make the extra attack of the Light property, you can make it as part of the Attack action instead of as a Bonus Action. You can make '
    'this extra attack only once per turn.',
    'Push': 'If you hit a creature with this weapon, you can push the creature up to 10 feet straight away from yourself if it is Large or smaller.',
    'Sap': 'If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.',
    'Slow': 'If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the '
    'creature is hit more than once by weapons that have this property, the Speed reduction doesn\'t exceed 10 feet.',
    'Topple': 'If you hit a creature with this weapon, you can force the creature to make a Constitution saving throw (DC 8 plus the ability modifier used to '
    'make the attack roll and your Proficiency Bonus). On a failed save, the creature has the Prone condition.',
    'Vex': '	If you hit a creature with this weapon and deal damage to the creature, you have Advantage on your next attack roll against that creature '
    'before the end of your next turn.'
}

PROPERTIES_DICT: dict[str, str] = {
    'Ammunition': 'You can use a weapon that has the Ammunition property to make a ranged attack only if you have ammunition to fire from it. The type of '
    'ammunition required is specified with the weapon\'s range. Each attack expends one piece of ammunition. Drawing the ammunition is part of the attack '
    '(you need a free hand to load a one-handed weapon). After a fight, you can spend 1 minute to recover half the ammunition (round down) you used in the '
    'fight; the rest is lost.',
    'Finesse': 'When making an attack roll with a weapon that has the Finesse property, you can use your choice of your Strength or Dexterity modifier for '
    'the attack and damage rolls. You must use the same modifier for both rolls.',
    'Heavy': 'You have Disadvantage on attack rolls with a Heavy weapon if it\'s a Melee weapon and your Strength score isn\'t at least 13 or if it\'s a Ranged '
    'weapon and your Dexterity score isn\'t at least 13.',
    'Light': 'When you take the Attack action on your turn and attack with a Light weapon, you can make one extra attack as a Bonus Action later on the same turn. '
    'That extra attack must be made with a different Light weapon, and you don\'t add your ability modifier to the extra attack\'s damage unless that modifier is '
    'negative. For example, you can attack with a Shortsword in one hand and a Dagger in the other using the Attack action and a Bonus Action, but you don\'t add '
    'your Strength or Dexterity modifier to the damage roll of the Bonus Action unless that modifier is negative.',
    'Loading': 'You can fire only one piece of ammunition from a Loading weapon when you use an action, a Bonus Action, or a Reaction to fire it, regardless of '
    'the number of attacks you can normally make.',
    'Range': 'A Range weapon has a range in parentheses after the Ammunition or Thrown property. The range lists two numbers. The first is the weapon\'s normal '
    'range in feet, and the second is the weapon\'s long range. When attacking a target beyond normal range, you have Disadvantage on the attack roll. You can\'t '
    'attack a target beyond the long range.',
    'Reach': '	A Reach weapon adds 5 feet to your reach when you attack with it, as well as when determining your reach for Opportunity Attacks with it.',
    'Thrown': '	If a weapon has the Thrown property, you can throw the weapon to make a ranged attack, and you can draw that weapon as part of the attack. If the '
    'weapon is a Melee weapon, use the same ability modifier for the attack and damage rolls that you use for a melee attack with that weapon.',
    'Two-Handed': 'A Two-Handed weapon requires two hands when you attack with it.',
    'Versatile': 'A Versatile weapon can be used with one or two hands. A damage value in parentheses appears with the property. The weapon deals that damage when '
    'used with two hands to make a melee attack.'
}

SIMPLE_WEAPONS_DICT: dict[str, dict] = {
    'Club': {
        'type': 'Simple Melee Weapon',
        'damage': '1d4 bludgeoning',
        'properties': ['Light'],
        'mastery': 'Slow',
        'cost': 0.1,
        'weight': 2,
    },
    'Dagger': {
        'type': 'Simple Melee Weapon',
        'damage': '1d4 piercing',
        'properties': ['Finesse', 'Light', 'Thrown (range 20/60)'],
        'mastery': 'Nick',
        'cost': 2,
        'weight': 1,
    },
    'Greatclub': {
        'type': 'Simple Melee Weapon',
        'damage': '1d8 bludgeoning',
        'properties': ['Two-Handed'],
        'mastery': 'Push',
        'cost': 0.2,
        'weight': 10,
    },
    'Handaxe': {
        'type': 'Simple Melee Weapon',
        'damage': '1d6 slashing',
        'properties': ['Light', 'Thrown (range 20/60)'],
        'mastery': 'Vex',
        'cost': 5,
        'weight': 2,
    },
    'Javelin': {
        'type': 'Simple Melee Weapon',
        'damage': '1d6 piercing',
        'properties': ['Thrown (range 30/120)'],
        'mastery': 'Slow',
        'cost': 0.5,
        'weight': 2,
    },
    'Light Hammer': {
        'type': 'Simple Melee Weapon',
        'damage': '1d4 bludgeoning',
        'properties': ['Light', 'Thrown (range 20/60)'],
        'mastery': 'Nick',
        'cost': 2,
        'weight': 2,
    },
    'Mace': {
        'type': 'Simple Melee Weapon',
        'damage': '1d6 bludgeoning',
        'properties': [],
        'mastery': 'Sap',
        'cost': 5,
        'weight': 4,
    },
    'Quarterstaff': {
        'type': 'Simple Melee Weapon',
        'damage': '1d6 bludgeoning',
        'properties': ['Versatile (1d8)'],
        'mastery': 'Topple',
        'cost': 0.2,
        'weight': 4,
    },
    'Sickle': {
        'type': 'Simple Melee Weapon',
        'damage': '1d4 slashing',
        'properties': ['Light'],
        'mastery': 'Nick',
        'cost': 1,
        'weight': 2,
    },
    'Spear': {
        'type': 'Simple Melee Weapon',
        'damage': '1d6 piercing',
        'properties': ['Thrown (range 20/60)', 'Versatile (1d8)'],
        'mastery': 'Sap',
        'cost': 0.5,
        'weight': 3,
    },
    'Light Crossbow': {
        'type': 'Simple Ranged Weapon',
        'damage': '1d8 piercing',
        'properties': ['Ammunition (range 80/320)', 'Loading', 'Two-Handed'],
        'mastery': 'Vex',
        'cost': 25,
        'weight': 5,
    },
    'Dart': {
        'type': 'Simple Ranged Weapon',
        'damage': '1d4 piercing',
        'properties': ['Finesse', 'Thrown (range 20/60)'],
        'mastery': 'Slow',
        'cost': 0.05,
        'weight': 0.25,
    },
    'Shortbow': {
        'type': 'Simple Ranged Weapon',
        'damage': '1d6 piercing',
        'properties': ['Ammunition (range 80/320)', 'Two-Handed'],
        'mastery': 'Vex',
        'cost': 25,
        'weight': 2,
    },
    'Sling': {
        'type': 'Simple Ranged Weapon',
        'damage': '1d4 bludgeoning',
        'properties': ['Ammunition (range 30/120)'],
        'mastery': 'Slow',
        'cost': 0.1,
        'weight': 0.2,
    },
}

MARTIAL_WEAPONS_DICT: dict[str, dict] = {
    'Battleaxe': {
        'type': 'Martial Melee Weapon',
        'damage': '1d8 slashing',
        'properties': ['Versatile (1d10)'],
        'mastery': 'Topple',
        'cost': 10,
        'weight': 4,
    },
    'Flail': {
        'type': 'Martial Melee Weapon',
        'damage': '1d8 bludgeoning',
        'properties': [],
        'mastery': 'Sap',
        'cost': 10,
        'weight': 2,
    },
    'Glaive': {
        'type': 'Martial Melee Weapon',
        'damage': '1d10 slashing',
        'properties': ['Heavy', 'Reach', 'Two-Handed'],
        'mastery': 'Grze',
        'cost': 20,
        'weight': 6,
    },
    'Greataxe': {
        'type': 'Martial Melee Weapon',
        'damage': '1d12 slashing',
        'properties': ['Heavy', 'Two-Handed'],
        'mastery': 'Cleave',
        'cost': 30,
        'weight': 7,
    },
    'Greatsword': {
        'type': 'Martial Melee Weapon',
        'damage': '2d6 slashing',
        'properties': ['Heavy', 'Two-Handed'],
        'mastery': 'Graze',
        'cost': 50,
        'weight': 6,
    },
    'Halberd': {
        'type': 'Martial Melee Weapon',
        'damage': '1d10 slashing',
        'properties': ['Heavy', 'Reach', 'Two-Handed'],
        'mastery': 'Cleave',
        'cost': 20,
        'weight': 6,
    },
    'Lance': {
        'type': 'Martial Melee Weapon',
        'damage': '1d12 piercing',
        'properties': ['Reach', 'Special'],
        'mastery': 'Topple',
        'cost': 10,
        'weight': 6,
    },
    'Longsword': {
        'type': 'Martial Melee Weapon',
        'damage': '1d8 slashing',
        'properties': ['Versatile (1d10)'],
        'mastery': 'Sap',
        'cost': 15,
        'weight': 3,
    },
    'Maul': {
        'type': 'Martial Melee Weapon',
        'damage': '2d6 bludgeoning',
        'properties': ['Heavy', 'Two-Handed'],
        'mastery': 'Topple',
        'cost': 10,
        'weight': 10,
    },
    'Morningstar': {
        'type': 'Martial Melee Weapon',
        'damage': '1d8 piercing',
        'properties': [],
        'mastery': 'Sap',
        'cost': 15,
        'weight': 4,
    },
    'Pike': {
        'type': 'Martial Melee Weapon',
        'damage': '1d10 piercing',
        'properties': ['Heavy', 'Reach', 'Two-Handed'],
        'mastery': 'Push',
        'cost': 5,
        'weight': 18,
    },
    'Rapier': {
        'type': 'Martial Melee Weapon',
        'damage': '1d8 piercing',
        'properties': ['Finesse'],
        'mastery': 'Vex',
        'cost': 25,
        'weight': 2,
    },
    'Scimitar': {
        'type': 'Martial Melee Weapon',
        'damage': '1d6 slashing',
        'properties': ['Finesse', 'Light'],
        'mastery': 'Nick',
        'cost': 25,
        'weight': 3,
    },
    'Shortsword': {
        'type': 'Martial Melee Weapon',
        'damage': '1d6 piercing',
        'properties': ['Finesse', 'Light'],
        'mastery': 'Vex',
        'cost': 10,
        'weight': 2,
    },
    'Trident': {
        'type': 'Martial Melee Weapon',
        'damage': '1d6 piercing',
        'properties': ['Thrown (range 20/60)', 'Versatile (1d8)'],
        'mastery': 'Topple',
        'cost': 5,
        'weight': 4,
    },
    'War Pick': {
        'type': 'Martial Melee Weapon',
        'damage': '1d8 piercing',
        'properties': [],
        'mastery': 'Sap',
        'cost': 5,
        'weight': 2,
    },
    'Warhammer': {
        'type': 'Martial Melee Weapon',
        'damage': '1d8 bludgeoning',
        'properties': ['Versatile (1d10)'],
        'mastery': 'Push',
        'cost': 15,
        'weight': 2,
    },
    'Whip': {
        'type': 'Martial Melee Weapon',
        'damage': '1d4 slashing',
        'properties': ['Finesse', 'Reach'],
        'mastery': 'Slow',
        'cost': 2,
        'weight': 3,
    },
    'Blowgun': {
        'type': 'Martial Ranged Weapon',
        'damage': '1 piercing',
        'properties': ['Ammunition (range 25/100)', 'Loading'],
        'mastery': 'Vex',
        'cost': 10,
        'weight': 1,
    },
    'Hand Crossbow': {
        'type': 'Martial Ranged Weapon',
        'damage': '1d6 piercing',
        'properties': ['Ammunition (range 30/120)', 'Light', 'Loading'],
        'mastery': 'Vex',
        'cost': 75,
        'weight': 3,
    },
    'Heavy Crossbow': {
        'type': 'Martial Ranged Weapon',
        'damage': '1d10 piercing',
        'properties': ['Ammunition (range 100/400)', 'Heavy', 'Loading', 'Two-Handed'],
        'mastery': 'Push',
        'cost': 50,
        'weight': 18,
    },
    'Longbow': {
        'type': 'Martial Ranged Weapon',
        'damage': '1d8 piercing',
        'properties': ['Ammunition (range 150/600)', 'Heavy', 'Two-Handed'],
        'mastery': 'Slow',
        'cost': 50,
        'weight': 2,
    },
    'Musket': {
        'type': 'Martial Ranged Weapon',
        'damage': '1d12 piercing',
        'properties': ['Ammunition (range 40/120)', 'Loading', 'Two-Handed'],
        'mastery': 'Slow',
        'cost': 500,
        'weight': 10,
    },
    'Pistol': {
        'type': 'Martial Ranged Weapon',
        'damage': '1d10 piercing',
        'properties': ['Ammunition (range 30/90)', 'Loading', 'Light'],
        'mastery': 'Vex',
        'cost': 250,
        'weight': 3,
    },
}

AMMUNITION_DICT: dict[str, dict] = {
    'Arrow': {
        'amount': 20,
        'storage': 'Quiver',
        'cost': 1,
        'weight': 1,
    },
    'Bolts': {
        'amount': 20,
        'storage': 'Case',
        'cost': 1,
        'weight': 1,
    },
    'Firearm Bullets': {
        'amount': 10,
        'storage': 'Pouch',
        'cost': 3,
        'weight': 2,
    },
    'Needles': {
        'amount': 50,
        'storage': 'Pouch',
        'cost': 1,
        'weight': 1,
    },
    'Sling Bullets': {
        'amount': 20,
        'storage': 'Pouch',
        'cost': .004,
        'weight': 1,
    }
}