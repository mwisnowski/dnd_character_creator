"""
Sorcerer class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

SORCERER_CLASS: Dict[str, Any] = {
    'name': 'Sorcerer',
    'hit_die': 6,
    'primary_ability': 'Charisma',
    'saving_throws': ['Constitution', 'Charisma'],
    'proficiencies': {
        'armor': [],
        'weapons': ['Simple Weapons'],
        'tools': [],
        'skills': ['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion'],
        'skills_choose': 2
    },
    'starting_equipment': [
        [
            'Spear', '2 Daggers', 'Arcane Focus (crystal)', "Dungeoneer's Pack", '28 GP'
        ],
        [
            '50 GP'
        ]
    ]
}
SORCERER_LEVELS: Dict[int, Dict[str, Any]] = {
    1: {
        'features': ['Spellcasting', 'Innate Sorcery'],
        'sorcery_points': None,
        'cantrips_known': 4,
        'spells_prepared': 2,
        'spells_known': 2,
        'spell_slots': {'1st': 2}
    },
    2: {
        'features': ['Font of Magic', 'Metamagic'],
        'sorcery_points': 2,
        'cantrips_known': 4,
        'spells_prepared': 4,
        'spells_known': 4,
        'spell_slots': {'1st': 3}
    },
    3: {
        'features': ['Sorcerer Subclass'],
        'sorcery_points': 3,
        'cantrips_known': 4,
        'spells_prepared': 6,
        'spells_known': 6,
        'spell_slots': {'1st': 4, '2nd': 2}
    },
    4: {
        'features': ['Ability Score Improvement'],
        'sorcery_points': 4,
        'cantrips_known': 5,
        'spells_prepared': 7,
        'spells_known': 7,
        'spell_slots': {'1st': 4, '2nd': 3}
    },
    5: {
        'features': ['Sorcerous Restoration'],
        'sorcery_points': 5,
        'cantrips_known': 5,
        'spells_prepared': 9,
        'spells_known': 9,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 2}
    },
    6: {
        'features': ['Subclass feature'],
        'sorcery_points': 6,
        'cantrips_known': 5,
        'spells_prepared': 10,
        'spells_known': 10,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3}
    },
    7: {
        'features': ['Sorcery Incarnate'],
        'sorcery_points': 7,
        'cantrips_known': 5,
        'spells_prepared': 11,
        'spells_known': 11,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 1}
    },
    8: {
        'features': ['Ability Score Improvement'],
        'sorcery_points': 8,
        'cantrips_known': 5,
        'spells_prepared': 12,
        'spells_known': 12,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 2}
    },
    9: {
        'features': [],
        'sorcery_points': 9,
        'cantrips_known': 5,
        'spells_prepared': 14,
        'spells_known': 14,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 1}
    },
    10: {
        'features': ['Metamagic'],
        'sorcery_points': 10,
        'cantrips_known': 6,
        'spells_prepared': 15,
        'spells_known': 15,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2}
    },
    11: {
        'features': [],
        'sorcery_points': 11,
        'cantrips_known': 6,
        'spells_prepared': 16,
        'spells_known': 16,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1}
    },
    12: {
        'features': ['Ability Score Improvement'],
        'sorcery_points': 12,
        'cantrips_known': 6,
        'spells_prepared': 16,
        'spells_known': 16,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1}
    },
    13: {
        'features': [],
        'sorcery_points': 13,
        'cantrips_known': 6,
        'spells_prepared': 17,
        'spells_known': 17,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1}
    },
    14: {
        'features': ['Subclass feature'],
        'sorcery_points': 14,
        'cantrips_known': 6,
        'spells_prepared': 17,
        'spells_known': 17,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1}
    },
    15: {
        'features': [],
        'sorcery_points': 15,
        'cantrips_known': 6,
        'spells_prepared': 18,
        'spells_known': 18,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1}
    },
    16: {
        'features': ['Ability Score Improvement'],
        'sorcery_points': 16,
        'cantrips_known': 6,
        'spells_prepared': 18,
        'spells_known': 18,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1}
    },
    17: {
        'features': ['Metamagic'],
        'sorcery_points': 17,
        'cantrips_known': 6,
        'spells_prepared': 19,
        'spells_known': 19,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': 1}
    },
    18: {
        'features': ['Subclass feature'],
        'sorcery_points': 18,
        'cantrips_known': 6,
        'spells_prepared': 20,
        'spells_known': 20,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 3, '6th': 1, '7th': 1, '8th': 1, '9th': 1}
    },
    19: {
        'features': ['Epic Boon'],
        'sorcery_points': 19,
        'cantrips_known': 6,
        'spells_prepared': 21,
        'spells_known': 21,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 3, '6th': 2, '7th': 1, '8th': 1, '9th': 1}
    },
    20: {
        'features': ['Arcane Apotheosis'],
        'sorcery_points': 20,
        'cantrips_known': 6,
        'spells_prepared': 22,
        'spells_known': 22,
        'spell_slots': {'1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 3, '6th': 2, '7th': 2, '8th': 1, '9th': 1}
    },
}
SORCERER_FEATURES: Dict[str, Any] = {
    'Spellcasting': (
        "Drawing from your innate magic, you can cast spells. See chapter 7 for the rules on spellcasting. "
        "The information below details how you use those rules with Sorcerer spells, which appear in the Sorcerer spell list later in the class’s description.\n\n"
        "  - Cantrips. You know four Sorcerer cantrips of your choice. Light, Prestidigitation, Shocking Grasp, and Sorcerous Burst are recommended. "
        "Whenever you gain a Sorcerer level, you can replace one of your cantrips from this feature with another Sorcerer cantrip of your choice.\n"
        "    When you reach Sorcerer levels 4 and 10, you learn another Sorcerer cantrip of your choice, as shown in the Cantrips column of the Sorcerer Features table.\n\n"
        "  - Spell Slots. The Sorcerer Features table shows how many spell slots you have to cast your level 1+ spells. You regain all expended slots when you finish a Long Rest.\n\n"
        "  - Prepared Spells of Level 1+. You prepare the list of level 1+ spells that are available for you to cast with this feature. To start, choose two level 1 Sorcerer spells. Burning Hands and Detect Magic are recommended.\n"
        "    The number of spells on your list increases as you gain Sorcerer levels, as shown in the Prepared Spells column of the Sorcerer Features table. Whenever that number increases, choose additional Sorcerer spells until the number of spells on your list matches the number in the Sorcerer Features table. The chosen spells must be of a level for which you have spell slots. For example, if you’re a level 3 Sorcerer, your list of prepared spells can include six Sorcerer spells of level 1 or 2 in any combination.\n"
        "    If another Sorcerer feature gives you spells that you always have prepared, those spells don’t count against the number of spells you can prepare with this feature, but those spells otherwise count as Sorcerer spells for you.\n\n"
        "  - Changing Your Prepared Spells. Whenever you gain a Sorcerer level, you can replace one spell on your list with another Sorcerer spell for which you have spell slots.\n\n"
        "  - Spellcasting Ability. Charisma is your spellcasting ability for your Sorcerer spells.\n\n"
        "  - Spellcasting Focus. You can use an Arcane Focus as a Spellcasting Focus for your Sorcerer spells."
    ),
    'Innate Sorcery': (
        "An event in your past left an indelible mark on you, infusing you with simmering magic. As a Bonus Action, you can unleash that magic for 1 minute, during which you gain the following benefits:\n\n"
        "  - The spell save DC of your Sorcerer spells increases by 1.\n"
        "  - You have Advantage on the attack rolls of Sorcerer spells you cast.\n"
        "  - You can use this feature twice, and you regain all expended uses of it when you finish a Long Rest."
    ),
    'Font of Magic': (
        "You can tap into the wellspring of magic within yourself. This wellspring is represented by Sorcery Points, which allow you to create a variety of magical effects.\n\n"
        "  - Sorcery Points. You have 2 Sorcery Points, and you gain more as you reach higher levels, as shown in the Sorcery Points column of the Sorcerer Features table. You can’t have more Sorcery Points than the number shown in the table for your level. You regain all expended Sorcery Points when you finish a Long Rest.\n\n"
        "  - Using Sorcery Points. You can use your Sorcery Points to fuel the options below, along with other features, such as Metamagic, that use those points.\n\n"
        "  - Converting Spell Slots to Sorcery Points. You can expend a spell slot to gain a number of Sorcery Points equal to the slot’s level (no action required).\n\n"
        "  - Creating Spell Slots. As a Bonus Action, you can transform unexpended Sorcery Points into one spell slot. The Creating Spell Slots table shows the cost of creating a spell slot of a given level, and it lists the minimum Sorcerer level you must be to create a slot. You can create a spell slot no higher than level 5.\n\n"
        "  - Any spell slot you create with this feature vanishes when you finish a Long Rest."
    ),
    'Metamagic': (
        "Because your magic flows from within, you can alter your spells to suit your needs; you gain two Metamagic options of your choice from “Metamagic Options” later in this class’s description. You use the chosen options to temporarily modify spells you cast. To use an option, you must spend the number of Sorcery Points that it costs.\n\n"
        "  - You can use only one Metamagic option on a spell when you cast it unless otherwise noted in one of those options.\n\n"
        "  - Whenever you gain a Sorcerer level, you can replace one of your Metamagic options with one you don’t know. You gain two more options at Sorcerer level 10 and two more at Sorcerer level 17."
    ),
    'Sorcerer Subclass': (
        "You gain a Sorcerer subclass of your choice. The Draconic Bloodline and Wild Magic subclasses are detailed after this class’s description. A subclass is a specialization that grants you features at certain Sorcerer levels. For the rest of your career, you gain each of your subclass’s features that are of your Sorcerer level or lower."
    ),
    'Ability Score Improvement': (
        "You gain the Ability Score Improvement feat or another feat of your choice for which you qualify. You gain this feature again at Sorcerer levels 8, 12, and 16."
    ),
    'Sorcerous Restoration': (
        "You regain 4 expended Sorcery Points whenever you finish a Short Rest."
    ),
    'Sorcery Incarnate': (
        "You can use a Bonus Action to regain a number of expended Sorcery Points equal to your Charisma modifier (minimum of 1). You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a Long Rest."
    ),
    'Epic Boon': (
        "You gain an Epic Boon feat or another feat of your choice for which you qualify. Boon of Dimensional Travel is recommended."
    ),
    'Arcane Apotheosis': (
        "You can cast the Wish spell once without expending a spell slot. You regain the ability to do so when you finish 2d4 Long Rests."
    ),
}

FONT_OF_MAGIC: Dict[int, Dict[str, int]] = {
    1: {'sorcery_point_cost': 2, 'min_sorcerer_level': 2},
    2: {'sorcery_point_cost': 3, 'min_sorcerer_level': 3},
    3: {'sorcery_point_cost': 5, 'min_sorcerer_level': 5},
    4: {'sorcery_point_cost': 6, 'min_sorcerer_level': 7},
    5: {'sorcery_point_cost': 7, 'min_sorcerer_level': 9},
}

# Aberrant Sorcery Subclass
ABERRANT_SORCERY: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        "Wield Unnatural Psionic Power\n\n"
        "An alien influence has wrapped its tendrils around your mind, giving you psionic power. You can now touch other minds with that power and alter the world around you. Will this power shine from you as a hopeful beacon to others? Or will you be a terror to those who feel the stab of your mind?\n\n"
        "Perhaps a psychic wind from the Astral Plane carried psionic energy to you, or you were exposed to the Far Realm’s warping influence. Alternatively, you were implanted with a mind flayer tadpole, but your transformation into a mind flayer never occurred; now the tadpole’s psionic power is yours. However you acquired this power, your mind is aflame with it."
    ),
    3: {
        'Psionic Spells': (
            "When you reach a Sorcerer level specified in the Psionic Spells table, you thereafter always have the listed spells prepared.\n\n"
            "Psionic Spells\nSorcerer Level\tSpells\n"
            "3\tArms of Hadar, Calm Emotions, Detect Thoughts, Dissonant Whispers, Mind Sliver\n"
            "5\tHunger of Hadar, Sending\n"
            "7\tEvard's Black Tentacles, Summon Aberration\n"
            "9\tRary's Telepathic Bond, Telekinesis"
        ),
        'Telepathic Speech': (
            "You can form a telepathic connection between your mind and the mind of another. As a Bonus Action, choose one creature you can see within 30 feet of yourself. You and the chosen creature can communicate telepathically with each other while the two of you are within a number of miles of each other equal to your Charisma modifier (minimum of 1 mile). To understand each other, you each must mentally use a language the other knows.\n\n"
            "The telepathic connection lasts for a number of minutes equal to your Sorcerer level. It ends early if you use this ability to form a connection with a different creature."
        )
    },
    6: {
        'Psionic Sorcery': (
            "When you cast any level 1+ spell from your Psionic Spells feature, you can cast it by expending a spell slot as normal or by spending a number of Sorcery Points equal to the spell’s level. If you cast the spell using Sorcery Points, it requires no Verbal or Somatic components, and it requires no Material components unless they are consumed by the spell or have a cost specified in it."
        ),
        'Psychic Defenses': (
            "You have Resistance to Psychic damage, and you have Advantage on saving throws to avoid or end the Charmed or Frightened condition."
        )
    },
    14: {
        'Revelation in Flesh': (
            "You can unleash the aberrant truth hidden within yourself. As a Bonus Action, you can spend 1 Sorcery Point or more to magically alter your body for 10 minutes. For each Sorcery Point you spend, you gain one of the following benefits of your choice, the effects of which last until the alteration ends.\n\n"
            "  - Aquatic Adaptation. You gain a Swim Speed equal to twice your Speed, and you can breathe underwater. Gills grow from your neck or flare behind your ears, and your fingers become webbed or you grow wriggling cilia.\n\n"
            "  - Glistening Flight. You gain a Fly Speed equal to your Speed, and you can hover. As you fly, your skin glistens with mucus or otherworldly light.\n\n"
            "  - See the Invisible. You can see any Invisible creature within 60 feet of yourself that isn’t behind Total Cover. Your eyes also turn black or become writhing sensory tendrils.\n\n"
            "  - Wormlike Movement. Your body, along with any equipment you are wearing or carrying, becomes slimy and pliable. You can move through any space as narrow as 1 inch, and you can spend 5 feet of movement to escape from nonmagical restraints or the Grappled condition."
        )
    },
    18: {
        'Warping Implosion': (
            "You can unleash a space-warping anomaly. As a Magic action, you teleport to an unoccupied space you can see within 120 feet of yourself. Immediately after you disappear, each creature within 30 feet of the space you left must make a Strength saving throw against your spell save DC. On a failed save, a creature takes 3d10 Force damage and is pulled straight toward the space you left, ending in an unoccupied space as close to your former space as possible. On a successful save, the creature takes half as much damage only.\n\n"
            "Once you use this feature, you can’t do so again until you finish a Long Rest unless you spend 5 Sorcery Points (no action required) to restore your use of it."
        )
    }
}

# Clockwork Sorcery Subclass
CLOCKWORK_SORCERY: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        "Channel Cosmic Forces of Order\n\n"
        "The cosmic force of order has suffused you with magic. That power arises from Mechanus or a realm like it—a plane of existence shaped entirely by clockwork efficiency. You or someone from your lineage might have become entangled in the machinations of modrons, the orderly beings who inhabit Mechanus. Perhaps your ancestor even took part in the Great Modron March. Whatever its origin within you, the power of order can seem strange to others, but for you, it’s part of a vast and glorious system."
    ),
    3: {
        'Clockwork Spells': (
            "When you reach a Sorcerer level specified in the Clockwork Spells table, you thereafter always have the listed spells prepared.\n\n"
            "Clockwork Spells\nSorcerer Level\tSpells\n"
            "3\tAid, Alarm, Lesser Restoration, Protection from Evil and Good\n"
            "5\tDispel Magic, Protection from Energy\n"
            "7\tFreedom of Movement, Summon Construct\n"
            "9\tGreater Restoration, Wall of Force\n\n"
            "In addition, consult the Manifestations of Order table and choose or randomly determine a way your connection to order manifests while you are casting any of your Sorcerer spells."
        ),
        'Restore Balance': (
            "Your connection to the plane of absolute order allows you to equalize chaotic moments. When a creature you can see within 60 feet of yourself is about to roll a d20 with Advantage or Disadvantage, you can take a Reaction to prevent the roll from being affected by Advantage and Disadvantage.\n\n"
            "You can use this feature a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest."
        )
    },
    6: {
        'Bastion of Law': (
            "You can tap into the grand equation of existence to imbue a creature with a shimmering shield of order. As a Magic action, you can expend 1 to 5 Sorcery Points to create a magical ward around yourself or another creature you can see within 30 feet of yourself. The ward is represented by a number of d8s equal to the number of Sorcery Points spent to create it. When the warded creature takes damage, it can expend a number of those dice, roll them, and reduce the damage taken by the total rolled on those dice.\n\n"
            "The ward lasts until you finish a Long Rest or until you use this feature again."
        )
    },
    14: {
        'Trance of Order': (
            "You gain the ability to align your consciousness with the endless calculations of Mechanus. As a Bonus Action, you can enter this state for 1 minute. For the duration, attack rolls against you can’t benefit from Advantage, and whenever you make a D20 Test, you can treat a roll of 9 or lower on the d20 as a 10.\n\n"
            "Once you use this feature, you can’t use it again until you finish a Long Rest unless you spend 5 Sorcery Points (no action required) to restore your use of it."
        )
    },
    18: {
        'Clockwork Cavalcade': (
            "You momentarily summon spirits of order to expunge disorder around you. As a Magic action, you summon the spirits in a 30-foot Cube originating from you. The spirits look like modrons or other Constructs of your choice. The spirits are intangible and invulnerable, and they create the effects below within the Cube before vanishing. Once you use this action, you can’t use it again until you finish a Long Rest unless you spend 7 Sorcery Points (no action required) to restore your use of it.\n\n"
            "  - Heal. The spirits restore up to 100 Hit Points, divided as you choose among any number of creatures of your choice in the Cube.\n\n"
            "  - Repair. Any damaged objects entirely in the Cube are repaired instantly.\n\n"
            "  - Dispel. Every spell of level 6 and lower ends on creatures and objects of your choice in the Cube."
        )
    }
}

# Draconic Sorcery Subclass
DRACONIC_SORCERY: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        "Breathe the Magic of Dragons\n\n"
        "Your innate magic comes from the gift of a dragon. Perhaps an ancient dragon facing death bequeathed some of its magical power to you or your ancestor. You might have absorbed magic from a site infused with dragons’ power. Or perhaps you handled a treasure taken from a dragon’s hoard that was steeped in draconic power. Or you might have a dragon for an ancestor."
    ),
    3: {
        'Draconic Resilience': (
            "The magic in your body manifests physical traits of your draconic gift. Your Hit Point maximum increases by 3, and it increases by 1 whenever you gain another Sorcerer level.\n\n"
            "Parts of you are also covered by dragon-like scales. While you aren’t wearing armor, your base Armor Class equals 10 plus your Dexterity and Charisma modifiers."
        ),
        'Draconic Spells': (
            "When you reach a Sorcerer level specified in the Draconic Spells table, you thereafter always have the listed spells prepared.\n\n"
            "Draconic Spells\nSorcerer Level\tSpells\n"
            "3\tAlter Self, Chromatic Orb, Command, Dragon's Breath\n"
            "5\tFear, Fly\n"
            "7\tArcane Eye, Charm Monster\n"
            "9\tLegend Lore, Summon Dragon"
        )
    },
    6: {
        'Elemental Affinity': (
            "Your draconic magic has an affinity with a damage type associated with dragons. Choose one of those types: Acid, Cold, Fire, Lightning, or Poison.\n\n"
            "You have Resistance to that damage type, and when you cast a spell that deals damage of that type, you can add your Charisma modifier to one damage roll of that spell."
        )
    },
    14: {
        'Dragon Wings': (
            "As a Bonus Action, you can cause draconic wings to appear on your back. The wings last for 1 hour or until you dismiss them (no action required). For the duration, you have a Fly Speed of 60 feet.\n\n"
            "Once you use this feature, you can’t use it again until you finish a Long Rest unless you spend 3 Sorcery Points (no action required) to restore your use of it."
        )
    },
    18: {
        'Dragon Companion': (
            "You can cast Summon Dragon without a Material component. You can also cast it once without a spell slot, and you regain the ability to cast it in this way when you finish a Long Rest.\n\n"
            "Whenever you start casting the spell, you can modify it so that it doesn’t require Concentration. If you do so, the spell’s duration becomes 1 minute for that casting."
        )
    }
}

# Wild Magic Sorcery Subclass
WILD_MAGIC_SORCERY: Dict[Union[str, int], Union[str, Dict[str, str]]] = {
    'description': (
        "Unleash Chaotic Magic\n\n"
        "Your innate magic stems from the forces of chaos that underlie the order of creation. You or an ancestor might have endured exposure to raw magic, perhaps through a planar portal leading to Limbo or the Elemental Planes. Perhaps you were blessed by a fey being or marked by a demon. Or your magic could be a fluke with no apparent cause. Whatever its source, this magic churns within you, waiting for any outlet."
    ),
    3: {
        'Wild Magic Surge': (
            "Your spellcasting can unleash surges of untamed magic. Once per turn, you can roll 1d20 immediately after you cast a Sorcerer spell with a spell slot. If you roll a 20, roll on the Wild Magic Surge table to create a magical effect.\n\n"
            "If the magical effect is a spell, it is too wild to be affected by your Metamagic."
        ),
        'Tides of Chaos': (
            "You can manipulate chaos itself to give yourself Advantage on one D20 Test before you roll the d20. Once you do so, you must cast a Sorcerer spell with a spell slot or finish a Long Rest before you can use this feature again.\n\n"
            "If you do cast a Sorcerer spell with a spell slot before you finish a Long Rest, you automatically roll on the Wild Magic Surge table."
        )
    },
    6: {
        'Bend Luck': (
            "You have the ability to twist fate using your wild magic. Immediately after another creature you can see rolls the d20 for a D20 Test, you can take a Reaction and spend 1 Sorcery Point to roll 1d4 and apply the number rolled as a bonus or penalty (your choice) to the d20 roll."
        )
    },
    14: {
        'Controlled Chaos': (
            "You gain a modicum of control over the surges of your wild magic. Whenever you roll on the Wild Magic Surge table, you can roll twice and use either number."
        )
    },
    18: {
        'Tamed Surge': (
            "Immediately after you cast a Sorcerer spell with a spell slot, you can create an effect of your choice from the Wild Magic Surge table instead of rolling on that table. You can choose any effect in the table except for the final row, and if the chosen effect involves a roll, you must make it.\n\n"
            "Once you use this feature, you can’t do so again until you finish a Long Rest."
        )
    }
}

WILD_MAGIC_SURGE_TABLE: Dict[str, str] = {
    "01-04": "Roll on this table at the start of each of your turns for the next minute, ignoring this result on subsequent rolls.",
    "05-08": "A creature that is Friendly toward you appears in a random unoccupied space within 60 feet of you. The creature is under the DM’s control and disappears 1 minute later. Roll 1d4 to determine the creature: on a 1, a Modron Duodrone appears; on a 2, a Flumph appears; on a 3, a Modron Monodrone appears; on a 4, a Unicorn appears. See the Monster Manual for the creature’s stat block.",
    "09-12": "For the next minute, you regain 5 Hit Points at the start of each of your turns.",
    "13-16": "Creatures have Disadvantage on saving throws against the next spell you cast in the next minute that involves a saving throw.",
    "17-20": "You are subjected to an effect that lasts for 1 minute unless its description says otherwise. Roll 1d8 to determine the effect: on a 1, you’re surrounded by faint, ethereal music only you and creatures within 5 feet of you can hear; on a 2, your size increases by one size category; on a 3, you grow a long beard made of feathers that remains until you sneeze, at which point the feathers explode from your face and vanish; on a 4, you must shout when you speak; on a 5, illusory butterflies flutter in the air within 10 feet of you; on a 6, an eye appears on your forehead, granting you Advantage on Wisdom (Perception) checks; on an 7, pink bubbles float out of your mouth whenever you speak; on an 8, your skin turns a vibrant shade of blue for 24 hours or until the effect is ended by a Remove Curse spell.",
    "21-24": "For the next minute, all your spells with a casting time of an action have a casting time of a Bonus Action.",
    "25-28": "You are transported to the Astral Plane until the end of your next turn. You then return to the space you previously occupied or the nearest unoccupied space if that space is occupied.",
    "29-32": "The next time you cast a spell that deals damage within the next minute, don’t roll the spell’s damage dice for the damage. Instead use the highest number possible for each damage die.",
    "33-36": "You have Resistance to all damage for the next minute.",
    "37-40": "You turn into a potted plant until the start of your next turn. While you’re a plant, you have the Incapacitated condition and have Vulnerability to all damage. If you drop to 0 Hit Points, your pot breaks, and your form reverts.",
    "41-44": "For the next minute, you can teleport up to 20 feet as a Bonus Action on each of your turns.",
    "45-48": "You and up to three creatures you choose within 30 feet of you have the Invisible condition for 1 minute. This invisibility ends on a creature immediately after it makes an attack roll, deals damage, or casts a spell.",
    "49-52": "A spectral shield hovers near you for the next minute, granting you a +2 bonus to AC and immunity to Magic Missile.",
    "53-56": "You can take one extra action on this turn.",
    "57-60": "You cast a random spell. If the spell normally requires Concentration, it doesn’t require Concentration in this case; the spell lasts for its full duration. Roll 1d10 to determine the spell: on a 1, Confusion; on a 2, Fireball; on a 3, Fog Cloud; on a 4, Fly (cast on a random creature within 60 feet of you), on a 5, Grease; on a 6, Levitate (cast on yourself); on a 7, Magic Missile (cast as a level 5 spell); on a 8, Mirror Image; on a 9, Polymorph (cast on yourself), and if you fail the saving throw, you turn into a Goat (see appendix B); on a 10, See Invisibility.",
    "61-64": "For the next minute, any flammable, nonmagical object you touch that isn’t being worn or carried by another creature bursts into flame, takes 1d4 Fire damage, and is burning.",
    "65-68": "If you die within the next hour, you immediately revive as if by the Reincarnate spell.",
    "69-72": "You have the Frightened condition until the end of your next turn. The DM determines the source of your fear.",
    "73-76": "You teleport up to 60 feet to an unoccupied space you can see.",
    "77-80": "A random creature within 60 feet of you has the Poisoned condition for 1d4 hours.",
    "81-84": "You radiate Bright Light in a 30-foot radius for the next minute. Any creature that ends its turn within 5 feet of you has the Blinded condition until the end of its next turn.",
    "85-88": "Up to three creatures of your choice that you can see within 30 feet of you take 1d10 Necrotic damage. You regain Hit Points equal to the sum of the Necrotic damage dealt.",
    "89-92": "Up to three creatures of your choice that you can see within 30 feet of you take 4d10 Lightning damage.",
    "93-96": "You and all creatures within 30 feet of you have Vulnerability to Piercing damage for the next minute.",
    "97-00": "Roll 1d6: On a 1, you regain 2d10 Hit Points; on a 2, one ally of your choice within 300 feet of you regains 2d10 Hit Points; on a 3, you regain your lowest-level expended spell slot; on a 4, one ally of your choice within 300 feet of you regains their lowest-level expended spell slot; on a 5, you regain all your expended Sorcery Points; on a 6, all the effects of row 17–20 affect you simultaneously."
}

# Manifestations of Order Table
MANIFESTATIONS_OF_ORDER: Dict[int, str] = {
    1: "Spectral cogwheels hover behind you.",
    2: "The hands of a clock spin in your eyes.",
    3: "Your skin glows with a brassy sheen.",
    4: "Floating equations and geometric objects overlay your body.",
    5: "Your Spellcasting Focus temporarily takes the form of a Tiny clockwork mechanism.",
    6: "The ticking of gears or ringing of a clock can be heard by you and those affected by your magic."
}