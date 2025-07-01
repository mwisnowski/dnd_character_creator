from __future__ import annotations
import inquirer

BACKGROUND_DICT: dict[str, dict[str, str | list[str] | list[list[str]]]] = {
    'Acolyte': {
        'Description': 'You were a devoted servant in a place of worship. You learned the rituals '
        'of your faith and how to channel divine power as part of your service.',
        'Ability Scores': ['Intelligence', 'Wisdom', 'Charisma'],
        'Feat': 'Magic Initiate (Cleric)',
        'Skill Proficiencies': ['Insight', 'Religion'],
        'Tool Proficiencies': ['Caligrapher\'s Supplies'],
        'Equipment': [['Caligrapher\'s Supplies', 'Holy Symbol', 'Book (prayers)',
                       'Parchment (10 sheets)', 'Robe', '8 GP'],
                      ['50 GP']]
    },
    'Artisan': {
        'Description': 'You worked your way up from scrubbing floors to an apprenticeship creating '
        'your own crafts. You know how to schmooze a customer and have a keen eye for detail.',
        'Ability Scores': ['Strenth', 'Dexterity', 'Intelligence'],
        'Feat': 'Crafter',
        'Skill Proficiencies': ['Investigation', 'Perception'],
        'Tool Proficiencies': ['Artisan\'s Tools'],
        'Equipment': [['Artisan\'s Tools', '2 Pouches', 'Traveler\'s Clothes', '32GP'],
                      ['50 GP']]
    },
    'Charlatan': {
        'Description': 'You have learned to seek out a mark in taverns and pubs, and find the people '
        'most in search of less than honest goods, such as forgeries or sham magic items.',
        'Ability Scores': ['Dexterity', 'Constitution', 'Charisma'],
        'Feat': 'Skilled',
        'Skill Proficiencies': ['Deception', 'Sleight of Hand'],
        'Tool Proficiencies': ['Forgery Kit'],
        'Equipment': [['Forgery Kit', 'Costume', 'Fine Clothes', '15 GP'],
                      ['50 GP']]
    },
    'Criminal': {
        'Description': 'Whether you were a member of a criminal crew or a solo thief who only looked '
        'out for yourself, you know the best ways to slice some purse strings or how to find '
        'alternative means to enter a locked shop.',
        'Ability Scores': ['Dexterity', 'Constitution', 'Charisma'],
        'Feat': 'Alert',
        'Skill Proficiencies': ['Stealth', 'Sleight of Hand'],
        'Tool Proficiencies': ['Thieves\' Tools'],
        'Equipment': [['2 Daggers', 'Thieves\' Tools', 'Crowbar', '2 Pouches', 
                       'Traveler\'s Clothes', '16 GP'],
                      ['50 GP']]
    },
    'Entertainer': {
        'Description': 'You\'ve spent your life on either a literal or proverbial stage, performing '
        'for willing audiences. You have learned how to channel your talent for creation into a '
        'crowd-pleasing art form.',
        'Ability Scores': ['Strength', 'Dexterity', 'Charisma'],
        'Feat': 'Musician',
        'Skill Proficiencies': ['Performance', 'Acrobatics'],
        'Tool Proficiencies': ['Musical Instrument'],
        'Equipment': [['Musical Instrument', '2 Costumes', 'Mirror', 'Perfume',
                       'Traveler\'s Cothes', '11 GP'],
                      ['50 GP']]
    },
    'Farmer': {
        'Description': 'You\'ve tilled the soil or raised animals as livestock or to aid you in '
        'cultivating your fields. You\'ve gained a healthy respect for nature, in both its bounty and '
        'its wrath.',
        'Ability Scores': ['Strength', 'Constitution', 'Wisdom'],
        'Feat': 'Tough',
        'Skill Proficiencies': ['Animal Handling', 'Survival'],
        'Tool Proficiencies': ['Carpenter\'s Tools'],
        'Equipment': [['Sickle', 'Carpeter\'s Tools', 'Healer\'s Kit', 'Iron Pot',
                       'Shovel', 'Traveler\'s Clothes', '30 GP'],
                      ['50 GP']]
    },
    'Guard': {
        'Description': 'You\'ve put in your time standing watch over a city or location. You\'ve had '
        'your head on a swivel, keeping a watchful eye on raiding enemies on one side of a wall or '
        'criminal elements on the other.',
        'Ability Scores': ['Strength', 'Intelligence', 'Wisdom'],
        'Feat': 'Alert',
        'Skill Proficiencies': ['Athletics', 'Perception'],
        'Tool Proficiencies': ['Gaming Set'],
        'Equipment': [['Spear', 'Light Crossbow', '20 Bolts', 'Gaming Set',
                       'Hooded Lantern', 'Manacles', 'Quiver', 'Traveler\'s Clothes',
                       '20 GP'],
                      ['50 GP']]
    },
    'Hermit': {
        'Description': 'Whether alone in a hut or as part of a monastery, you\'ve spent a considerable '
        'amount of time outside the trappings of society. You’ve grown comfortable pondering the wonders '
        'and mysteries of creation.',
        'Ability Scores': ['Constitution', 'Wisdom', 'Charisma'],
        'Feat': 'Healer',
        'Skill Proficiencies': ['Religion', 'Medicine'],
        'Tool Proficiencies': ['Herbalism Kit'],
        'Equipment': [['Quarterstaff', 'Herbalism Kit', 'Bedroll', 'Book (philosophy)',
                       'Lamp', 'Oil (3 flasks)', 'Traveler\'s Clothes', '16 GP'],
                      ['50 GP']]
    },
    'Merchant': {
        'Description': 'As an apprentice to a trader or shopkeeper, you traveled either supplying artisans '
        'with the materials they needed or acquiring their goods to sell to your customers. You know how '
        'to make a deal and how to handle a long journey.',
        'Ability Scores': ['Constitution', 'Intelligence', 'Charisma'],
        'Feat': 'Lucky',
        'Skill Proficiencies': ['Animal Handling', 'Persuasion'],
        'Tool Proficiencies': ['Navigator\'s Tools'],
        'Equipment': [['Navigator\'s Tools', '2 Pouches', 'Traveler\'s Clothes',
                       '22 GP'],
                      ['50 GP']]
    },
    'Noble': {
        'Description': 'You grew up in the opulence and structure of wealth and societal privilege. You may '
        'have bristled against the restrictions and expectations of your role, but you learned a lot about '
        'courtly intrigue and the skills of leadership.',
        'Ability Scores': ['Strength', 'Intelligence', 'Charisma'],
        'Feat': 'Skilled',
        'Skill Proficiencies': ['History', 'Persuasion'],
        'Tool Proficiencies': ['Gaming Set'],
        'Equipment': [['Gaming Set', 'Fine Clothes', 'Perfume', '29 GP'],
                      ['50 GP']]
    },
    'Sage': {
        'Description': 'Your thirst for knowledge drew you to some of the greatest libraries and archives in '
        'the world. You\'ve got a knack for research and perhaps a rudimentary knowledge of magic gleaned '
        'from a book or two.',
        'Ability Scores': ['Constitution', 'Intelligence', 'Wisdom'],
        'Feat': 'Magic Initiate (Wizard)',
        'Skill Proficiencies': ['Arcana', 'History'],
        'Tool Proficiencies': ['Caligrapher\'s Supplies'],
        'Equipment': [['Quarterstaff', 'Caligrapher\'s Supplies', 'Book (history)',
                       'Parchment (8 sheets)', 'Robe', '8 GP'],
                      ['50 GP']]
    },
    'Sailor': {
        'Description': 'You called the open water your home, survived some of the sea\'s harshest storms. '
        'You\'ve swapped stories with the best of them, whether that\'s on the barstool of a random port or '
        'the denizens of the world beneath the waves.',
        'Ability Scores': ['Strength', 'Dexterity', 'Wisdom'],
        'Feat': 'Tavern Brawler',
        'Skill Proficiencies': ['Acrobatics', 'Survival'],
        'Tool Proficiencies': ['Navigator\'s Tools'],
        'Equipment': [['Dagger', 'Navigator\'s Tools', 'Rope', 'Traveler\'s Clothes',
                       '20 GP'],
                      ['50 GP']]
    },
    'Scribe': {
        'Description': 'The written word has been your domain, either copying tomes, crafting government '
        'documents, or producing your own texts. Your eye for detail and ability to catch errors and '
        'mistakes is finely honed.',
        'Ability Scores': ['Dexterity', 'Intelligence', 'Wisdom'],
        'Feat': 'Skilled',
        'Skill Proficiencies': ['Insight', 'Perception'],
        'Tool Proficiencies': ['Calligrapher\'s Supplies'],
        'Equipment': [['Calligrapher\'s Supplies', 'Fine Clothes', 'Lamp', 'Oil (3 flasks)',
                       'Parchment (12 sheets)', '23 GP'],
                      ['50 GP']]
    },
    'Soldier': {
        'Description': 'You can hardly remember a time when you didn\'t wield a weapon. You\'re well-versed '
        'in the ways of battle and war to protect the realm, and you have the muscle memory to prove it.',
        'Ability Scores': ['Strength', 'Dexterity', 'Constitution'],
        'Feat': 'Savage Attacker',
        'Skill Proficiencies': ['Athletics', 'Intimidation'],
        'Tool Proficiencies': ['Gaming Set'],
        'Equipment': [['Gaming Set', 'Traveler\'s Clothes', '20 GP'],
                      ['50 GP']]
    },
    'Wayfarer': {
        'Description': 'An urchin or societal castoff, you learned to survive. Forging your own path on the '
        'streets and possibly turning to crime when needed, you’ve managed to keep your pride and hope that '
        'destiny has more for you yet.',
        'Ability Scores': ['Dexterity', 'Wisdom', 'Charisma'],
        'Feat': 'Lucky',
        'Skill Proficiencies': ['Insight', 'Stealth'],
        'Tool Proficiencies': ['Thieve\'s Tools'],
        'Equipment': [['2 Daggers', 'Thieve\'s Tools','Gaming Set (any)', 'Bedroll',
                       '2 pouces', 'Traveler\'s Clothes', '16 GP'],
                      ['50 GP']]
    }
}

def select_background() -> dict[str, str | list[str] | list[list[str]]]:
    """
    Use inquirer to select a background and handle ability score increases.
    Returns the selected background's full info, including chosen ability score increases.
    """
    background_names = list(BACKGROUND_DICT.keys())
    while True:
        bg_question = [
            inquirer.List(
                'background',
                message="Select a background:",
                choices=background_names,
                carousel=True,
            )
        ]
        bg_answer = inquirer.prompt(bg_question)
        if not bg_answer:
            print("No background selected.")
            return {}
        bg_name = bg_answer['background']
        bg_info = dict(BACKGROUND_DICT[bg_name])  # Copy to avoid mutating original

        # Show details and confirm selection
        print(f"\nDetails for {bg_name}:")
        for key, value in bg_info.items():
            if key == 'Equipment':
                print(f"{key}: Option 1: {', '.join(value[0])}")
                print(f"           Option 2: {', '.join(value[1])}")
            elif isinstance(value, list):
                print(f"{key}: {', '.join(value)}")
            else:
                print(f"{key}: {value}")
        confirm_question = [
            inquirer.Confirm(
                'confirm',
                message=f"Would you like to select {bg_name} as your background?",
                default=True
            )
        ]
        confirm_answer = inquirer.prompt(confirm_question)
        if not confirm_answer or not confirm_answer.get('confirm'):
            print("Background not selected. Returning to background list.")
            continue

        # Ability score increase logic
        ability_scores = bg_info.get('Ability Scores', [])
        if isinstance(ability_scores, list) and len(ability_scores) == 3:
            as_choices = [
                "+1 to all three",
                "+2 to one, +1 to another"
            ]
            as_question = [
                inquirer.List(
                    'as_method',
                    message=f"How would you like to assign ability score increases for {bg_name}?",
                    choices=as_choices
                )
            ]
            as_answer = inquirer.prompt(as_question)
            if as_answer['as_method'] == "+1 to all three":
                bg_info['Ability Score Increases'] = {k: 1 for k in ability_scores}
            else:
                # Choose +2
                plus_two_question = [
                    inquirer.List(
                        'plus_two',
                        message="Which ability gets +2?",
                        choices=ability_scores
                    )
                ]
                plus_two_answer = inquirer.prompt(plus_two_question)
                plus_two = plus_two_answer['plus_two']
                # Choose +1 (not the same as +2)
                plus_one_choices = [a for a in ability_scores if a != plus_two]
                plus_one_question = [
                    inquirer.List(
                        'plus_one',
                        message="Which ability gets +1?",
                        choices=plus_one_choices
                    )
                ]
                plus_one_answer = inquirer.prompt(plus_one_question)
                plus_one = plus_one_answer['plus_one']
                bg_info['Ability Score Increases'] = {
                    plus_two: 2,
                    plus_one: 1,
                    [a for a in ability_scores if a not in (plus_two, plus_one)][0]: 0
                }
        # Equipment selection logic
        equipment = bg_info.get('Equipment', [])
        if isinstance(equipment, list) and len(equipment) == 2:
            equip_choices = [
                f"Option 1: {', '.join(equipment[0])}",
                f"Option 2: {', '.join(equipment[1])}"
            ]
            equip_question = [
                inquirer.List(
                    'equip_choice',
                    message="Choose your starting equipment:",
                    choices=equip_choices
                )
            ]
            equip_answer = inquirer.prompt(equip_question)
            if equip_answer['equip_choice'] == equip_choices[0]:
                bg_info['Selected Equipment'] = equipment[0]
            else:
                bg_info['Selected Equipment'] = equipment[1]
        return bg_info

