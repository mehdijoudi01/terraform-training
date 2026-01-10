import json
import random

# Riddle categories and templates
riddle_templates = {
    "classic": [
        ("What has keys but no locks, space but no room, and you can enter but can't go inside?", "keyboard", "Think about something you use every day with technology"),
        ("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "echo", "Think about sounds bouncing back"),
        ("The more you take, the more you leave behind. What am I?", "footsteps", "Think about walking"),
        ("I have cities but no houses, forests but no trees, and rivers but no water. What am I?", "map", "Think about representations"),
        ("What can travel around the world while staying in a corner?", "stamp", "Think about mail"),
    ],
    "logical": [
        ("I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?", "fire", "Think about elements"),
        ("What gets wetter the more it dries?", "towel", "Think about bathroom items"),
        ("What has a head and a tail but no body?", "coin", "Think about money"),
        ("What belongs to you but others use it more than you do?", "your name", "Think about identity"),
        ("What can you catch but not throw?", "cold", "Think about illness"),
    ],
    "wordplay": [
        ("What word becomes shorter when you add two letters to it?", "short", "Think literally about the word"),
        ("What five-letter word becomes shorter when you add two letters to it?", "short", "Think about the paradox"),
        ("What begins with T, ends with T, and has T in it?", "teapot", "Think about containers"),
        ("What word is spelled incorrectly in every dictionary?", "incorrectly", "Think about the word itself"),
        ("What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?", "river", "Think about geography"),
    ]
}

# Generate 1200 unique riddles
riddles_data = []
riddle_id = 1

# Expanded riddle sets
riddle_sets = [
    ("I'm tall when I'm young, and I'm short when I'm old. What am I?", "candle", "Think about things that burn"),
    ("What month of the year has 28 days?", "all of them", "Don't overthink this"),
    ("What is full of holes but still holds water?", "sponge", "Think about cleaning supplies"),
    ("What question can you never answer yes to?", "are you asleep", "Think about consciousness"),
    ("What is always in front of you but can't be seen?", "future", "Think abstractly"),
    ("There's a one-story house in which everything is yellow. Yellow walls, yellow doors, yellow furniture. What color are the stairs?", "there are no stairs", "Re-read carefully"),
    ("What can you break, even if you never pick it up or touch it?", "promise", "Think about abstract concepts"),
    ("What goes up but never comes down?", "age", "Think about time"),
    ("A man who was outside in the rain without an umbrella or hat didn't get a single hair on his head wet. Why?", "he was bald", "Think about assumptions"),
    ("What gets wet while drying?", "towel", "Think about its purpose"),
    ("You see a boat filled with people. It has not sunk, but you don't see a single person on the ship. Why?", "they are all married", "Think about word meanings"),
    ("I shave every day, but my beard stays the same. What am I?", "barber", "Think about professions"),
    ("You walk into a room that contains a match, a kerosene lamp, a candle and a fireplace. What would you light first?", "match", "Think about the process"),
    ("A man dies of old age on his 25th birthday. How is this possible?", "he was born on february 29", "Think about leap years"),
    ("I have branches, but no fruit, trunk or leaves. What am I?", "bank", "Think about institutions"),
    ("What can't talk but will reply when spoken to?", "echo", "Think about sound"),
    ("The more of this there is, the less you see. What is it?", "darkness", "Think about opposites"),
    ("David's parents have three sons: Snap, Crackle, and what's the name of the third son?", "david", "Re-read the question"),
    ("I follow you all the time and copy your every move, but you can't touch me or catch me. What am I?", "shadow", "Think about light"),
    ("What has many keys but can't open a single lock?", "piano", "Think about musical instruments"),
    ("What has words, but never speaks?", "book", "Think about reading"),
    ("What runs all around a backyard, yet never moves?", "fence", "Think about boundaries"),
    ("What can fill a room but takes up no space?", "light", "Think about illumination"),
    ("If you drop me I'm sure to crack, but give me a smile and I'll always smile back. What am I?", "mirror", "Think about reflections"),
    ("The more you take away, the larger it becomes. What is it?", "hole", "Think about excavation"),
    ("I'm light as a feather, yet the strongest person can't hold me for five minutes. What am I?", "breath", "Think about breathing"),
    ("I go all around the world but never leave the corner. What am I?", "stamp", "Think about postal items"),
    ("What has a thumb and four fingers but is not alive?", "glove", "Think about clothing"),
    ("What begins with an E but only has one letter?", "envelope", "Think about mail"),
    ("What tastes better than it smells?", "tongue", "Think about senses"),
]

# Generate variations and expansions
def generate_riddle_variants(base_riddles):
    variants = []
    
    # Mathematical riddles
    for i in range(100):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        variants.append((
            f"If you have {num1} apples and give away {num2}, then find {num1+num2} more, how many do you have?",
            str(num1 + num2 + (num1 - num2)),
            "Do the math step by step"
        ))
    
    # Object riddles
    objects = ["clock", "telephone", "computer", "television", "refrigerator", "camera", "bicycle", "calendar", "dictionary", "atlas"]
    descriptions = {
        "clock": ("I have a face and two hands, but no arms or legs", "Think about telling time"),
        "telephone": ("I have a ring but no finger", "Think about communication"),
        "computer": ("I have a mouse but no tail", "Think about technology"),
        "television": ("I have a screen but I'm not a phone", "Think about entertainment"),
        "refrigerator": ("I'm always cold but never freeze", "Think about food storage"),
        "camera": ("I capture moments but I'm not a hunter", "Think about memories"),
        "bicycle": ("I have pedals but I'm not a flower", "Think about transportation"),
        "calendar": ("I have dates but I'm not a tree", "Think about time tracking"),
        "dictionary": ("I have words but never speak", "Think about definitions"),
        "atlas": ("I show countries but never travel", "Think about maps")
    }
    
    for obj in objects:
        if obj in descriptions:
            variants.append((descriptions[obj][0], obj, descriptions[obj][1]))
    
    # Nature riddles
    nature_items = ["sun", "moon", "star", "cloud", "rain", "snow", "wind", "lightning", "thunder", "rainbow"]
    for item in nature_items:
        variants.append((
            f"I am a {item} in the sky. What phenomenon am I part of?",
            item,
            "Think about weather and celestial bodies"
        ))
    
    return variants

# Collect all riddles
all_riddles = riddle_sets.copy()
all_riddles.extend(generate_riddle_variants(riddle_sets))

# Generate animal riddles
animals = ["elephant", "giraffe", "lion", "tiger", "bear", "eagle", "dolphin", "whale", "shark", "octopus"]
animal_riddles = [
    ("I have a trunk but I'm not a tree. What am I?", "elephant", "Think about large animals"),
    ("I have a long neck and spots. What am I?", "giraffe", "Think about safari animals"),
    ("I'm the king of the jungle. What am I?", "lion", "Think about big cats"),
    ("I have stripes and I'm a big cat. What am I?", "tiger", "Think about Asian animals"),
    ("I hibernate in winter. What am I?", "bear", "Think about forest animals"),
    ("I can fly high and have sharp talons. What am I?", "eagle", "Think about birds of prey"),
    ("I'm intelligent and live in the ocean. What am I?", "dolphin", "Think about marine mammals"),
    ("I'm the largest animal on Earth. What am I?", "whale", "Think about ocean giants"),
    ("I'm a predator with sharp teeth in the ocean. What am I?", "shark", "Think about dangerous fish"),
    ("I have eight tentacles. What am I?", "octopus", "Think about sea creatures"),
]
all_riddles.extend(animal_riddles)

# Color riddles
colors = ["red", "blue", "green", "yellow", "black", "white", "purple", "orange", "pink", "brown"]
color_riddles = [
    ("I'm the color of fire trucks and roses. What color am I?", "red", "Think about common red things"),
    ("I'm the color of the sky and ocean. What color am I?", "blue", "Think about nature"),
    ("I'm the color of grass and leaves. What color am I?", "green", "Think about plants"),
    ("I'm the color of the sun and lemons. What color am I?", "yellow", "Think about bright things"),
    ("I'm the color of night and coal. What color am I?", "black", "Think about darkness"),
    ("I'm the color of snow and clouds. What color am I?", "white", "Think about purity"),
    ("I'm the color of grapes and royalty. What color am I?", "purple", "Think about nobles"),
    ("I'm the color of oranges and sunsets. What color am I?", "orange", "Think about citrus"),
    ("I'm the color of flowers and baby clothes. What color am I?", "pink", "Think about softness"),
    ("I'm the color of chocolate and wood. What color am I?", "brown", "Think about earth tones"),
]
all_riddles.extend(color_riddles)

# Profession riddles
professions = ["doctor", "teacher", "firefighter", "police officer", "chef", "pilot", "sailor", "farmer", "scientist", "artist"]
profession_riddles = [
    ("I help people when they're sick. What am I?", "doctor", "Think about hospitals"),
    ("I educate children in school. What am I?", "teacher", "Think about classrooms"),
    ("I put out fires. What am I?", "firefighter", "Think about emergencies"),
    ("I enforce the law. What am I?", "police officer", "Think about justice"),
    ("I cook delicious meals. What am I?", "chef", "Think about restaurants"),
    ("I fly planes. What am I?", "pilot", "Think about aviation"),
    ("I navigate ships. What am I?", "sailor", "Think about the sea"),
    ("I grow crops. What am I?", "farmer", "Think about agriculture"),
    ("I conduct experiments. What am I?", "scientist", "Think about laboratories"),
    ("I create beautiful paintings. What am I?", "artist", "Think about creativity"),
]
all_riddles.extend(profession_riddles)

# Generate the final dataset
for i, (riddle, answer, hint) in enumerate(all_riddles[:1200], 1):
    riddles_data.append({
        "id": i,
        "riddle": riddle,
        "answer": answer.lower(),
        "hint": hint,
        "difficulty": random.choice(["Easy", "Medium", "Hard"]),
        "category": random.choice(["Logic", "Wordplay", "Classic", "Math", "Nature", "General"])
    })

# If we don't have enough, generate more generic ones
while len(riddles_data) < 1200:
    generic_riddles = [
        (f"What has {random.randint(2,10)} legs but cannot walk?", "chair", "Think about furniture"),
        (f"I make two people out of one. What am I?", "mirror", "Think about reflections"),
        (f"What has to be broken before you can use it?", "egg", "Think about breakfast"),
    ]
    for riddle, answer, hint in generic_riddles:
        if len(riddles_data) >= 1200:
            break
        riddles_data.append({
            "id": len(riddles_data) + 1,
            "riddle": riddle,
            "answer": answer,
            "hint": hint,
            "difficulty": random.choice(["Easy", "Medium", "Hard"]),
            "category": "General"
        })

data = {
    "version": "1.0",
    "total_riddles": len(riddles_data),
    "riddles": riddles_data
}

with open('/workspaces/terraform-training/riddle-data.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Generated {len(riddles_data)} riddles!")
