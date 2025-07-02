from InquirerPy import inquirer
from equipment.weapons_dict import SIMPLE_WEAPONS_DICT, MARTIAL_WEAPONS_DICT
from spells.spells import add_class_spell

def handle_class_feature_choices(class_name, class_data, class_features, known_spells=None):
    """
    Handles class-specific feature choices and assignments (e.g., Weapon Mastery, Divine Order).
    Modifies class_data and known_spells in-place as needed.
    Returns a dict of extra choices made (e.g., weapon_mastery, divine_order, extra_cantrips).
    """
    if known_spells is None:
        known_spells = {}
    extra_choices = {}
    # Barbarian: Weapon Mastery
    if class_name == 'Barbarian' and 'Weapon Mastery' in class_features:
        weapon_mastery = choose_weapon_mastery(num_choices=2)
        extra_choices['weapon_mastery'] = weapon_mastery
    # Cleric: Divine Order
    if class_name == 'Cleric' and 'Divine Order' in class_features:
        divine_order = choose_divine_order()
        extra_choices['divine_order'] = divine_order
        # Track proficiencies to pass back
        gained_profs = {'weapons': set(), 'armor': set(), 'tools': set()}
        if divine_order == 'Protector':
            # Add heavy armor and martial weapons proficiency
            if 'Heavy Armor' not in class_data['proficiencies']['armor']:
                class_data['proficiencies']['armor'].append('Heavy Armor')
            if 'Martial Weapons' not in class_data['proficiencies']['weapons']:
                class_data['proficiencies']['weapons'].append('Martial Weapons')
            gained_profs['armor'].add('Heavy Armor')
            gained_profs['weapons'].add('Martial Weapons')
            # Only add proficiencies for Protector
            if any(gained_profs.values()):
                extra_choices['gained_proficiencies'] = gained_profs
        elif divine_order == 'Thaumaturge':
            # Prompt for extra cantrip
            known_cantrips = set(known_spells.get('Cantrips', {}))
            spell_name, spell_data = choose_extra_cantrip(class_name, known_cantrips)
            if spell_name:
                if 'Cantrips' not in known_spells:
                    known_spells['Cantrips'] = {}
                known_spells['Cantrips'][spell_name] = spell_data
                if 'extra_cantrips' not in extra_choices:
                    extra_choices['extra_cantrips'] = []
                extra_choices['extra_cantrips'].append((spell_name, spell_data))
    return extra_choices

"""
Utility functions for handling class-specific feature choices and prompts.
Includes Barbarian Weapon Mastery and Cleric Divine Order logic.
"""
def choose_weapon_mastery(num_choices=2):
    """
    Prompt the user to select weapon types for Weapon Mastery (Barbarian feature).
    Returns a list of chosen weapon names.
    """
    weapon_choices = list(SIMPLE_WEAPONS_DICT.keys()) + list(MARTIAL_WEAPONS_DICT.keys())
    selected = inquirer.checkbox(
        message=f"Choose {num_choices} weapons for Weapon Mastery:",
        choices=weapon_choices,
        validate=lambda result: (len(result) == num_choices) or (f"You must select exactly {num_choices} weapons.")
    ).execute()
    while len(selected) != num_choices:
        print(f"You must select exactly {num_choices} weapons.")
        selected = inquirer.checkbox(
            message=f"Choose {num_choices} weapons for Weapon Mastery:",
            choices=weapon_choices,
            validate=lambda result: (len(result) == num_choices) or (f"You must select exactly {num_choices} weapons.")
        ).execute()
    return selected

def choose_divine_order():
    """
    Prompt the user to select a Divine Order for Cleric: Protector or Thaumaturge.
    Returns the chosen order as a string.
    """
    order = inquirer.select(
        message="Choose your Divine Order:",
        choices=["Protector (Martial Weapons & Heavy Armor)", "Thaumaturge (Extra Cantrip, Arcana/Religion bonus)"]
    ).execute()
    if order.startswith("Protector"):
        return "Protector"
    else:
        return "Thaumaturge"

def choose_extra_cantrip(class_name, known_cantrips):
    """
    Prompt the user to select an extra cantrip (for Thaumaturge Divine Order).
    Returns (spell_name, spell_data) tuple.
    """
    spell_name, spell_data = add_class_spell(class_name, 0, set(known_cantrips))
    return spell_name, spell_data
