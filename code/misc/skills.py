from __future__ import annotations

from misc.abilities import ability_modifier

SKILLS_DICT: dict[str, str] = {
    'Acrobatics': {
        'description': 'Stay on your feet in a tricky situation, or perform an acrobatic stunt.',
        'ability': 'Dexterity',
        'proficiency': False,
        'expertise': False
    },
    'Animal Handling': {
        'description': 'Calm or train an animal, or get an animal to behave in a certain way.',
        'ability': 'Wisdom',
        'proficiency': False,
        'expertise': False
    },
    'Arcana': {
        'description': 'Recall lore about spells, magic items, and the planes of existence.',
        'ability': 'Intelligence',
        'proficiency': False,
        'expertise': False
    },
    'Athletics': {
        'description': 'Jump farther than normal, stay afloat in rough water, or break something.',
        'ability': 'Strength',
        'proficiency': False,
        'expertise': False
    },
    'Deception': {
        'description': 'Tell a convincing lie, or wear a disguise convincingly.',
        'ability': 'Charisma',
        'proficiency': False,
        'expertise': False
    },
    'History': {
        'description': 'Recall lore about historical events, people, nations, and cultures.',
        'ability': 'Intelligence',
        'proficiency': False,
        'expertise': False
    },
    'Insight': {
        'description': 'Discern a person’s mood and intentions.',
        'ability': 'Wisdom',
        'proficiency': False,
        'expertise': False
    },
    'Intimidation': {
        'description': 'Awe or threaten someone into doing what you want.',
        'ability': 'Charisma',
        'proficiency': False,
        'expertise': False
    },
    'Investigation': {
        'description': 'Find obscure information in books, or deduce how something works.',
        'ability': 'Intelligence',
        'proficiency': False,
        'expertise': False
    },
    'Medicine': {
        'description': 'Diagnose an illness, or determine what killed the recently slain.',
        'ability': 'Wisdom',
        'proficiency': False,
        'expertise': False
    },
    'Nature': {
        'description': 'Recall lore about terrain, plants, animals, and weather.',
        'ability': 'Intelligence',
        'proficiency': False,
        'expertise': False
    },
    'Perception': {
        'description': 'Using a combination of senses, notice something that’s easy to miss.',
        'ability': 'Wisdom',
        'proficiency': False,
        'expertise': False
    },
    'Performance': {
        'description': 'Act, tell a story, perform music, or dance.',
        'ability': 'Charisma',
        'proficiency': False,
        'expertise': False
    },
    'Persuasion': {
        'description': 'Honestly and graciously convince someone of something.',
        'ability': 'Charisma',
        'proficiency': False,
        'expertise': False
    },
    'Religion': {
        'description': 'Recall lore about gods, religious rituals, and holy symbols.',
        'ability': 'Intelligence',
        'proficiency': False,
        'expertise': False
    },
    'Sleight of Hand': {
        'description': 'Pick a pocket, conceal a handheld object, or perform legerdemain.',
        'ability': 'Dexterity',
        'proficiency': False,
        'expertise': False
    },
    'Stealth': {
        'description': 'Escape notice by moving quietly and hiding behind things.',
        'ability': 'Dexterity',
        'proficiency': False,
        'expertise': False
    },
    'Survival': {
        'description': 'Follow tracks, forage, find a trail, or avoid natural hazards.',
        'ability': 'Wisdom',
        'proficiency': False,
        'expertise': False
    }
}


def calculate_skill_scores(ability_scores: dict, proficiency_bonus: int, skills_list: list = None) -> dict:
    """
    Calculate skill values for a character.
    Each skill = ability modifier + proficiency bonus (if proficient).
    skills_list: if provided, only these skills are considered proficient.
    Returns a dict of skill: (value, is_proficient)
    """
    skill_scores = {}
    for skill, info in SKILLS_DICT.items():
        ability = info['ability']
        mod = ability_modifier(ability_scores.get(ability, 10))
        proficient = skills_list is not None and skill in skills_list
        value = mod + (proficiency_bonus if proficient else 0)
        skill_scores[skill] = (value, proficient)
    return skill_scores