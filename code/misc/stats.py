"""
D&D 5e character statistics utilities.
Provides functions for ability scores, modifiers, HP, AC, and other stat calculations.
"""

import inquirer
from .dice_rolling import Dice

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

# Note: Install inquirer with 'pip install inquirer' if not already installed.
