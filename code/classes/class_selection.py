from __future__ import annotations
from prettytable import PrettyTable
from InquirerPy import inquirer
from .barbarian import BARBARIAN_CLASS, BARBARIAN_LEVELS
from .bard import BARD_CLASS, BARD_LEVELS
from misc.skills import SKILLS_DICT
from collections import Counter
import re
from equipment.armor_dict import LIGHT_ARMOR_DICT, MEDIUM_ARMOR_DICT, HEAVY_ARMOR_DICT, SHIELD_DICT
from equipment.weapons_dict import SIMPLE_WEAPONS_DICT, MARTIAL_WEAPONS_DICT, AMMUNITION_DICT

AVAILABLE_CLASSES = {
    'Barbarian': (BARBARIAN_CLASS, BARBARIAN_LEVELS),
    'Bard': (BARD_CLASS, BARD_LEVELS),
}

def display_class_tables(class_name, class_levels):
    """
    Display the class progression and spellcasting tables for the selected class.

    This function prints two tables using PrettyTable:
    1. The class progression table, showing level-based features and stats for the class.
    2. If the class has spellcasting, a separate spellcasting table is shown, with spell slot progression and other spell-related info.

    Args:
        class_name (str): The name of the class being displayed.
        class_levels (dict): A dictionary mapping level numbers to dictionaries of level-specific data (features, spellcasting, etc).
    """
    all_columns = set()
    for lvl_data in class_levels.values():
        all_columns.update(lvl_data.keys())
    columns = ['Level'] + [col for col in sorted(all_columns) if col not in ('features', 'spellcasting')]
    if 'features' in all_columns:
        columns.append('features')
    table = PrettyTable()
    table.field_names = [col.capitalize().replace('_', ' ') for col in columns]
    table.align = "l"
    for lvl in sorted(class_levels.keys()):
        row = class_levels[lvl]
        row_data = [
            lvl,
            *[row.get(col, '-') if col != 'features' else ', '.join(row.get('features', [])) for col in columns[1:]]
        ]
        table.add_row(row_data)
    print(f"\n{class_name} Progression Table:")
    print(table)
    # Spellcasting table
    has_spellcasting = any('spellcasting' in lvl_data for lvl_data in class_levels.values())
    if has_spellcasting:
        spell_cols = set()
        for lvl_data in class_levels.values():
            if 'spellcasting' in lvl_data:
                spell_cols.update(lvl_data['spellcasting'].keys())
        spell_cols.discard('spells_known')
        spell_cols = [col for col in sorted(spell_cols) if col != 'spell_slots'] + (['spell_slots'] if 'spell_slots' in spell_cols else [])
        spell_cols = ['Level'] + spell_cols
        spellcasting_table = PrettyTable()
        spellcasting_table.field_names = [col.capitalize().replace('_', ' ') for col in spell_cols]
        spellcasting_table.align = "l"
        for lvl in sorted(class_levels.keys()):
            row = class_levels[lvl]
            if 'spellcasting' in row:
                spell_row = [lvl]
                for col in spell_cols[1:]:
                    val = row['spellcasting'].get(col, '-')
                    if col == 'spell_slots' and isinstance(val, dict):
                        val = ', '.join(f"{k}: {v}" for k, v in val.items())
                    spell_row.append(val)
                spellcasting_table.add_row(spell_row)
        print(f"\n{class_name} Spellcasting Table:")
        print(spellcasting_table)


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
        class_data, class_levels = available_classes[class_name]
        display_class_tables(class_name, class_levels)
        confirm = inquirer.confirm(
            message=f"Do you want to choose {class_name}?",
            default=True
        ).execute()
        if confirm:
            return class_name, class_data, class_levels
        else:
            print("Returning to class selection...")


def choose_proficiencies(class_data, already_proficient):
    """
    Handles skill proficiency selection for the chosen class.

    Prompts the user to select skill proficiencies based on the class's rules. Supports both "choose any N skills" and
    fixed skill lists. Ensures the user cannot select skills they are already proficient in.

    Args:
        class_data (dict): The class data dictionary, including proficiency info.
        already_proficient (list): List of skills the character is already proficient in.

    Returns:
        list: The list of chosen skill proficiencies.
    """
    chosen_skills = []
    skills_prof = class_data['proficiencies']['skills']
    any_skills_match = re.match(r'Choose any (\d+) skills', skills_prof[0]) if skills_prof and isinstance(skills_prof[0], str) else None
    if any_skills_match:
        num_skills = int(any_skills_match.group(1))
        all_skills = list(SKILLS_DICT.keys())
        available_skills = [s for s in all_skills if s not in already_proficient]
        chosen_skills = inquirer.checkbox(
            message=f"Choose {num_skills} skill proficiencies:",
            choices=available_skills,
            validate=lambda result: (len(result) == num_skills) or (f"You must select exactly {num_skills} skills.")
        ).execute()
        while len(chosen_skills) != num_skills:
            print(f"You must select exactly {num_skills} skills.")
            chosen_skills = inquirer.checkbox(
                message=f"Choose {num_skills} skill proficiencies:",
                choices=available_skills,
                validate=lambda result: (len(result) == num_skills) or (f"You must select exactly {num_skills} skills.")
            ).execute()
    else:
        available_skills = [s for s in skills_prof if s not in already_proficient]
        if not available_skills:
            print("No available skill proficiencies to choose from.")
        elif len(available_skills) <= 2:
            chosen_skills = available_skills.copy()
            print(f"Automatically selected: {', '.join(chosen_skills)}")
        else:
            chosen_skills = inquirer.checkbox(
                message="Choose 2 skill proficiencies:",
                choices=available_skills,
                validate=lambda result: (len(result) == 2) or ("You must select exactly 2 skills.")
            ).execute()
            while len(chosen_skills) != 2:
                print("You must select exactly 2 skills.")
                chosen_skills = inquirer.checkbox(
                    message="Choose 2 skill proficiencies:",
                    choices=available_skills,
                    validate=lambda result: (len(result) == 2) or ("You must select exactly 2 skills.")
                ).execute()
    return chosen_skills


def organize_equipment(class_data):
    """
    Handles equipment, inventory, and currency selection and organization for the chosen class.

    Prompts the user to choose between equipment options if multiple are available, parses the selected items,
    and sorts them into equipment, inventory, and currency. Handles item quantities and recognizes armor, weapons,
    and ammunition using the relevant dictionaries.

    Args:
        class_data (dict): The class data dictionary, including starting equipment info.

    Returns:
        tuple: (equipment, inventory, gold_pieces, silver_pieces, copper_pieces)
            - equipment (list): List of equipped items (with quantities if >1).
            - inventory (list): List of other items.
            - gold_pieces (int): Number of gold pieces.
            - silver_pieces (int): Number of silver pieces.
            - copper_pieces (int): Number of copper pieces.
    """
    equipment = []
    inventory = []
    gold_pieces = 0
    silver_pieces = 0
    copper_pieces = 0
    if class_data and 'starting_equipment' in class_data:
        equip_choices = class_data['starting_equipment']
        if len(equip_choices) > 1:
            equip_choice = inquirer.select(
                message="Choose your starting equipment:",
                choices=[f"Option {i+1}: {', '.join(opt)}" for i, opt in enumerate(equip_choices)]
            ).execute()
            idx = int(equip_choice.split()[1].replace(':','')) - 1
            selected_items = equip_choices[idx]
        else:
            selected_items = equip_choices[0]
        for item in selected_items:
            gp_match = re.match(r"(\d+) GP", item)
            sp_match = re.match(r"(\d+) SP", item)
            cp_match = re.match(r"(\d+) CP", item)
            multi_match = re.match(r"(\d+) (.+)", item)
            if gp_match:
                gold_pieces += int(gp_match.group(1))
            elif sp_match:
                silver_pieces += int(sp_match.group(1))
            elif cp_match:
                copper_pieces += int(cp_match.group(1))
            elif multi_match:
                count = int(multi_match.group(1))
                base_item = multi_match.group(2).strip()
                singular_item = base_item.rstrip('s') if base_item.endswith('s') and not base_item.lower().endswith('ss') else base_item
                found = False
                for test_item in (base_item, singular_item):
                    if test_item in LIGHT_ARMOR_DICT or test_item in MEDIUM_ARMOR_DICT or test_item in HEAVY_ARMOR_DICT or test_item in SHIELD_DICT:
                        equipment.extend([test_item]*count)
                        found = True
                        break
                    elif test_item in SIMPLE_WEAPONS_DICT or test_item in MARTIAL_WEAPONS_DICT or test_item in AMMUNITION_DICT:
                        equipment.extend([test_item]*count)
                        found = True
                        break
                if not found:
                    inventory.extend([base_item]*count)
            elif item in LIGHT_ARMOR_DICT or item in MEDIUM_ARMOR_DICT or item in HEAVY_ARMOR_DICT or item in SHIELD_DICT:
                equipment.append(item)
            elif item in SIMPLE_WEAPONS_DICT or item in MARTIAL_WEAPONS_DICT or item in AMMUNITION_DICT:
                equipment.append(item)
            else:
                inventory.append(item)
        equip_counter = Counter(equipment)
        equipment = [f"{name} x {count}" if count > 1 else name for name, count in equip_counter.items()]
    return equipment, inventory, gold_pieces, silver_pieces, copper_pieces


def select_class(current_level=1, already_proficient=None):
    """
    Main entry point for class selection and setup.

    Guides the user through selecting a class, choosing skill proficiencies, and organizing starting equipment.
    Returns a dictionary with all relevant class, skill, equipment, and currency information for the character.

    Args:
        current_level (int, optional): The character's starting level. Defaults to 1.
        already_proficient (list, optional): List of skills the character is already proficient in. Defaults to None.

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
    """
    if already_proficient is None:
        already_proficient = []
    class_name, class_data, class_levels = choose_class(AVAILABLE_CLASSES)
    chosen_skills = choose_proficiencies(class_data, already_proficient)
    equipment, inventory, gold_pieces, silver_pieces, copper_pieces = organize_equipment(class_data)
    class_features = []
    if current_level in class_levels:
        class_features = class_levels[current_level].get('features', [])
    return {
        'class_name': class_name,
        'chosen_skills': chosen_skills,
        'class_features': class_features,
        'equipment': equipment,
        'inventory': inventory,
        'gold_pieces': gold_pieces,
        'silver_pieces': silver_pieces,
        'copper_pieces': copper_pieces
    }

