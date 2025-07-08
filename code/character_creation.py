"""
Core character creation logic for the D&D character creator project.
Handles ability scores, species, class, background, and skill calculation.
"""

from __future__ import annotations


from misc.abilities import interactive_ability_assignment, ability_modifier
from misc.backgrounds import select_background
from misc.skills import calculate_skill_scores
from misc.backgrounds_utils import parse_equipment_items
from species.species import main as species_select_main
from species.species_utils import handle_special_skill_traits
from classes.class_selection import select_class
from misc.feats_utils import parse_feat
from equipment.weapons_dict import SIMPLE_WEAPONS_DICT, MARTIAL_WEAPONS_DICT
from equipment.armor_dict import LIGHT_ARMOR_DICT, MEDIUM_ARMOR_DICT, HEAVY_ARMOR_DICT, SHIELD_DICT

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

    Main output format is via __str__, which prints a detailed character sheet.
    Use as_dict() for a dictionary representation suitable for export or further processing.
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
        # Feats (always a list of dicts, e.g. {"feat": "Fighting Style", "fighting_style": "Archery"})
        self.feats = []

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

        # Print Feats Section
        lines.append("Feats:")
        if self.feats:
            for feat in self.feats:
                if isinstance(feat, dict):
                    if feat.get('feat') == 'Fighting Style' and feat.get('fighting_style'):
                        lines.append(f"  - Fighting Style ({feat['fighting_style']})")
                    elif feat.get('feat'):
                        lines.append(f"  - {feat['feat']}")
                elif isinstance(feat, str):
                    lines.append(f"  - {feat}")
        else:
            lines.append("  None")

        # ...existing code for Class Features, Proficiencies, Ability Scores, etc...
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

        # ...existing code for Proficiencies, Ability Scores, etc...
        # Print Proficiencies
        profs = char_dict.get("Proficiencies", {})
        lines.append("Proficiencies:")
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
        armor_profs = profs.get('armor', set())
        lines.append("  Armor:")
        if armor_profs:
            for a in sorted(armor_profs):
                lines.append(f"    - {a}")
        else:
            lines.append("  None")
        tool_profs = profs.get('tools', set())
        if tool_profs:
            for t in sorted(tool_profs):
                lines.append(f"  {t}")
        else:
            lines.append("  None")

        # ...existing code for Ability Scores, Skills, Traits, Inventory, Equipment, Currency, Spellcasting, Spell List...
        # Print Ability Scores
        lines.append("Ability Scores:")
        abilities = char_dict["Ability Scores"]
        saving_throw_profs = getattr(self, 'saving_throw_proficiencies', [])
        if abilities:
            ability_key_len = max(len(k) for k in abilities)
            for subk, subv in abilities.items():
                mod = ability_modifier(subv)
                mod_str = f"+{mod}" if mod > 0 else str(mod)
                save_prof = " (P)" if subk in saving_throw_profs else ""
                lines.append(f"  {subk + ':':<{ability_key_len+3}} {subv} ({mod_str}){save_prof}")
        else:
            lines.append("  None")

        lines.append("Skill Scores:")
        skills = char_dict["Skill Scores"]
        if skills:
            skill_key_len = max(len(k) for k in skills)
            for skill, tup in skills.items():
                value, proficient = tup if isinstance(tup, tuple) else (tup, False)
                mod_str = f"+{value}" if value > 0 else str(value)
                prof_mark = " (P)" if proficient else ""
                lines.append(f"  {skill + ':':<{skill_key_len+3}} {mod_str}{prof_mark}")
        else:
            lines.append("  None")

        lines.append("Species Traits:")
        traits = char_dict["Species Traits"]
        if traits:
            for item in traits:
                lines.append(f"  - {item}")
        else:
            lines.append("  None")

        lines.append("Inventory:")
        inventory = getattr(self, 'inventory', []) or [None]
        weapon_mastery = set()
        if hasattr(self, 'class_special_choices') and self.class_special_choices:
            for k, v in self.class_special_choices.items():
                if isinstance(v, list):
                    for item in v:
                        weapon_mastery.add(item)
                elif isinstance(v, str):
                    weapon_mastery.add(v)
        for item in inventory:
            if item:
                base = item.split(' x ')[0] if ' x ' in item else item
                mark = " (M)" if base in weapon_mastery else ""
                lines.append(f"  - {item}{mark}")
            else:
                lines.append("  None")

        lines.append("Equipment:")
        equipment = getattr(self, 'equipment', []) or [None]
        weapon_profs = self.proficiencies.get('weapons', set())
        armor_profs = self.proficiencies.get('armor', set())
        for item in equipment:
            if item:
                base = item.split(' x ')[0] if ' x ' in item else item
                mark = ""
                if base in weapon_mastery:
                    mark += " (M)"
                is_prof = False
                if (
                    base in weapon_profs or
                    ("Simple Weapons" in weapon_profs and base in SIMPLE_WEAPONS_DICT) or
                    ("Martial Weapons" in weapon_profs and base in MARTIAL_WEAPONS_DICT)
                ):
                    is_prof = True
                if (
                    base in armor_profs or
                    ("Light Armor" in armor_profs and base in LIGHT_ARMOR_DICT) or
                    ("Medium Armor" in armor_profs and base in MEDIUM_ARMOR_DICT) or
                    ("Heavy Armor" in armor_profs and base in HEAVY_ARMOR_DICT) or
                    ("Shields" in armor_profs and base in SHIELD_DICT)
                ):
                    is_prof = True
                if is_prof:
                    mark += " (P)"
                lines.append(f"  - {item}{mark}")
            else:
                lines.append("  None")

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

        if hasattr(self, 'spellcasting_ability') and self.spellcasting_ability:
            lines.append("Spellcasting:")
            lines.append(f"  Ability: {self.spellcasting_ability}")
            mod = getattr(self, 'spellcasting_modifier', None)
            if mod is not None:
                mod_str = f"+{mod}" if mod > 0 else str(mod)
                lines.append(f"  Modifier: {mod_str}")
            dc = getattr(self, 'spell_save_dc', None)
            if dc is not None:
                lines.append(f"  Save DC: {dc}")

        lines.append("Spell List:")
        # Combine known_spells and class_feature_spells for display
        known_spells = getattr(self, 'known_spells', {})
        feature_spells = getattr(self, 'class_feature_spells', {})
        # Merge both dicts into a new dict for display
        combined_spells = {}
        # Add known_spells
        for level, spells in (known_spells or {}).items():
            combined_spells.setdefault(level, {}).update(spells)
        # Add feature_spells (convert int keys to str for consistency)
        for level, spells in (feature_spells or {}).items():
            level_key = 'Cantrips' if str(level) == '0' else str(level)
            combined_spells.setdefault(level_key, {}).update(spells)
        if combined_spells:
            def level_label(level):
                if level == 'Cantrips':
                    return 'Cantrips'
                else:
                    return f"Level {level}"
            for level in sorted(combined_spells.keys(), key=lambda x: (x != 'Cantrips', int(x) if x.isdigit() else 0)):
                lines.append(f"  {level_label(level)}:")
                for spell in sorted(combined_spells[level].keys()):
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
    
    def add_items_from_source(self, source: dict) -> None:
        """
        Add equipment, inventory, and currency from a source dict (background, class, etc).
        Modifies self.equipment, self.inventory, self.gold_pieces, self.silver_pieces, self.copper_pieces in place.
        """
        self.equipment.extend(source.get('equipment', []))
        self.inventory.extend(source.get('inventory', []))
        self.gold_pieces += source.get('gold_pieces', 0)
        self.silver_pieces += source.get('silver_pieces', 0)
        self.copper_pieces += source.get('copper_pieces', 0)

    def merge_proficiencies(self, prof_dict: dict) -> None:
        """
        Merge weapon, armor, and tool proficiencies from a dict into self.proficiencies.
        """
        for k in ['weapons', 'armor', 'tools']:
            self.proficiencies[k].update(prof_dict.get(k, set()))

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
            self.feats = []
            if bg_info.get('Feat'):
                parsed_feat = parse_feat(bg_info['Feat'])
                if parsed_feat:
                    # Always store as dict for consistency
                    if isinstance(parsed_feat, dict):
                        self.feats.append(parsed_feat)
                    elif isinstance(parsed_feat, str):
                        self.feats.append({'feat': parsed_feat})
            # Skills
            self.skills = bg_info.get('Skill Proficiencies', [])
            # Equipment, inventory, currency
            self.add_items_from_source(bg_info)
            # Proficiencies
            self.merge_proficiencies(bg_info.get('proficiencies', {}))
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
        # Pass self as the character instance to select_class so that add_feat can prompt and update feats/fighting_styles
        result = select_class(current_level=self.level, already_proficient=already_proficient, known_spells=known_spells, character=self)
        if result:
            self.class_name = result['class_name']
            # Save spellcasting ability if present
            self.spellcasting_ability = result.get('spellcasting_ability')
            # Save saving throw proficiencies if present
            self.saving_throw_proficiencies = result.get('saving_throws', [])
            # Set spellcasting modifier if ability and scores are present
            if self.spellcasting_ability and self.ability_scores and self.spellcasting_ability in self.ability_scores:
                self.spellcasting_modifier = ability_modifier(self.ability_scores[self.spellcasting_ability])
            else:
                self.spellcasting_modifier = None
            # Set spell save DC if spellcasting modifier is available
            if self.spellcasting_modifier is not None:
                self.spell_save_dc = 8 + self.spellcasting_modifier + self.proficiency_bonus
            else:
                self.spell_save_dc = None
            # Add chosen class skills to self.skills, avoiding duplicates
            for skill in result['chosen_skills']:
                if skill not in self.skills:
                    self.skills.append(skill)
            self.class_features = result['class_features']
            # Save special class feature choices for display (e.g., weapon mastery, divine order)
            self.class_special_choices = {}
            for key in result:
                if key not in [
                    'class_name', 'chosen_skills', 'class_features', 'equipment', 'inventory',
                    'gold_pieces', 'silver_pieces', 'copper_pieces', 'new_spells', 'proficiencies', 'gained_proficiencies', 'extra_cantrips', 'spellcasting_ability', 'feats_gained', 'class_feature_spells'
                ]:
                    feature_name = key.replace('_', ' ').title()
                    self.class_special_choices[feature_name] = result[key]
            # Handle feats from class selection
            feats_gained = result.get('feats_gained', [])
            if feats_gained:
                for feat in feats_gained:
                    # Always store as dict for consistency
                    if isinstance(feat, dict):
                        self.feats.append(feat)
                    elif isinstance(feat, str):
                        parsed = parse_feat(feat)
                        if parsed:
                            if isinstance(parsed, dict):
                                self.feats.append(parsed)
                            elif isinstance(parsed, str):
                                self.feats.append({'feat': parsed})
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
            self.add_items_from_source(result)
            # Proficiencies
            self.merge_proficiencies(result.get('proficiencies', {}))
            # Merge any proficiencies gained from class feature choices (e.g. Protector Divine Order)
            self.merge_proficiencies(result.get('gained_proficiencies', {}))
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
            # Store class feature-granted spells
            self.class_feature_spells = result.get('class_feature_spells', {})
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
