from __future__ import annotations

# Standard Python imports
from typing import Dict, List

# String constants for dictionary keys
size: str = 'Size'
speed: str = 'Speed'
traits: str = 'Traits'
description: str = 'Description'

# Main species data structure
SPECIES_DATA: Dict[str, Dict[str, str | List[str]]] = {
    'Aasimar': {
        size: 'Small (~2-4 feet tall)/Medium (~4-7 feet tall), chosen when you select this species',
        speed: '30 ft',
        description: 'Aasimar (pronounced AH-sih-mar) are mortals who carry a spark of the Upper Planes within their souls. Whether descended from an angelic being or infused.',
        traits: [
            'Celestial Resistance', 'Darkvision', 'Healing Hands', 'Light Bearer',
            'Celestial Revelation'
        ]
    },
    'Dragonborn': {
        size: 'Medium (~5-7 feet tall), chosen when you select this species',
        speed: '30 ft',
        description: 'Dragonborn are proud, strong, and honorable. They are born of dragons and have a draconic ancestry that grants them unique abilities.',
        traits: [
            'Draconic Ancestry', 'Breath Weapon', 'Damage Resistance', 'Darkvision',
            'Draconic Flight'
        ]
    },
    'Dwarf': {
        size: 'Medium (~4-5 feet tall), chosen when you select this species',
        speed: '30 ft',
        description: 'Dwarves are sturdy and resilient, known for their craftsmanship and connection to the earth.',
        traits: [
            'Darkvision', 'Dwarven Resilience', 'Dwarven Toughness', 'Stonecunning'
        ]
    },
    'Elf': {
        size: 'Medium (~5-6 feet tall), chosen when you select this species',
        speed: '30 ft',
        description: 'Elves are graceful and agile, known for their keen senses and connection to nature.',
        traits: [
            'Darkvision', 'Elven Lineage', 'Fey Ancestry', 'Keen Senses', 'Trance'
        ]
    },
    'Gnome': {
        size: 'Small (~3-4 feet tall), chosen when you select this species',
        speed: '30 ft',
        description: 'Gnomes are small, clever, and curious beings known for their inventiveness and affinity for magic.',
        traits: [
            'Darkvision', 'Gnomish Cunning', 'Gnomish Lineage'
        ]
    },
    'Goliath': {
        size: 'Medium (~7-8 feet tall), chosen when you select this species',
        speed: '30 ft',
        description: 'Goliaths are large, strong beings known for their physical prowess and connection to the mountains.',
        traits: [
            'Giant Ancestry', 'Large Form', 'Powerful Build'
        ]
    },
    'Halfling': {
        size: 'Small (~2-3 feet tall), chosen when you select this species',
        speed: '30 ft',
        description: 'Halflings are small, nimble, and resourceful beings known for their adventurous spirit.',
        traits: [
            'Brave', 'Halfling Nimbleness', 'Luck', 'Naturally Stealthy'
        ]
    },
    'Human': {
        size: 'Small (~2-4 feet tall)/Medium (~4-7 feet tall), chosen when you select this species',
        speed: '30 ft',
        description: 'Humans are adaptable and diverse, known for their resourcefulness and versatility.',
        traits: [
            'Resourceful', 'Skillful', 'Versatile'
        ]
    },
    'Orc': {
        size: 'Medium (~5-6 feet tall), chosen when you select this species',
        speed: '30 ft',
        description: 'Orcs are strong and fierce warriors, known for their combat prowess and tribal culture.',
        traits: [
            'Adrenaline Rush', 'Darkvision', 'Relentless Endurance'
        ]
    },
    'Tiefling': {
        size: 'Small (~3-4 feet tall)/Medium (~4-7 feet tall), chosen when you select this species',
        speed: '30 ft',
        description: 'Tieflings are mortals with infernal heritage, often marked by their fiendish ancestry.',
        traits: [
            'Darkvision', 'Fiendish Legacy', 'Otherworldly Presence'
        ]
    }
}

# Sub-feature tables for traits that reference additional options
CELESTIAL_REVELATION: Dict[str, str] = {
    'Heavenly Wings':
        'Two spectral wings sprout from your back temporarily. Until the transformation ends, you have a '
        'Fly Speed equal to your Speed.\n',
    'Inner Radiance':
        'Searing light temporarily radiates from your eyes and mouth. For the duration, you shed Bright '
        'Light in a 10-foot radius and Dim Light for an additional 10 feet, and at the end of each of '
        'your turns, each creature within 10 feet of you takes Radiant damage equal to your Proficiency '
        'Bonus.\n',
    'Necrotic Shroud':
        'Your eyes briefly become pools of darkness, and flightless wings sprout from your back temporarily. '
        'Creatures other than your allies within 10 feet of you must succeed on a Charisma saving throw '
        '(DC 8 plus your Charisma modifier and Proficiency Bonus) or have the Frightened condition until '
        'the end of your next turn.\n'
}

DRACONIC_ANCESTRY: Dict[str, str] = {
    'Black': 'Acid',
    'Blue': 'Lightning',
    'Brass': 'Fire',
    'Bronze': 'Lightning',
    'Copper': 'Acid',
    'Gold': 'Fire',
    'Green': 'Poison',
    'Red': 'Fire',
    'Silver': 'Cold',
    'White': 'Cold'
}

ELVEN_LINEAGE: Dict[str, str] = {
    'Drow':
        '- The range of your Darkvision increases to 120 feet, and you can see in magical darkness as if it '
        'were dim light. You know the Dancing Lights cantrip.\n'
        '- At 3rd level, you can cast the Faerie Fire spell once per long rest.\n'
        '- At 5th level, you can cast the Darkness spell once per long rest.',
    'High Elf':
        '- You know the Prestidigitation cantrip.\n'
        '- At 3rd level, you can cast the Detect Magic spell once per long rest.\n'
        '- At 5th level, you can cast the Misty Step spell once per long rest.',
    'Wood Elf':
        '- Your speed increases to 35 feet. You also know the Druidcraft cantrip.\n'
        '- At 3rd level, you can cast the Longstrider spell once per long rest.\n'
        '- At 5th level, you can cast the Pass Without Trace spell once per long rest.',
}

GIANT_ANCESTRY: Dict[str, str] = {
    'Cloud\'s Jaunt (Cloud Giant)':
        'As a Bonus Action, you magically teleport up to 30 feet to an unoccupied space you can see.',
    'Fire\'s Burn (Fire Giant)':
        'When you hit a target with an attack roll and deal damage to it, you can also deal 1d10 Fire damage '
        'to that target.',
    'Frost\'s Chill (Frost Giant)':
        'When you hit a target with an attack roll and deal damage to it, you can also 1d6 Cold damage to that '
        'target and reduce its Speed by 10 feet until the start of your next turn.',
    'Hill\'s Tumble (Hill Giant)':
        'When you hit a Large or smaller creature with an attack roll and deal damage to it, you can give '
        'that target the Prone condition.',
    'Stone\'s Endurance (Stone Giant)':
        'When you take damage, you can take a Reaction to roll 1d12. Add your Constitution modifier to the '
        'number rolled and reduce the damage by that total.',
    'Storm\'s Thunder (Storm Giant)':
        'When you take damage from a creature within 60 feet of you, you can take a Reaction to deal 1d8 Thunder '
        'damage to that creature.'
}

GNOMSIH_LINEAGE: Dict[str, str] = {
    'Forest Gnome':
        'You know the Minor Illusion cantrip.\n'
        'You also always have the Speak with Animals spell prepared. You can cast it without a spell slot a '
        'number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a '
        'Long Rest. You can also use any spell slots you have to cast the spell.',
    'Rock Gnome':
        'You know the Mending and Prestidigitation cantrips. In addition, you can spend 10 minutes casting '
        'Prestidigitation to create a Tiny clockwork device (AC 5,1 HP), such as a toy, fire starter, or '
        'music box. When you create the device, you determine its function by choosing one effect from '
        'Prestidigitation; the device produces that effect whenever you or another creature takes a Bonus '
        'Action to activate it with a touch. If the chosen effect has options within it, you choose one of '
        'those options for the device when you create it. For example, if you choose the spell\'s ignite-'
        'extinguish effect, you determine whether the device ignites or extinguishes fire; the device doesn\'t '
        'do both. You can have three such devices in existence at a time, and each falls apart 8 hours after '
        'its creation or when you dismantle it with a touch as a Utilize action.'
}

FIENDISH_LEGACY: Dict[str, str] = {
    'Abyssal': 
        '- You have Resistance to Poison damage. You also know the Poison Spray cantrip.\n'
        '- At 3rd level, you can cast the Ray of Sickness spell once per long rest.\n'
        '- At 5th level, you can cast the Hold Person spell once per long rest.\n',
    'Chthonic':
        '- You have Resistance to Necrotic damage. You also know the Chill Touch cantrip.\n'
        '- At 3rd level, you can cast the Ralse Life spell once per long rest.\n'
        '- At 5th level, you can cast the Ray of Enfeeblement spell once per long rest.\n',
    'Infernal':
        '- You have Resistance to Poison damage. You also know the Poison Spray cantrip.\n'
        '- At 3rd level, you can cast the Hellish Rebuke spell once per long rest.\n'
        '- At 5th level, you can cast the Darkness spell once per long rest.\n'
}

# Trait descriptions and references to sub-feature tables
TRAIT_DATA: Dict[str, str | List[str | Dict[str, str]]] = {
    'Adrenaline Rush':
        "You can take the Dash action as a Bonus Action. When you do so, you gain a number of Temporary Hit "
        "Points equal to your Proficiency Bonus.\n\n"
        "You can use this trait a number of times equal to your Proficiency Bonus, and you regain all "
        "expended uses when you finish a Short or Long Rest.",

    'Brave':
        "You have Advantage on saving throws you make to avoid or end the Frightened condition.",

    'Breath Weapon': [
        'You can use your action to exhale destructive energy. Your Draconic Ancestry determines the size, '
        'shape, and damage type of the exhalation. The exhalation is a 15-foot cone or a 5-foot by 30-foot '
        'line (your choice). Each creature in that area must make a Dexterity saving throw, taking damage '
        'equal to your Proficiency Bonus plus your Constitution modifier on a failed save, or half as much '
        'damage on a successful one. The damage type is determined by your Draconic Ancestry. You can use '
        'this trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when '
        'you finish a Short or Long Rest. The damage increases as you gain levels in this class, as shown in '
        'the Draconic Ancestry table.',
        DRACONIC_ANCESTRY
    ],

    'Celestial Resistance':
        'You have Resistance to Necrotic damage and Radiant damage.',

    'Celestial Revelation': [
        'Celestial Revelation. When you reach character level 3, you can transform as a Bonus Action using '
        'one of the options below (choose the option each time you transform). The transformation lasts for '
        '1 minute or until you end it (no action required). Once you transform, you can\'t do so again until '
        'you finish a Long Rest. Once on each of your turns before the transformation ends, you can deal '
        'extra damage to one target when you deal damage to it with an attack or a spell. The extra damage '
        "equals your Proficiency Bonus, and the extra damage's type is either Necrotic for Necrotic Shroud "
        'or Radiant for Heavenly Wings and Inner Radiance.\n\nHere are the transformation options:\n',
        CELESTIAL_REVELATION
    ],

    'Damage Resistance':
        'You have resistance to the damage type associated with your Draconic Ancestry.',

    'Darkvision':
        'You have Darkvision with a range of 60 feet.',

    'Draconic Ancestry': [
        'Your lineage stems from a dragon progenitor. Choose the kind of dragon from the Draconic Ancestry '
        'table. Your choice affects your Breath Weapon and Damage Resistance traits as well as your appearance.\n\n',
        DRACONIC_ANCESTRY
    ],

    'Draconic Flight':
        'You have a limited ability to sprout draconic wings and fly for short periods.',

    'Dwarven Resilience':
        'You have advantage on saving throws against poison, and you have resistance against poison damage.',

    'Dwarven Toughness':
        'Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.',

    'Elven Lineage': [
        'You are part of a lineage that grants you supernatural abilities. Choose a lineage from the Elven '
        'Lineages table. You gain the level 1 benefit of that lineage.\n\n'
        '  When you reach character levels 3 and 5, you learn a higher-level spell, as shown on the table. '
        'You always have that spell prepared. You can cast it once without a spell slot, and you regain the '
        'ability to cast it in that way when you finish a Long Rest. You can also cast the spell using any '
        'spell slots you have of the appropriate level.\n\n'
        '  Intelligence, Wisdom, or Charisma is your spellcasting ability for the spells you cast with '
        'this trait (choose the ability when you select the lineage).\n\n',
        ELVEN_LINEAGE
    ],

    'Fey Ancestry':
        "You have Advantage on saving throws you make to avoid or end the Charmed condition.",

    'Fiendish Legacy': [
        'You are the recipient of a legacy that grants you supernatural abilities. Choose a legacy from the '
        'Fiendish Legacies table. You gain the level 1 benefit of the chosen legacy.\n\n'
        'When you reach character levels 3 and 5, you learn a higher-level spell, as shown on the table. You '
        'always have that spell prepared. You can cast it once without a spell slot, and you regain the '
        'ability to cast it in that way when you finish a Long Rest. You can also cast the spell using any '
        'spell slots you have of the appropriate level.\n\n'
        'Intelligence, Wisdom, or Charisma is your spellcasting ability for the spells you cast with this trait '
        '(choose the ability when you select the legacy).\n\n',
        FIENDISH_LEGACY],

    'Giant Ancestry':
        ['You are descended from Giants. Choose one of the following benefits - a supernatural boon from your ancestry; '
        'you can use the chosen benefit a number of times equal to your Proficiency Bonus, and you regain all expended '
        'uses when you finish a Long Rest:',
        GIANT_ANCESTRY],

    'Gnomish Cunning':
        'You have advantage on all Intelligence, Wisdom, and Charisma saving throws.',

    'Gnomish Lineage':
        ['You are part of a lineage that grants you supernatural abilities. Choose one of the following options; '
        'whichever one you choose, Intelligence, Wisdom, or Charisma is your spellcasting ability for the spells '
        'you cast with this trait (choose the ability when you select the lineage):',
        GNOMSIH_LINEAGE],

    'Halfling Nimbleness':
        'You can move through the space of any creature that is of a size larger than yours, but you can\'t stop in the same '
        'space.',

    'Healing Hands':
        'As an action, you can touch a creature and cause it to regain hit points equal to your level. Once per long rest.',

    'Keen Senses':
        'You have proficiency in the Insight, Perception, or Survival skill.',

    'Large Form':
        'Starting at character level 5, you can change your size to Large as a Bonus Action if you\'re in a big enough space. '
        'This transformation lasts for 10 minutes or until you end it (no action required). For that duration, you have '
        'Advantage on Strength checks, and your Speed increases by 10 feet. Once you use this trait, you can\'t use it again '
        'until you finish a Long Rest.',

    'Light Bearer':
        'You know the Light cantrip. Charisma is your spellcasting ability for it.',

    'Luck':
        'When you roll a 1 on the d20 of a D20 Test, you can reroll the die, and you must use the new roll.',

    'Naturally Stealthy':
        'You can take the Hide action even when you are obscured only by a creature that is at least one size larger than you.',

    'Otherworldly Presence':
        'You know the Thaumaturgy cantrip. When you cast it with this trait, the spell uses the same spellcasting ability you '
        'use for your Fiendish Legacy trait.',

    'Powerful Build':
        'You have Advantage on any ability check you make to end the Grappled condition. You also count as one size larger when '
        'determining your carrying capacity.',

    'Relentless Endurance':
        'When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. Once per long rest.',

    'Resourceful':
        'You gain Heroic Inspiration whenever you finish a Long Rest.',

    'Skillful':
        'You gain proficiency in one skill of your choice.',

    'Stonecunning':
        'As a Bonus Action, you gain Tremorsense with a range of 60 feet for 10 minutes. You must be on a stone surface or touching'
        'a stone surface to use this Tremorsense. The stone can be natural or worked.\n\n'
        '  You can use this Bonus Action a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest.',

    'Trance':
        "Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day.",

    'Versatile':
        'You gain an Origin feat of your choice. Skilled is recommended'
}