from misc.feats_utils import add_feat
from misc.feats import FIGHTING_STYLE_FEATS
from InquirerPy import inquirer
from equipment.weapons_dict import SIMPLE_WEAPONS_DICT, MARTIAL_WEAPONS_DICT
from spells.spells import add_class_spell
from prettytable import PrettyTable, ALL
from .barbarian import BARBARIAN_CLASS, BARBARIAN_LEVELS, BARBARIAN_FEATURES, PATH_OF_THE_BERSERKER, PATH_OF_THE_WILD_HEART, PATH_OF_THE_WORLD_TREE, PATH_OF_THE_ZEALOT
from .bard import BARD_CLASS, BARD_LEVELS, BARD_FEATURES, COLLEGE_OF_DANCE, COLLEGE_OF_GLAMOUR, COLLEGE_OF_LORE, COLLEGE_OF_VALOR
from .cleric import CLERIC_CLASS, CLERIC_LEVELS, CLERIC_FEATURES, LIFE_DOMAIN, LIGHT_DOMAIN, WAR_DOMAIN
from .druid import DRUID_CLASS, DRUID_LEVELS, DRUID_FEATURES, CIRCLE_OF_THE_LAND, CIRCLE_OF_THE_MOON, CIRCLE_OF_THE_SEA, CIRCLE_OF_THE_STARS
from .fighter import FIGHTER_CLASS, FIGHTER_LEVELS, FIGHTER_FEATURES, BATTLE_MASTER, CHAMPION, ELDRITCH_KNIGHT, PSI_WARRIOR
from .monk import MONK_CLASS, MONK_LEVELS, MONK_FEATURES, WARRIOR_OF_MERCY, WAY_OF_SHADOW, WAY_OF_THE_ELEMENTS, WAY_OF_THE_OPEN_HAND
from .paladin import PALADIN_CLASS, PALADIN_LEVELS, PALADIN_FEATURES, OATH_OF_DEVOTION, OATH_OF_THE_ANCIENTS, OATH_OF_VENGEANCE
from .ranger import RANGER_CLASS, RANGER_LEVELS, RANGER_FEATURES, BEAST_OF_THE_LAND, BEAST_OF_THE_SEA, BEAST_OF_THE_SKY, BEAST_MASTER, FEYWILD_GIFTS, FEY_WANDERER, GLOOM_STALKER, HUNTER

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
        'Beast of the Land': BEAST_OF_THE_LAND,
        'Beast of the Sea': BEAST_OF_THE_SEA,
        'Beast of the Sky': BEAST_OF_THE_SKY,
        'Beast Master': BEAST_MASTER,
        'Feywild Gifts': FEYWILD_GIFTS,
        'Fey Wanderer': FEY_WANDERER,
        'Gloom Stalker': GLOOM_STALKER,
        'Hunter': HUNTER,
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

    # Special: If class is Fighter, also show Eldritch Knight spellcasting table for reference
    if class_name == 'Fighter':
        from .fighter import ELDRITCH_KNIGHT_SPELLCASTING
        display_table(
            ELDRITCH_KNIGHT_SPELLCASTING,
            title="Eldritch Knight Spellcasting Table:",
            columns=["Level", "spells_prepared", "1st", "2nd", "3rd", "4th"],
            field_name_map={
                "spells_prepared": "Spells Prepared",
                "1st": "1st",
                "2nd": "2nd",
                "3rd": "3rd",
                "4th": "4th"
            }
        )

    # Special: If class is Monk, show Martial Arts table
    if class_name == 'Monk':
        from .monk import MARTIAL_ARTS
        display_table(MARTIAL_ARTS, title="Monk Martial Arts Table:")

def display_eldritch_knight_spellcasting_table():
    """
    Display the Eldritch Knight Spellcasting table using PrettyTable.
    """
    from .fighter import ELDRITCH_KNIGHT_SPELLCASTING
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["Level", "Spells Prepared", "1st", "2nd", "3rd", "4th"]
    table.align = "l"
    for lvl in sorted(ELDRITCH_KNIGHT_SPELLCASTING.keys()):
        row = ELDRITCH_KNIGHT_SPELLCASTING[lvl]
        table.add_row([
            lvl,
            row.get("spells_prepared", "-"),
            row.get("1st", "-"),
            row.get("2nd", "-"),
            row.get("3rd", "-"),
            row.get("4th", "-")
        ])
    print("\nEldritch Knight Spellcasting Table:")
    print(table)

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
        choices.append({'name': 'Continue', 'value': '__continue__'})
        selected = inquirer.select(
            message=f"Browse {class_name} features (select to view, or Continue):",
            choices=choices
        ).execute()
        if selected == '__continue__':
            break
        # Check if this is a subclass feature
        if subclass_dicts and (selected == 'Subclass Feature' or selected.endswith('Subclass')):
            while True:
                subclass_names = list(subclass_dicts.keys())
                subclass_choice = inquirer.select(
                    message="Select a subclass to view features:",
                    choices=subclass_names + ['Back']
                ).execute()
                if subclass_choice == 'Back':
                    break
                subclass = subclass_dicts[subclass_choice]
                # Print subclass description if present
                if 'description' in subclass:
                    print_feature_desc(subclass['description'], title=f"{subclass_choice} Description")
                # Special: Show Eldritch Knight spellcasting table if browsing that subclass
                if class_name == 'Fighter' and subclass_choice == 'Eldritch Knight':
                    display_eldritch_knight_spellcasting_table()
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
                        selected_level = inquirer.select(
                            message="Select a level to view all feature descriptions:",
                            choices=level_choices
                        ).execute()
                        if selected_level == 'Back':
                            break
                        lvl = selected_level
                        # Show all feature descriptions for this level
                        if isinstance(subclass[lvl], dict):
                            for feat in level_to_feats[lvl]:
                                desc = subclass[lvl][feat]
                                print_feature_desc(desc, title=f"{subclass_choice} {lvl} - {feat}")
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
