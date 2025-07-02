
"""
D&D 5e spell list utilities and CLI spell selection.
Provides functions for prompting and displaying spells by class and level.
"""

from .cantrips import CANTRIPS_DICT
from .level1 import FIRST_LEVEL_SPELLS_DICT
from .level2 import SECOND_LEVEL_SPELLS_DICT
from .level3 import THIRD_LEVEL_SPELLS_DICT
from InquirerPy import inquirer
try:
    from prettytable import PrettyTable
except ImportError:
    PrettyTable = None


def prompt_and_print_class_spell_list():
    """
    Prompts the user for a class name (using inquirer selection from all unique classes in the spell dictionaries)
    and spell level, then prints a dictionary of spells for that class and level.
    Uses PrettyTable for formatted output if available.
    """
    spell_dicts = {
        0: CANTRIPS_DICT,
        1: FIRST_LEVEL_SPELLS_DICT,
        2: SECOND_LEVEL_SPELLS_DICT,
        3: THIRD_LEVEL_SPELLS_DICT,
    }
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
    filtered = {name: data for name, data in spells.items() if class_name in data.get("classes", [])}
    print(f"\n{class_name} level {level} spell list:")

    if not filtered:
        print("No spells found for this class and level.")
        return

    if PrettyTable is None:
        print("PrettyTable is not installed. Please install it with 'pip install prettytable'.")
        print(filtered)
        return

    # Determine columns to show (name, school, casting time, etc. if present)
    # We'll show: Name, School, Casting Time, Range, Duration, Description (if present)
    columns = ["Name", "School", "Casting Time", "Range", "Duration", "Description"]
    table = PrettyTable()
    table.field_names = columns
    for name, data in filtered.items():
        table.add_row([
            name,
            data.get("school", ""),
            data.get("casting_time", ""),
            data.get("range", ""),
            data.get("duration", ""),
            (data.get("description", "") or "")[:60] + ("..." if data.get("description") and len(data.get("description")) > 60 else "")
        ])
    print(table)

def add_class_spell(class_name, level, known_spells=None):
    """
    Prompts the user to select a spell for the given class and level, displaying a PrettyTable of available spells.
    Only spells not already in known_spells are selectable. Uses inquirer with bottom>top cycling.

    Args:
        class_name (str): The class for which to select a spell.
        level (int): The spell level (0 for cantrips).
        known_spells (list or set, optional): List or set of already known spell names for this level.

    Returns:
        tuple: (spell_name, spell_data) for the selected spell, or (None, None) if cancelled.
    """

    if PrettyTable is None:
        print("PrettyTable is not installed. Please install it with 'pip install prettytable'.")
        return None, None

    spell_dicts = {
        0: CANTRIPS_DICT,
        1: FIRST_LEVEL_SPELLS_DICT,
        2: SECOND_LEVEL_SPELLS_DICT,
        3: THIRD_LEVEL_SPELLS_DICT,
    }
    spells = spell_dicts.get(level, {})
    # Filter for class and not already known
    if known_spells is None:
        known_spells = set()
    else:
        known_spells = set(known_spells)
    filtered = {name: data for name, data in spells.items() if class_name in data.get("classes", []) and name not in known_spells}
    if not filtered:
        print("No available spells for this class and level (or all are already known).")
        return None, None

    # Display table
    columns = ["Name", "School", "Casting Time", "Range", "Duration", "Description"]
    table = PrettyTable()
    table.field_names = columns
    table.align = "l"
    for name, data in filtered.items():
        table.add_row([
            name,
            data.get("school", ""),
            data.get("casting_time", ""),
            data.get("range", ""),
            data.get("duration", ""),
            (data.get("description", "") or "")[:60] + ("..." if data.get("description") and len(data.get("description")) > 60 else "")
        ])
    print(table)

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
