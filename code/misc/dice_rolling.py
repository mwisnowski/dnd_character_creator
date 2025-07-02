"""
D&D 5e dice rolling utilities.
Provides functions and a Dice class for rolling dice, including advantage/disadvantage mechanics.
"""

import random
from typing import List


def roll_die(sides: int) -> int:
    """
    Roll a single die with the specified number of sides.
    
    Args:
        sides (int): Number of sides on the die (e.g., 6 for d6, 20 for d20)
    
    Returns:
        int: Random integer between 1 and sides (inclusive)
    
    Raises:
        ValueError: If sides is less than 1
    """
    if sides < 1:
        raise ValueError("Die must have at least 1 side")
    return random.randint(1, sides)


def roll_dice(num_dice: int, sides: int, modifier: int = 0) -> int:
    """
    Roll multiple dice and return the sum plus any modifier.
    
    Args:
        num_dice (int): Number of dice to roll
        sides (int): Number of sides on each die
        modifier (int): Modifier to add to the total (default: 0)
    
    Returns:
        int: Sum of all dice rolls plus modifier
    
    Raises:
        ValueError: If num_dice or sides is less than 1
    """
    if num_dice < 1:
        raise ValueError("Must roll at least 1 die")
    if sides < 1:
        raise ValueError("Die must have at least 1 side")
    
    total = sum(roll_die(sides) for _ in range(num_dice))
    return total + modifier


class Dice:
    """
    A class for handling complex dice operations commonly used in D&D.
    """
    
    def __init__(self, num_dice: int = 1, sides: int = 20, modifier: int = 0):
        """
        Initialize a dice object.
        
        Args:
            num_dice (int): Number of dice to roll (default: 1)
            sides (int): Number of sides on each die (default: 20)
            modifier (int): Modifier to add to rolls (default: 0)
        """
        if num_dice < 1:
            raise ValueError("Must have at least 1 die")
        if sides < 1:
            raise ValueError("Die must have at least 1 side")
        
        self.num_dice = num_dice
        self.sides = sides
        self.modifier = modifier
    
    def roll(self) -> int:
        """
        Roll the dice and return the total.
        
        Returns:
            int: Sum of all dice rolls plus modifier
        """
        return roll_dice(self.num_dice, self.sides, self.modifier)
    
    def roll_with_advantage(self) -> int:
        """
        Roll with advantage (roll twice, take higher). Only works with single die rolls.
        
        Returns:
            int: Higher of two rolls plus modifier
        
        Raises:
            ValueError: If trying to use advantage with multiple dice
        """
        if self.num_dice != 1:
            raise ValueError("Advantage only works with single die rolls")
        
        roll1 = roll_die(self.sides)
        roll2 = roll_die(self.sides)
        return max(roll1, roll2) + self.modifier
    
    def roll_with_disadvantage(self) -> int:
        """
        Roll with disadvantage (roll twice, take lower). Only works with single die rolls.
        
        Returns:
            int: Lower of two rolls plus modifier
        
        Raises:
            ValueError: If trying to use disadvantage with multiple dice
        """
        if self.num_dice != 1:
            raise ValueError("Disadvantage only works with single die rolls")
        
        roll1 = roll_die(self.sides)
        roll2 = roll_die(self.sides)
        return min(roll1, roll2) + self.modifier
    
    def roll_multiple(self, times: int) -> List[int]:
        """
        Roll the dice multiple times and return all results as a list.
        
        Args:
            times (int): Number of times to roll the dice
        
        Returns:
            List[int]: List of results for each roll
        """
        return [self.roll() for _ in range(times)]
    
    def roll_drop_lowest(self, drop_count: int = 1) -> int:
        """
        Roll dice and drop the lowest results (useful for ability scores).
        
        Args:
            drop_count: Number of lowest dice to drop (default: 1)
        
        Returns:
            Sum of remaining dice plus modifier
        
        Raises:
            ValueError: If trying to drop more dice than available
        """
        if drop_count >= self.num_dice:
            raise ValueError("Cannot drop more dice than available")
        
        rolls = [roll_die(self.sides) for _ in range(self.num_dice)]
        rolls.sort(reverse=True)  # Sort descending
        kept_rolls = rolls[:self.num_dice - drop_count]
        return sum(kept_rolls) + self.modifier
    
    def __str__(self) -> str:
        """String representation of the dice."""
        modifier_str = ""
        if self.modifier > 0:
            modifier_str = f"+{self.modifier}"
        elif self.modifier < 0:
            modifier_str = str(self.modifier)
        
        return f"{self.num_dice}d{self.sides}{modifier_str}"
    
    def __repr__(self) -> str:
        """Representation of the dice object."""
        return f"Dice({self.num_dice}, {self.sides}, {self.modifier})"


# Common D&D dice presets
d4 = Dice(1, 4)
d6 = Dice(1, 6)
d8 = Dice(1, 8)
d10 = Dice(1, 10)
d12 = Dice(1, 12)
d20 = Dice(1, 20)
d100 = Dice(1, 100)

# Common ability score rolling (4d6 drop lowest)
ability_score_dice = Dice(4, 6)


def roll_ability_scores() -> List[int]:
    """
    Roll ability scores using the standard 4d6 drop lowest method.
    
    Returns:
        List of 6 ability scores
    """
    return [ability_score_dice.roll_drop_lowest() for _ in range(6)]


def parse_dice_string(dice_string: str) -> Dice:
    """
    Parse a dice string like "2d8+3" or "1d20-1" into a Dice object.
    
    Args:
        dice_string: String in format "XdY+Z" or "XdY-Z" or "XdY"
    
    Returns:
        Dice object representing the parsed string
    
    Raises:
        ValueError: If the string format is invalid
    """
    dice_string = dice_string.strip().lower().replace(" ", "")
    
    # Handle modifier
    modifier = 0
    if "+" in dice_string:
        dice_part, mod_part = dice_string.split("+", 1)
        modifier = int(mod_part)
    elif "-" in dice_string and dice_string.count("-") == 1:
        dice_part, mod_part = dice_string.split("-", 1)
        modifier = -int(mod_part)
    else:
        dice_part = dice_string
    
    # Parse dice part
    if "d" not in dice_part:
        raise ValueError("Invalid dice string format. Expected format: 'XdY' or 'XdY+Z'")
    
    num_str, sides_str = dice_part.split("d", 1)
    
    # Handle implicit 1 (e.g., "d20" instead of "1d20")
    if num_str == "":
        num_dice = 1
    else:
        num_dice = int(num_str)
    
    sides = int(sides_str)
    
    return Dice(num_dice, sides, modifier)