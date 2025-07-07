"""
backgrounds_utils.py
-------------------
Helper functions for D&D 5e backgrounds equipment and inventory parsing.
"""

import re
from collections import Counter
from equipment.armor_dict import LIGHT_ARMOR_DICT, MEDIUM_ARMOR_DICT, HEAVY_ARMOR_DICT, SHIELD_DICT
from equipment.weapons_dict import SIMPLE_WEAPONS_DICT, MARTIAL_WEAPONS_DICT, AMMUNITION_DICT

def parse_equipment_items(selected_items):
    """
    Parse a list of selected equipment items into categorized equipment, inventory, and currency.
    Handles multiples, currency, and collapses duplicates.

    Args:
        selected_items (list): List of equipment/inventory/currency strings.

    Returns:
        tuple: (parsed_equipment, parsed_inventory, gold_pieces, silver_pieces, copper_pieces)
    """
    parsed_equipment = []
    parsed_inventory = []
    gold_pieces = 0
    silver_pieces = 0
    copper_pieces = 0
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
                    parsed_equipment.extend([test_item]*count)
                    found = True
                    break
                elif test_item in SIMPLE_WEAPONS_DICT or test_item in MARTIAL_WEAPONS_DICT or test_item in AMMUNITION_DICT:
                    parsed_equipment.extend([test_item]*count)
                    found = True
                    break
            if not found:
                parsed_inventory.extend([base_item]*count)
        elif item in LIGHT_ARMOR_DICT or item in MEDIUM_ARMOR_DICT or item in HEAVY_ARMOR_DICT or item in SHIELD_DICT:
            parsed_equipment.append(item)
        elif item in SIMPLE_WEAPONS_DICT or item in MARTIAL_WEAPONS_DICT or item in AMMUNITION_DICT:
            parsed_equipment.append(item)
        else:
            parsed_inventory.append(item)
    # Collapse multiples in equipment and inventory
    equip_counter = Counter(parsed_equipment)
    inv_counter = Counter(parsed_inventory)
    parsed_equipment = [f"{name} x {count}" if count > 1 else name for name, count in equip_counter.items()]
    parsed_inventory = [f"{name} x {count}" if count > 1 else name for name, count in inv_counter.items()]
    return parsed_equipment, parsed_inventory, gold_pieces, silver_pieces, copper_pieces
