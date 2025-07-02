SECOND_LEVEL_SPELLS_DICT: dict[str, dict] = {
    "Aid": {
        "school": "Abjuration",
        "classes": ["Cleric", "Paladin"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "8 hours",
        "description": "Bolster up to three creatures; each target's hit point maximum and current hit points increase by 5 for the duration."
    },
    "Animal Messenger": {
        "school": "Enchantment",
        "classes": ["Bard", "Druid", "Ranger"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "24 hours",
        "description": "Use a Tiny beast to deliver a message to a recipient you describe."
    },
    "Alter Self": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 hour",
        "description": "Assume a different form: Aquatic Adaptation, Change Appearance, or Natural Weapons."
    },
    "Arcane Vigor": {
        "school": "Abjuration",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "1 minute",
        "description": "You gain temporary hit points equal to your spellcasting ability modifier plus your spellcasting level."
    },
    "Arcane Lock": {
        "school": "Abjuration",
        "classes": ["Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Until dispelled",
        "description": "Magically lock a door, window, gate, chest, or entryway."
    },
    "Augury": {
        "school": "Divination",
        "classes": ["Cleric"],
        "casting_time": "1 minute",
        "range": "Self",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "Receive an omen about the results of a specific course of action within 30 minutes."
    },
    "Barkskin": {
        "school": "Transmutation",
        "classes": ["Druid", "Ranger"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 hour",
        "description": "Target's skin becomes bark-like; AC can't be less than 16."
    },
    "Beast Sense": {
        "school": "Divination",
        "classes": ["Druid", "Ranger"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["S"],
        "duration": "Concentration, up to 1 hour",
        "description": "You touch a willing beast and perceive through its senses."
    },
    "Blindness/Deafness": {
        "school": "Necromancy",
        "classes": ["Bard", "Cleric", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V"],
        "duration": "1 minute",
        "description": "Cause one creature to be blinded or deafened (Concentration not required)."
    },
    "Blur": {
        "school": "Illusion",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V"],
        "duration": "Concentration, up to 1 minute",
        "description": "Your body becomes blurred, shifting and wavering to all who can see you."
    },
    "Borrowed Knowledge": {
        "school": "Divination",
        "classes": ["Bard", "Cleric", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "Gain proficiency in one skill for the duration."
    },
    "Calm Emotions": {
        "school": "Enchantment",
        "classes": ["Bard", "Cleric"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Suppress strong emotions in a group of people."
    },
    "Cloud of Daggers": {
        "school": "Conjuration",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Fill a 5-foot cube with spinning daggers."
    },
    "Continual Flame": {
        "school": "Evocation",
        "classes": ["Cleric", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Until dispelled",
        "description": "Create a flame that burns without heat or fuel."
    },
    "Cordon of Arrows": {
        "school": "Transmutation",
        "classes": ["Ranger"],
        "casting_time": "Action",
        "range": "5 feet",
        "components": ["V", "S", "M"],
        "duration": "8 hours",
        "description": "Plant four pieces of nonmagical ammunition in the ground to ward an area."
    },
    "Crown of Madness": {
        "school": "Enchantment",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "One humanoid must make a Wisdom save or be charmed and forced to attack others."
    },
    "Darkness": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Magical darkness spreads from a point you choose."
    },
    "Darkvision": {
        "school": "Transmutation",
        "classes": ["Druid", "Ranger", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "8 hours",
        "description": "Grant a creature the ability to see in the dark."
    },
    "Detect Thoughts": {
        "school": "Divination",
        "classes": ["Bard", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Read the surface thoughts of creatures."
    },
    "Dragon's Breath": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Bonus Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Grant a creature the ability to exhale magical energy in a chosen damage type."
    },
    "Enhance Ability": {
        "school": "Transmutation",
        "classes": ["Bard", "Cleric", "Druid", "Sorcerer"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 hour",
        "description": "Grant a creature advantage on ability checks with one ability score."
    },
    "Enlarge/Reduce": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Cause a creature or object to grow larger or smaller."
    },
    "Enthrall": {
        "school": "Enchantment",
        "classes": ["Bard", "Warlock"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "1 minute",
        "description": "You weave a distracting string of words, causing creatures of your choice to have disadvantage on Wisdom (Perception) checks to perceive creatures other than you."
    },
    "Find Steed": {
        "school": "Conjuration",
        "classes": ["Paladin"],
        "casting_time": "10 minutes",
        "range": "30 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Summon a spirit that assumes the form of a loyal steed."
    },
    "Find Traps": {
        "school": "Divination",
        "classes": ["Cleric", "Druid", "Ranger"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Sense the presence of any trap within range that is within line of sight."
    },
    "Flame Blade": {
        "school": "Evocation",
        "classes": ["Druid"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Create a fiery blade in your hand."
    },
    "Flaming Sphere": {
        "school": "Conjuration",
        "classes": ["Druid", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Create a 5-foot-diameter sphere of fire."
    },
    "Gentle Repose": {
        "school": "Necromancy",
        "classes": ["Cleric", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "10 days",
        "description": "Protect a corpse from decay and necromancy."
    },
    "Gust of Wind": {
        "school": "Evocation",
        "classes": ["Druid", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Self (60-foot line)",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "A line of strong wind blasts from you in a direction you choose."
    },
    "Heat Metal": {
        "school": "Transmutation",
        "classes": ["Bard", "Druid"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Cause a manufactured metal object to glow red-hot and deal damage."
    },
    "Hold Person": {
        "school": "Enchantment",
        "classes": ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Paralyze a humanoid target."
    },
    "Invisibility": {
        "school": "Illusion",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 hour",
        "description": "A creature you touch becomes invisible until the spell ends."
    },
    "Kinetic Jaunt": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Move with supernatural agility, allowing you to move through other creatures' spaces."
    },
    "Knock": {
        "school": "Transmutation",
        "classes": ["Bard", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V"],
        "duration": "Instantaneous",
        "description": "Choose an object that is a door, box, chest, set of manacles, padlock, or other object that contains a mundane or magical means that prevents access. A loud knock, audible from as far away as 300 feet, emanates from the target object."
    },
    "Lesser Restoration": {
        "school": "Abjuration",
        "classes": ["Bard", "Cleric", "Druid", "Paladin", "Ranger"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "End one disease or condition afflicting a creature."
    },
    "Levitate": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "One creature or object rises vertically, up to 20 feet."
    },
    "Locate Animals or Plants": {
        "school": "Divination",
        "classes": ["Bard", "Druid", "Ranger"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Describe or name a specific kind of beast or plant; sense its direction and distance."
    },
    "Locate Object": {
        "school": "Divination",
        "classes": ["Bard", "Cleric", "Druid", "Paladin", "Ranger", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Describe or name an object; sense its direction if within 1,000 feet."
    },
    "Magic Mouth": {
        "school": "Illusion",
        "classes": ["Bard", "Wizard"],
        "casting_time": "1 minute",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "Until dispelled",
        "description": "Imbue an object with a message that is spoken when a trigger condition is met."
    },
    "Magic Weapon": {
        "school": "Transmutation",
        "classes": ["Paladin", "Wizard"],
        "casting_time": "Bonus Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 hour",
        "description": "A nonmagical weapon becomes a magic weapon."
    },
    "Maximilian's Earthen Grasp": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "A Medium hand made from compacted soil rises and grabs a creature."
    },
    "Melf's Acid Arrow": {
        "school": "Evocation",
        "classes": ["Wizard"],
        "casting_time": "Action",
        "range": "90 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "A shimmering green arrow streaks toward a target, dealing acid damage on a hit and additional acid damage at the end of its next turn."
    },
    "Mind Spike": {
        "school": "Divination",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["S"],
        "duration": "Concentration, up to 1 hour",
        "description": "You drive a spike of psychic energy into the mind of one creature you can see within range."
    },
    "Mirror Image": {
        "school": "Illusion",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "1 minute",
        "description": "Create three illusory duplicates of yourself."
    },
    "Misty Step": {
        "school": "Conjuration",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V"],
        "duration": "Instantaneous",
        "description": "Briefly surrounded by silvery mist, you teleport up to 30 feet to an unoccupied space that you can see."
    },
    "Moonbeam": {
        "school": "Evocation",
        "classes": ["Druid"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "A silvery beam of pale light shines down in a 5-foot radius, 40-foot high cylinder centered on a point within range."
    },
    "Nystul's Magic Aura": {
        "school": "Illusion",
        "classes": ["Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "24 hours",
        "description": "Change the way a creature or object is perceived by divination spells."
    },
    "Pass without Trace": {
        "school": "Abjuration",
        "classes": ["Druid", "Ranger"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 hour",
        "description": "A veil of shadows and silence radiates from you, masking you and your companions from detection."
    },
    "Phantasmal Force": {
        "school": "Illusion",
        "classes": ["Bard", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Craft an illusion that takes root in the mind of a creature."
    },
    "Prayer of Healing": {
        "school": "Evocation",
        "classes": ["Bard", "Cleric"],
        "casting_time": "10 minutes",
        "range": "30 feet",
        "components": ["V"],
        "duration": "Instantaneous",
        "description": "Up to six creatures of your choice regain hit points."
    },
    "Protection from Poison": {
        "school": "Abjuration",
        "classes": ["Cleric", "Druid", "Paladin", "Ranger"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "1 hour",
        "description": "Neutralize one poison affecting a creature, or grant advantage on saving throws against poison."
    },
    "Ray of Enfeeblement": {
        "school": "Necromancy",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "A black beam saps the strength of a creature."
    },
    "Rime's Binding Ice": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Self (30-foot cone)",
        "components": ["S", "M"],
        "duration": "Instantaneous",
        "description": "A burst of cold energy in a 30-foot cone; creatures take cold damage and are hindered by ice."
    },
    "Rope Trick": {
        "school": "Transmutation",
        "classes": ["Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "A rope rises into the air, creating an extradimensional space."
    },
    "Scorching Ray": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "Create three rays of fire and hurl them at targets within range."
    },
    "See Invisibility": {
        "school": "Divination",
        "classes": ["Bard", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "You can see invisible creatures and objects."
    },
    "Shadow Blade": {
        "school": "Illusion",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "You weave together threads of shadow to create a sword of solidified gloom."
    },
    "Shatter": {
        "school": "Evocation",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "A sudden loud ringing noise, painfully intense, erupts from a point of your choice."
    },
    "Shining Smite": {
        "school": "Evocation",
        "classes": ["Paladin"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V"],
        "duration": "Concentration, up to 1 minute",
        "description": "The next time you hit a creature with a melee weapon attack, your weapon gleams with radiant energy and deals extra radiant damage."
    },
    "Silence": {
        "school": "Illusion",
        "classes": ["Bard", "Cleric", "Ranger"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S"],
        "duration": "Concentration, up to 10 minutes",
        "description": "No sound can be created within or pass through a 20-foot-radius sphere centered on a point you choose."
    },
    "Skywrite": {
        "school": "Transmutation",
        "classes": ["Bard", "Druid", "Wizard"],
        "casting_time": "Action",
        "range": "Sight",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 hour",
        "description": "You cause up to ten words to form in a part of the sky you can see."
    },
    "Snilloc's Snowball Swarm": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "90 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "A flurry of magic snowballs erupts in a 5-foot-radius sphere."
    },
    "Spider Climb": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 hour",
        "description": "A creature can move up and down and across vertical surfaces and upside down along ceilings."
    },
    "Spike Growth": {
        "school": "Transmutation",
        "classes": ["Druid", "Ranger"],
        "casting_time": "Action",
        "range": "150 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "The ground in a 20-foot radius becomes difficult terrain and deals damage."
    },
    "Spiritual Weapon": {
        "school": "Evocation",
        "classes": ["Cleric"],
        "casting_time": "Bonus Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "1 minute",
        "description": "Create a floating, spectral weapon that attacks creatures."
    },
    "Suggestion": {
        "school": "Enchantment",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "M"],
        "duration": "Concentration, up to 8 hours",
        "description": "Suggest a course of activity to a creature."
    },
    "Summon Beast": {
        "school": "Conjuration",
        "classes": ["Druid", "Ranger"],
        "casting_time": "Action",
        "range": "90 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 hour",
        "description": "Summon a beast spirit that takes physical form and obeys your commands."
    },
    "Vortex Warp": {
        "school": "Conjuration",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "90 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Teleport a creature to another unoccupied space you can see within range."
    },
    "Warding Bond": {
        "school": "Abjuration",
        "classes": ["Cleric", "Paladin"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "Create a magical connection between you and another creature, granting bonuses to AC and saving throws, and resistance to all damage."
    },
    "Web": {
        "school": "Conjuration",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 hour",
        "description": "You conjure a mass of thick, sticky webbing at a point of your choice within range."
    },
    "Wither and Bloom": {
        "school": "Necromancy",
        "classes": ["Druid", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "You invoke both death and life upon a 10-foot radius area."
    },
    "Zone of Truth": {
        "school": "Enchantment",
        "classes": ["Bard", "Cleric", "Paladin"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "10 minutes",
        "description": "Create a magical zone that guards against deception in a 15-foot-radius sphere."
    },
}
