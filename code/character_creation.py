# Core Character Creation Module
from __future__ import annotations

from misc.dice_rolling import Dice  # Dependency for abilities
from misc.abilities import (
    roll_ability_scores,
    save_ability_scores,
    interactive_ability_assignment,
    ABILITY_NAMES
)
from species.species import main as species_select_main

# Add additional imports as needed for other modules

class charGen:
    def __init__(
        self,
        name: str = "",
        species: str = "",
        class_name: str = "",
        background: str = "",
        level: int = 1,
        ability_scores: dict[str, int] = None,
        alignment: str = "",
        player_name: str = "",
        experience_points: int = 0,
        gender: str = "",
        age: int = 0,
    ):
        self.name = name
        self.species = species
        self.class_name = class_name
        self.background = background
        self.level = level
        self.ability_scores = ability_scores
        self.alignment = alignment
        self.player_name = player_name
        self.experience_points = experience_points
        self.gender = gender
        self.age = age

    def __str__(self):
        max_key_len = max(len(k) for k in self.ability_scores) if self.ability_scores else 0
        abilities = "\n".join(f"{k.ljust(max_key_len)} : {v}" for k, v in self.ability_scores.items())
        return (
            f"Name           : {self.name}\n"
            f"Species        : {self.species}\n"
            f"Class          : {self.class_name}\n"
            f"Background     : {self.background}\n"
            f"Level          : {self.level}\n"
            f"Alignment      : {self.alignment}\n"
            f"Player Name    : {self.player_name}\n"
            f"XP             : {self.experience_points}\n"
            f"Gender         : {self.gender}\n"
            f"Age            : {self.age}\n"
            f"Ability Scores :\n{abilities}"
        )
        
    def make_character(self):
        """
        Create a character instance with the provided attributes.
        This method can be expanded to include more complex character creation logic.
        """
        self.character_setup()
        self.choose_background()
        self.choose_class()
        self.choose_species()
        self.determine_ability_scores()
        print("Character created successfully!")
        print(self)
        
    def character_setup(self):
        """
        Set up the character by rolling ability scores and choosing species.
        This method can be expanded to include more setup steps.
        """
        print("Setting up character...")
        self.player_name = input("What is your, the player's, name?\n> ")
        self.character_name = input("What is your characters name?\n> ")
    
    def choose_background(self):
        """
        Choose a background for the character using the background selection module.
        Saves the background to the character instance.
        """
        # Placeholder for background selection logic
        self.background = input("Choose a background for your character: ")
        print(f"{self.background} selected as background.")
    
    def choose_class(self):
        """
        Choose a class for the character using the class selection module.
        Saves the class name to the character instance.
        """ 
        pass
    
    def choose_species(self):
        """
        Choose a species for the character using the species selection module.
        Saves the species and its traits to the character instance.
        """
        result = species_select_main()
        if result and isinstance(result, dict):
            self.species = result.get('species', '')
            self.species_traits = result.get('species_traits', {})
            print(f"{self.species} selected as species.")
        else:
            print("No species selected.")
    
    def determine_ability_scores(self):
        """
        Roll ability scores using the standard method and save them to the character instance.
        """
        if self.ability_scores is None:
            self.ability_scores = interactive_ability_assignment()
        else:
            print(self.ability_scores)

# Example usage (remove or comment out in production):
if __name__ == "__main__":
    # Example: Create a character and print details
    character = charGen()
    character.make_character()
    print("\nCharacter Sheet:\n", character)
