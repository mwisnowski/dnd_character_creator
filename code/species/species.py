"""
Entry point for the species selection and information display in the D&D character creator project.

This module prompts the user for a species name and prints detailed information about the selected
species using the print_species_traits utility function. Intended to be called from the main menu.
"""

from InquirerPy import inquirer
from species.species_utils import print_species_traits, SPECIES_DATA, traits
from species.species_dict import TRAIT_DATA

def main():
    # Present a selection menu for species instead of text input
    species_choices = list(SPECIES_DATA.keys())
    species_name = inquirer.select(
        message="Select a species:",
        choices=species_choices,
    ).execute()
    species_info = SPECIES_DATA.get(species_name)
    # Check for lineage/ancestry traits
    trait_list = species_info[traits].copy()
    trait_desc_overrides = {}
    lineage_map = {
        'Elven Lineage': ('Lineage', 'Elven Lineage'),
        'Draconic Ancestry': ('Ancestry', 'Draconic Ancestry'),
        'Giant Ancestry': ('Ancestry', 'Giant Ancestry'),
        'Gnomish Lineage': ('Lineage', 'Gnomish Lineage'),
        'Fiendish Legacy': ('Legacy', 'Fiendish Legacy'),
    }
    final_species_name = species_name
    for trait in list(trait_list):
        if trait in lineage_map:
            display_type, trait_data_key = lineage_map[trait]
            options_dict = TRAIT_DATA[trait][1] if isinstance(TRAIT_DATA[trait], list) else TRAIT_DATA[trait]
            lineage_options = list(options_dict.keys())
            chosen_lineage = inquirer.select(
                message=f"Select {display_type}:",
                choices=[opt.strip() for opt in lineage_options],
            ).execute()
            # Remove the generic trait and add the chosen one
            trait_list.remove(trait)
            trait_list.append(chosen_lineage)
            # Set the description override for the chosen lineage
            trait_desc_overrides[chosen_lineage] = options_dict[chosen_lineage]
            # Set the species name to the chosen lineage + base species (if not already included)
            if display_type == 'Lineage' and 'Elf' in species_name:
                final_species_name = f"{chosen_lineage}"
            elif display_type == 'Ancestry' and 'Dragonborn' in species_name:
                final_species_name = f"{chosen_lineage} Dragonborn"
            elif display_type == 'Legacy' and 'Tiefling' in species_name:
                final_species_name = f"{chosen_lineage.strip()} Tiefling"
            elif display_type == 'Ancestry' and 'Giant' in species_name:
                final_species_name = f"{chosen_lineage} Goliath"
            elif display_type == 'Lineage' and 'Gnome' in species_name:
                final_species_name = f"{chosen_lineage.strip()} Gnome"
    # Print species info with updated traits and description overrides, using the base species_name for lookup
    print_species_traits(species_name, override_traits=trait_list, trait_desc_overrides=trait_desc_overrides)
    print(f"{final_species_name} selected as species.")
    # Return species and traits for use by caller
    return {
        'species': final_species_name,
        'species_traits': trait_list
    }

if __name__ == "__main__":
    main()
