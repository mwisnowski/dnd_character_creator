"""
Utility functions for species data management and display in the D&D character creator project.
Provides formatted printing of species traits and related helpers for the CLI.
"""

from __future__ import annotations

# Standard Python imports
import textwrap

# Local imports
from .species_dict import SPECIES_DATA, TRAIT_DATA, size, speed, traits, description
from InquirerPy import inquirer
from misc.skills import SKILLS_DICT


def print_species_traits(species_name: str, override_traits: list[str] = None, trait_desc_overrides: dict = None) -> None:
    """
    Prints the traits and descriptions for a given species name.

    Args:
        species_name (str): The name of the species to display information for.
        override_traits (list[str], optional): If provided, use this list of traits instead of the default.
        trait_desc_overrides (dict, optional): If provided, use these descriptions for the specified traits.

    Returns:
        None

    Tip:
        This function prints all relevant species information, including special handling for Darkvision
        in Dwarves and Orcs, and aligns trait tables for readability.
    """
    species_info = SPECIES_DATA.get(species_name)
    if not species_info:
        print(f'Species "{species_name}" not found.')
        return
    print(f'Species: {species_name}')
    print(f'Size: {species_info[size]}')
    print(f'Speed: {species_info[speed]}')
    print(f'Description: {species_info.get(description, "No description available")}\n')
    print(f'As a {species_name} you have the following traits:')
    trait_source = override_traits if override_traits is not None else species_info[traits]

    def print_trait_description(trait, desc):
        if desc is None:
            print('  (No description available)')
        elif isinstance(desc, list):
            for item in desc:
                if isinstance(item, dict):
                    max_key_len = max(len(k.rstrip()) for k in item.keys())
                    print(f'  {trait}:')
                    for k, v in item.items():
                        k = k + ":"
                        key_no_trail = k.rstrip()
                        trailing_spaces = k[len(key_no_trail):]
                        prefix = f'    {key_no_trail:{max_key_len + 2}}{trailing_spaces}'
                        indent = ' ' * (len(prefix))
                        lines = str(v).split('\n')
                        for idx, line in enumerate(lines):
                            if line.strip() == '' and idx != len(lines) - 1:
                                print()
                                continue
                            wrapped = textwrap.fill(
                                line,
                                width=100,
                                initial_indent=prefix if idx == 0 else indent,
                                subsequent_indent=indent,
                                break_long_words=False,
                            )
                            print(wrapped)
                elif isinstance(item, str):
                    print(f'  {item.strip()}\n')
        else:
            print(f'  {desc}\n')

    for trait in trait_source:
        print(f'Trait: {trait}')
        desc = trait_desc_overrides[trait] if trait_desc_overrides and trait in trait_desc_overrides else TRAIT_DATA.get(trait)
        # Special case: Dwarves and Orcs have 120 ft Darkvision
        if (species_name.lower() == "dwarf" or species_name.lower() == 'orc') and trait == "Darkvision":
            print('  You have Darkvision with a range of 120 feet.\n')
            continue
        print_trait_description(trait, desc)

def get_species_traits(species_name: str):
    """
    Return the list of traits for the given species name from SPECIES_DATA.

    Args:
        species_name (str): The name of the species to get traits for.

    Returns:
        list: A list of traits for the species, or an empty list if the species is not found.

    Tip:
        This function provides a simple way to access the traits of a species
        without additional formatting or display logic.
    """
    species = SPECIES_DATA.get(species_name)
    if species:
        return species.get(traits, [])
    return []



def handle_special_skill_traits(traits: list, current_skills: list) -> list:
    """
    Handle special skill-granting traits like Keen Senses and Skillful.
    Prompts the user to choose a skill if needed and returns the updated skills list.
    """
    # For Keen Senses
    keen_skills = ["Insight", "Perception", "Survival"]
    if "Keen Senses" in traits:
        # Only show non-proficient keen skills
        non_proficient_keen = [s for s in keen_skills if s not in current_skills]
        if non_proficient_keen:
            choice = inquirer.select(
                message="Keen Senses: Choose a skill to gain proficiency in:",
                choices=non_proficient_keen
            ).execute()
            current_skills.append(choice)
    # For Skillful
    if "Skillful" in traits:
        all_skills = list(SKILLS_DICT.keys())
        non_proficient = [s for s in all_skills if s not in current_skills]
        if non_proficient:
            choice = inquirer.select(
                message="Skillful: Choose any skill to gain proficiency in:",
                choices=non_proficient
            ).execute()
            current_skills.append(choice)
    return current_skills


