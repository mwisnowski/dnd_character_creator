from __future__ import annotations
from prettytable import PrettyTable
from InquirerPy import inquirer

from .barbarian import BARBARIAN_CLASS, BARBARIAN_LEVELS
from .bard import BARD_CLASS, BARD_LEVELS
from misc.skills import SKILLS_DICT

AVAILABLE_CLASSES = {
    'Barbarian': (BARBARIAN_CLASS, BARBARIAN_LEVELS),
    'Bard': (BARD_CLASS, BARD_LEVELS),
}

def select_class(current_level=1, already_proficient=None):
    """
    Presents a list of available classes, displays the class table, and prompts for confirmation.
    Returns a dict with class_name, chosen_skills, and class_features for the selected level.
    """
    if already_proficient is None:
        already_proficient = []
    # Use inquirer for class selection
    class_choices = list(AVAILABLE_CLASSES.keys())
    class_name = inquirer.select(
        message="Select a class:",
        choices=class_choices
    ).execute()
    class_data, class_levels = AVAILABLE_CLASSES[class_name]
    # Display class table
    table = PrettyTable()
    table.field_names = ["Level", "Features", "Rages/Day", "Rage Bonus", "Weapon Masteries"]
    for lvl in sorted(class_levels.keys()):
        row = class_levels[lvl]
        table.add_row([
            lvl,
            ", ".join(row.get('features', [])),
            row.get('rages_per_day', '-'),
            row.get('rage_damage_bonus', '-'),
            row.get('weapon_masteries', '-')
        ])
    print(f"\n{class_name} Progression Table:")
    print(table)
    confirm = inquirer.confirm(
        message=f"Do you want to choose {class_name}?",
        default=True
    ).execute()
    if not confirm:
        print("Class selection cancelled.")
        return None
    # Skill proficiency selection
    chosen_skills = []
    skills_prof = class_data['proficiencies']['skills']
    import re
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
    # Equipment selection
    import re
    from equipment.armor_dict import LIGHT_ARMOR_DICT, MEDIUM_ARMOR_DICT, HEAVY_ARMOR_DICT, SHIELD_DICT
    from equipment.weapons_dict import SIMPLE_WEAPONS_DICT, MARTIAL_WEAPONS_DICT, AMMUNITION_DICT
    equipment = []
    inventory = []
    gold_pieces = 0
    silver_pieces = 0
    copper_pieces = 0
    class_dict = class_data
    if class_dict and 'starting_equipment' in class_dict:
        equip_choices = class_dict['starting_equipment']
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
            # Check for multiples, e.g. '2 Daggers', '4 Handaxes', '20 Arrows'
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
                # Remove plural 's' for common items, but keep as is for arrows/bolts/etc.
                # Try to match singular in equipment dicts
                singular_item = base_item.rstrip('s') if base_item.endswith('s') and not base_item.lower().endswith('ss') else base_item
                # Try both base_item and singular_item for matching
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
        # After collecting, collapse multiples in equipment to '[item] x [amount]'
        from collections import Counter
        equip_counter = Counter(equipment)
        equipment = [f"{name} x {count}" if count > 1 else name for name, count in equip_counter.items()]
    # Get class features for the current level
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

