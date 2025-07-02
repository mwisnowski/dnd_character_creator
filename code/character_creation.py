"""
Core character creation logic for the D&D character creator project.
Handles ability scores, species, class, background, and skill calculation.
"""

from __future__ import annotations

from misc.abilities import interactive_ability_assignment, ability_modifier
from misc.backgrounds import select_background
from misc.skills import calculate_skill_scores
from species.species import main as species_select_main
from species.species_utils import handle_special_skill_traits
from classes.class_selection import select_class

PROFICIENCY_BONUS: dict[str, str] = {
    "<4": "+2",
}

def get_proficiency_bonus(level: int) -> int:
    """
    Returns the proficiency bonus for a given character level.
    1-4: +2, 5-8: +3, 9-12: +4, 13-16: +5, 17-20: +6
    """
    if level >= 17:
        return 6
    elif level >= 13:
        return 5
    elif level >= 9:
        return 4
    elif level >= 5:
        return 3
    else:
        return 2

class charGen:
    """
    Character generator class for D&D 5e.
    Stores all relevant character information and provides methods for creation.
    """
    def __init__(
        self,
        name: str = "",
        species: str = "",
        class_name: str = "",
        background: str = "",
        level: int = 1,
        ability_scores: dict[str, int] = None,
        alignment: str = "N/A",
        player_name: str = "",
        experience_points: int = 0,
        gender: str = "N/A",
        age: int = 18,
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
        self.proficiency_bonus = get_proficiency_bonus(self.level)
        self.inventory = []
        self.equipment = []
        self.gold_pieces = 0
        self.silver_pieces = 0
        self.copper_pieces = 0

    def as_dict(self):
        """
        Return the character as a dictionary of all main attributes for easy display or export.
        """
        return {
            "Name": self.name,
            "Species": self.species,
            "Class": self.class_name,
            "Background": self.background,
            "Level": self.level,
            "Alignment": self.alignment,
            "Player Name": self.player_name,
            "XP": self.experience_points,
            "Gender": self.gender,
            "Age": self.age,
            "Ability Scores": self.ability_scores if self.ability_scores else {},
            "Species Traits": getattr(self, 'species_traits', []),
            "Skill Scores": getattr(self, 'skill_scores', {}),
        }

    def __str__(self):
        char_dict = self.as_dict()
        # Only keys from Name through Age for alignment
        main_keys = [
            "Name", "Species", "Class", "Background", "Level", "Alignment",
            "Player Name", "XP", "Gender", "Age"
        ]
        max_key_len = max(len(k) for k in main_keys)
        lines = [f"{k + ':':<{max_key_len+2}} {char_dict[k]}" for k in main_keys]
        # Print Ability Scores
        lines.append("Ability Scores:")
        abilities = char_dict["Ability Scores"]
        if abilities:
            ability_key_len = max(len(k) for k in abilities)
            for subk, subv in abilities.items():
                mod = ability_modifier(subv)
                mod_str = f"+{mod}" if mod > 0 else str(mod)
                lines.append(f"  {subk + ':':<{ability_key_len+3}} {subv} ({mod_str})")
        else:
            lines.append("  None")
        # Print Skill Scores
        lines.append("Skill Scores:")
        skills = char_dict["Skill Scores"]
        if skills:
            skill_key_len = max(len(k) for k in skills)
            for skill, tup in skills.items():
                value, proficient = tup if isinstance(tup, tuple) else (tup, False)
                mod_str = f"+{value}" if value > 0 else str(value)
                prof_mark = " (X)" if proficient else ""
                lines.append(f"  {skill + ':':<{skill_key_len+3}} {mod_str}{prof_mark}")
        else:
            lines.append("  None")
        # Print Species Traits
        lines.append("Species Traits:")
        traits = char_dict["Species Traits"]
        if traits:
            for item in traits:
                lines.append(f"  - {item}")
        else:
            lines.append("  None")
        # Print Inventory
        lines.append("Inventory:")
        for item in getattr(self, 'inventory', []) or [None]:
            lines.append(f"  - {item}" if item else "  None")
        # Print Equipment (Weapons/Armor)
        lines.append("Equipment:")
        for item in getattr(self, 'equipment', []) or [None]:
            lines.append(f"  - {item}" if item else "  None")
        # Print Currency
        lines.append("Currency:")
        gp = getattr(self, 'gold_pieces', 0)
        sp = getattr(self, 'silver_pieces', 0)
        cp = getattr(self, 'copper_pieces', 0)
        if gp or sp or cp:
            currency_line = []
            if gp:
                currency_line.append(f"{gp} gp")
            if sp:
                currency_line.append(f"{sp} sp")
            if cp:
                currency_line.append(f"{cp} cp")
            lines.append("  " + ", ".join(currency_line))
        else:
            lines.append("  None")
        # Print Spell List
        lines.append("Spell List:")
        known_spells = getattr(self, 'known_spells', {})
        if known_spells:
            def level_label(level):
                if level == 'Cantrips':
                    return 'Cantrips'
                else:
                    return f"Level {level}"
            for level in sorted(known_spells.keys(), key=lambda x: (x != 'Cantrips', int(x) if x.isdigit() else 0)):
                lines.append(f"  {level_label(level)}:")
                for spell in sorted(known_spells[level].keys()):
                    lines.append(f"    - {spell}")
        else:
            lines.append("  None")
        return "\n".join(lines)
        
    def make_character(self):
        """
        Create a character instance with the provided attributes.
        This method can be expanded to include more complex character creation logic.
        """
        self.character_setup()
        self.determine_ability_scores()
        self.choose_background()
        self.choose_class()
        self.choose_species()
        self.calculate_skills()
        print("Character created successfully!")
        
    def character_setup(self):
        """
        Set up the character by rolling ability scores and choosing species.
        This method can be expanded to include more setup steps.
        """
        print("Setting up character...")
        self.player_name = input("What is your, the player's, name?\n> ")
        self.name = input("What is your characters name?\n> ")
    
    def choose_background(self):
        """
        Choose a background for the character using the backgrounds selection function.
        Saves the background and its details to the character instance.
        Also saves feat, skills, equipment, and applies ability score increases.
        Equipment and currency are parsed and merged with the character's inventory and currency.
        """
        bg_info = select_background()
        if bg_info:
            self.background = bg_info.get('Name', '') or next(iter(bg_info.keys()), '')
            self.background_details = bg_info
            # Feat
            self.feats = [bg_info.get('Feat')] if bg_info.get('Feat') else []
            # Skills
            self.skills = bg_info.get('Skill Proficiencies', [])
            # Equipment and inventory
            self.equipment.extend(bg_info.get('equipment', []))
            self.inventory.extend(bg_info.get('inventory', []))
            self.gold_pieces += bg_info.get('gold_pieces', 0)
            self.silver_pieces += bg_info.get('silver_pieces', 0)
            self.copper_pieces += bg_info.get('copper_pieces', 0)
            # Apply ability score increases
            asi = bg_info.get('Ability Score Increases', {})
            if asi and self.ability_scores:
                for k, v in asi.items():
                    if k in self.ability_scores:
                        self.ability_scores[k] += v
            print(f"Background selected: {self.background}")
        else:
            print("No background selected.")
            
    def choose_class(self):
        """
        Choose a class for the character using the class selection module.
        Saves the class name, chosen skills, class features, starting equipment, and selected spell to the character instance.
        Also manages the known_spells dictionary, with nested dicts for each spell level ("Cantrips" for level 0).
        """
        already_proficient = getattr(self, 'skills', [])
        # Pass known_spells to select_class
        known_spells = getattr(self, 'known_spells', {})
        result = select_class(current_level=self.level, already_proficient=already_proficient, known_spells=known_spells)
        if result:
            self.class_name = result['class_name']
            # Add chosen class skills to self.skills, avoiding duplicates
            for skill in result['chosen_skills']:
                if skill not in self.skills:
                    self.skills.append(skill)
            self.class_features = result['class_features']
            # Assign equipment, inventory, and currency
            self.equipment.extend(result.get('equipment', []))
            self.inventory.extend(result.get('inventory', []))
            self.gold_pieces += result.get('gold_pieces', 0)
            self.silver_pieces += result.get('silver_pieces', 0)
            self.copper_pieces += result.get('copper_pieces', 0)
            # Handle spell selection and known_spells (support multiple spells)
            new_spells = result.get('new_spells')
            if new_spells:
                if not hasattr(self, 'known_spells'):
                    self.known_spells = {}
                for spell_level, spell_name, spell_data in new_spells:
                    level_key = 'Cantrips' if spell_level == 0 else str(spell_level)
                    if level_key not in self.known_spells:
                        self.known_spells[level_key] = {}
                    self.known_spells[level_key][spell_name] = spell_data
            print(f"Class selected: {self.class_name}")
        else:
            print("No class selected.")
    
    def choose_species(self):
        """
        Choose a species for the character using the species selection module.
        Saves the species and its traits to the character instance.
        """
        result = species_select_main()
        if result and isinstance(result, dict):
            self.species = result.get('species', '')
            self.species_traits = result.get('species_traits', {})
            # Handle special skill-granting traits
            if hasattr(self, 'skills'):
                skills_before = set(self.skills)
            else:
                self.skills = []
                skills_before = set()
            updated_skills = handle_special_skill_traits(self.species_traits, self.skills)
            # If a skill was added, update the trait name to include the skill
            keen_skills = ["Insight", "Perception", "Survival"]
            if "Keen Senses" in self.species_traits:
                added = set(updated_skills) - skills_before
                for skill in keen_skills:
                    if skill in added:
                        idx = self.species_traits.index("Keen Senses")
                        self.species_traits[idx] = f"Keen Senses - {skill}"
                        break
            if "Skillful" in self.species_traits:
                added = set(updated_skills) - skills_before
                for skill in updated_skills:
                    if skill in added:
                        idx = self.species_traits.index("Skillful")
                        self.species_traits[idx] = f"Skillful - {skill}"
                        break
            self.skills = updated_skills
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

    def calculate_skills(self):
        """
        Determine skills for the character based on class and background.
        Calculates skill values using ability scores and proficiency bonus.
        """
        if not hasattr(self, 'skills'):
            self.skills = []
        self.skill_scores = calculate_skill_scores(
            self.ability_scores or {},
            self.proficiency_bonus,
            self.skills
        )

if __name__ == "__main__":
    # Example: Create a character and print details
    character = charGen()
    character.make_character()
    print("\nCharacter Sheet:\n", character, sep='')
