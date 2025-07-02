from __future__ import annotations

from InquirerPy import inquirer

def main():
    while True:
        choice = inquirer.select(
            message="Main Menu:",
            choices=[
                {"name": "Species", "value": "species"},
                {"name": "Spells", "value": "spells"},
                {"name": "Exit", "value": "exit"}
            ],
        ).execute()
        if choice == "species":
            from species.species import main as species_main
            species_main()
            break
        elif choice == "spells":
            from spells import prompt_and_print_class_spell_list
            prompt_and_print_class_spell_list()
        elif choice == "exit":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()