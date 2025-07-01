from __future__ import annotations
from prettytable import PrettyTable
from InquirerPy import inquirer
from .barbarian import BARBARIAN_CLASS, BARBARIAN_LEVELS

AVAILABLE_CLASSES = {
    'Barbarian': (BARBARIAN_CLASS, BARBARIAN_LEVELS)
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
    available_skills = [s for s in class_data['proficiencies']['skills'] if s not in already_proficient]
    chosen_skills = []
    if not available_skills:
        print("No available skill proficiencies to choose from.")
    elif len(available_skills) <= 2:
        # If 1 or 2 available, auto-select all
        chosen_skills = available_skills.copy()
        print(f"Automatically selected: {', '.join(chosen_skills)}")
    else:
        chosen_skills = inquirer.checkbox(
            message="Choose 2 skill proficiencies:",
            choices=available_skills,
            validate=lambda result: (len(result) == 2) or ("You must select exactly 2 skills.")
        ).execute()
        # Defensive: If user skips, re-prompt until valid
        while len(chosen_skills) != 2:
            print("You must select exactly 2 skills.")
            chosen_skills = inquirer.checkbox(
                message="Choose 2 skill proficiencies:",
                choices=available_skills,
                validate=lambda result: (len(result) == 2) or ("You must select exactly 2 skills.")
            ).execute()
    # Get class features for the current level
    class_features = []
    if current_level in class_levels:
        class_features = class_levels[current_level].get('features', [])
    return {
        'class_name': class_name,
        'chosen_skills': chosen_skills,
        'class_features': class_features
    }

