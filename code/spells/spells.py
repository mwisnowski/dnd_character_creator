from __future__ import annotations

from .cantrips import CANTRIPS_DICT
from .level1 import FIRST_LEVEL_SPELLS_DICT
from .level2 import SECOND_LEVEL_SPELLS_DICT
from .level3 import THIRD_LEVEL_SPELLS_DICT

def prompt_and_print_class_spell_list():
    """
    Prompts the user for a class name (using inquirer selection from all unique classes in the spell dictionaries)
    and spell level, then prints a dictionary of spells for that class and level.
    """
    import inquirer
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

    try:
        from prettytable import PrettyTable
    except ImportError:
        print("PrettyTable is not installed. Please install it with 'pip install prettytable'.")
        print(filtered)
        return

    if not filtered:
        print("No spells found for this class and level.")
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
