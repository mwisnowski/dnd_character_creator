from __future__ import annotations

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
    """
    dice = Dice(4, 6)
    scores = {name: dice.roll_drop_lowest() for name in ABILITY_NAMES}
    return scores


def save_ability_scores(scores: dict[str, int]) -> dict[str, int]:
    """
    Save the chosen ability scores to a dictionary for character creation.
    Returns the dictionary for later use (e.g., in a Character class).
    """
    return dict(scores)

def interactive_ability_assignment() -> dict[str, int]:
    """
    Roll 7 ability scores, let user assign each to an ability, removing chosen score from pool after each pick.
    Uses inquirer for interactive selection.
    Returns the saved ability scores dictionary.
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
        ability = ability +':'
        print(f"{ability.ljust(max_key_len + 2)} {value}")
    return save_ability_scores(assigned)

def ability_modifier(score: int) -> int:
    """
    Calculate the D&D ability modifier for a given ability score.
    10-11 = 0, every 2 above 10 is +1, every 2 below 10 is -1.
    """
    return (score - 10) // 2


# Example usage:
# rolled_scores = roll_ability_scores()
# save_ability_scores(rolled_scores, 'chosen_ability_scores.txt')
# interactive_ability_assignment()

# Note: Install inquirer with 'pip install inquirer' if not already installed.