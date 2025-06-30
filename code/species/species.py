"""
Entry point for the species selection and information display in the D&D character creator project.

This module prompts the user for a species name and prints detailed information about the selected
species using the print_species_traits utility function. Intended to be called from the main menu.
"""

from species.species_utils import print_species_traits

def main():
    species_name = input('Enter a species name: ').strip()
    print_species_traits(species_name)

if __name__ == "__main__":
    main()
