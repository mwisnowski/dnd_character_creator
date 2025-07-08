# Dungeons & Dragons 5e Character Generator

A command-line tool for creating, managing, and exporting Dungeons & Dragons 5e characters, based on the 2024 Player's Handbook. This project aims to provide a comprehensive, user-friendly experience for both new and experienced players, supporting the latest rules and options.

## Features

- Interactive, step-by-step character creation process
- Support for all core classes, subclasses, species, backgrounds, and feats from the 2024 PHB
- Handles class feature-granted spells, spell selection, and spellcasting rules
- Displays readable tables for spellcasting, class features, and companion stat blocks
- Clarifies lineage/ancestry/legacy trait selection for species
- Save and load in-progress characters (CSV format)
- Export character sheets to PDF (with official template)
- Browse and lookup class, feat, and spell information
- Consistent, readable formatting for all tables and lists
- Designed for extensibility and future D&D 5e updates

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mwisnowski/dnd_character_creator.git
   cd dnd_character_creator
   ```

2. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using:
```bash
python main.py
```

The main menu provides the following options:
- **New**: Create a new character
- **Load**: Load an existing character from a CSV file (in progress)
- **Browse**: Lookup class, feat, and spell information

## Project Structure

- `code/`: Core logic and modules
  - `main.py`: Entry point and CLI interface
  - `character_creation.py`: Main character creation logic and data model
  - `classes/`: Class, subclass, and feature definitions
  - `species/`: Species, lineage, and ancestry logic
  - `spells/`: Spell lists, spell utilities, and spellcasting rules
  - `equipment/`: Weapons, armor, and equipment data
  - `misc/`: Abilities, backgrounds, feats, skills, and utility functions
- `resources/`: PDF templates and static resources

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.