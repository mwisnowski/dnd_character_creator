"""
Utility functions for species data management and display in the D&D character creator project.

This module provides fuzzy matching for species names and formatted printing of species traits,
including special handling for trait tables and readable output for the command-line interface.
It is intended to be imported and used by the main menu and species modules.
"""

from __future__ import annotations

# Standard Python imports
import difflib
import textwrap

# Local imports
from .species_dict import SPECIES_DATA, TRAIT_DATA, size, speed, traits, description

def get_best_species_match(user_input: str, species_dict: dict) -> str | None:
    """
    Attempts to find the best matching species name from the dictionary.

    Args:
        user_input (str): The species name input by the user (case-insensitive, can be plural or misspelled).
        species_dict (dict): The dictionary of available species.

    Returns:
        str | None: The best-matching species name from the dictionary, or None if no match is found.

    Tip:
        This function supports direct, singular/plural, and fuzzy matching for user convenience.
    """
    lower_map = {k.lower(): k for k in species_dict.keys()}
    user_input_l = user_input.lower()
    # Try direct match
    if user_input_l in lower_map:
        return lower_map[user_input_l]
    # Try removing plural 's' or 'ves'
    if user_input_l.endswith('ves'):
        singular = user_input_l[:-3] + 'f'
        if singular in lower_map:
            return lower_map[singular]
    if user_input_l.endswith('s'):
        singular = user_input_l[:-1]
        if singular in lower_map:
            return lower_map[singular]
    # Fuzzy match
    close = difflib.get_close_matches(user_input_l, lower_map.keys(), n=1, cutoff=0.7)
    if close:
        return lower_map[close[0]]
    return None

def print_species_traits(species_name: str) -> None:
    """
    Prints the traits and descriptions for a given species name.

    Args:
        species_name (str): The name of the species to display information for.

    Returns:
        None

    Tip:
        This function prints all relevant species information, including special handling for Darkvision
        in Dwarves and Orcs, and aligns trait tables for readability.
    """
    best_match = get_best_species_match(species_name, SPECIES_DATA)
    if not best_match:
        print(f'Species "{species_name}" not found.')
        return
    species_info = SPECIES_DATA[best_match]
    print(f'Species: {best_match}')
    print(f'Size: {species_info[size]}')
    print(f'Speed: {species_info[speed]}')
    print(f'Description: {species_info.get(description, "No description available")}\n')
    print(f'As a {best_match} you have the following traits:')
    for trait in species_info[traits]:
        print(f'Trait: {trait}')
        desc = TRAIT_DATA.get(trait)
        # Special case: Dwarves and Orcs have 120 ft Darkvision
        if (best_match.lower() == "dwarf" or best_match.lower() == 'orc') and trait == "Darkvision":
            print('  You have Darkvision with a range of 120 feet.\n')
            continue
        if desc is None:
            print('  (No description available)')
        elif isinstance(desc, list):
            for item in desc:
                if isinstance(item, dict):
                    max_key_len = max(len(k.rstrip()) for k in item.keys())
                    # Special formatting for Draconic Ancestry and similar tables
                    print(f'  {trait}:')
                    for k, v in item.items():
                        k = k + ":"
                        key_no_trail = k.rstrip()
                        trailing_spaces = k[len(key_no_trail):]
                        prefix = f'    {key_no_trail:{max_key_len + 2}}{trailing_spaces}'
                        indent = ' ' * (len(prefix))
                        # Split on '\n', wrap each line, and preserve explicit newlines with indent
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


