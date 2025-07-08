"""
spells_utils.py
----------------
Helper functions for D&D 5e spell utilities.
Provides reusable logic for filtering, displaying, and managing spell data.

Functions:
    get_spell_dicts(): Returns a dictionary mapping spell levels to their respective spell dictionaries.
    filter_spells_by_class_and_known(spells, class_name, known_spells=None): Filters spells by class and optionally excludes already known spells.
    print_spell_table(filtered, columns, prettytable_cls=None): Prints a PrettyTable of spells with selected columns.
"""

def get_spell_dicts():
    """
    Import and return a dictionary mapping spell levels to their respective spell dictionaries.

    Returns:
        dict: {level: spell_dict} for levels 0-3.
    """
    from .cantrips import CANTRIPS_DICT
    from .level1 import FIRST_LEVEL_SPELLS_DICT
    from .level2 import SECOND_LEVEL_SPELLS_DICT
    from .level3 import THIRD_LEVEL_SPELLS_DICT
    return {
        0: CANTRIPS_DICT,
        1: FIRST_LEVEL_SPELLS_DICT,
        2: SECOND_LEVEL_SPELLS_DICT,
        3: THIRD_LEVEL_SPELLS_DICT,
    }

def filter_spells_by_class_and_known(spells, class_name, known_spells=None, exclude_spells=None):
    """
    Filter a spell dictionary for spells available to a given class, optionally excluding already known spells and any in exclude_spells.

    Args:
        spells (dict): Dictionary of spells to filter.
        class_name (str): The class to filter spells for.
        known_spells (set or list, optional): Spells to exclude from the result.
        exclude_spells (set or list, optional): Additional spells to exclude (e.g., feature-granted spells).

    Returns:
        dict: Filtered dictionary of spells for the class and not already known or excluded.
    """
    if known_spells is None:
        known_spells = set()
    else:
        known_spells = set(known_spells)
    if exclude_spells is None:
        exclude_spells = set()
    else:
        exclude_spells = set(exclude_spells)
    all_excluded = known_spells | exclude_spells
    return {name: data for name, data in spells.items() if class_name in data.get("classes", []) and name not in all_excluded}

def print_spell_table(filtered, columns, prettytable_cls=None):
    """
    Print a PrettyTable of spells with the given columns.

    Args:
        filtered (dict): Dictionary of spells to display.
        columns (list): List of column names for the table.
        prettytable_cls (type, optional): PrettyTable class to use (for dependency injection/testing).

    Returns:
        None
    """
    if prettytable_cls is None:
        try:
            from prettytable import PrettyTable
        except ImportError:
            print("PrettyTable is not installed. Please install it with 'pip install prettytable'.")
            print(filtered)
            return
    else:
        PrettyTable = prettytable_cls
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
