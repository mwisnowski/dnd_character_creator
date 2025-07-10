from __future__ import annotations

from InquirerPy import inquirer

def invocation_prereqs_met(inv_name, character_level, known_cantrips, known_invocations):
    """
    Check if the prerequisites for an invocation are met.
    """
    prereqs = ELDRITCH_INVOCATIONS[inv_name].get('prerequisite', [])
    for prereq in prereqs:
        if isinstance(prereq, str):
            # Level requirement
            if 'Level' in prereq:
                import re
                match = re.match(r'Level (\d+)\+ Warlock', prereq)
                if match:
                    req_level = int(match.group(1))
                    if character_level < req_level:
                        return False
            # Invocation requirement
            elif 'Invocation' in prereq:
                # e.g., 'Pact of the Blade Invocation'
                required = prereq.replace(' Invocation', '')
                if required not in known_invocations:
                    return False
            # Cantrip requirement (string form)
            elif 'Cantrip' in prereq:
                # e.g., 'a Warlock Cantrip That Deals Damage via an Attack Roll'
                # For now, just require at least one cantrip known
                if not known_cantrips:
                    return False
        elif isinstance(prereq, list):
            # List of cantrips, at least one must be known
            if not any(c in known_cantrips for c in prereq):
                return False
    return True

def choose_invocation(invocations_available, character=None, character_level=None, known_cantrips=None, known_invocations=None):
    """
    Prompt the user to select an invocation from the available list, filtering out any already chosen by the character and for which prerequisites are met.
    Returns the chosen invocation as a string.
    """
    filtered_invocations = list(invocations_available)
    if character is not None:
        already_chosen = set(getattr(character, 'invocations', []))
        filtered_invocations = [i for i in invocations_available if i not in already_chosen]
    if character_level is not None and known_cantrips is not None and known_invocations is not None:
        filtered_invocations = [i for i in filtered_invocations if invocation_prereqs_met(i, character_level, known_cantrips, known_invocations)]
    if not filtered_invocations:
        print("No new invocations available to choose.")
        return None
    invocation = inquirer.select(
        message="Choose an Eldritch Invocation:",
        choices=filtered_invocations
    ).execute()
    return invocation

def add_invocation(character, invocation_data=None, available_invocations=None, character_level=None, known_cantrips=None, known_invocations=None):
    """
    Add an invocation to the character, handling any special logic.
    Returns the invocation name as a string for display.
    """
    if not available_invocations:
        available_invocations = list(ELDRITCH_INVOCATIONS.keys())
    invocation = choose_invocation(
        available_invocations,
        character=character,
        character_level=character_level,
        known_cantrips=known_cantrips,
        known_invocations=known_invocations
    )
    if invocation is None:
        return None
    if character is not None:
        if not hasattr(character, 'invocations'):
            character.invocations = []
        if invocation not in character.invocations:
            character.invocations.append(invocation)
    # Return the invocation name for display purposes
    return invocation

ELDRITCH_INVOCATIONS = {
    'Agonizing Blast': {
        'prerequisite': ['Level 2+ Warlock', ['Chill Touch', 'Eldritch Blast', 'Mind Sliver', 'Poison Spray', 'Thunderclap', 'Toll the Dead']],
        'description': (
            "Choose one of your known Warlock cantrips that deals damage. You can add your Charisma modifier to that spell’s damage rolls."
        ),
        'repeatable': True
    },
    'Armor of Shadows': {
        'prerequisite': [],
        'description': "You can cast Mage Armor on yourself without expending a spell slot.",
        'repeatable': False
    },
    'Ascendant Step': {
        'prerequisite': ['Level 5+ Warlock'],
        'description': "You can cast Levitate on yourself without expending a spell slot.",
        'repeatable': False
    },
    'Devil’s Sight': {
        'prerequisite': ['Level 2+ Warlock'],
        'description': "You can see normally in Dim Light and Darkness—both magical and nonmagical—within 120 feet of yourself.",
        'repeatable': False
    },
    'Devouring Blade': {
        'prerequisite': ['Level 12+ Warlock', 'Thirsting Blade Invocation'],
        'description': "The Extra Attack of your Thirsting Blade invocation confers two extra attacks rather than one.",
        'repeatable': False
    },
    'Eldritch Mind': {
        'prerequisite': [],
        'description': "You have Advantage on Constitution saving throws that you make to maintain Concentration.",
        'repeatable': False
    },
    'Eldritch Smite': {
        'prerequisite': ['Level 5+ Warlock', 'Pact of the Blade Invocation'],
        'description': (
            "Once per turn when you hit a creature with your pact weapon, you can expend a Pact Magic spell slot to deal an extra 1d8 Force damage to the target, plus another 1d8 per level of the spell slot, and you can give the target the Prone condition if it is Huge or smaller."
        ),
        'repeatable': False
    },
    'Eldritch Spear': {
        'prerequisite': ['Level 2+ Warlock', ['Chill Touch', 'Eldritch Blast', 'Mind Sliver', 'Poison Spray', 'Thunderclap', 'Toll the Dead']],
        'description': (
            "Choose one of your known Warlock cantrips that deals damage and has a range of 10+ feet. When you cast that spell, its range increases by a number of feet equal to 30 times your Warlock level."
        ),
        'repeatable': True
    },
    'Fiendish Vigor': {
        'prerequisite': ['Level 2+ Warlock'],
        'description': (
            "You can cast False Life on yourself without expending a spell slot. When you cast the spell with this feature, you don’t roll the die for the Temporary Hit Points; you automatically get the highest number on the die."
        ),
        'repeatable': False
    },
    'Gaze of Two Minds': {
        'prerequisite': ['Level 5+ Warlock'],
        'description': (
            "You can use a Bonus Action to touch a willing creature and perceive through its senses until the end of your next turn. As long as the creature is on the same plane of existence as you, you can take a Bonus Action on subsequent turns to maintain this connection, extending the duration until the end of your next turn. The connection ends if you don’t maintain it in this way.\n\nWhile perceiving through the other creature’s senses, you benefit from any special senses possessed by that creature, and you can cast spells as if you were in your space or the other creature’s space if the two of you are within 60 feet of each other."
        ),
        'repeatable': False
    },
    'Gift of the Depths': {
        'prerequisite': ['Level 5+ Warlock'],
        'description': (
            "You can breathe underwater, and you gain a Swim Speed equal to your Speed.\n\nYou can also cast Water Breathing once without expending a spell slot. You regain the ability to cast it in this way again when you finish a Long Rest."
        ),
        'repeatable': False
    },
    'Gift of the Protectors': {
        'prerequisite': ['Level 9+ Warlock', 'Pact of the Tome Invocation'],
        'description': (
            "A new page appears in your Book of Shadows when you conjure it. With your permission, a creature can take an action to write its name on that page, which can contain a number of names equal to your Charisma modifier (minimum of one name).\n\nWhen any creature whose name is on the page is reduced to 0 Hit Points but not killed outright, the creature magically drops to 1 Hit Point instead. Once this magic is triggered, no creature can benefit from it until you finish a Long Rest.\n\nAs a Magic action, you can erase a name on the page by touching it."
        ),
        'repeatable': False
    },
    'Investment of the Chain Master': {
        'prerequisite': ['Level 5+ Warlock', 'Pact of the Chain Invocation'],
        'description': (
            "When you cast Find Familiar, you infuse the summoned familiar with a measure of your eldritch power, granting the creature the following benefits.\n\nAerial or Aquatic. The familiar gains either a Fly Speed or a Swim Speed (your choice) of 40 feet.\n\nQuick Attack. As a Bonus Action, you can command the familiar to take the Attack action.\n\nNecrotic or Radiant Damage. Whenever the familiar deals Bludgeoning, Piercing, or Slashing damage, you can make it deal Necrotic or Radiant damage instead.\n\nYour Save DC. If the familiar forces a creature to make a saving throw, it uses your spell save DC.\n\nResistance. When the familiar takes damage, you can take a Reaction to grant it Resistance against that damage."
        ),
        'repeatable': False
    },
    'Lessons of the First Ones': {
        'prerequisite': ['Level 2+ Warlock'],
        'description': "You have received knowledge from an elder entity of the multiverse, allowing you to gain one Origin feat of your choice.",
        'repeatable': True
    },
    'Lifedrinker': {
        'prerequisite': ['Level 9+ Warlock', 'Pact of the Blade Invocation'],
        'description': (
            "Once per turn when you hit a creature with your pact weapon, you can deal an extra 1d6 Necrotic, Psychic, or Radiant damage (your choice) to the creature, and you can expend one of your Hit Point Dice to roll it and regain a number of Hit Points equal to the roll plus your Constitution modifier (minimum of 1 Hit Point)."
        ),
        'repeatable': False
    },
    'Mask of Many Faces': {
        'prerequisite': ['Level 2+ Warlock'],
        'description': "You can cast Disguise Self without expending a spell slot.",
        'repeatable': False
    },
    'Master of Myriad Forms': {
        'prerequisite': ['Level 5+ Warlock'],
        'description': "You can cast Alter Self without expending a spell slot.",
        'repeatable': False
    },
    'Misty Visions': {
        'prerequisite': ['Level 2+ Warlock'],
        'description': "You can cast Silent Image without expending a spell slot.",
        'repeatable': False
    },
    'One with Shadows': {
        'prerequisite': ['Level 5+ Warlock'],
        'description': "While you’re in an area of Dim Light or Darkness, you can cast Invisibility on yourself without expending a spell slot.",
        'repeatable': False
    },
    'Otherworldly Leap': {
        'prerequisite': ['Level 2+ Warlock'],
        'description': "You can cast Jump on yourself without expending a spell slot.",
        'repeatable': False
    },
    'Pact of the Blade': {
        'prerequisite': [],
        'description': (
            "As a Bonus Action, you can conjure a pact weapon in your hand—a Simple or Martial Melee weapon of your choice with which you bond—or create a bond with a magic weapon you touch; you can’t bond with a magic weapon if someone else is attuned to it or another Warlock is bonded with it. Until the bond ends, you have proficiency with the weapon, and you can use it as a Spellcasting Focus.\n\nWhenever you attack with the bonded weapon, you can use your Charisma modifier for the attack and damage rolls instead of using Strength or Dexterity; and you can cause the weapon to deal Necrotic, Psychic, or Radiant damage or its normal damage type.\n\nYour bond with the weapon ends if you use this feature’s Bonus Action again, if the weapon is more than 5 feet away from you for 1 minute or more, or if you die. A conjured weapon disappears when the bond ends."
        ),
        'repeatable': False
    },
    'Pact of the Chain': {
        'prerequisite': [],
        'description': (
            "You learn the Find Familiar spell and can cast it as a Magic action without expending a spell slot.\n\nWhen you cast the spell, you choose one of the normal forms for your familiar or one of the following special forms: Imp, Pseudodragon, Quasit, Skeleton, Slaad Tadpole, Sphinx of Wonder, Sprite, or Venomous Snake (see appendix B for the familiar’s stat block).\n\nAdditionally, when you take the Attack action, you can forgo one of your own attacks to allow your familiar to make one attack of its own with its Reaction."
        ),
        'repeatable': False
    },
    'Pact of the Tome': {
        'prerequisite': [],
        'description': (
            "Stitching together strands of shadow, you conjure forth a book in your hand at the end of a Short or Long Rest. This Book of Shadows (you determine its appearance) contains eldritch magic that only you can access, granting you the benefits below. The book disappears if you conjure another book with this feature or if you die.\n\nCantrips and Rituals. When the book appears, choose three cantrips, and choose two level 1 spells that have the Ritual tag. The spells can be from any class’s spell list, and they must be spells you don’t already have prepared. While the book is on your person, you have the chosen spells prepared, and they function as Warlock spells for you.\n\nSpellcasting Focus. You can use the book as a Spellcasting Focus."
        ),
        'repeatable': False
    },
    'Repelling Blast': {
        'prerequisite': ['Level 2+ Warlock', 'a Warlock Cantrip That Deals Damage via an Attack Roll'],
        'description': (
            "Choose one of your known Warlock cantrips that requires an attack roll. When you hit a Large or smaller creature with that cantrip, you can push the creature up to 10 feet straight away from you."
        ),
        'repeatable': True
    },
    'Thirsting Blade': {
        'prerequisite': ['Level 5+ Warlock', 'Pact of the Blade Invocation'],
        'description': (
            "You gain the Extra Attack feature for your pact weapon only. With that feature, you can attack twice with the weapon instead of once when you take the Attack action on your turn."
        ),
        'repeatable': False
    },
    'Visions of Distant Realms': {
        'prerequisite': ['Level 9+ Warlock'],
        'description': "You can cast Arcane Eye without expending a spell slot.",
        'repeatable': False
    },
    'Whispers of the Grave': {
        'prerequisite': ['Level 7+ Warlock'],
        'description': "You can cast Speak with Dead without expending a spell slot.",
        'repeatable': False
    },
    'Witch Sight': {
        'prerequisite': ['Level 15+ Warlock'],
        'description': "You have Truesight with a range of 30 feet.",
        'repeatable': False
    }
}