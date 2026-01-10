import json
import random

# Comprehensive character generation data
races = [
    {"name": "Human", "traits": ["Versatile", "Ambitious", "Adaptable"]},
    {"name": "Elf", "traits": ["Graceful", "Long-lived", "Magical"]},
    {"name": "Dwarf", "traits": ["Sturdy", "Crafty", "Resilient"]},
    {"name": "Halfling", "traits": ["Lucky", "Cheerful", "Nimble"]},
    {"name": "Orc", "traits": ["Strong", "Fierce", "Honorable"]},
    {"name": "Tiefling", "traits": ["Charismatic", "Mysterious", "Cunning"]},
    {"name": "Dragonborn", "traits": ["Proud", "Powerful", "Draconic"]},
    {"name": "Gnome", "traits": ["Inventive", "Curious", "Small"]},
    {"name": "Half-Elf", "traits": ["Diplomatic", "Versatile", "Charming"]},
    {"name": "Half-Orc", "traits": ["Tough", "Intimidating", "Enduring"]},
    {"name": "Goliath", "traits": ["Towering", "Competitive", "Mountaineer"]},
    {"name": "Tabaxi", "traits": ["Feline", "Curious", "Agile"]},
    {"name": "Kenku", "traits": ["Mimicking", "Dexterous", "Clever"]},
    {"name": "Lizardfolk", "traits": ["Cold-blooded", "Pragmatic", "Survivalist"]},
    {"name": "Aasimar", "traits": ["Divine", "Radiant", "Righteous"]},
    {"name": "Firbolg", "traits": ["Gentle", "Nature-bound", "Reclusive"]},
    {"name": "Triton", "traits": ["Aquatic", "Noble", "Guardian"]},
    {"name": "Warforged", "traits": ["Constructed", "Dutiful", "Resilient"]},
    {"name": "Changeling", "traits": ["Shapeshifting", "Deceptive", "Fluid"]},
    {"name": "Genasi", "traits": ["Elemental", "Volatile", "Powerful"]}
]

classes = [
    {"name": "Warrior", "skills": ["Combat", "Tactics", "Endurance"]},
    {"name": "Rogue", "skills": ["Stealth", "Lockpicking", "Deception"]},
    {"name": "Wizard", "skills": ["Arcane Magic", "Knowledge", "Spellcasting"]},
    {"name": "Cleric", "skills": ["Divine Magic", "Healing", "Faith"]},
    {"name": "Ranger", "skills": ["Tracking", "Archery", "Survival"]},
    {"name": "Paladin", "skills": ["Holy Magic", "Protection", "Leadership"]},
    {"name": "Bard", "skills": ["Performance", "Inspiration", "Charm"]},
    {"name": "Druid", "skills": ["Nature Magic", "Shapeshifting", "Animal Handling"]},
    {"name": "Monk", "skills": ["Martial Arts", "Meditation", "Discipline"]},
    {"name": "Sorcerer", "skills": ["Innate Magic", "Charisma", "Metamagic"]},
    {"name": "Warlock", "skills": ["Pact Magic", "Eldritch Power", "Invocations"]},
    {"name": "Barbarian", "skills": ["Rage", "Strength", "Intimidation"]},
    {"name": "Artificer", "skills": ["Invention", "Crafting", "Technology"]},
    {"name": "Blood Hunter", "skills": ["Dark Magic", "Monster Hunting", "Sacrifice"]},
    {"name": "Necromancer", "skills": ["Death Magic", "Undead Control", "Forbidden Knowledge"]},
    {"name": "Alchemist", "skills": ["Potion Making", "Chemistry", "Transmutation"]},
    {"name": "Assassin", "skills": ["Silent Killing", "Poison", "Infiltration"]},
    {"name": "Summoner", "skills": ["Creature Summoning", "Bonding", "Planar Magic"]},
    {"name": "Battlemage", "skills": ["Combat Magic", "Weapon Fighting", "Versatility"]},
    {"name": "Psion", "skills": ["Mind Powers", "Telepathy", "Mental Fortitude"]}
]

childhood_events = [
    "Raised by wolves in the wilderness",
    "Orphaned and raised in a monastery",
    "Born into nobility but lost everything",
    "Discovered magical powers at age 5",
    "Survived a dragon attack on their village",
    "Trained by a legendary warrior from birth",
    "Found as a baby on a doorstep",
    "Grew up in the slums, learning to survive",
    "Witnessed parents murdered by assassins",
    "Blessed by a deity at birth",
    "Cursed by a witch as a child",
    "Sold into slavery and escaped",
    "Raised by a traveling circus",
    "Mentored by a master thief",
    "Found an ancient artifact as a child",
    "Survived alone after shipwreck",
    "Trained in a secret martial arts temple",
    "Grew up in an enchanted forest",
    "Born during a celestial alignment",
    "Raised by druids in nature",
    "Escaped from a cult",
    "Protected by a guardian angel",
    "Haunted by prophetic dreams",
    "Trained as a spy from childhood",
    "Discovered as heir to a throne"
]

formative_experiences = [
    "Betrayed by closest friend",
    "Saved a village from bandits",
    "Made a pact with otherworldly entity",
    "Lost loved one to disease",
    "Won a legendary tournament",
    "Discovered family secret",
    "Framed for crime didn't commit",
    "Found true love then lost them",
    "Witnessed supernatural phenomenon",
    "Rescued from certain death",
    "Inherited mysterious power",
    "Defeated powerful nemesis",
    "Failed to save someone important",
    "Uncovered ancient conspiracy",
    "Embarked on spirit quest",
    "Survived deadly plague",
    "Exposed corruption in leadership",
    "Formed unbreakable bond with companion",
    "Touched by divine intervention",
    "Escaped death by pure luck",
    "Learned forbidden knowledge",
    "Broke ancient curse",
    "United warring factions",
    "Discovered hidden heritage",
    "Sacrificed something precious"
]

personality_traits = [
    "Brave and reckless",
    "Cautious and analytical",
    "Charismatic and manipulative",
    "Honest to a fault",
    "Cunning and deceptive",
    "Kind and compassionate",
    "Ambitious and ruthless",
    "Loyal and protective",
    "Curious and adventurous",
    "Wise and patient",
    "Hot-tempered and passionate",
    "Cold and calculating",
    "Optimistic and naive",
    "Cynical and world-weary",
    "Mysterious and secretive",
    "Boisterous and friendly",
    "Quiet and observant",
    "Arrogant and confident",
    "Humble and modest",
    "Rebellious and independent"
]

motivations = [
    "Seeking revenge for past wrong",
    "Searching for lost family member",
    "Pursuing ultimate power",
    "Protecting the innocent",
    "Uncovering hidden truth",
    "Proving their worth",
    "Escaping their past",
    "Finding redemption",
    "Accumulating wealth",
    "Seeking knowledge",
    "Following prophecy",
    "Honoring fallen mentor",
    "Breaking a curse",
    "Fulfilling sacred duty",
    "Chasing adventure",
    "Establishing legacy",
    "Righting ancient wrong",
    "Conquering fear",
    "Uniting their people",
    "Transcending mortality"
]

quirks = [
    "Always carries lucky charm",
    "Speaks to imaginary friend",
    "Collects unusual trophies",
    "Never removes specific item",
    "Has prophetic dreams",
    "Sees ghosts of the dead",
    "Compulsively counts things",
    "Never lies, even when beneficial",
    "Afraid of specific creature",
    "Talks to weapons",
    "Has unique laugh",
    "Collects rare books",
    "Writes everything down",
    "Never breaks promises",
    "Superstitious about omens",
    "Speaks in third person",
    "Hums while fighting",
    "Has distinctive scar with story",
    "Refuses to eat certain food",
    "Always arrives fashionably late"
]

def generate_character(index):
    race = random.choice(races)
    char_class = random.choice(classes)
    childhood = random.choice(childhood_events)
    experience = random.choice(formative_experiences)
    personality = random.choice(personality_traits)
    motivation = random.choice(motivations)
    quirk = random.choice(quirks)
    
    # Generate backstory narrative
    backstory_templates = [
        f"Born a {race['name']}, they were {childhood.lower()}. This shaped them into a {char_class['name']} who is {personality.lower()}. After they {experience.lower()}, they became driven by {motivation.lower()}. They are known for the fact that they {quirk.lower()}.",
        
        f"A {race['name']} {char_class['name']}, their story began when they {childhood.lower()}. The experience left them {personality.lower()} and determined to master the ways of a {char_class['name']}. When they {experience.lower()}, it changed everything. Now they are consumed by {motivation.lower()}, though those who know them also notice they {quirk.lower()}.",
        
        f"This {race['name']} learned the path of the {char_class['name']} after they {childhood.lower()}. Their {personality.lower()} nature was forged through hardship. The turning point came when they {experience.lower()}, setting them on a quest of {motivation.lower()}. Companions quickly learn they {quirk.lower()}.",
        
        f"Few know the true story of this {personality.lower()} {race['name']} {char_class['name']}. They {childhood.lower()}, which set them apart from others of their kind. After they {experience.lower()}, they dedicated themselves to {motivation.lower()}. A peculiar habit: they {quirk.lower()}."
    ]
    
    character = {
        "id": index,
        "race": race["name"],
        "racial_traits": race["traits"],
        "class": char_class["name"],
        "class_skills": char_class["skills"],
        "childhood_event": childhood,
        "formative_experience": experience,
        "personality": personality,
        "motivation": motivation,
        "quirk": quirk,
        "backstory": random.choice(backstory_templates)
    }
    
    return character

# Generate 1500 characters
print("Generating characters...")
characters = [generate_character(i) for i in range(1, 1501)]

data = {
    "version": "1.0",
    "total_characters": len(characters),
    "races": races,
    "classes": classes,
    "characters": characters
}

with open('/workspaces/terraform-training/character-data.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Generated {len(characters)} characters!")
