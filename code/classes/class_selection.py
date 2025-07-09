"""
class_selection.py

This module handles the interactive selection and setup of D&D character classes, including:
- Presenting available classes and subclasses for user selection
- Displaying class progression, spellcasting, and special tables (e.g., Martial Arts)
- Guiding the user through skill proficiency and equipment choices
- Organizing starting equipment, inventory, and currency
- Managing spell learning for spellcasting classes
- Integrating with class data, feature browsing, and utility functions
"""

# Standard libraries
from collections import Counter
import re

# 3rd-party imports
from InquirerPy import inquirer

# Local imports
from .class_utils import (
    AVAILABLE_CLASSES,
    browse_class_features_prompt,
    display_class_tables,
    handle_class_feature_spells,
    choose_proficiencies,
    organize_equipment,
    learn_spell
)

def choose_class(available_classes):
    """
    Handles the class selection and confirmation loop.

    Prompts the user to select a class from the available options, displays the class tables for review,
    and asks for confirmation. If the user declines, the selection restarts.

    Args:
        available_classes (dict): Dictionary mapping class names to (class_data, class_levels) tuples.

    Returns:
        tuple: (class_name, class_data, class_levels) for the selected class.
    """
    while True:
        class_choices = list(available_classes.keys())
        class_name = inquirer.select(
            message="Select a class:",
            choices=class_choices
        ).execute()
        class_data, class_levels, class_features, subclass_dicts = available_classes[class_name]
        class_hit_die = class_data.get('hit_die', None)
        if class_hit_die is not None:
            class_hit_die = f"d{class_hit_die}"
        display_class_tables(class_name, class_levels)
        # New: Allow browsing features before confirmation
        result = browse_class_features_prompt(class_name, class_data, class_levels, class_features, subclass_dicts)
        if result == 'back_to_class_selection':
            continue  # Go back to class selection menu
        confirm = inquirer.confirm(
            message=f"Do you want to choose {class_name}?",
            default=True
        ).execute()
        if confirm:
            return class_name, class_data, class_levels, class_hit_die
        else:
            print("Returning to class selection...")

def select_class(current_level=1, already_proficient=None, known_spells=None, character=None):
    """
    Main entry point for class selection and setup.

    Guides the user through selecting a class, choosing skill proficiencies, and organizing starting equipment.
    Returns a dictionary with all relevant class, skill, equipment, and currency information for the character.

    Args:
        current_level (int, optional): The character's starting level. Defaults to 1.
        already_proficient (list, optional): List of skills the character is already proficient in. Defaults to None.
        known_spells (dict, optional): Dictionary of already known spells by level. Defaults to None.

    Returns:
        dict: A dictionary containing the following keys:
            - 'class_name': Name of the chosen class.
            - 'chosen_skills': List of chosen skill proficiencies.
            - 'class_features': List of class features at the current level.
            - 'equipment': List of equipped items.
            - 'inventory': List of other items.
            - 'gold_pieces': Number of gold pieces.
            - 'silver_pieces': Number of silver pieces.
            - 'copper_pieces': Number of copper pieces.
            - 'new_spells': List of (spell_level, spell_name, spell_data) tuples for all newly learned spells.
    """
    if already_proficient is None:
        already_proficient = []
    if known_spells is None:
        known_spells = {}
    class_name, class_data, class_levels, class_hit_die = choose_class(AVAILABLE_CLASSES)
    chosen_skills = choose_proficiencies(class_data, already_proficient)
    equipment, inventory, gold_pieces, silver_pieces, copper_pieces = organize_equipment(class_data)
    class_features = class_levels[current_level].get('features', [])
    new_spells = []
    extra_choices = {}
    spellcasting_ability = None
    # Gather proficiencies from class_data
    proficiencies = {'weapons': set(), 'armor': set(), 'tools': set()}
    class_profs = class_data.get('proficiencies', {})
    for k in ['weapons', 'armor', 'tools']:
        vals = class_profs.get(k, [])
        if isinstance(vals, str):
            proficiencies[k].add(vals)
        else:
            proficiencies[k].update(vals)
    # Get saving throw proficiencies
    saving_throws = class_data.get('saving_throws', [])

    # Handle class feature-granted spells (e.g., Ranger's Favored Enemy)
    class_feature_spells = handle_class_feature_spells(class_name, class_data, class_features)

    # Spellcasting feature spel llearning
    if current_level in class_levels:
        spellcasting = class_levels[current_level].get('spellcasting')
        # Handle all class-specific feature choices in class_utils
        from .class_utils import handle_class_feature_choices
        extra_choices = handle_class_feature_choices(class_name, class_data, class_features, known_spells, character=character)
        if spellcasting:
            # Try to extract spellcasting ability from the Spellcasting feature description
            features_dict = AVAILABLE_CLASSES[class_name][2]
            spellcasting_desc = features_dict.get('Spellcasting')
            # Ensure spellcasting_desc is a string for regex
            if isinstance(spellcasting_desc, (set, list)):
                spellcasting_desc = next((s for s in spellcasting_desc if isinstance(s, str)), None)
            if isinstance(spellcasting_desc, str):
                match = re.search(r'Spellcasting Ability\.\s*([A-Za-z]+) is your spellcasting ability', spellcasting_desc)
                if match:
                    spellcasting_ability = match.group(1)
            # Use known_spells only
            new_spells = learn_spell(class_name, spellcasting, known_spells, class_feature_spells)
    return {
        'class_name': class_name,
        'chosen_skills': chosen_skills,
        'class_features': class_features,
        'equipment': equipment,
        'inventory': inventory,
        'gold_pieces': gold_pieces,
        'silver_pieces': silver_pieces,
        'copper_pieces': copper_pieces,
        'new_spells': new_spells,
        'proficiencies': proficiencies,
        'spellcasting_ability': spellcasting_ability,
        'saving_throws': saving_throws,
        'class_feature_spells': class_feature_spells,
        'class_hit_die': class_hit_die,
        **extra_choices
    }
