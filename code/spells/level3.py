THIRD_LEVEL_SPELLS_DICT: dict[str, dict] = {
    "Animate Dead": {
        "school": "Necromancy",
        "classes": ["Cleric", "Wizard"],
        "casting_time": "Action",
        "range": "10 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "Create undead servants by reanimating skeletons or corpses."
    },
    "Aura of Vitality": {
        "school": "Evocation",
        "classes": ["Paladin"],
        "casting_time": "Action",
        "range": "Self (30-foot radius)",
        "components": ["V"],
        "duration": "Concentration, up to 1 minute",
        "description": "Healing energy radiates from you in an aura. As a bonus action, you can cause one creature in the aura to regain hit points."
    },
    "Beacon of Hope": {
        "school": "Abjuration",
        "classes": ["Cleric"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Bestow hope and vitality to allies, granting advantage on Wisdom saving throws and death saving throws, and restoring maximum possible hit points from healing."
    },
    "Bestow Curse": {
        "school": "Necromancy",
        "classes": ["Cleric", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Touch a creature to inflict a curse of your choice."
    },
    "Blinding Smite": {
        "school": "Evocation",
        "classes": ["Paladin"],
        "casting_time": "Bonus Action",
        "range": "Self",
        "components": ["V"],
        "duration": "Concentration, up to 1 minute",
        "description": "Your weapon flares with bright light, dealing extra radiant damage and possibly blinding the target."
    },
    "Blink": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "1 minute",
        "description": "Roll at the end of each of your turns; on a 11 or higher, you vanish from the Material Plane to the Ethereal Plane until the start of your next turn."
    },
    "Call Lightning": {
        "school": "Conjuration",
        "classes": ["Druid"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "A storm cloud appears and you call down lightning bolts."
    },
    "Catnap": {
        "school": "Enchantment",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["S", "M"],
        "duration": "10 minutes",
        "description": "Up to three willing creatures fall unconscious for 10 minutes and gain the benefits of a short rest."
    },
    "Clairvoyance": {
        "school": "Divination",
        "classes": ["Bard", "Cleric", "Sorcerer", "Wizard"],
        "casting_time": "10 minutes",
        "range": "1 mile",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Create an invisible sensor to see or hear a location within range."
    },
    "Conjure Animals": {
        "school": "Conjuration",
        "classes": ["Druid", "Ranger"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 hour",
        "description": "Summon fey spirits that take the form of beasts."
    },
    "Conjure Barrage": {
        "school": "Conjuration",
        "classes": ["Ranger"],
        "casting_time": "Action",
        "range": "Self (60-foot cone)",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "Throw a nonmagical weapon or fire a piece of nonmagical ammunition into the air to create a cone of identical weapons that rain down."
    },
    "Counterspell": {
        "school": "Abjuration",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Reaction",
        "range": "60 feet",
        "components": ["S"],
        "duration": "Instantaneous",
        "description": "Interrupt another creature in the process of casting a spell."
    },
    "Create Food and Water": {
        "school": "Conjuration",
        "classes": ["Cleric", "Paladin"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "Create enough food and water to sustain up to fifteen humanoids or five steeds."
    },
    "Crusader's Mantle": {
        "school": "Evocation",
        "classes": ["Paladin"],
        "casting_time": "Action",
        "range": "Self (30-foot radius)",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Holy power radiates from you in an aura, granting extra radiant damage to all allies' weapon attacks."
    },
    "Daylight": {
        "school": "Evocation",
        "classes": ["Cleric", "Druid", "Paladin", "Ranger"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "A 60-foot-radius sphere of light spreads from a point you choose."
    },
    "Dispel Magic": {
        "school": "Abjuration",
        "classes": ["Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "End one spell on a creature, object, or area."
    },
    "Elemental Weapon": {
        "school": "Transmutation",
        "classes": ["Paladin"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 hour",
        "description": "Imbue a weapon with elemental energy."
    },
    "Enemies Abound": {
        "school": "Enchantment",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Confuse a creature so it can't distinguish friend from foe."
    },
    "Erupting Earth": {
        "school": "Transmutation",
        "classes": ["Druid", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "A fountain of churned earth and stone erupts in a 20-foot cube."
    },
    "Fear": {
        "school": "Illusion",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Self (30-foot cone)",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Project an image of fear; creatures drop what they are holding and flee."
    },
    "Feign Death": {
        "school": "Necromancy",
        "classes": ["Bard", "Cleric", "Druid", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "Put a willing creature into a cataleptic state that is indistinguishable from death."
    },
    "Fireball": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "150 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "A bright streak flashes to a point you choose, then blossoms with a low roar into an explosion of flame."
    },
    "Flame Arrows": {
        "school": "Transmutation",
        "classes": ["Druid", "Ranger", "Wizard"],
        "casting_time": "Bonus Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 hour",
        "description": "Up to twelve nonmagical arrows or bolts become magical and deal extra fire damage."
    },
    "Fly": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "A willing creature gains a flying speed of 60 feet."
    },
    "Gaseous Form": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 hour",
        "description": "Transform a willing creature into a misty cloud."
    },
    "Glyph of Warding": {
        "school": "Abjuration",
        "classes": ["Bard", "Cleric", "Wizard"],
        "casting_time": "1 hour",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Until dispelled or triggered",
        "description": "Inscribe a glyph that triggers a magical effect when activated."
    },
    "Haste": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Choose a willing creature; its speed is doubled, it gains a bonus to AC, advantage on Dexterity saving throws, and an additional action each turn."
    },
    "Hunger of Hadar": {
        "school": "Conjuration",
        "classes": ["Warlock"],
        "casting_time": "Action",
        "range": "150 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Open a gateway to the dark between the stars, filling a 20-foot-radius sphere with cold and darkness."
    },
    "Hypnotic Pattern": {
        "school": "Illusion",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "A twisting pattern of colors weaves through the air, charming and incapacitating creatures."
    },
    "Leomund's Tiny Hut": {
        "school": "Evocation",
        "classes": ["Bard", "Wizard"],
        "casting_time": "1 minute",
        "range": "Self (10-foot-radius hemisphere)",
        "components": ["V", "S", "M"],
        "duration": "8 hours",
        "description": "A dome of force springs into existence around and above you."
    },
    "Life Transference": {
        "school": "Necromancy",
        "classes": ["Cleric", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Sacrifice your own vitality to heal another creature."
    },
    "Lightning Bolt": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "100 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "A stroke of lightning forms a line 100 feet long and 5 feet wide, dealing lightning damage."
    },
    "Magic Circle": {
        "school": "Abjuration",
        "classes": ["Cleric", "Paladin", "Warlock", "Wizard"],
        "casting_time": "1 minute",
        "range": "10 feet",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "Create a 10-foot-radius, 20-foot-tall cylinder of magical energy that traps certain types of creatures."
    },
    "Major Image": {
        "school": "Illusion",
        "classes": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Create a realistic illusion of an object, creature, or phenomenon."
    },
    "Mass Healing Word": {
        "school": "Evocation",
        "classes": ["Bard", "Cleric"],
        "casting_time": "Bonus Action",
        "range": "60 feet",
        "components": ["V"],
        "duration": "Instantaneous",
        "description": "Up to six creatures of your choice regain hit points."
    },
    "Meld into Stone": {
        "school": "Transmutation",
        "classes": ["Cleric", "Druid"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "8 hours",
        "description": "Step into a stone object or surface large enough to fully contain your body."
    },
    "Melf's Minute Meteors": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Create six tiny meteors that you can hurl at points you choose."
    },
    "Nondetection": {
        "school": "Abjuration",
        "classes": ["Bard", "Ranger", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "8 hours",
        "description": "Protect a target from divination magic."
    },
    "Phantom Steed": {
        "school": "Illusion",
        "classes": ["Wizard"],
        "casting_time": "1 minute",
        "range": "30 feet",
        "components": ["V", "S"],
        "duration": "1 hour",
        "description": "Create a Large, quasi-real, horselike mount."
    },
    "Plant Growth": {
        "school": "Transmutation",
        "classes": ["Bard", "Druid", "Ranger"],
        "casting_time": "Action",
        "range": "150 feet",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "Channel vitality into plants within a 100-foot radius."
    },
    "Protection from Energy": {
        "school": "Abjuration",
        "classes": ["Cleric", "Druid", "Ranger", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 hour",
        "description": "Grant resistance to one damage type."
    },
    "Remove Curse": {
        "school": "Abjuration",
        "classes": ["Cleric", "Paladin", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "Instantaneous",
        "description": "End all curses affecting one creature or object."
    },
    "Revivify": {
        "school": "Conjuration",
        "classes": ["Cleric", "Paladin"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "Return a creature that has died within the last minute to life."
    },
    "Sending": {
        "school": "Evocation",
        "classes": ["Bard", "Cleric", "Wizard"],
        "casting_time": "Action",
        "range": "Unlimited",
        "components": ["V", "S", "M"],
        "duration": "1 round",
        "description": "Send a short message of twenty-five words or less to a creature with which you are familiar."
    },
    "Sleet Storm": {
        "school": "Conjuration",
        "classes": ["Druid", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "150 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "A 20-foot-tall cylinder of sleet appears, making the area difficult terrain and possibly knocking creatures prone."
    },
    "Slow": {
        "school": "Transmutation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Alter time for up to six creatures, halving their speed and imposing penalties."
    },
    "Speak with Dead": {
        "school": "Necromancy",
        "classes": ["Bard", "Cleric"],
        "casting_time": "Action",
        "range": "10 feet",
        "components": ["V", "S", "M"],
        "duration": "10 minutes",
        "description": "Grant limited sentience and animation to a corpse, allowing it to answer questions."
    },
    "Speak with Plants": {
        "school": "Transmutation",
        "classes": ["Bard", "Druid", "Ranger"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S"],
        "duration": "10 minutes",
        "description": "Grant sentience and mobility to plants, allowing you to question them about events in the area."
    },
    "Spirit Guardians": {
        "school": "Conjuration",
        "classes": ["Cleric"],
        "casting_time": "Action",
        "range": "Self (15-foot radius)",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Call forth spirits to protect you, dealing radiant or necrotic damage to enemies."
    },
    "Stinking Cloud": {
        "school": "Conjuration",
        "classes": ["Bard", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "90 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "Create a 20-foot-radius sphere of yellow, nauseating gas."
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
    "Summon Fey": {
        "school": "Conjuration",
        "classes": ["Druid", "Ranger", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "90 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 hour",
        "description": "Summon a fey creature of challenge rating 3 or lower that obeys your commands."
    },
    "Summon Undead": {
        "school": "Necromancy",
        "classes": ["Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "90 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 hour",
        "description": "Summon an undead spirit in corporeal form that obeys your commands."
    },
    "Thunder Step": {
        "school": "Conjuration",
        "classes": ["Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "90 feet",
        "components": ["V"],
        "duration": "Instantaneous",
        "description": "Teleport yourself to an unoccupied space you can see, and each creature within 10 feet of the space you left takes thunder damage."
    },
    "Tidal Wave": {
        "school": "Conjuration",
        "classes": ["Druid", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S", "M"],
        "duration": "Instantaneous",
        "description": "You conjure up a wave of water that crashes down on an area within range."
    },
    "Tiny Servant": {
        "school": "Transmutation",
        "classes": ["Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "8 hours",
        "description": "Touch a Tiny, nonmagical object to animate it as a creature."
    },
    "Tongues": {
        "school": "Divination",
        "classes": ["Bard", "Cleric", "Sorcerer", "Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Touch",
        "components": ["V", "S"],
        "duration": "1 hour",
        "description": "The target can understand any spoken language it hears."
    },
    "Vampiric Touch": {
        "school": "Necromancy",
        "classes": ["Warlock", "Wizard"],
        "casting_time": "Action",
        "range": "Self",
        "components": ["V", "S"],
        "duration": "Concentration, up to 1 minute",
        "description": "Your hand becomes a conduit for necrotic energy, draining life from others."
    },
    "Wall of Sand": {
        "school": "Evocation",
        "classes": ["Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "90 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Create a wall of swirling sand up to 30 feet long, 10 feet high, and 10 feet thick."
    },
    "Wall of Water": {
        "school": "Evocation",
        "classes": ["Druid", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "60 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 10 minutes",
        "description": "Create a wall of water up to 30 feet long, 10 feet high, and 1 foot thick."
    },
    "Water Breathing": {
        "school": "Transmutation",
        "classes": ["Druid", "Ranger", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "24 hours",
        "description": "Up to ten willing creatures can breathe underwater."
    },
    "Water Walk": {
        "school": "Transmutation",
        "classes": ["Cleric", "Druid", "Ranger", "Sorcerer"],
        "casting_time": "Action",
        "range": "30 feet",
        "components": ["V", "S", "M"],
        "duration": "1 hour",
        "description": "Up to ten willing creatures can move across any liquid surface as if it were harmless solid ground."
    },
    "Wind Wall": {
        "school": "Evocation",
        "classes": ["Druid", "Ranger", "Sorcerer", "Wizard"],
        "casting_time": "Action",
        "range": "120 feet",
        "components": ["V", "S", "M"],
        "duration": "Concentration, up to 1 minute",
        "description": "A wall of strong wind rises from the ground at a point you choose."
    },
}
