CANTRIPS_DICT: dict[str, dict] = {
    "Acid Splash": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "You hurl a bubble of acid."
    },
    "Blade Ward": {
        "school": "Abjuration",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "You gain resistance to bludgeoning, piercing, and slashing damage from weapon attacks until the end of your next turn."
    },
    "Chill Touch": {
        "school": "Necromancy",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "You create a ghostly skeletal hand."
    },
    "Dancing Lights": {
        "school": "Illusion",
        "classes": ["Bard", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "You create up to four torch-sized lights."
    },
    "Druidcraft": {
        "school": "Transmutation",
        "classes": ["Druid"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Whisper to the spirits of nature."
    },
    "Eldritch Blast": {
        "school": "Evocation",
        "classes": ["Warlock"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "A beam of crackling energy."
    },
    "Elementalism": {
        "school": "Transmutation",
        "classes": ["Druid", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Manipulate elemental forces."
    },
    "Fire Bolt": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "A mote of fire."
    },
    "Friends": {
        "school": "Enchantment",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "10 feet",
        "components": ["S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Advantage on Charisma checks directed at one creature."
    },
    "Guidance": {
        "school": "Divination",
        "classes": ["Cleric", "Druid"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Touch one willing creature. Add 1d4 to an ability check."
    },
    "Light": {
        "school": "Evocation",
        "classes": ["Bard", "Cleric", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "M"],
        "duration": "1 hour",
        "description": "Object sheds bright light in a 20-foot radius."
    },
    "Mage Hand": {
        "school": "Conjuration",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S"],
        "duration": "1 minute",
        "description": "A spectral hand appears."
    },
    "Mending": {
        "school": "Transmutation",
        "classes": ["Bard", "Cleric", "Druid", "Sorcerer", "Wizard"],
        "casting_time": "1 minute",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "Repairs a single break or tear."
    },
    "Message": {
        "school": "Transmutation",
        "classes": ["Bard", "Druid", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["S", "M"],
        "duration": "1 round",
        "description": "Whisper a message."
    },
    "Mind Sliver": {
        "school": "Enchantment",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V"],
        "duration": "1 round",
        "description": "Psychic spike."
    },
    "Minor Illusion": {
        "school": "Illusion",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["S", "M"],
        "duration": "1 minute",
        "description": "Create a sound or image."
    },
    "Poison Spray": {
        "school": "Necromancy",
        "classes": ["Druid", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "A puff of poison."
    },
    "Prestidigitation": {
        "school": "Transmutation",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "10 feet",
        "components": ["V", "S"],
        "duration": "Up to 1 hour",
        "description": "Minor magical tricks."
    },
    "Produce Flame": {
        "school": "Conjuration",
        "classes": ["Druid"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "10 minutes",
        "description": "A flickering flame appears."
    },
    "Ray of Frost": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "A frigid beam."
    },
    "Resistance": {
        "school": "Abjuration",
        "classes": ["Cleric", "Druid"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Touch one willing creature. Add 1d4 to a saving throw."
    },
    "Sacred Flame": {
        "school": "Evocation",
        "classes": ["Cleric"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Radiant flame descends."
    },
    "Shillelagh": {
        "school": "Transmutation",
        "classes": ["Druid"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V", "S", "M"],
        "duration": "1 minute",
        "description": "Club or quarterstaff becomes magical."
    },
    "Shocking Grasp": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Lightning springs from your hand."
    },
    "Sorcerous Burst": {
        "school": "Evocation",
        "classes": ["Sorcerer"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Burst of magical energy."
    },
    "Spare the Dying": {
        "school": "Necromancy",
        "classes": ["Cleric", "Druid"],
        "casting_time": "Action",
        "range": "15 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Stabilize a creature at 0 hit points."
    },
    "Starry Wisp": {
        "school": "Evocation",
        "classes": ["Bard", "Druid"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "A mote of starlight."
    },
    "Thaumaturgy": {
        "school": "Transmutation",
        "classes": ["Cleric"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V"],
        "duration": "Up to 1 minute",
        "description": "Manifest a minor wonder."
    },
    "Thorn Whip": {
        "school": "Transmutation",
        "classes": ["Druid"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "A vine whips out."
    },
    "Thunderclap": {
        "school": "Evocation",
        "classes": ["Bard", "Druid", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["S"],
        "duration": "Instantaneous",
        "description": "A burst of thunderous sound."
    },
    "Toll the Dead": {
        "school": "Necromancy",
        "classes": ["Cleric", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "A bell tolls for the dead."
    },
    "True Strike": {
        "school": "Divination",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["S", "M"],
        "duration": "Instantaneous",
        "description": "Divine insight."
    },
    "Vicious Mockery": {
        "school": "Enchantment",
        "classes": ["Bard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V"],
        "duration": "Instantaneous",
        "description": "Insult a creature."
    },
    "Word of Radiance": {
        "school": "Evocation",
        "classes": ["Cleric"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "M"],
        "duration": "Instantaneous",
        "description": "Divine radiance erupts."
    },
}
