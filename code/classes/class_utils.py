"""
Class utilities for the D&D character creator.
Handles class-specific feature choices, class and subclass browsing UI, table display utilities, and integration with spell, feat, and equipment logic.
"""

# 3rd-party imports
from InquirerPy import inquirer
from prettytable import PrettyTable, ALL

# Local imports
from misc.feats_utils import add_feat
from misc.feats import FIGHTING_STYLE_FEATS
from equipment.weapons_dict import SIMPLE_WEAPONS_DICT, MARTIAL_WEAPONS_DICT
from spells.spells import add_class_spell
from .barbarian import BARBARIAN_CLASS, BARBARIAN_LEVELS, BARBARIAN_FEATURES, PATH_OF_THE_BERSERKER, PATH_OF_THE_WILD_HEART, PATH_OF_THE_WORLD_TREE, PATH_OF_THE_ZEALOT
from .bard import BARD_CLASS, BARD_LEVELS, BARD_FEATURES, COLLEGE_OF_DANCE, COLLEGE_OF_GLAMOUR, COLLEGE_OF_LORE, COLLEGE_OF_VALOR
from .cleric import CLERIC_CLASS, CLERIC_LEVELS, CLERIC_FEATURES, LIFE_DOMAIN, LIGHT_DOMAIN, WAR_DOMAIN
from .druid import DRUID_CLASS, DRUID_LEVELS, DRUID_FEATURES, CIRCLE_OF_THE_LAND, CIRCLE_OF_THE_MOON, CIRCLE_OF_THE_SEA, CIRCLE_OF_THE_STARS
from .fighter import FIGHTER_CLASS, FIGHTER_LEVELS, FIGHTER_FEATURES, BATTLE_MASTER, CHAMPION, ELDRITCH_KNIGHT, PSI_WARRIOR, ELDRITCH_KNIGHT_SPELLCASTING
from .monk import MONK_CLASS, MONK_LEVELS, MONK_FEATURES, WARRIOR_OF_MERCY, WAY_OF_SHADOW, WAY_OF_THE_ELEMENTS, WAY_OF_THE_OPEN_HAND
from .paladin import PALADIN_CLASS, PALADIN_LEVELS, PALADIN_FEATURES, OATH_OF_DEVOTION, OATH_OF_THE_ANCIENTS, OATH_OF_VENGEANCE
from .ranger import RANGER_CLASS, RANGER_LEVELS, RANGER_FEATURES, BEAST_MASTER, FEY_WANDERER, GLOOM_STALKER, HUNTER, BEAST_OF_THE_LAND, BEAST_OF_THE_SEA, BEAST_OF_THE_SKY
from .rogue import (
    ROGUE_CLASS, ROGUE_LEVELS, ROGUE_FEATURES,
    ARCANE_TRICKSTER, ARCANE_TRICKSTER_SPELLCASTING,
    ASSASSIN, SOULKNIFE, SOULKNIFE_ENERGY_DICE, THIEF
)

# --- AVAILABLE_CLASSES: Central registry of all supported D&D classes and their data ---
AVAILABLE_CLASSES = {
    'Barbarian': (BARBARIAN_CLASS, BARBARIAN_LEVELS, BARBARIAN_FEATURES, {
        'Path of the Berserker': PATH_OF_THE_BERSERKER,
        'Path of the Wild Heart': PATH_OF_THE_WILD_HEART,
        'Path of the World Tree': PATH_OF_THE_WORLD_TREE,
        'Path of the Zealot': PATH_OF_THE_ZEALOT,
    }),
    'Bard': (BARD_CLASS, BARD_LEVELS, BARD_FEATURES, {
        'College of Dance': COLLEGE_OF_DANCE,
        'College of Glamour': COLLEGE_OF_GLAMOUR,
        'College of Lore': COLLEGE_OF_LORE,
        'College of Valor': COLLEGE_OF_VALOR,
    }),
    'Cleric': (CLERIC_CLASS, CLERIC_LEVELS, CLERIC_FEATURES, {
        'Life Domain': LIFE_DOMAIN,
        'Light Domain': LIGHT_DOMAIN,
        'War Domain': WAR_DOMAIN,
    }),
    'Druid': (DRUID_CLASS, DRUID_LEVELS, DRUID_FEATURES, {
        'Circle of the Land': CIRCLE_OF_THE_LAND,
        'Circle of the Moon': CIRCLE_OF_THE_MOON,
        'Circle of the Sea': CIRCLE_OF_THE_SEA,
        'Circle of the Stars': CIRCLE_OF_THE_STARS,
    }),
    'Fighter': (FIGHTER_CLASS, FIGHTER_LEVELS, FIGHTER_FEATURES, {
        'Battle Master': BATTLE_MASTER,
        'Champion': CHAMPION,
        'Eldritch Knight': ELDRITCH_KNIGHT,
        'Psi Warrior': PSI_WARRIOR,
    }),
    'Monk': (MONK_CLASS, MONK_LEVELS, MONK_FEATURES, {
        'Warrior of Mercy': WARRIOR_OF_MERCY,
        'Way of Shadow': WAY_OF_SHADOW,
        'Way of the Elements': WAY_OF_THE_ELEMENTS,
        'Way of the Open Hand': WAY_OF_THE_OPEN_HAND,
    }),
    'Paladin': (PALADIN_CLASS, PALADIN_LEVELS, PALADIN_FEATURES, {
        'Oath of Devotion': OATH_OF_DEVOTION,
        'Oath of the Ancients': OATH_OF_THE_ANCIENTS,
        'Oath of Vengeance': OATH_OF_VENGEANCE,
    }),
    'Ranger': (RANGER_CLASS, RANGER_LEVELS, RANGER_FEATURES, {
        'Beast Master': BEAST_MASTER,
        'Fey Wanderer': FEY_WANDERER,
        'Gloom Stalker': GLOOM_STALKER,
        'Hunter': HUNTER,
    }),
    'Rogue': (ROGUE_CLASS, ROGUE_LEVELS, ROGUE_FEATURES, {
        'Arcane Trickster': ARCANE_TRICKSTER,
        'Assassin': ASSASSIN,
        'Soulknife': SOULKNIFE,
        'Thief': THIEF,
    }),
}

def handle_class_feature_choices(class_name, class_data, class_features, known_spells, character=None):
    """
    Handles class-specific feature choices (e.g., Fighting Style, Divine Domain).
    This function should only update known_spells directly if a feature grants a spell.
    All spells (user-chosen and feature-granted) are managed in known_spells.
    """
    extra_choices = {}
    
    # Barbarian, Fighter, & Paladin: Weapon Mastery
    if class_name in ('Barbarian', 'Fighter', 'Paladin', 'Ranger') and 'Weapon Mastery' in class_features:
        weapon_mastery = choose_weapon_mastery(num_choices=2)
        extra_choices['weapon_mastery'] = weapon_mastery
        
    # Cleric: Divine Order
    if class_name == 'Cleric' and 'Divine Order' in class_features:
        from .cleric import CLERIC_FEATURES
        options = {
            'Protector': {
                'proficiencies': {'weapons': ['Martial Weapons'], 'armor': ['Heavy Armor'], 'tools': []},
                'extra_cantrip': False
            },
            'Thaumaturge': {
                'proficiencies': {'weapons': [], 'armor': [], 'tools': []},
                'extra_cantrip': True
            }
        }
        feature_desc = CLERIC_FEATURES.get('Divine Order', '')
        handle_order_feature(class_name, class_data, known_spells, extra_choices, 'Divine Order', options, feature_desc)
    
    # Druid: Primal Order
    if class_name == 'Druid' and 'Primal Order' in class_features:
        from .druid import DRUID_FEATURES
        options = {
            'Magician': {
                'proficiencies': {'weapons': [], 'armor': [], 'tools': []},
                'extra_cantrip': True
            },
            'Warden': {
                'proficiencies': {'weapons': ['Martial Weapons'], 'armor': ['Medium Armor'], 'tools': []},
                'extra_cantrip': False
            }
        }
        feature_desc = DRUID_FEATURES.get('Primal Order', '')
        handle_order_feature(class_name, class_data, known_spells, extra_choices, 'Primal Order', options, feature_desc)
    
    # Fighter: Fighting Style feat
    feats_gained = []
    if class_name == 'Fighter' and any("Fighting Style" in f for f in class_features):
        # Determine currently known fighting styles (if any)
        known_styles = set()
        # Try to get from class_data or extra_choices if present
        if 'fighting_styles' in class_data and class_data['fighting_styles']:
            known_styles.update(class_data['fighting_styles'])
        elif 'fighting_styles' in extra_choices and extra_choices['fighting_styles']:
            known_styles.update(extra_choices['fighting_styles'])
        # FIGHTING_STYLE_FEATS is a dict: keys are style names
        available_fighting_styles = [style for style in FIGHTING_STYLE_FEATS.keys() if style not in known_styles]
        feat_result = add_feat(
            character=character,  # Pass character instance for proper feat handling
            feat_name='Fighting Style',
            available_fighting_styles=available_fighting_styles
        )
        if feat_result and isinstance(feat_result, dict) and feat_result.get('feat') == 'Fighting Style' and feat_result.get('fighting_style'):
            feats_gained.append(feat_result)
    if feats_gained:
        extra_choices['feats_gained'] = feats_gained

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
    weapon_choices = sorted(set(weapon_choices), key=str.lower)
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

def handle_order_feature(class_name, class_data, known_spells, extra_choices, feature_name, options, feature_desc=None):
    """
    Generic handler for order-like features (e.g., Divine Order, Primal Order).
    options: dict of {option_name: {'proficiencies': {'weapons': [], 'armor': [], 'tools': []}, 'extra_cantrip': bool}}
    feature_desc: string description of the feature to display before prompting.
    Adds the chosen order, gained proficiencies, and extra cantrips to extra_choices.
    """
    if feature_desc:
        print(f"\n{feature_name}:\n{feature_desc}\n")
    order_choices = list(options.keys())
    order = inquirer.select(
        message=f"Choose your {feature_name}:",
        choices=order_choices
    ).execute()
    chosen = order
    extra_choices[feature_name.lower().replace(' ', '_')] = chosen
    gained_profs = {'weapons': set(), 'armor': set(), 'tools': set()}
    # Add proficiencies if any
    for k in ['weapons', 'armor', 'tools']:
        for prof in options[chosen].get('proficiencies', {}).get(k, []):
            if prof not in class_data['proficiencies'][k]:
                class_data['proficiencies'][k].append(prof)
            gained_profs[k].add(prof)
    if any(gained_profs.values()):
        extra_choices['gained_proficiencies'] = gained_profs
    # Handle extra cantrip if needed
    if options[chosen].get('extra_cantrip'):
        known_cantrips = set(known_spells.get('Cantrips', {}))
        spell_name, spell_data = choose_extra_cantrip(class_name, known_cantrips)
        if spell_name:
            if 'Cantrips' not in known_spells:
                known_spells['Cantrips'] = {}
            known_spells['Cantrips'][spell_name] = spell_data
            if 'extra_cantrips' not in extra_choices:
                extra_choices['extra_cantrips'] = []
            extra_choices['extra_cantrips'].append((spell_name, spell_data))

def handle_class_feature_spells(class_name, class_data, class_features):
    """
    Returns a dictionary of spells granted by class features (not chosen by the user).
    Example: Ranger's Favored Enemy grants Hunter's Mark at level 1.
    Returns: {level: {spell_name: spell_data}}
    """
    from spells.spells_utils import get_spell_dicts
    feature_spells = {}
    # Example: Ranger - Favored Enemy grants Hunter's Mark at level 1
    if class_name == 'Ranger' and 'Favored Enemy' in class_features:
        spell_dicts = get_spell_dicts()
        # Hunter's Mark is a 1st-level spell
        spell_name = "Hunter's Mark"
        spell_data = spell_dicts[1].get(spell_name)
        if spell_data:
            feature_spells.setdefault(1, {})[spell_name] = spell_data
    # Add more class/feature spell grants here as needed
    return feature_spells

def display_table(data, title=None, columns=None, field_name_map=None, special_formatters=None):
    """
    Generic PrettyTable display for a list/dict of dicts.
    Args:
        data: dict of dicts or list of dicts (e.g., class_levels, spellcasting table, etc.)
        title: Optional table title to print before the table.
        columns: Optional list of columns to display (if None, auto-detect from data).
        field_name_map: Optional dict to map column keys to display names.
        special_formatters: Optional dict mapping column names to formatting functions.
    """
    if isinstance(data, dict):
        # Assume each value already has 'Level' or equivalent key
        rows = [v for _, v in sorted(data.items())]
    else:
        rows = data
    if not columns:
        columns = set()
        for row in rows:
            columns.update(row.keys())
        columns = sorted(columns)
    table = PrettyTable()
    if field_name_map:
        table.field_names = [field_name_map.get(col, col.capitalize().replace('_', ' ')) for col in columns]
    else:
        table.field_names = [col.capitalize().replace('_', ' ') for col in columns]
    table.align = "l"
    for row in rows:
        row_data = []
        for col in columns:
            val = row.get(col, '-')
            if special_formatters and col in special_formatters:
                val = special_formatters[col](val)
            elif isinstance(val, list):
                val = ', '.join(str(x) for x in val)
            elif isinstance(val, dict):
                val = ', '.join(f"{k}: {v}" for k, v in val.items())
            row_data.append(val)
        table.add_row(row_data)
    if title:
        print(f"\n{title}")
    print(table)

def display_class_tables(class_name, class_levels):
    """
    Display the class progression and spellcasting tables for the selected class.
    """
    # Class progression table
    display_table(class_levels, title=f"{class_name} Progression Table:")

    # Spellcasting table
    has_spellcasting = any('spellcasting' in lvl_data for lvl_data in class_levels.values())
    if has_spellcasting:
        # Build spellcasting table data
        spell_rows = {}
        spell_cols = set()
        for lvl, lvl_data in class_levels.items():
            if 'spellcasting' in lvl_data:
                row = {'Level': lvl}
                for k, v in lvl_data['spellcasting'].items():
                    if k == 'spells_known':
                        continue
                    row[k] = v
                    spell_cols.add(k)
                spell_rows[lvl] = row
        spell_cols = [col for col in sorted(spell_cols) if col != 'spell_slots'] + (['spell_slots'] if 'spell_slots' in spell_cols else [])
        columns = ['Level'] + spell_cols
        display_table(spell_rows, title=f"{class_name} Spellcasting Table:", columns=columns)

    # Special: If class is Monk, show Martial Arts table
    if class_name == 'Monk':
        from .monk import MARTIAL_ARTS
        display_table(MARTIAL_ARTS, title="Monk Martial Arts Table:")

def display_subclass_spellcasting_table(subclass_dict: dict, subclass_name: str) -> None:
    """
    Display the subclass spellcasting table using PrettyTable.
    Args:
        subclass_dict (dict): The subclass spellcasting data.
        subclass_name (str): The name of the subclass.
    """
    table = PrettyTable()
    table.field_names = ["Level", "Spells Prepared", "1st", "2nd", "3rd", "4th"]
    table.align = "l"
    for lvl in sorted(subclass_dict.keys()):
        row = subclass_dict[lvl]
        table.add_row([
            lvl,
            row.get("spells_prepared", "-"),
            row.get("1st", "-"),
            row.get("2nd", "-"),
            row.get("3rd", "-"),
            row.get("4th", "-")
        ])
    print(f"\n{subclass_name} Spellcasting Table:")
    print(table)

def display_dict_table(subclass_name: str, subclass_dict: dict, feature_name: str = None) -> None:
    """
    Display a table for any dict-of-dicts, extracting field names and row values dynamically.
    Args:
        subclass_name (str): The name of the subclass or table.
        subclass_dict (dict): The data dictionary (keys: int/str, values: dict).
        feature_name (str, optional): The feature this table is for (e.g., 'Energy Dice').
    """
    if not subclass_dict:
        print(f"\n{subclass_name}: No data to display.")
        return
    # Get all possible field names from all rows
    field_names = set()
    for row in subclass_dict.values():
        if isinstance(row, dict):
            field_names.update(row.keys())
    field_names = ["Level"] + sorted(field_names)
    table = PrettyTable()
    table.field_names = ["Level"] + [fn.replace('_', ' ').title() for fn in field_names[1:]]
    table.align = "l"
    for lvl in sorted(subclass_dict.keys()):
        row = subclass_dict[lvl]
        row_data = [lvl]
        for fn in field_names[1:]:
            row_data.append(row.get(fn, "-"))
        table.add_row(row_data)
    title = f"\n{subclass_name}"
    if feature_name:
        title = f"{feature_name} Table:"
    else:
        title += " Table:"
    print(title)
    print(table)

def display_stat_block(stat_block: dict, title: str = None):
    """
    Print a D&D-style stat block from a dict, handling nested dicts/lists for readability.
    """
    import textwrap
    def print_kv(key, value, indent=0):
        prefix = ' ' * indent + f"{key.replace('_', ' ').title()}: "
        if isinstance(value, dict):
            print(prefix)
            for k, v in value.items():
                print_kv(k, v, indent + 2)
        elif isinstance(value, list):
            print(prefix)
            for item in value:
                if isinstance(item, dict):
                    for k, v in item.items():
                        print_kv(k, v, indent + 2)
                else:
                    print(' ' * (indent + 2) + str(item))
        else:
            val_str = textwrap.fill(str(value), width=100, subsequent_indent=' ' * (indent + 2))
            print(prefix + val_str)
    if title:
        print(f"\n=== {title} ===")
    for k, v in stat_block.items():
        print_kv(k, v, indent=0)

def browse_class_features_prompt(class_name: str, class_data: dict, class_levels: dict, class_features: dict, subclass_dicts: dict) -> None:
    """
    Interactive prompt to let the user browse class features (and subclass features if present)
    before confirming their class choice. Lists features in order, allows viewing descriptions,
    and supports navigation. Exits only when the user selects "Continue".
    Args:
        class_name (str): The name of the class.
        class_data (dict): The class data dictionary (should include 'features' and optionally 'subclasses').
        class_levels (dict): The class levels dictionary (should include features per level).
        class_features (dict): The class features dictionary for feature descriptions.
        subclass_dicts (dict): Dict of subclass name to subclass feature dicts.
    """
    # Gather all features in order by level
    features_by_level = []  # List of (level, feature_name)
    for lvl in sorted(class_levels.keys()):
        for feat in class_levels[lvl].get('features', []):
            features_by_level.append((lvl, feat))
    # Remove duplicates while preserving order
    seen = set()
    ordered_features = []
    for lvl, feat in features_by_level:
        if feat not in seen:
            ordered_features.append((lvl, feat))
            seen.add(feat)

    def print_feature_desc(desc, title=None):
        if title:
            print(f"\n{title}:")
        border = '-' * 80
        def format_dict(d):
            return '\n'.join(f"{k}: {v}" for k, v in d.items())
        def humanize_key(key):
            # Convert snake_case or camelCase to Title Case with spaces
            import re
            s = str(key)
            s = re.sub(r'_', ' ', s)
            s = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
            return s.title()
        # Enhanced: if desc is a dict whose values are all dicts, render as a multi-column table
        if isinstance(desc, list):
            for idx, part in enumerate(desc):
                if idx > 0:
                    print(border)
                if isinstance(part, str):
                    print(part)
                elif isinstance(part, dict):
                    # Check if all values are dicts (for WILD_SHAPE style tables)
                    if part and all(isinstance(v, dict) for v in part.values()):
                        first_col = 'Level' if all(isinstance(k, int) for k in part.keys()) else 'Feature'
                        # Collect all subkeys
                        subkeys = set()
                        for v in part.values():
                            subkeys.update(v.keys())
                        subkeys = list(subkeys)
                        table = PrettyTable()
                        table.field_names = [first_col] + [humanize_key(sk) for sk in subkeys]
                        table.align = "l"
                        table.hrules = ALL
                        table.vrules = ALL
                        for k in sorted(part.keys()):
                            row = [k]
                            for subk in subkeys:
                                row.append(part[k].get(subk, "-"))
                            table.add_row(row)
                        print(table)
                    else:
                        table = PrettyTable()
                        table.field_names = ["Feature", "Description"]
                        table.align = "l"
                        table.hrules = ALL
                        table.vrules = ALL
                        for k, v in part.items():
                            if isinstance(v, dict):
                                v = format_dict(v)
                            table.add_row([k, v])
                        print(table)
                else:
                    print(part)
            print()
        elif isinstance(desc, dict):
            # Check if all values are dicts (for WILD_SHAPE style tables)
            if desc and all(isinstance(v, dict) for v in desc.values()):
                first_col = 'Level' if all(isinstance(k, int) for k in desc.keys()) else 'Feature'
                subkeys = set()
                for v in desc.values():
                    subkeys.update(v.keys())
                subkeys = list(subkeys)
                table = PrettyTable()
                table.field_names = [first_col] + [humanize_key(sk) for sk in subkeys]
                table.align = "l"
                table.hrules = ALL
                table.vrules = ALL
                for k in sorted(desc.keys()):
                    row = [k]
                    for subk in subkeys:
                        row.append(desc[k].get(subk, "-"))
                    table.add_row(row)
                print(table)
            else:
                table = PrettyTable()
                table.field_names = ["Feature", "Description"]
                table.align = "l"
                table.hrules = ALL
                table.vrules = ALL
                for k, v in desc.items():
                    if isinstance(v, dict):
                        v = format_dict(v)
                    table.add_row([k, v])
                print(table)
        else:
            print(desc)
        print()

    while True:
        choices = [
            {
                'name': f"Level {lvl}: {feat}",
                'value': feat
            } for lvl, feat in ordered_features
        ]
        choices.append({'name': 'Back to Class Selection', 'value': '__back_to_class_selection__'})
        choices.append({'name': 'Continue', 'value': '__continue__'})
        selected = inquirer.select(
            message=f"Browse {class_name} features (select to view, or Continue):",
            choices=choices
        ).execute()
        if selected == '__back_to_class_selection__':
            return 'back_to_class_selection'
        if selected == '__continue__':
            break
        # Check if this is a subclass feature
        if subclass_dicts and (selected == 'Subclass Feature' or selected.endswith('Subclass')):
            while True:
                subclass_names = list(subclass_dicts.keys())
                subclass_choices = subclass_names + ['Back', 'Back to Class Selection']
                subclass_choice = inquirer.select(
                    message="Select a subclass to view features:",
                    choices=subclass_choices
                ).execute()
                if subclass_choice == 'Back':
                    break
                if subclass_choice == 'Back to Class Selection':
                    # Signal to caller to return to main class selection menu
                    return 'back_to_class_selection'
                subclass = subclass_dicts[subclass_choice]
                
                # Print subclass description if present
                if 'description' in subclass:
                    print_feature_desc(subclass['description'], title=f"{subclass_choice} Description")
                
                # Special: Show subclass spellcasting table if browsing that subclass
                if (class_name == 'Fighter' or class_name == 'Rogue') and (subclass_choice == 'Eldritch Knight' or subclass_choice == 'Arcane Trickster'):
                    if subclass_choice == 'Eldritch Knight':
                        subclass_dict = ELDRITCH_KNIGHT_SPELLCASTING
                    elif subclass_choice == 'Arcane Trickster':
                        subclass_dict = ARCANE_TRICKSTER_SPELLCASTING
                    display_subclass_spellcasting_table(subclass_dict, subclass_choice)
                
                # Special handling for Soulknife subclass
                if class_name == 'Rogue' and subclass_choice == 'Soulknife':
                    subclass_dict = SOULKNIFE_ENERGY_DICE
                    display_dict_table(subclass_choice, subclass_dict, 'Soulknife Energy Dice')
                
                # Special handling for Ranger > Beast Master companion tables
                # (Moved logic to feature selection below)
                
                feature_keys = [k for k in subclass.keys() if k != 'description']
                if feature_keys and all(isinstance(k, int) for k in feature_keys):
                    while True:
                        level_choices = []
                        level_to_feats = {}
                        for lvl in sorted(feature_keys):
                            feats = list(subclass[lvl].keys()) if isinstance(subclass[lvl], dict) else [subclass[lvl]]
                            level_choices.append({'name': f"{lvl}: {', '.join(feats)}", 'value': lvl})
                            level_to_feats[lvl] = feats
                        level_choices.append({'name': 'Back', 'value': 'Back'})
                        level_choices.append({'name': 'Back to Class Selection', 'value': 'Back to Class Selection'})
                        selected_level = inquirer.select(
                            message="Select a level to view all feature descriptions:",
                            choices=level_choices
                        ).execute()
                        if selected_level == 'Back':
                            break
                        if selected_level == 'Back to Class Selection':
                            # Signal to caller to return to main class selection menu
                            return 'back_to_class_selection'
                        lvl = selected_level
                        # Show all feature descriptions for this level
                        if isinstance(subclass[lvl], dict):
                            for feat in level_to_feats[lvl]:
                                desc = subclass[lvl][feat]
                                print_feature_desc(desc, title=f"{subclass_choice} {lvl} - {feat}")
                                # Special handling: If Beast Master 3 - Primal Companion, prompt to view stat block
                                if class_name == 'Ranger' and subclass_choice == 'Beast Master' and lvl == 3 and feat == 'Primal Companion':
                                    primal_choice = inquirer.select(
                                        message="View Primal Companion stat block?",
                                        choices=["Primal Companion", "Back"]
                                    ).execute()
                                    if primal_choice == "Primal Companion":
                                        beast_options = [
                                            ('Beast of the Land', BEAST_OF_THE_LAND),
                                            ('Beast of the Sea', BEAST_OF_THE_SEA),
                                            ('Beast of the Sky', BEAST_OF_THE_SKY)
                                        ]
                                        beast_names = [b[0] for b in beast_options]
                                        while True:
                                            beast_select = inquirer.select(
                                                message="Select your Beast Companion type:",
                                                choices=beast_names + ['Back']
                                            ).execute()
                                            if beast_select == 'Back':
                                                break
                                            beast_dict = dict(beast_options)[beast_select]
                                            display_stat_block(beast_dict, title=beast_select)
                                            inquirer.text(message="Press Enter to return.").execute()
                        else:
                            desc = subclass[lvl]
                            print_feature_desc(desc, title=f"{subclass_choice} {lvl}")
                            inquirer.text(message="Press Enter to return.").execute()
                else:
                    if not feature_keys:
                        desc = subclass.get('description', 'No description available.')
                        print_feature_desc(desc, title=subclass_choice)
                        inquirer.text(message="Press Enter to return.").execute()
                        continue
                    while True:
                        subfeat = inquirer.select(
                            message=f"Select a feature of {subclass_choice} to view:",
                            choices=feature_keys + ['Back']
                        ).execute()
                        if subfeat == 'Back':
                            break
                        desc = subclass.get(subfeat, 'No description available.')
                        print_feature_desc(desc, title=f"{subclass_choice} - {subfeat}")
                        inquirer.text(message="Press Enter to return.").execute()
        else:
            desc = class_features.get(selected, "No description available.")
            print_feature_desc(desc, title=selected)
            inquirer.text(message="Press Enter to return.").execute()

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
    from misc.skills import SKILLS_DICT  # Ensure SKILLS_DICT is available
    chosen_skills = []
    profs = class_data['proficiencies']
    skills_prof = profs.get('skills', [])
    num_skills = profs.get('skills_choose', 2)
    # If skills_prof is empty or contains a string like 'any', allow any skill
    if not skills_prof or (isinstance(skills_prof, list) and skills_prof and isinstance(skills_prof[0], str) and 'any' in skills_prof[0].lower()):
        available_skills = [s for s in SKILLS_DICT.keys() if s not in already_proficient]
    else:
        available_skills = [s for s in skills_prof if s not in already_proficient]
    if not available_skills:
        print("No available skill proficiencies to choose from.")
    elif len(available_skills) <= num_skills:
        chosen_skills = available_skills.copy()
        print(f"Automatically selected: {', '.join(chosen_skills)}")
    else:
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
    from collections import Counter
    import re
    from equipment.armor_dict import HEAVY_ARMOR_DICT, LIGHT_ARMOR_DICT, MEDIUM_ARMOR_DICT, SHIELD_DICT
    from equipment.weapons_dict import AMMUNITION_DICT, MARTIAL_WEAPONS_DICT, SIMPLE_WEAPONS_DICT
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

def learn_spell(class_name, spellcasting, known_spells, class_feature_spells=None):
    """
    Handles the spell learning process for a class at a given level.
    Prompts the user to select all required cantrips and leveled spells not already known or granted by features.
    Returns a list of (spell_level, spell_name, spell_data) for all newly learned spells.
    """
    learned_spells = []
    # Prepare set of feature-granted spells for each level
    feature_spells_by_level = {}
    if class_feature_spells:
        for lvl, spells in class_feature_spells.items():
            feature_spells_by_level[str(lvl)] = set(spells.keys())
            if str(lvl) == '0':
                feature_spells_by_level['Cantrips'] = set(spells.keys())
    # Learn cantrips
    cantrips_to_learn = spellcasting.get('cantrips_known', 0)
    if cantrips_to_learn:
        known_cantrips = set(known_spells.get('Cantrips', {}))
        exclude_cantrips = feature_spells_by_level.get('Cantrips', set())
        while len(known_cantrips) < cantrips_to_learn:
            spell_name, spell_data = add_class_spell(class_name, 0, known_cantrips, exclude_cantrips)
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
            # Filter out already known spells at this level and feature-granted spells
            known_at_level = set(known_spells.get(str(spell_level), {})) | {name for lvl, name, _ in learned_spells if lvl == spell_level}
            exclude_at_level = feature_spells_by_level.get(str(spell_level), set())
            spell_name, spell_data = add_class_spell(class_name, spell_level, known_at_level, exclude_at_level)
            if not spell_name:
                break
            learned_spells.append((spell_level, spell_name, spell_data))
            known_level_spells.add(spell_name)
    return learned_spells
