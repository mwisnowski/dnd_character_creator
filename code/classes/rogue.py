"""
Rogue class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

ROGUE_CLASS: Dict[str, Any] = {
    "name": "Rogue",
    "hit_die": 8,
    "primary_ability": ["Dexterity"],
    "saving_throws": ["Dexterity", "Intelligence"],
    "proficiencies": {
        "armor": ["Light Armor"],
        "weapons": [
            "Simple Weapons",
            "Martial Weapons (Finesse or Light property)"
        ],
        "tools": ["Thieves' Tools"],
        "skills": [
            "Acrobatics", "Athletics", "Deception", "Insight", "Intimidation",
            "Investigation", "Perception", "Persuasion", "Sleight of Hand", "Stealth"
        ],
        "skills_choose": 4
    },
    "starting_equipment": [
        [
            "Leather Armor", "2 Daggers", "Shortsword", "Shortbow", "20 Arrows", "Quiver", "Thieves' Tools", "Burglar's Pack", "8 GP"
        ],
        ["100 GP"]
    ]
}

ROGUE_LEVELS: Dict[int, Dict[str, Any]] = {
    1:  {"proficiency_bonus": 2, "features": ["Expertise", "Sneak Attack", "Thieves' Cant", "Weapon Mastery"], "sneak_attack": "1d6"},
    2:  {"proficiency_bonus": 2, "features": ["Cunning Action"], "sneak_attack": "1d6"},
    3:  {"proficiency_bonus": 2, "features": ["Rogue Subclass", "Steady Aim"], "sneak_attack": "2d6"},
    4:  {"proficiency_bonus": 2, "features": ["Ability Score Improvement"], "sneak_attack": "2d6"},
    5:  {"proficiency_bonus": 3, "features": ["Cunning Strike", "Uncanny Dodge"], "sneak_attack": "3d6"},
    6:  {"proficiency_bonus": 3, "features": ["Expertise"], "sneak_attack": "3d6"},
    7:  {"proficiency_bonus": 3, "features": ["Evasion", "Reliable Talent"], "sneak_attack": "4d6"},
    8:  {"proficiency_bonus": 3, "features": ["Ability Score Improvement"], "sneak_attack": "4d6"},
    9:  {"proficiency_bonus": 4, "features": ["Subclass Feature"], "sneak_attack": "5d6"},
    10: {"proficiency_bonus": 4, "features": ["Ability Score Improvement"], "sneak_attack": "5d6"},
    11: {"proficiency_bonus": 4, "features": ["Improved Cunning Strike"], "sneak_attack": "6d6"},
    12: {"proficiency_bonus": 4, "features": ["Ability Score Improvement"], "sneak_attack": "6d6"},
    13: {"proficiency_bonus": 5, "features": ["Subclass Feature"], "sneak_attack": "7d6"},
    14: {"proficiency_bonus": 5, "features": ["Devious Strikes"], "sneak_attack": "7d6"},
    15: {"proficiency_bonus": 5, "features": ["Slippery Mind"], "sneak_attack": "8d6"},
    16: {"proficiency_bonus": 5, "features": ["Ability Score Improvement"], "sneak_attack": "8d6"},
    17: {"proficiency_bonus": 6, "features": ["Subclass Feature"], "sneak_attack": "9d6"},
    18: {"proficiency_bonus": 6, "features": ["Elusive"], "sneak_attack": "9d6"},
    19: {"proficiency_bonus": 6, "features": ["Epic Boon"], "sneak_attack": "10d6"},
    20: {"proficiency_bonus": 6, "features": ["Stroke of Luck"], "sneak_attack": "10d6"},
}

ROGUE_FEATURES: Dict[str, Any] = {
    "Expertise": (
        "You gain Expertise in two of your skill proficiencies of your choice. Sleight of Hand and Stealth are recommended if you have proficiency in them.\n\n"
        "At Rogue Level 6, you gain Expertise in two more of your skill proficiencies of your choice."
    ),
    "Sneak Attack": (
        "You know how to strike subtly and exploit a foe's distraction. Once per turn you can deal an extra 1d6 damage to one creature you hit with an attack roll if you have Advantage on the roll and the attack uses a Finesse or a Ranged weapon. The extra damage's type is the same as the weapon's type.\n\n"
        "You don't need Advantage on the attack roll if at least one of your allies is within 5 feet of the target, the ally doesn't have the Incapacitated condition and you don't have Disadvantage on the attack roll.\n\n"
        "The extra damage increases as you gain Rogue levels, as shown in the Sneak Attack column of the Rogue Features table."
    ),
    "Thieves' Cant": (
        "You picked up various languages in the communities where you plied your roguish talents. You know Thieves' Cant and one other language of your choice, which you choose from the language tables in Chapter 2."
    ),
    "Weapon Mastery": (
        "Your training with weapons allows you to use the mastery properties of two kinds of weapons of your choice with which you have proficiency, such as Daggers and Shortbows.\n\n"
        "Whenever you finish a Long Rest, you can change the kinds of weapons you chose. For example, you could switch to using the mastery properties of Scimitars and Shortswords."
    ),
    "Cunning Action": (
        "Your quick thinking and agility allow you to move and act quickly. On your turn, you can take one of the following actions as a Bonus Action: Dash, Disengage, or Hide."
    ),
    "Rogue Subclass": (
        "You gain a Rogue subclass of your choice. The Arcane Trickster, Assassin, Soulknife, and the Thief subclasses are detailed after this class's description. A Subclass is a specialization that grants you features at certain Rogue levels. For the rest of your career, you gain each of your subclass’s features that are of your Rogue level or lower."
    ),
    "Steady Aim": (
        "As a Bonus Action, you give yourself Advantage on your next attack roll on your current turn. You can use this feature only if you haven't moved during this turn, and after you use it, your Speed is 0 until the end of the current turn."
    ),
    "Ability Score Improvement": (
        "You gain the Ability Score Improvement feat or another feat of your choice for which you qualify. You gain this feature again at Rogue levels 8, 10, 12, and 16."
    ),
    "Cunning Strike": (
        "You've developed cunning ways to use your Sneak Attack. When you deal Sneak Attack damage, you can add one of the following Cunning Strike effects. Each effect has a die cost, which is the number of Sneak Attack dice you must forgo to add the effect. You remove the die before rolling, and the effect occurs immediately after the attack's damage is dealt. For example, if you add the Poison effect, remove 1d6 from the Sneak Attack's damage before rolling.\n\n"
        "If a Cunning Strike requires a saving throw, the DC equals 8 plus your Dexterity modifier and Proficiency Bonus.\n\n"
        "Poison (Cost: 1d6). You add a toxin to your strike, forcing the target to make a Constitution saving throw. On a failed save, the target has the Poisoned condition for 1 minute. At the end of each of its turns, the poisoned target repeats the save, ending the effect on a success.\n\n"
        "To use this effect, you must have a Poisoner's Kit on your person.\n\n"
        "Trip (Cost: 1d6). If the target is Large or smaller, it must succeed on a Dexterity saving throw or have the Prone condition.\n\n"
        "Withdraw (Cost: 1d6). Immediately after the attack, you move up to half your speed without provoking Opportunity Attacks."
    ),
    "Uncanny Dodge": (
        "When an attacker that you can see hits you with an attack roll, you can take a Reaction to halve the attack's damage against you (round down)."
    ),
    "Evasion": (
        "You can nimbly dodge out of the way of certain dangers. When you're subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw and only half damage if you fail. You can't use this feature if you have the Incapacitated condition."
    ),
    "Reliable Talent": (
        "Whenever you make an ability check that uses one of your skill or tool proficiencies, you can treat a d20 roll of 9 or lower as a 10."
    ),
    "Improved Cunning Strike": (
        "You can use up to two Cunning Strike effects when you deal Sneak Attack damage, paying the die cost for each effect."
    ),
    "Devious Strikes": (
        "You've practiced new ways to use your Sneak Attack deviously. The following effects are now among your Cunning Strike options.\n\n"
        "Daze (Cost: 2d6). The target must succeed on a Constitution saving throw, or on its next turn, it can do only one of the following: move or take an action or a Bonus Action.\n\n"
        "Knock Out (Cost: 6d6). The target must succeed on a Constitution saving throw, or it has the Unconscious condition for 1 minute or until it takes any damage. The Unconscious target repeats the save at the end of its turns, ending the effect on itself on a success.\n\n"
        "Obscure (Cost: 3d6). The target must succeed on a Dexterity saving throw, or it has the Blinded condition until the end of its next turn."
    ),
    "Slippery Mind": (
        "Your mind is exceptionally difficult to control. You gain proficiency in Wisdom and Charisma saving throws."
    ),
    "Elusive": (
        "You're so evasive that attackers rarely gain the upper hand against you. No attack roll can have advantage against you unless you have the Incapacitated condition."
    ),
    "Epic Boon": (
        "You gain an Epic Boon feat or another feat of your choice for which you qualify. Boon of the Night Spirit is recommended."
    ),
    "Stroke of Luck": (
        "You have a marvelous knack for succeeding when you need to. If you fail a d20 Test, you can turn the roll into a 20.\n\n"
        "Once you use this feature, you can't use it again until you finish a Short or Long Rest."
    ),
}

ARCANE_TRICKSTER: Dict[Union[str, int], Any] = {
    "description": "Enhance Stealth with Arcane Spells. Some Rogues enhance their fine-honed skills of stealth and agility with spells, learning magical tricks to aid them in their trade. Some Arcane Tricksters use their talents as pickpockets and burglars, while others are pranksters.",
    3: {
        "Spellcasting": (
            "You have learned to cast spells. See chapter 7 for the rules on spellcasting. The information below details how you use those rules as an Arcane Trickster.\n\n"
            "  - Cantrips. You know three cantrips: Mage Hand and two other cantrips of your choice from the Wizard spell list (See that class's section for its list). Mind Sliver and Minor Illusion are recommended.\n\n"
            "    Whenever you gain a Rogue level, you can replace one of your cantrips, except Mage Hand, with another Wizard cantrip of your choice.\n\n"
            "    When you reach Rogue level 10, you learn another Wizard cantrip of your choice.\n\n"
            "  - Spell Slots. The Arcane Trickster Spellcasting table shows how many spell slots you have to cast your level 1+ spells. You regain all expended spell slots when you finish a Long Rest.\n\n"
            "  - Prepared Spells of Level 1+. You prepare a list of the level 1+ spells that are available for you to cast with this feature. To start, choose three level 1 Wizard spells. Charm Person, Disguise Self and Fog Cloud are recommended.\n\n"
            "    The number of spells on your list increases as you gain Rogue levels, as shown in the Prepared Spells column of the Arcane Trickster Spellcasting table. Whenever that number increases, choose additional Wizard spells until the number of spells on your list matches the number in the Arcane Trickster Spellcasting table. The chosen spells must be of a level for which you have spell slots. For example, if you're a level 7 Rogue, your list of prepared spells can include five Wizard spells of level 1 or 2 in any combination.\n\n"
            "  - Changing Your Prepared Spells. Whenever you gain a Rogue level, you can replace one spell on your list with another Wizard spell for which you have spell slots.\n\n"
            "  - Spellcasting Ability. Intelligence is your Spellcasting ability for your Wizard Spells.\n\n"
            "  - Spellcasting Focus. You can use an Arcane Focus as a Spellcasting Focus for your Wizard Spells."
        ),
        "Mage Hand Legerdemain": (
            "When you cast Mage Hand, you can cast it as a Bonus Action, and you can make the spectral hand Invisible. You can control the hand as a Bonus Action, and through it, you can make Dexterity (Sleight of Hand) checks."
        ),
    },
    9: {
        "Magical Ambush": (
            "If you have the Invisible condition when you cast a spell on a creature, it has Disadvantage on any saving throw it makes against the spell on the same turn."
        ),
    },
    13: {
        "Versatile Trickster": (
            "You gain the ability to distract targets with your Mage Hand. When you use the Trip option of your Cunning Strike on a creature, you can also use that option on another creature within 5 feet of the spectral hand."
        ),
    },
    17: {
        "Spell Thief": (
            "You gain the ability to magically steal the knowledge of how to cast a spell from another spellcaster.\n\n"
            "Immediately after a creature casts a spell that targets you or includes you in its area of effect, you can take a Reaction to force the creature to make an Intelligence saving throw. The DC equals your spell save DC. On a failed save, you negate the spell's effect against you, and you steal the knowledge of the spell if it is at least level 1 and of a level you can cast (it doesn't need to be a Wizard spell). For the next 8 hours, you have the spell prepared. The creature can't cast it until 8 hours have passed.\n\n"
            "Once you steal a spell with this feature, you can't use this feature again until you finish a Long Rest."
        ),
    },
}

ARCANE_TRICKSTER_SPELLCASTING: Dict[int, Dict[str, Union[int, str]]] = {
    3:  {"spells_prepared": 3, "spells_known": 3, "1st": 2, "2nd": 0, "3rd": 0, "4th": 0},
    4:  {"spells_prepared": 4, "spells_known": 4, "1st": 3, "2nd": 0, "3rd": 0, "4th": 0},
    5:  {"spells_prepared": 4, "spells_known": 4, "1st": 3, "2nd": 0, "3rd": 0, "4th": 0},
    6:  {"spells_prepared": 4, "spells_known": 4, "1st": 3, "2nd": 0, "3rd": 0, "4th": 0},
    7:  {"spells_prepared": 5, "spells_known": 5, "1st": 4, "2nd": 2, "3rd": 0, "4th": 0},
    8:  {"spells_prepared": 6, "spells_known": 6, "1st": 4, "2nd": 2, "3rd": 0, "4th": 0},
    9:  {"spells_prepared": 6, "spells_known": 6, "1st": 4, "2nd": 2, "3rd": 0, "4th": 0},
    10: {"spells_prepared": 7, "spells_known": 7, "1st": 4, "2nd": 3, "3rd": 0, "4th": 0},
    11: {"spells_prepared": 8, "spells_known": 8, "1st": 4, "2nd": 3, "3rd": 0, "4th": 0},
    12: {"spells_prepared": 8, "spells_known": 8, "1st": 4, "2nd": 3, "3rd": 0, "4th": 0},
    13: {"spells_prepared": 9, "spells_known": 9, "1st": 4, "2nd": 3, "3rd": 2, "4th": 0},
    14: {"spells_prepared": 10, "spells_known": 10, "1st": 4, "2nd": 3, "3rd": 2, "4th": 0},
    15: {"spells_prepared": 10, "spells_known": 10, "1st": 4, "2nd": 3, "3rd": 2, "4th": 0},
    16: {"spells_prepared": 11, "spells_known": 11, "1st": 4, "2nd": 3, "3rd": 3, "4th": 0},
    17: {"spells_prepared": 11, "spells_known": 11, "1st": 4, "2nd": 3, "3rd": 3, "4th": 0},
    18: {"spells_prepared": 11, "spells_known": 11, "1st": 4, "2nd": 3, "3rd": 3, "4th": 0},
    19: {"spells_prepared": 12, "spells_known": 12, "1st": 4, "2nd": 3, "3rd": 3, "4th": 1},
    20: {"spells_prepared": 13, "spells_known": 13, "1st": 4, "2nd": 3, "3rd": 3, "4th": 1},
}

ASSASSIN: Dict[Union[str, int], Any] = {
    "description": "Practice the Grim Art of Death. An Assassin's training focuses on using stealth, poison, and disguise to eliminate foes with deadly efficiency. While some Rogues who follow this path are hired killers, spies, or bounty hunters, the capabilities of this subclass are equally useful for adventurers facing a variety of monstrous enemies.",
    3: {
        "Assassinate": (
            "You're adept at ambushing a target, granting you the following benefits.\n\n"
            "Initiative. You have Advantage on Initiative rolls.\n\n"
            "Surprising Strikes. During the first round of each combat, you have Advantage on attack rolls against any creature that hasn't taken a turn. If your Sneak Attack hits any target during that round, the target takes extra damage of the weapon's type equal to your Rogue level."
        ),
        "Assassin's Tools": (
            "You gain a Disguise Kit and a Poisoner's Kit, and you have proficiency with them."
        ),
    },
    9: {
        "Infiltration Expertise": (
            "You are an expert at the following techniques that aid your infiltrations.\n\n"
            "Masterful Mimicry. You can unerringly mimic another person's speech, handwriting or both if you have spent at least 1 hour studying them.\n\n"
            "Roving Aim. Your speed isn't reduced to 0 by using Steady Aim."
        ),
    },
    13: {
        "Envenom Weapons": (
            "When you use the Poison option of your Cunning Strike, the target also takes 2d6 Poison damage whenever it fails the saving throw. This damage ignores Resistance to Poison damage."
        ),
    },
    17: {
        "Death Strike": (
            "When you hit with your Sneak Attack on the first round of a combat, the target must succeed on a Constitution saving throw (DC 8 plus your Dexterity modifier and Proficiency Bonus), or the attack's damage is doubled against the target."
        ),
    },
}

SOULKNIFE: Dict[Union[str, int], Any] = {
    "description": "Strike Foes with Psionic Blades. A Soulknife strikes with the mind, cutting through barriers both physical and psychic. These Rogues discover psionic power within themselves and channel it to do their roguish work.",
    3: {
        "Psionic Power": (
            "You harbor a wellspring of psionic energy within yourself. It is represented by your Psionic Energy Dice, which fuel certain powers you have from this subclass. The Soulknife Energy Dice table shows the number of these dice you have when you reach certain Rogue levels, and the table shows the die size.\n\n"
            "Any features in this subclass that use a Psionic Energy Die use only the dice from this subclass. Some of your powers expend a Psionic Energy Die, as specified in the power's description, and you can't use the power if it requires you to use a die when your Psionic Energy Dice are all expended.\n\n"
            "You regain one of your expended Psionic Energy Dice when you finish a Short Rest, and you regain all of them when you finish a Long Rest.\n\n"
            "Psi-Bolstered Knack. If you fail an ability check using a skill or tool with which you have proficiency, you can roll one Psionic Energy Die and add the number rolled to the check, potentially turning failure into success. The die is expended only if the roll then succeeds.\n\n"
            "Psychic Whispers. You can establish telepathic communication between yourself and others. As a Magic action, choose one or more creatures you can see, up to a number of creatures equal to your Proficiency Bonus, and then roll one Psionic Energy Die. For a number of hours equal to the number rolled, the chosen creatures can speak telepathically to you, and you can speak telepathically with them. To send or receive a message (no action required), you and the other creature must be within 1 mile of each other. A creature can end the telepathic connection at any time (no action required)."
        ),
        "Psychic Blades": (
            "You can manifest shimmering blades of psychic energy. Whenever you take the Attack action or make an Opportunity Attack, you can manifest a Psychic Blade in your free hand and make the attack with that blade. The magic blade has the following traits:\n\n"
            "Weapon Category: Simple Melee\n"
            "Damage on a Hit: 1d6 Psychic plus the ability modifier used for the attack roll\n"
            "Properties: Finesse, Thrown (range 60/120 feet)\n"
            "Mastery: Vex (you can use this property, and it doesn't count against the number of properties you can use with Weapon Mastery)\n\n"
            "The blade vanishes immediately after it hits or misses its target, and it leaves no mark if it deals damage.\n\n"
            "After you attack with the blade on your turn, you can make a melee or ranged attack with a second psychic blade as a Bonus Action on the same turn if your other hand is free to create it. The damage die of this bonus attack is 1d4 instead of 1d6."
        ),
    },
    9: {
        "Soul Blades": (
            "You can now use the following powers with your Psychic Blades.\n\n"
            "Homing Strikes. If you make an attack roll with your Psychic Blade and miss the target, you can roll one Psionic Energy Die and add the number rolled to the attack roll. If this causes the attack to hit, the die is expended.\n\n"
            "Psychic Teleportation. As a Bonus Action, you manifest a Psychic Blade, expend one Psionic Energy Die and roll it, and throw the blade at an unoccupied space you can see up to a number of feet away equal to 10 times the number rolled. You then teleport to that space, and the blade vanishes."
        ),
    },
    13: {
        "Psychic Veil": (
            "You can weave a veil of psychic static to mask yourself. As a Magic action, you gain the Invisible condition for 1 hour or until you dismiss the effect (no action required). This invisibility ends early immediately after you deal damage to a creature or you force a creature to make a saving throw.\n\n"
            "Once you use this feature, you can't do so again until you finish a Long Rest unless you expend a Psionic Energy Die (no action required) to restore your use of it."
        ),
    },
    17: {
        "Rend Mind": (
            "You can sweep your Psychic Blades through a creature's mind. When you use you Psychic Blades to deal Sneak Attack damage to a creature, you can force that target to make a Wisdom saving throw (DC 8 plus your Dexterity modifier and Proficiency Bonus). If the save fails, the target has the Stunned condition for 1 minute. The Stunned target repeats the save at the end of its turns, ending the effect on itself with a success.\n\n"
            "Once you use this feature, you can't do so again until you finish a Long Rest unless you expend three Psionic Energy Dice (no action required) to restore your use of it."
        ),
    },
}

SOULKNIFE_ENERGY_DICE: Dict[int, Dict[str, int | str]] = {
    3:  {"die_size": "d6",  "number": 4},
    5:  {"die_size": "d8",  "number": 6},
    9:  {"die_size": "d8",  "number": 8},
    11: {"die_size": "d10", "number": 8},
    13: {"die_size": "d10", "number": 10},
    17: {"die_size": "d12", "number": 12},
}

THIEF: Dict[Union[str, int], Any] = {
    "description": "Hunt for Treasure as a Classic Adventurer. A mix of burglar, treasure hunter, and explorer, you are the epitome of an adventurer. In addition to improving your agility and stealth, you gain abilities useful for delving into ruins and getting maximum benefit from the magic items you find there.",
    3: {
        "Fast Hands": (
            "As a Bonus Action, you can do one of the following.\n\n"
            "Sleight of Hand. Make a Dexterity (Sleight of Hand) check to pick a lock or disarm a trap with Thieves' Tools or to pick a pocket.\n\n"
            "Use an Object. Take the Utilize action, or take the Magic action to use a magic item that requires an action."
        ),
        "Second Story Work": (
            "You've trained to get into especially hard-to-reach places, granting you these benefits.\n\n"
            "Climber. You gain a Climb Speed equal to your Speed.\n\n"
            "Jumper. You can determine your jump distance using your Dexterity rather than your Strength."
        ),
    },
    9: {
        "Supreme Sneak": (
            "You gain the following Cunning Strike option.\n\n"
            "Stealth Attack (Cost: 1d6). If you have the Hide action's Invisible condition, this attack doesn't end that condition on you if you end the turn behind Three-Quarters Cover or Total Cover."
        ),
    },
    13: {
        "Use Magic Device": (
            "You've learned how to maximize use of magic items, granting you the following benefits.\n\n"
            "Attunement. You can attune to up to four magic items at once.\n\n"
            "Charges. Whenever you use a magic item property that expends charges, roll 1d6. On a roll of 6, you use the property without expending the charges.\n\n"
            "Scrolls. You can use any *Spell Scroll*, using Intelligence as your spellcasting ability for the spell. If the spell is a cantrip or a level 1 spell, you can cast it reliably. If the scroll contains a higher-level spell, you must first succeed on an Intelligence (Arcana) check (DC 10 plus the spell's level). On a successful check, you cast the spell from the scroll. On a failed check, the scroll disintegrates."
        ),
    },
    17: {
        "Thief's Reflexes": (
            "You are adept at laying ambushes and quickly escaping danger. You can take two turns during the first round of any combat. You take your first turn at your normal Initiative and your second turn at your Initiative minus 10."
        ),
    },
}
