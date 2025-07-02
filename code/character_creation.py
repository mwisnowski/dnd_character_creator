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
        # Track all proficiencies from class, background, and species
        self.proficiencies = {
            'weapons': set(),
            'armor': set(),
            'tools': set(),
        }

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
            "Proficiencies": self.proficiencies,
        }


    def __str__(self):
        char_dict = self.as_dict()
        main_keys = [
            "Name", "Species", "Class", "Background", "Level", "Alignment",
            "Player Name", "XP", "Gender", "Age"
        ]
        max_key_len = max(len(k) for k in main_keys)
        lines = [f"{k + ':':<{max_key_len+2}} {char_dict[k]}" for k in main_keys]

        # Print Class Features
        lines.append("Class Features:")
        class_name = getattr(self, 'class_name', None)
        class_features = getattr(self, 'class_features', [])
        special_choices = getattr(self, 'class_special_choices', {})
        if class_name and class_features:
            lines.append(f"  {class_name}")
            for feature in class_features:
                lines.append(f"    - {feature}")
                # Show special choices for this feature if present
                if special_choices and feature in special_choices:
                    val = special_choices[feature]
                    if isinstance(val, list):
                        for v in val:
                            lines.append(f"      * {v}")
                    else:
                        lines.append(f"      * {val}")
        else:
            lines.append("  None")
            
        # Print Proficiencies
        lines.append("Proficiencies:")
        profs = char_dict.get("Proficiencies", {})
        # Weapons
        from equipment.weapons_dict import SIMPLE_WEAPONS_DICT, MARTIAL_WEAPONS_DICT
        weapon_profs = profs.get('weapons', set())
        simple_weapons = set()
        martial_weapons = set()
        simple_all = False
        martial_all = False
        for w in weapon_profs:
            if w.lower() in ["simple weapons", "all simple weapons", "simple weapon proficiency"]:
                simple_all = True
            elif w.lower() in ["martial weapons", "all martial weapons", "martial weapon proficiency"]:
                martial_all = True
            elif w in SIMPLE_WEAPONS_DICT:
                simple_weapons.add(w)
            elif w in MARTIAL_WEAPONS_DICT:
                martial_weapons.add(w)
            else:
                # If not recognized, just list it under simple for now
                simple_weapons.add(w)
        lines.append("  Weapons:")
        lines.append("    Simple Weapons:")
        if simple_all:
            lines.append("      - All")
        elif simple_weapons:
            for w in sorted(simple_weapons):
                lines.append(f"      - {w}")
        else:
            lines.append("      - None")
        lines.append("    Martial Weapons:")
        if martial_all:
            lines.append("      - All")
        elif martial_weapons:
            for w in sorted(martial_weapons):
                lines.append(f"      - {w}")
        else:
            lines.append("      - None")
        # Armor
        armor_profs = profs.get('armor', set())
        lines.append("  Armor:")
        if armor_profs:
            for a in sorted(armor_profs):
                lines.append(f"    - {a}")
        else:
            lines.append("  None")
        # Tools
        tool_profs = profs.get('tools', set())
        if tool_profs:
            for t in sorted(tool_profs):
                lines.append(f"  {t}")
        else:
            lines.append("  None")

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
        inventory = getattr(self, 'inventory', []) or [None]
        weapon_mastery = set()
        if hasattr(self, 'class_special_choices') and self.class_special_choices:
            # If weapon mastery present, collect mastered weapons
            for k, v in self.class_special_choices.items():
                if isinstance(v, list):
                    for item in v:
                        weapon_mastery.add(item)
                elif isinstance(v, str):
                    weapon_mastery.add(v)
        for item in inventory:
            if item:
                # Mark with (M) if weapon mastery applies
                base = item.split(' x ')[0] if ' x ' in item else item
                mark = " (M)" if base in weapon_mastery else ""
                lines.append(f"  - {item}{mark}")
            else:
                lines.append("  None")

        # Print Equipment (Weapons/Armor)
        lines.append("Equipment:")
        equipment = getattr(self, 'equipment', []) or [None]
        for item in equipment:
            if item:
                base = item.split(' x ')[0] if ' x ' in item else item
                mark = " (M)" if base in weapon_mastery else ""
                lines.append(f"  - {item}{mark}")
            else:
                lines.append("  None")

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
            # Proficiencies
            bg_profs = bg_info.get('proficiencies', {})
            for k in ['weapons', 'armor', 'tools']:
                self.proficiencies[k].update(bg_profs.get(k, set()))
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
        Also saves any special class feature choices (e.g., weapon mastery, divine order) for display.
        """
        already_proficient = getattr(self, 'skills', [])
        known_spells = getattr(self, 'known_spells', {})
        result = select_class(current_level=self.level, already_proficient=already_proficient, known_spells=known_spells)
        if result:
            self.class_name = result['class_name']
            # Add chosen class skills to self.skills, avoiding duplicates
            for skill in result['chosen_skills']:
                if skill not in self.skills:
                    self.skills.append(skill)
            self.class_features = result['class_features']
            # Save special class feature choices for display (e.g., weapon mastery, divine order)
            self.class_special_choices = {}
            for key in result:
                # Only include keys that are not standard fields
                if key not in [
                    'class_name', 'chosen_skills', 'class_features', 'equipment', 'inventory',
                    'gold_pieces', 'silver_pieces', 'copper_pieces', 'new_spells', 'proficiencies', 'gained_proficiencies', 'extra_cantrips'
                ]:
                    # Map to the feature name if possible
                    feature_name = key.replace('_', ' ').title()
                    self.class_special_choices[feature_name] = result[key]
            # If extra cantrips were granted (e.g. Thaumaturge), add them to known_spells
            extra_cantrips = result.get('extra_cantrips', [])
            if extra_cantrips:
                if not hasattr(self, 'known_spells'):
                    self.known_spells = {}
                if 'Cantrips' not in self.known_spells:
                    self.known_spells['Cantrips'] = {}
                for spell_name, spell_data in extra_cantrips:
                    self.known_spells['Cantrips'][spell_name] = spell_data
            # Assign equipment, inventory, and currency
            self.equipment.extend(result.get('equipment', []))
            self.inventory.extend(result.get('inventory', []))
            self.gold_pieces += result.get('gold_pieces', 0)
            self.silver_pieces += result.get('silver_pieces', 0)
            self.copper_pieces += result.get('copper_pieces', 0)
            # Proficiencies
            class_profs = result.get('proficiencies', {})
            for k in ['weapons', 'armor', 'tools']:
                self.proficiencies[k].update(class_profs.get(k, set()))
            # Merge any proficiencies gained from class feature choices (e.g. Protector Divine Order)
            gained_profs = result.get('gained_proficiencies', {})
            for k in ['weapons', 'armor', 'tools']:
                self.proficiencies[k].update(gained_profs.get(k, set()))
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
            # Proficiencies
            species_profs = result.get('proficiencies', {})
            for k in ['weapons', 'armor', 'tools']:
                self.proficiencies[k].update(species_profs.get(k, set()))
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
