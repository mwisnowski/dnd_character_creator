from __future__ import annotations

LIGHT_ARMOR_DICT: dict[str, dict] = {
    'Padded Leather Armor': {
        'ac': 11,
        'strength': 0,
        'stealth': True,
        'weight': 8,
        'cost': 10,
    },
    'Leather Armor': {
        'ac': 11,
        'strength': 0,
        'stealth': False,
        'weight': 10,
        'cost':10,
    },
    'Studded Leather Armor': {
        'ac': 12,
        'strength': 0,
        'stealth': False,
        'weight': 13,
        'cost': 45,
    },
}

MEDIUM_ARMOR_DICT: dict[str, dict] = {
    'Hide Armor': {
        'ac': 12,
        'strength': 0,
        'stealth': True,
        'weight': 12,
        'cost': 10,
    },
    'Chain Shirt': {
        'ac': 13,
        'strength': 0,
        'stealth': True,
        'weight': 20,
        'cost': 50,
    },
    'Scale Mail': {
        'ac': 14,
        'strength': 0,
        'stealth': True,
        'weight': 45,
        'cost': 50,
    },
    'Breastplate': {
        'ac': 14,
        'strength': 0,
        'stealth': False,
        'weight': 20,
        'cost': 400,
    },
    'Half Plate': {
        'ac': 15,
        'strength': 0,
        'stealth': True,
        'weight': 40,
        'cost': 750,
    },
}

HEAVY_ARMOR_DICT: dict[str, dict] = {
    'Ring Mail': {
        'ac': 14,
        'strength': 0,
        'stealth': True,
        'weight': 40,
        'cost': 30,
    },
    'Chain Mail': {
        'ac': 16,
        'strength': 13,
        'stealth': True,
        'weight': 55,
        'cost': 75,
    },
    'Splint': {
        'ac': 17,
        'strength': 15,
        'stealth': True,
        'weight': 60,
        'cost': 200,
    },
    'Plate Armor': {
        'ac': 18,
        'strength': 15,
        'stealth': True,
        'weight': 65,
        'cost': 1500,
    },
}

SHIELD_DICT: dict[str, dict] = {
    'Shield': {
        'ac': 2,
        'strength': 0,
        'stealth': False,
        'weight': 6,
        'cost': 10,
    },
}