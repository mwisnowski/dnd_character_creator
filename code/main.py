from __future__ import annotations

from InquirerPy import inquirer

def main():
    while True:
        choice = inquirer.select(
            message="Main Menu:",
            choices=[
                {"name": "Species", "value": "species"},
                {"name": "Exit", "value": "exit"}
            ],
            
        ).execute()
        if choice == "species":
            from species.species import main as species_main
            species_main()
            break
        elif choice == "exit":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()