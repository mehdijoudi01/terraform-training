import json
import random

# Data for quest generation
quest_types = ["rescue", "retrieval", "escort", "investigation", "defense", "conquest", "exploration", "diplomatic", "assassination", "sabotage"]

locations = ["ancient ruins", "dark forest", "mountain peak", "desert wasteland", "frozen tundra", "haunted castle", "underground cavern", "floating islands", "volcanic region", "mystical temple", "abandoned city", "enchanted grove", "dragon's lair", "pirate cove", "royal palace", "merchant district", "slums", "wizard's tower", "necropolis", "battlefield"]

characters = ["mysterious stranger", "village elder", "royal guard", "merchant", "blacksmith", "wizard", "priest", "beggar", "noble", "thief", "warrior", "ranger", "scholar", "alchemist", "bard", "farmer", "innkeeper", "captain", "assassin", "hermit"]

items = ["ancient artifact", "magic sword", "healing potion", "sacred relic", "treasure map", "enchanted ring", "spell scroll", "dragon scale", "royal crown", "mysterious key", "cursed amulet", "legendary armor", "magic wand", "rare herb", "stolen jewel"]

enemies = ["bandits", "goblins", "undead", "cultists", "wild beasts", "mercenaries", "demons", "orcs", "trolls", "giants", "dragons", "assassins", "dark knights", "corrupted guards", "monsters"]

rewards = ["gold", "magical weapon", "rare armor", "ancient knowledge", "political favor", "land deed", "title of nobility", "magical ability", "legendary mount", "priceless artifact"]

def generate_choice_outcome(choice_text, stat_changes, consequence):
    return {
        "text": choice_text,
        "health": stat_changes.get("health", 0),
        "glory": stat_changes.get("glory", 0),
        "gold": stat_changes.get("gold", 0),
        "consequence": consequence
    }

def generate_chapter_choices():
    # Generate 2-4 choices per chapter
    num_choices = random.randint(2, 4)
    choices = []
    
    choice_templates = [
        ("Attack head-on", {"health": -10, "glory": 15}, "You charge into battle with courage"),
        ("Negotiate peacefully", {"glory": 10, "gold": 20}, "Your words find common ground"),
        ("Sneak around", {"health": 5, "gold": 15}, "You move silently through the shadows"),
        ("Use magic", {"health": -5, "glory": 20}, "Arcane power flows through you"),
        ("Retreat and regroup", {"health": 10, "glory": -5}, "You live to fight another day"),
        ("Call for reinforcements", {"gold": -20, "glory": 10}, "Allies answer your call"),
        ("Set a trap", {"glory": 15, "gold": 10}, "Your cunning pays off"),
        ("Investigate further", {"glory": 5}, "You uncover hidden information"),
        ("Bribe your way through", {"gold": -30, "glory": -5}, "Gold opens many doors"),
        ("Help the locals", {"glory": 20, "gold": -10}, "Your kindness is remembered"),
        ("Accept the challenge", {"health": -15, "glory": 25}, "You prove your worth"),
        ("Seek ancient knowledge", {"glory": 15}, "Wisdom guides your path"),
        ("Form an alliance", {"gold": 10, "glory": 10}, "United you stand stronger"),
        ("Take the risky path", {"health": -20, "glory": 30}, "Fortune favors the bold"),
        ("Play it safe", {"health": 5, "glory": 5}, "Caution serves you well")
    ]
    
    selected_choices = random.sample(choice_templates, num_choices)
    for choice_text, stats, consequence in selected_choices:
        choices.append(generate_choice_outcome(choice_text, stats, consequence))
    
    return choices

def generate_quest(index):
    quest_type = random.choice(quest_types)
    location = random.choice(locations)
    character = random.choice(characters)
    item = random.choice(items)
    enemy = random.choice(enemies)
    reward = random.choice(rewards)
    
    # Generate quest title and description
    title_templates = [
        f"The {quest_type.title()} of {location.title()}",
        f"{character.title()}'s {quest_type.title()}",
        f"Quest for the {item.title()}",
        f"Battle against the {enemy.title()}",
        f"The {location.title()} Mystery"
    ]
    
    title = random.choice(title_templates)
    
    description = f"A {character} approaches you with an urgent request. {random.choice([
        f'They need you to venture into the {location} and complete a dangerous {quest_type} mission.',
        f'The {item} has been lost in the {location} and must be recovered.',
        f'{enemy.title()} have been terrorizing the area near {location}.',
        f'An ancient prophecy speaks of a hero who will {quest_type} at the {location}.'
    ])}"
    
    # Generate 3-5 chapters
    num_chapters = random.randint(3, 5)
    chapters = []
    
    chapter_templates = [
        f"You arrive at the {location} and must decide your approach.",
        f"Deep within the {location}, you encounter {enemy}.",
        f"A {character} blocks your path, demanding payment.",
        f"You discover the {item} but it's guarded.",
        f"The final challenge awaits at the heart of the {location}.",
        f"An unexpected ally offers assistance.",
        f"A terrible storm forces you to seek shelter.",
        f"You find clues about the {item}'s true purpose.",
        f"The {enemy} leader challenges you to single combat.",
        f"A moral dilemma tests your character."
    ]
    
    selected_chapters = random.sample(chapter_templates, num_chapters)
    for i, chapter_text in enumerate(selected_chapters, 1):
        chapters.append({
            "chapter": i,
            "text": chapter_text,
            "choices": generate_chapter_choices()
        })
    
    quest = {
        "id": index,
        "title": title,
        "description": description,
        "difficulty": random.choice(["Easy", "Medium", "Hard", "Epic"]),
        "estimatedTime": f"{random.randint(10, 45)} minutes",
        "reward": reward,
        "chapters": chapters
    }
    
    return quest

# Generate 1200 quests
print("Generating quests...")
quests = [generate_quest(i) for i in range(1, 1201)]

data = {
    "version": "1.0",
    "total_quests": len(quests),
    "quests": quests
}

with open('/workspaces/terraform-training/quest-data.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Generated {len(quests)} quests!")
