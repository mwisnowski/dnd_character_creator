"""
Utility functions for handling feats: adding, parsing, and applying feat effects (e.g., ability increases, fighting styles, tool/skill proficiencies).
"""
from InquirerPy import inquirer
from misc.feats import ORIGIN_FEATS, FIGHTING_STYLE_FEATS



ABILITY_SCORE_FEATS = [
    # Add feat names that grant ability score increases
]

def choose_fighting_style(styles_available, character=None):
    """
    Prompt the user to select a fighting style from the available list, filtering out any already chosen by the character.
    Returns the chosen style as a string.
    """
    filtered_styles = list(styles_available)
    if character is not None:
        # Gather all fighting styles already chosen (from feats or fighting_styles)
        already_chosen = set()
        # Check feats for tuples like ("Fighting Style", style)
        for feat in getattr(character, 'feats', []):
            if isinstance(feat, tuple) and feat[0] == 'Fighting Style' and len(feat) == 2:
                already_chosen.add(feat[1])
        # Also check character.fighting_styles if present
        for style in getattr(character, 'fighting_styles', []):
            already_chosen.add(style)
        filtered_styles = [s for s in styles_available if s not in already_chosen]
    if not filtered_styles:
        print("No new fighting styles available to choose.")
        return None
    style = inquirer.select(
        message="Choose a Fighting Style:",
        choices=filtered_styles
    ).execute()
    return style

def add_feat(character, feat_name, feat_data=None, available_fighting_styles=None):
    """
    Add a feat to the character, handling any special logic (e.g., fighting style selection, ability increases).
    Returns a dict of feat results (e.g., chosen style, ability increases) for display.
    """
    if feat_data is None:
        feat_data = ORIGIN_FEATS.get(feat_name, {})
    # Special handling for Fighting Style feat
    if feat_name == 'Fighting Style':
        # Always require available_fighting_styles
        from misc.feats import FIGHTING_STYLE_FEATS
        if not available_fighting_styles:
            available_fighting_styles = list(FIGHTING_STYLE_FEATS.keys())
        if feat_name not in available_fighting_styles:
            print(f"{feat_name} is not available to choose from.")
            return None
        style = choose_fighting_style(available_fighting_styles, character=character)
        if style is None:
            return None
        # Add to character's fighting_styles if present
        if character is not None:
            if not hasattr(character, 'fighting_styles'):
                character.fighting_styles = []
            if style not in character.fighting_styles:
                character.fighting_styles.append(style)
        return {'feat': feat_name, 'fighting_style': style}
    # For other feats, just return the name if valid
    if feat_name:
        return {'feat': feat_name}
    return None

def parse_feat(feat_name):
    """
    Return the parsed data for a feat (description, prerequisites, benefits).
    """
    result = ORIGIN_FEATS.get(feat_name)
    if result is None:
        return None
    return result
