from __future__ import annotations
from prettytable import PrettyTable
from InquirerPy import inquirer
from .barbarian import BARBARIAN_CLASS, BARBARIAN_LEVELS
from .bard import BARD_CLASS, BARD_LEVELS
from .cleric import CLERIC_CLASS, CLERIC_LEVELS
from .class_utils import choose_weapon_mastery, choose_divine_order, choose_extra_cantrip
from misc.skills import SKILLS_DICT
from collections import Counter
import re
from equipment.armor_dict import LIGHT_ARMOR_DICT, MEDIUM_ARMOR_DICT, HEAVY_ARMOR_DICT, SHIELD_DICT
from equipment.weapons_dict import SIMPLE_WEAPONS_DICT, MARTIAL_WEAPONS_DICT, AMMUNITION_DICT
from spells.spells import add_class_spell

AVAILABLE_CLASSES = {
    'Barbarian': (BARBARIAN_CLASS, BARBARIAN_LEVELS),
    'Bard': (BARD_CLASS, BARD_LEVELS),
    'Cleric': (CLERIC_CLASS, CLERIC_LEVELS),
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


def learn_spell(class_name, spellcasting, known_spells):
    """
    Handles the spell learning process for a class at a given level.
    Prompts the user to select all required cantrips and leveled spells not already known.
    Returns a list of (spell_level, spell_name, spell_data) for all newly learned spells.
    """
    learned_spells = []
    # Learn cantrips
    cantrips_to_learn = spellcasting.get('cantrips_known', 0)
    if cantrips_to_learn:
        known_cantrips = set(known_spells.get('Cantrips', {}))
        while len(known_cantrips) < cantrips_to_learn:
            spell_name, spell_data = add_class_spell(class_name, 0, known_cantrips)
            if not spell_name:
                break
            learned_spells.append((0, spell_name, spell_data))
            known_cantrips.add(spell_name)

    # Learn leveled spells (use 'spells_known' if present, else 'spells_prepared')
    spells_to_learn = spellcasting.get('spells_known', spellcasting.get('spells_prepared', 0))
    if spells_to_learn:
        # Gather all available spell levels
        available_levels = []
        for key in spellcasting.get('spell_slots', {}).keys():
            try:
                lvl_num = int(key.split()[-1])
                available_levels.append(lvl_num)
            except (ValueError, IndexError):
                continue
        available_levels = sorted(set(available_levels))
        # Gather all known spells across all available levels
        known_level_spells = set()
        for lvl in available_levels:
            known_level_spells.update(known_spells.get(str(lvl), {}))
        # Loop until the total number of known spells matches spells_to_learn
        while len(known_level_spells) < spells_to_learn:
            # Prompt user to pick a spell level
            level_choices = [str(lvl) for lvl in available_levels]
            spell_level_str = inquirer.select(
                message="Select spell level to learn a new spell:",
                choices=level_choices
            ).execute()
            spell_level = int(spell_level_str)
            # Filter out already known spells at this level
            known_at_level = set(known_spells.get(str(spell_level), {})) | {name for lvl, name, _ in learned_spells if lvl == spell_level}
            spell_name, spell_data = add_class_spell(class_name, spell_level, known_at_level)
            if not spell_name:
                break
            learned_spells.append((spell_level, spell_name, spell_data))
            known_level_spells.add(spell_name)
    return learned_spells


def select_class(current_level=1, already_proficient=None, known_spells=None):
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
    class_name, class_data, class_levels = choose_class(AVAILABLE_CLASSES)
    chosen_skills = choose_proficiencies(class_data, already_proficient)
    equipment, inventory, gold_pieces, silver_pieces, copper_pieces = organize_equipment(class_data)
    class_features = []
    new_spells = []
    extra_choices = {}
    # Gather proficiencies from class_data
    proficiencies = {'weapons': set(), 'armor': set(), 'tools': set()}
    class_profs = class_data.get('proficiencies', {})
    for k in ['weapons', 'armor', 'tools']:
        vals = class_profs.get(k, [])
        if isinstance(vals, str):
            proficiencies[k].add(vals)
        else:
            proficiencies[k].update(vals)
    if current_level in class_levels:
        class_features = class_levels[current_level].get('features', [])
        spellcasting = class_levels[current_level].get('spellcasting')
        # Handle all class-specific feature choices in class_utils
        from .class_utils import handle_class_feature_choices
        extra_choices = handle_class_feature_choices(class_name, class_data, class_features, known_spells)
        if spellcasting:
            new_spells = learn_spell(class_name, spellcasting, known_spells)
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
        **extra_choices
    }

