"""
Entry point for the species selection and information display in the D&D character creator project.
handle_special_skill_traitsPrompts the user for a species and handles lineage/ancestry/legacy selection.
"""

from InquirerPy import inquirer
from species.species_utils import print_species_traits, SPECIES_DATA, traits
from species.species_dict import TRAIT_DATA

def main():
    """
    Presents a selection menu for species, handles lineage/ancestry/legacy traits,
    and prints detailed information about the selected species.
    
    Returns:
        dict: Contains the final species name, trait list, and trait description overrides.
    """
    # Present a selection menu for species instead of text input
    species_choices = list(SPECIES_DATA.keys())
    species_name = inquirer.select(
        message="Select a species:",
        choices=species_choices,
    ).execute()
    species_info = SPECIES_DATA.get(species_name)
    # Check for lineage/ancestry traits
    trait_list = species_info[traits][:]
    trait_desc_overrides = {}
    lineage_map = {
        'Elven Lineage': 'Lineage',
        'Draconic Ancestry': 'Ancestry',
        'Giant Ancestry': 'Ancestry',
        'Gnomish Lineage': 'Lineage',
        'Fiendish Legacy': 'Legacy',
    }

    def get_final_species_name(display_type, chosen_lineage, species_name):
        if display_type == 'Lineage' and 'Elf' in species_name:
            return f"{chosen_lineage}"
        elif display_type == 'Ancestry' and 'Dragonborn' in species_name:
            return f"{chosen_lineage} Dragonborn"
        elif display_type == 'Legacy' and 'Tiefling' in species_name:
            return f"{chosen_lineage} Tiefling"
        elif display_type == 'Ancestry' and 'Giant' in species_name:
            return f"{chosen_lineage} Goliath"
        elif display_type == 'Lineage' and 'Gnome' in species_name:
            return f"{chosen_lineage} Gnome"
        return species_name

    final_species_name = species_name
    # Use a copy to avoid modifying while iterating
    for trait in trait_list[:]:
        if trait in lineage_map:
            display_type = lineage_map[trait]
            options_dict = TRAIT_DATA[trait][1] if isinstance(TRAIT_DATA[trait], list) else TRAIT_DATA[trait]
            lineage_options = list(options_dict.keys())
            chosen_lineage = inquirer.select(
                message=f"Select {display_type}:",
                choices=lineage_options,
            ).execute()
            trait_list.remove(trait)
            trait_list.append(chosen_lineage)
            trait_desc_overrides[chosen_lineage] = options_dict[chosen_lineage]
            final_species_name = get_final_species_name(display_type, chosen_lineage, species_name)
    while True:
        # Print species info with updated traits and description overrides, using the base species_name for lookup
        print_species_traits(species_name, override_traits=trait_list, trait_desc_overrides=trait_desc_overrides)
        print(f"\nFinal traits for {final_species_name}:")
        for trait in trait_list:
            print(f"  - {trait}")
        confirm = inquirer.select(
            message=f"Do you want to be a {final_species_name}?",
            choices=["Yes", "No"],
        ).execute()
        if confirm == "Yes":
            break
        # If No, go back to main species selection
        species_name = inquirer.select(
            message="Select a species:",
            choices=list(SPECIES_DATA.keys()),
        ).execute()
        species_info = SPECIES_DATA.get(species_name)
        trait_list = species_info[traits][:]
        trait_desc_overrides = {}
        final_species_name = species_name
        for trait in trait_list[:]:
            if trait in lineage_map:
                display_type = lineage_map[trait]
                options_dict = TRAIT_DATA[trait][1] if isinstance(TRAIT_DATA[trait], list) else TRAIT_DATA[trait]
                lineage_options = list(options_dict.keys())
                chosen_lineage = inquirer.select(
                    message=f"Select {display_type}:",
                    choices=lineage_options,
                ).execute()
                trait_list.remove(trait)
                trait_list.append(chosen_lineage)
                trait_desc_overrides[chosen_lineage] = options_dict[chosen_lineage]
                final_species_name = get_final_species_name(display_type, chosen_lineage, species_name)
    print(f"{final_species_name} selected as species.")
    # Return species and traits for use by caller
    # Add proficiencies if any species grants them (future-proof, e.g. custom/variant)
    proficiencies = {'weapons': set(), 'armor': set(), 'tools': set()}
    # Example: if a trait grants a proficiency, add here (none in default data)
    # For now, just return empty sets
    return {
        'species': final_species_name,
        'species_traits': trait_list,
        'proficiencies': proficiencies
    }

if __name__ == "__main__":
    main()
