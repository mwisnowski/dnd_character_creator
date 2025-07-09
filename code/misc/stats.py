"""
D&D 5e character statistics utilities.
Provides functions for ability scores, modifiers, HP, AC, and other stat calculations.
"""

import inquirer
from .dice_rolling import Dice
from equipment.armor_dict import LIGHT_ARMOR_DICT, MEDIUM_ARMOR_DICT, HEAVY_ARMOR_DICT

ABILITY_NAMES = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma"
]

def roll_ability_scores() -> dict[str, int]:
    """
    Roll 4d6, drop the lowest, for each ability and return as a dictionary.
    Returns:
        dict[str, int]: Mapping of ability names to rolled scores.
    """
    dice = Dice(4, 6)
    scores = {name: dice.roll_drop_lowest() for name in ABILITY_NAMES}
    return scores

def save_ability_scores(scores: dict[str, int]) -> dict[str, int]:
    """
    Return a copy of the chosen ability scores dictionary.
    Args:
        scores (dict[str, int]): Ability scores to save.
    Returns:
        dict[str, int]: Copy of the ability scores.
    """
    return dict(scores)

def interactive_ability_assignment() -> dict[str, int]:
    """
    Roll 7 ability scores, let user assign each to an ability, removing chosen score from pool after each pick.
    Uses inquirer for interactive selection.
    Returns:
        dict[str, int]: Final assigned ability scores.
    """
    dice = Dice(4, 6)
    pool = [dice.roll_drop_lowest() for _ in range(7)]
    print(f"Rolled ability scores: {pool}")
    assigned = {}
    remaining = pool.copy()
    for ability in ABILITY_NAMES:
        question = [
            inquirer.List(
                'score',
                message=f"Select a score for {ability}",
                choices=[str(val) for val in remaining],
            )
        ]
        answer = inquirer.prompt(question)
        if answer is None:
            print("No selection made. Exiting.")
            return save_ability_scores(assigned)
        value = int(answer['score'])
        assigned[ability] = value
        remaining.remove(value)
    print("\nFinal ability assignments:")
    max_key_len = max(len(name) for name in ABILITY_NAMES)
    for ability in ABILITY_NAMES:
        value = assigned[ability]
        print(f"{ability + ':':<{max_key_len + 2}} {value}")
    return save_ability_scores(assigned)

def ability_modifier(score: int) -> int:
    """
    Calculate the D&D ability modifier for a given ability score.
    Args:
        score (int): The ability score.
    Returns:
        int: The corresponding modifier (e.g., 10-11 = 0, every 2 above 10 is +1, every 2 below 10 is -1).
    """
    return (score - 10) // 2

def calc_hp(class_hit_die: int, con_mod: int, level: int = 1, tough: bool = False) -> int:
    """
    Calculate character HP for a given class hit die, Constitution modifier, and level.
    If tough is True, add +2 HP per level (Tough feat).
    Args:
        class_hit_die (int): The class's hit die value (e.g., 12 for d12).
        con_mod (int): The character's Constitution modifier.
        level (int, optional): The character's level. Defaults to 1.
        tough (bool, optional): Whether the character has the Tough feat. Defaults to False.
    Returns:
        int: The calculated hit points.
    """
    hp = (class_hit_die + con_mod) * level
    if tough:
        hp += 2 * level
    return hp

def calc_ac(equipped_armor=None, dex_mod=0, con_mod=0, wis_mod=0, barbarian=False, monk=False, shield=False):
    """
    Calculate Armor Class (AC) based on equipped armor, ability modifiers, and class features.
    - If monk (and using no armor or shield): AC = 10 + DEX + WIS
    - If barbarian (and using no armor): AC = 10 + DEX + CON
    - If light armor: AC = armor base + DEX
    - If medium armor: AC = armor base + min(DEX, 2)
    - If heavy armor: AC = armor base (no DEX)
    - If shield (and not monk): +2 AC
    """
    # Monk: Unarmored Defense (Monk) - no shield
    if monk and not shield and equipped_armor is None:
        return 10 + dex_mod + wis_mod
    # Barbarian: Unarmored Defense (Barbarian)
    elif barbarian and equipped_armor is None:
        return 10 + dex_mod + con_mod
    # Armor equipped
    ac = 10
    armor_ac = 0
    if equipped_armor:
        if equipped_armor in LIGHT_ARMOR_DICT:
            armor_ac = LIGHT_ARMOR_DICT[equipped_armor]['ac']
            ac = armor_ac + dex_mod
        elif equipped_armor in MEDIUM_ARMOR_DICT:
            armor_ac = MEDIUM_ARMOR_DICT[equipped_armor]['ac']
            ac = armor_ac + min(dex_mod, 2)
        elif equipped_armor in HEAVY_ARMOR_DICT:
            armor_ac = HEAVY_ARMOR_DICT[equipped_armor]['ac']
            ac = armor_ac  # No DEX mod
        else:
            # Unknown armor, fallback to base 10 + DEX
            ac = 10 + dex_mod
    else:
        # No armor: base 10 + DEX
        ac = 10 + dex_mod
    # Add shield bonus if applicable (not for monk)
    if shield and not monk:
        ac += 2
    return ac

