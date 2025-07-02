FIRST_LEVEL_SPELLS_DICT: dict[str, dict] = {
    "Absorb Elements": {
        "school": "Abjuration",
        "classes": ["Druid", "Ranger", "Sorcerer", "Wizard"],
        "casting_time": "Reaction",
        "range": "Self",
        "components": ["S"],
        "duration": "1 round",
        "description": "Capture incoming energy to gain resistance and add it to your next melee attack."
    },
    "Alarm": {
        "school": "Abjuration",
        "classes": ["Ranger", "Wizard"],
        "casting_time": "1 minute",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "8 hours",
        "description": "Set a magical alarm against unwanted intrusion."
    },
    "Animal Friendship": {
        "school": "Enchantment",
        "classes": ["Bard", "Druid", "Ranger"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "24 hours",
        "description": "Convince a beast you mean it no harm."
    },
    "Armor of Agathys": {
        "school": "Abjuration",
        "classes": ["Warlock"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "Gain temporary hit points and deal cold damage to attackers."
    },
    "Arms of Hadar": {
        "school": "Conjuration",
        "classes": ["Warlock"],
        "casting_time": "Action",
        "range": "Self (10-foot radius)",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Tendrils of dark energy erupt from you and batter all creatures within 10 feet."
    },
    "Bane": {
        "school": "Enchantment",
        "classes": ["Bard", "Cleric"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Up to three creatures must subtract 1d4 from attack rolls and saving throws."
    },
    "Bless": {
        "school": "Enchantment",
        "classes": ["Cleric", "Paladin"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Up to three creatures add 1d4 to attack rolls and saving throws."
    },
    "Burning Hands": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Self (15-foot cone)",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "A cone of fire erupts from your hands."
    },
    "Charm Person": {
        "school": "Enchantment",
        "classes": ["Bard", "Druid", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S"],
        "duration": "1 hour",
        "description": "Charm a humanoid you can see."
    },
    "Chromatic Orb": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "90 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "Hurl an orb of energy of a chosen type."
    },
    "Color Spray": {
        "school": "Illusion",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Self (15-foot cone)",
        "components": ["V", "S", "M"],
        "duration": "1 round",
        "description": "Dazzle creatures with a rainbow of light."
    },
    "Command": {
        "school": "Enchantment",
        "classes": ["Cleric", "Paladin"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V"],
        "duration": "1 round",
        "description": "Speak a one-word command to a creature."
    },
    "Compelled Duel": {
        "school": "Enchantment",
        "classes": ["Paladin"],
        "casting_time": "Bonus Action",
        "range": "30 feet",
        "components": ["V"],
        "duration": "Concentration, up to 1 minute",
        "description": "Compel a creature to duel you."
    },
    "Comprehend Languages": {
        "school": "Divination",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "1 action",
        "range": "Self",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "Understand the literal meaning of any spoken language."
    },
    "Create or Destroy Water": {
        "school": "Transmutation",
        "classes": ["Cleric", "Druid"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "Create or destroy water in an area."
    },
    "Cure Wounds": {
        "school": "Evocation",
        "classes": ["Bard", "Cleric", "Druid", "Paladin", "Ranger"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Heal a creature you touch."
    },
    "Detect Evil and Good": {
        "school": "Divination",
        "classes": ["Cleric", "Paladin"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Sense aberrations, celestials, elementals, fey, fiends, and undead within 30 feet."
    },
    "Detect Magic": {
        "school": "Divination",
        "classes": ["Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Sense the presence of magic within 30 feet of you."
    },
    "Detect Poison and Disease": {
        "school": "Divination",
        "classes": ["Cleric", "Druid", "Paladin", "Ranger"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "You can sense the presence and location of poisons, poisonous creatures, and diseases within 30 feet of you."
    },
    "Disguise Self": {
        "school": "Illusion",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "1 hour",
        "description": "Change your appearance for the duration."
    },
    "Dissonant Whispers": {
        "school": "Enchantment",
        "classes": ["Bard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V"],
        "duration": "Instantaneous",
        "description": "You whisper a discordant melody that only one creature of your choice within range can hear, wracking it with terrible pain. The target must make a Wisdom saving throw. On a failed save, it takes psychic damage and must immediately use its reaction, if available, to move as far as its speed allows away from you. On a successful save, the target takes half as much damage and doesn't have to move."
    },
    "Divine Favor": {
        "school": "Evocation",
        "classes": ["Paladin"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Your weapon attacks deal extra radiant damage."
    },
    "Divine Smite": {
        "school": "Evocation",
        "classes": ["Paladin"],
        "casting_time": "Special",
        "range": "Self",
        "components": ["V"],
        "duration": "Instantaneous",
        "description": "When you hit a creature with a melee weapon attack, you can expend one spell slot to deal radiant damage to the target, in addition to the weapon's damage. The extra damage increases if the target is an undead or a fiend."
    },
    "Entangle": {
        "school": "Conjuration",
        "classes": ["Druid"],
        "casting_time": "Action",
        "range": "90 feet",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Grasping weeds and vines sprout in a 20-foot square."
    },
    "Expeditious Retreat": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "Concentration, up to 10 minutes",
        "description": "This spell allows you to move at an incredible pace. When you cast this spell, and then as a bonus action on each of your turns until the spell ends, you can take the Dash action."
    },
    "Faerie Fire": {
        "school": "Evocation",
        "classes": ["Bard", "Druid"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V"],
        "duration": "Concentration, up to 1 minute",
        "description": "Each object in a 20-foot cube is outlined in light."
    },
    "False Life": {
        "school": "Necromancy",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "Bolster yourself with a necromantic facsimile of life, gaining temporary hit points."
    },
    "Feather Fall": {
        "school": "Transmutation",
        "classes": ["Bard", "Sorcerer", "Wizard"],
        "casting_time": "Reaction",
        "range": "60 feet",
        "components": ["V", "M"],
        "duration": "1 minute",
        "description": "Choose up to five falling creatures to slow their descent."
    },
    "Find Familiar": {
        "school": "Conjuration",
        "classes": ["Wizard"],
        "casting_time": "1 hour",
        "range": "10 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "Gain the service of a spirit animal companion."
    },
    "Fog Cloud": {
        "school": "Conjuration",
        "classes": ["Druid", "Ranger", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 hour",
        "description": "Create a 20-foot-radius sphere of fog."
    },
    "Goodberry": {
        "school": "Transmutation",
        "classes": ["Druid", "Ranger"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "Up to ten magical berries appear in your hand."
    },
    "Grease": {
        "school": "Conjuration",
        "classes": ["Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "1 minute",
        "description": "Slick grease covers the ground in a 10-foot square, turning it into difficult terrain and possibly causing creatures to fall prone."
    },
    "Guiding Bolt": {
        "school": "Evocation",
        "classes": ["Cleric"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "A flash of light streaks toward a creature."
    },
    "Hail of Thorns": {
        "school": "Conjuration",
        "classes": ["Ranger"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V"],
        "duration": "Concentration, up to 1 minute",
        "description": "The next time you hit a creature with a ranged weapon attack before this spell ends, this spell creates a rain of thorns that sprouts from your ranged weapon or ammunition."
    },
    "Healing Word": {
        "school": "Evocation",
        "classes": ["Bard", "Cleric", "Druid"],
        "casting_time": "Bonus Action",
        "range": "60 feet",
        "components": ["V"],
        "duration": "Instantaneous",
        "description": "A creature of your choice regains hit points."
    },
    "Hellish Rebuke": {
        "school": "Evocation",
        "classes": ["Warlock"],
        "casting_time": "Reaction",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Point your finger and the creature that damaged you is momentarily surrounded by hellish flames."
    },
    "Heroism": {
        "school": "Enchantment",
        "classes": ["Bard", "Cleric", "Paladin"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "A willing creature is imbued with bravery."
    },
    "Hex": {
        "school": "Enchantment",
        "classes": ["Warlock"],
        "casting_time": "Bonus Action",
        "range": "90 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 hour",
        "description": "You place a curse on a creature that you can see within range. Until the spell ends, you deal extra necrotic damage to the target whenever you hit it with an attack."
    },
    "Hunter's Mark": {
        "school": "Divination",
        "classes": ["Ranger"],
        "casting_time": "Bonus Action",
        "range": "90 feet",
        "components": ["V"],
        "duration": "Concentration, up to 1 hour",
        "description": "Mark a creature as your quarry."
    },
    "Ice Knife": {
        "school": "Conjuration",
        "classes": ["Druid", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["S", "M"],
        "duration": "Instantaneous",
        "description": "You create a shard of ice and fling it at one creature within range. Make a ranged spell attack. On a hit, the target takes piercing damage. Hit or miss, the shard then explodes. The target and each creature within 5 feet must succeed on a Dexterity saving throw or take cold damage."
    },
    "Identify": {
        "school": "Divination",
        "classes": ["Bard", "Wizard"],
        "casting_time": "1 minute",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "Learn the properties of a magic item or spell."
    },
    "Illusory Script": {
        "school": "Illusion",
        "classes": ["Bard", "Warlock", "Wizard"],
        "casting_time": "1 minute",
        "range": "Touch",
        "components": ["S", "M"],
        "duration": "10 days",
        "description": "Write a hidden message only certain creatures can read."
    },
    "Inflict Wounds": {
        "school": "Necromancy",
        "classes": ["Cleric"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Make a melee spell attack to deal necrotic damage."
    },
    "Jump": {
        "school": "Transmutation",
        "classes": ["Druid", "Ranger", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "1 minute",
        "description": "Triple a creature's jump distance."
    },
    "Longstrider": {
        "school": "Transmutation",
        "classes": ["Bard", "Druid", "Ranger", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "Increase a creature's speed by 10 feet."
    },
    "Mage Armor": {
        "school": "Abjuration",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "8 hours",
        "description": "Protect a creature with a magical force."
    },
    "Magic Missile": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Create three glowing darts of magical force."
    },
    "Protection from Evil and Good": {
        "school": "Abjuration",
        "classes": ["Cleric", "Paladin", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Protect a creature from aberrations, celestials, elementals, fey, fiends, and undead."
    },
    "Purify Food and Drink": {
        "school": "Transmutation",
        "classes": ["Cleric", "Druid", "Paladin"],
        "casting_time": "Action",
        "range": "10 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "All nonmagical food and drink in a 5-foot-radius sphere is purified."
    },
    "Ray of Sickness": {
        "school": "Necromancy",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "A ray of sickening greenish energy lashes out toward a creature within range. Make a ranged spell attack. On a hit, the target takes poison damage and must make a Constitution saving throw or be poisoned until the end of your next turn."
    },
    "Sanctuary": {
        "school": "Abjuration",
        "classes": ["Cleric"],
        "casting_time": "Bonus Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "1 minute",
        "description": "You ward a creature within range against attack. Until the spell ends, any creature who targets the warded creature with an attack or a harmful spell must first make a Wisdom saving throw. On a failed save, the creature must choose a new target or lose the attack or spell."
    },
    "Searing Smite": {
        "school": "Evocation",
        "classes": ["Paladin"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V"],
        "duration": "Concentration, up to 1 minute",
        "description": "The next time you hit a creature with a melee weapon attack during this spell's duration, your weapon flares with white-hot intensity and deals extra fire damage."
    },
    "Shield": {
        "school": "Abjuration",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Reaction",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "1 round",
        "description": "An invisible barrier of magical force appears and protects you."
    },
    "Shield of Faith": {
        "school": "Abjuration",
        "classes": ["Cleric", "Paladin"],
        "casting_time": "Bonus Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "Concentration, up to 10 minutes",
        "description": "A shimmering field appears and gives a creature +2 AC."
    },
    "Silent Image": {
        "school": "Illusion",
        "classes": ["Bard", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Create the image of an object, a creature, or some other visible phenomenon."
    },
    "Sleep": {
        "school": "Enchantment",
        "classes": ["Bard", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "90 feet",
        "components": ["V", "S", "M"],
        "duration": "1 minute",
        "description": "Send creatures into a magical slumber."
    },
    "Speak with Animals": {
        "school": "Divination",
        "classes": ["Bard", "Druid", "Ranger"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "10 minutes",
        "description": "You gain the ability to comprehend and verbally communicate with beasts."
    },
    "Tasha's Hideous Laughter": {
        "school": "Enchantment",
        "classes": ["Bard", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "A creature of your choice perceives everything as hilariously funny and falls prone."
    },
    "Tenser's Floating Disk": {
        "school": "Conjuration",
        "classes": ["Wizard"],
        "casting_time": "1 action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "Create a floating, 3-foot-diameter disk of force."
    },
    "Thunderous Smite": {
        "school": "Evocation",
        "classes": ["Paladin"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V"],
        "duration": "Concentration, up to 1 minute",
        "description": "The next time you hit with a melee weapon attack during this spell's duration, your weapon rings with thunder that is audible within 300 feet of you, and the attack deals extra thunder damage."
    },
    "Thunderwave": {
        "school": "Evocation",
        "classes": ["Bard", "Druid", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Self (15-foot cube)",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "A wave of thunderous force sweeps out from you."
    },
    "Unseen Servant": {
        "school": "Conjuration",
        "classes": ["Bard", "Warlock", "Wizard"],
        "casting_time": "1 action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "Create an invisible, mindless, shapeless force."
    },
    "Witch Bolt": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "A beam of crackling, blue energy lances out toward a creature."
    },
    "Wrathful Smite": {
        "school": "Evocation",
        "classes": ["Paladin"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V"],
        "duration": "Concentration, up to 1 minute",
        "description": "The next time you hit with a melee weapon attack, the attack deals extra psychic damage."
    },
}
