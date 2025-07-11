"""
spells.py
---------
D&D 5e spell list utilities and CLI spell selection.
Provides functions for prompting and displaying spells by class and level.

Functions:
    prompt_and_print_class_spell_list(): Prompts for class and level, then displays available spells.
    add_class_spell(class_name, level, known_spells=None): Prompts user to select a spell for a class/level, excluding already known spells.
"""

from .spells_utils import get_spell_dicts, filter_spells_by_class_and_known, print_spell_table
from InquirerPy import inquirer
try:
    from prettytable import PrettyTable
except ImportError:
    PrettyTable = None


def prompt_and_print_class_spell_list():
    """
    Prompts the user for a class name (using inquirer selection from all unique classes in the spell dictionaries)
    and spell level, then prints a table of spells for that class and level.
    Uses PrettyTable for formatted output if available.

    Returns:
        None
    """
    spell_dicts = get_spell_dicts()
    # Collect all unique classes from all spell dictionaries
    all_classes = set()
    for d in spell_dicts.values():
        for spell in d.values():
            all_classes.update(spell.get("classes", []))
    all_classes = sorted(all_classes)

    questions = [
        inquirer.List(
            "class_name",
            message="Select a class:",
            choices=all_classes
        ),
        inquirer.List(
            "level",
            message="Select spell level:",
            choices=[("Cantrips (0)", 0), ("1st Level", 1), ("2nd Level", 2), ("3rd Level", 3)]
        )
    ]
    answers = inquirer.prompt(questions)
    if not answers:
        print("No selection made.")
        return
    class_name = answers["class_name"]
    level = answers["level"]
    spells = spell_dicts[level]
    filtered = filter_spells_by_class_and_known(spells, class_name)
    print(f"\n{class_name} level {level} spell list:")

    if not filtered:
        print("No spells found for this class and level.")
        return

    columns = ["Name", "School", "Casting Time", "Range", "Duration", "Description"]
    print_spell_table(filtered, columns, PrettyTable)

def add_class_spell(class_name, level, known_spells=None, exclude_spells=None):
    """
    Prompts the user to select a spell for the given class and level, displaying a PrettyTable of available spells.
    Only spells not already in known_spells or exclude_spells are selectable. Uses inquirer with bottom>top cycling.

    Args:
        class_name (str): The class for which to select a spell.
        level (int): The spell level (0 for cantrips).
        known_spells (list or set, optional): List or set of already known spell names for this level.
        exclude_spells (list or set, optional): List or set of spell names to exclude (e.g., feature-granted spells).

    Returns:
        tuple: (spell_name, spell_data) for the selected spell, or (None, None) if cancelled.
    """
    if PrettyTable is None:
        print("PrettyTable is not installed. Please install it with 'pip install prettytable'.")
        return None, None

    spell_dicts = get_spell_dicts()
    spells = spell_dicts.get(level, {})
    filtered = filter_spells_by_class_and_known(spells, class_name, known_spells, exclude_spells)
    if not filtered:
        print("No available spells for this class and level (or all are already known or granted by features).")
        return None, None

    columns = ["Name", "School", "Casting Time", "Range", "Duration", "Description"]
    print_spell_table(filtered, columns, PrettyTable)

    # Inquirer prompt with bottom>top cycling
    spell_choices = list(filtered.keys())
    if not spell_choices:
        print("No selectable spells.")
        return None, None
    spell_name = inquirer.select(
        message="Select a spell:",
        choices=spell_choices,
        cycle=True,
        pointer=">"
    ).execute()
    if not spell_name:
        print("No spell selected.")
        return None, None
    return spell_name, filtered[spell_name]
