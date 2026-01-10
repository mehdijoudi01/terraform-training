import json
import random

# Templates pour générer des cas variés
locations = ["mansion", "office", "warehouse", "museum", "laboratory", "restaurant", "hotel", "theater", "library", "casino", "yacht", "park", "subway", "airport", "hospital", "school", "factory", "bank", "church", "cemetery"]

crimes = ["murder", "theft", "kidnapping", "fraud", "blackmail", "arson", "smuggling", "sabotage", "espionage", "forgery"]

victim_titles = ["CEO", "Detective", "Professor", "Artist", "Scientist", "Chef", "Actor", "Journalist", "Politician", "Millionaire", "Doctor", "Lawyer", "Banker", "Author", "Director", "Engineer", "Diplomat", "Curator", "Philanthropist", "Inventor"]

first_names = ["James", "Emma", "Oliver", "Sophia", "William", "Isabella", "Henry", "Charlotte", "Alexander", "Amelia", "Benjamin", "Mia", "Sebastian", "Harper", "Theodore", "Evelyn", "Nicholas", "Abigail", "Daniel", "Emily", "Matthew", "Elizabeth", "Christopher", "Sofia", "Andrew", "Avery", "Joshua", "Ella", "David", "Scarlett", "Joseph", "Grace", "Samuel", "Chloe", "Michael", "Victoria", "Jack", "Riley", "Lucas", "Aria", "Gabriel", "Lily", "Nathan", "Zoey", "Isaac", "Penelope", "Caleb", "Layla", "Ryan", "Nora"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Thompson", "White", "Harris", "Clark", "Lewis", "Walker", "Hall", "Allen", "Young", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner"]

professions = ["butler", "secretary", "business partner", "rival", "ex-spouse", "colleague", "assistant", "competitor", "neighbor", "family member", "investor", "employee", "contractor", "accountant", "bodyguard", "driver", "maid", "chef", "doctor", "lawyer"]

clue_templates = [
    "A {item} found at the scene",
    "Fingerprints on a {object}",
    "A torn {document}",
    "Security footage showing {event}",
    "A witness saw {observation}",
    "Blood stains on {location_item}",
    "A suspicious {communication}",
    "Missing {valuable}",
    "A {weapon} hidden nearby",
    "Strange marks on {surface}",
    "{substance} traces detected",
    "A cryptic {message_type}",
    "Footprints leading to {direction}",
    "A broken {item}",
    "Unusual {smell} in the room"
]

items = ["letter", "key", "photograph", "receipt", "ticket", "business card", "note", "diary", "phone", "wallet", "watch", "ring", "necklace", "glasses", "glove"]

objects = ["door handle", "window", "glass", "weapon", "safe", "desk", "phone", "computer", "steering wheel", "bottle"]

documents = ["contract", "will", "letter", "invoice", "memo", "report", "manuscript", "blueprint", "map", "certificate"]

events = ["someone leaving", "an argument", "a struggle", "a delivery", "an exchange", "suspicious activity", "a chase", "someone entering", "a confrontation", "a meeting"]

observations = ["someone running away", "a figure in dark clothes", "two people arguing", "someone carrying something heavy", "a car speeding off", "someone acting nervously", "unusual behavior", "someone with a weapon", "a person sneaking around", "suspicious movements"]

motives = ["financial gain", "revenge", "jealousy", "covering up a crime", "protecting a secret", "inheritance", "business rivalry", "personal vendetta", "blackmail", "desperation", "greed", "hatred", "fear of exposure", "eliminating competition", "passion"]

def generate_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_clue():
    template = random.choice(clue_templates)
    return template.format(
        item=random.choice(items),
        object=random.choice(objects),
        document=random.choice(documents),
        event=random.choice(events),
        observation=random.choice(observations),
        location_item=random.choice(["the floor", "the wall", "furniture", "clothing", "the carpet"]),
        communication=random.choice(["email", "text message", "letter", "phone call record", "voicemail"]),
        valuable=random.choice(["jewelry", "documents", "money", "artifact", "painting"]),
        weapon=random.choice(["knife", "gun", "poison", "blunt object", "rope"]),
        surface=random.choice(["the door", "the window", "the wall", "the floor", "the furniture"]),
        substance=random.choice(["poison", "gunpowder", "chemical", "drug", "blood"]),
        message_type=random.choice(["message", "note", "symbol", "code", "threat"]),
        direction=random.choice(["the back door", "the window", "the exit", "the basement", "the roof"]),
        smell=random.choice(["chemical", "perfume", "smoke", "gasoline", "cleaning product"])
    )

def generate_case(index):
    location = random.choice(locations)
    crime = random.choice(crimes)
    victim_name = generate_name()
    victim_title = random.choice(victim_titles)
    
    # Generate suspects
    num_suspects = random.randint(3, 5)
    suspects = []
    culprit_index = random.randint(0, num_suspects - 1)
    
    for i in range(num_suspects):
        suspect_name = generate_name()
        profession = random.choice(professions)
        motive = random.choice(motives)
        is_guilty = (i == culprit_index)
        
        suspects.append({
            "name": suspect_name,
            "description": f"{victim_name}'s {profession}",
            "motive": motive,
            "guilty": is_guilty
        })
    
    # Generate clues (12-15 per case)
    num_clues = random.randint(12, 15)
    clues = [generate_clue() for _ in range(num_clues)]
    
    case = {
        "id": index,
        "title": f"The {location.title()} {crime.title()}",
        "victim": f"{victim_name}, {victim_title}",
        "location": location,
        "description": f"A {crime} has occurred at a prestigious {location}. {victim_name}, a renowned {victim_title}, is at the center of this mystery.",
        "clues": clues,
        "suspects": suspects
    }
    
    return case

# Generate 1200 cases
cases = [generate_case(i) for i in range(1, 1201)]

data = {
    "version": "1.0",
    "total_cases": len(cases),
    "cases": cases
}

with open('/workspaces/terraform-training/mystery-data.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Generated {len(cases)} mystery cases!")
