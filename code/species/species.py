"""
Entry point for the species selection and information display in the D&D character creator project.

This module prompts the user for a species name and prints detailed information about the selected
species using the print_species_traits utility function. Intended to be called from the main menu.
"""

import inquirer
from species.species_utils import print_species_traits, get_species_traits

def main():
    species_name = input('Enter a species name: ').strip()
    print_species_traits(species_name)
    traits = get_species_traits(species_name)
    question = [
        inquirer.Confirm(
            'choose',
            message=f"Would you like to choose {species_name} as your character species?",
            default=True
        )
    ]
    answer = inquirer.prompt(question)
    if answer and answer.get('choose'):
        print(f"\n{species_name} selected!")
        return {'species': species_name, 'species_traits': traits}
    else:
        print("Species not selected.")
        return None

if __name__ == "__main__":
    main()
