import json
import random

# Event categories
event_categories = ["Political", "Economic", "Military", "Cultural", "Natural", "Technological", "Social", "Religious"]

# Event templates for each category
political_events = [
    {"title": "Royal Marriage Proposal", "description": "A neighboring kingdom proposes a marriage alliance", "choices": [
        {"text": "Accept the marriage", "popularity": 15, "stability": 10, "resources": 20},
        {"text": "Decline diplomatically", "popularity": 5, "stability": -5, "resources": 0},
        {"text": "Demand better terms", "popularity": 10, "stability": 5, "resources": 30}
    ]},
    {"title": "Border Dispute", "description": "A territorial dispute arises with a neighbor", "choices": [
        {"text": "Go to war", "popularity": -10, "stability": -20, "resources": -30},
        {"text": "Negotiate peace", "popularity": 10, "stability": 10, "resources": 5},
        {"text": "Cede territory", "popularity": -20, "stability": 5, "resources": 15}
    ]},
]

economic_events = [
    {"title": "Trade Opportunity", "description": "Merchants propose a new trade route", "choices": [
        {"text": "Invest heavily", "popularity": 10, "stability": 5, "resources": 50},
        {"text": "Make modest investment", "popularity": 5, "stability": 0, "resources": 20},
        {"text": "Decline the opportunity", "popularity": -5, "stability": 0, "resources": 0}
    ]},
    {"title": "Economic Crisis", "description": "A financial crash threatens your economy", "choices": [
        {"text": "Bail out banks", "popularity": -15, "stability": 10, "resources": -40},
        {"text": "Let market correct", "popularity": -20, "stability": -15, "resources": 0},
        {"text": "Implement reforms", "popularity": 5, "stability": -5, "resources": -20}
    ]},
]

military_events = [
    {"title": "Military Recruitment", "description": "Your generals request more soldiers", "choices": [
        {"text": "Mandatory conscription", "popularity": -20, "stability": -10, "resources": -30},
        {"text": "Volunteer army", "popularity": 10, "stability": 5, "resources": -50},
        {"text": "Maintain current size", "popularity": 0, "stability": -5, "resources": 0}
    ]},
    {"title": "Fortress Construction", "description": "Advisors suggest building border fortresses", "choices": [
        {"text": "Build extensive fortifications", "popularity": 5, "stability": 15, "resources": -60},
        {"text": "Build modest defenses", "popularity": 5, "stability": 10, "resources": -30},
        {"text": "Focus on diplomacy instead", "popularity": 0, "stability": -5, "resources": 10}
    ]},
]

cultural_events = [
    {"title": "Cultural Festival", "description": "Citizens request a grand festival", "choices": [
        {"text": "Host elaborate celebration", "popularity": 25, "stability": 10, "resources": -40},
        {"text": "Simple local festivals", "popularity": 10, "stability": 5, "resources": -10},
        {"text": "Cancel for austerity", "popularity": -20, "stability": -10, "resources": 20}
    ]},
    {"title": "Artist Patronage", "description": "Famous artists seek your sponsorship", "choices": [
        {"text": "Become major patron", "popularity": 15, "stability": 5, "resources": -30},
        {"text": "Modest support", "popularity": 5, "stability": 0, "resources": -10},
        {"text": "No support", "popularity": -10, "stability": 0, "resources": 0}
    ]},
]

natural_events = [
    {"title": "Drought", "description": "A severe drought threatens your farmlands", "choices": [
        {"text": "Emergency water projects", "popularity": 15, "stability": 5, "resources": -50},
        {"text": "Import food", "popularity": 10, "stability": 0, "resources": -30},
        {"text": "Pray for rain", "popularity": -10, "stability": -10, "resources": 0}
    ]},
    {"title": "Earthquake", "description": "A powerful earthquake strikes your capital", "choices": [
        {"text": "Massive reconstruction", "popularity": 20, "stability": 10, "resources": -70},
        {"text": "Basic repairs", "popularity": 5, "stability": -5, "resources": -30},
        {"text": "Minimal response", "popularity": -25, "stability": -20, "resources": -10}
    ]},
]

technological_events = [
    {"title": "New Invention", "description": "An inventor presents a revolutionary device", "choices": [
        {"text": "Fund development", "popularity": 10, "stability": 5, "resources": -40},
        {"text": "Observe cautiously", "popularity": 0, "stability": 0, "resources": 0},
        {"text": "Reject as heresy", "popularity": -10, "stability": 5, "resources": 0}
    ]},
    {"title": "Infrastructure Upgrade", "description": "Engineers propose new roads and bridges", "choices": [
        {"text": "Major infrastructure program", "popularity": 15, "stability": 10, "resources": -80},
        {"text": "Modest improvements", "popularity": 10, "stability": 5, "resources": -35},
        {"text": "No changes", "popularity": -5, "stability": 0, "resources": 0}
    ]},
]

social_events = [
    {"title": "Social Unrest", "description": "Workers demand better conditions", "choices": [
        {"text": "Grant all demands", "popularity": 20, "stability": 10, "resources": -40},
        {"text": "Negotiate compromise", "popularity": 10, "stability": 5, "resources": -20},
        {"text": "Suppress the movement", "popularity": -30, "stability": -15, "resources": 0}
    ]},
    {"title": "Education Reform", "description": "Scholars propose universal education", "choices": [
        {"text": "Implement fully", "popularity": 15, "stability": 10, "resources": -50},
        {"text": "Gradual implementation", "popularity": 10, "stability": 5, "resources": -25},
        {"text": "Maintain status quo", "popularity": -10, "stability": 0, "resources": 0}
    ]},
]

religious_events = [
    {"title": "Religious Schism", "description": "A new religious sect emerges", "choices": [
        {"text": "Support new sect", "popularity": -20, "stability": -15, "resources": 0},
        {"text": "Remain neutral", "popularity": 0, "stability": -5, "resources": 0},
        {"text": "Suppress heretics", "popularity": 10, "stability": 5, "resources": -10}
    ]},
    {"title": "Holy Pilgrimage", "description": "Religious leaders request funding for pilgrimage site", "choices": [
        {"text": "Full funding", "popularity": 20, "stability": 15, "resources": -45},
        {"text": "Partial funding", "popularity": 10, "stability": 5, "resources": -20},
        {"text": "No funding", "popularity": -15, "stability": -10, "resources": 0}
    ]},
]

all_event_templates = {
    "Political": political_events,
    "Economic": economic_events,
    "Military": military_events,
    "Cultural": cultural_events,
    "Natural": natural_events,
    "Technological": technological_events,
    "Social": social_events,
    "Religious": religious_events
}

# Generate unique events
def generate_event(event_id):
    category = random.choice(list(all_event_templates.keys()))
    base_events = all_event_templates[category]
    template = random.choice(base_events)
    
    # Create variation of the template
    event = {
        "id": event_id,
        "title": template["title"],
        "description": template["description"],
        "category": category,
        "year": random.randint(1, 100),
        "choices": []
    }
    
    # Add some randomization to the choices
    for choice in template["choices"]:
        randomized_choice = {
            "text": choice["text"],
            "popularity": choice["popularity"] + random.randint(-5, 5),
            "stability": choice["stability"] + random.randint(-3, 3),
            "resources": choice["resources"] + random.randint(-10, 10)
        }
        event["choices"].append(randomized_choice)
    
    return event

# Additional event variations
extra_titles = {
    "Political": ["Assassination Plot", "Succession Crisis", "Rebellion", "Alliance Offer", "Diplomatic Incident", "Coronation", "Constitutional Crisis", "Power Struggle", "Foreign Interference", "Civil Unrest"],
    "Economic": ["Market Boom", "Resource Discovery", "Banking Crisis", "Trade War", "Currency Devaluation", "Tax Revolt", "Merchant Guild", "Mining Opportunity", "Inflation Crisis", "Economic Miracle"],
    "Military": ["Invasion Threat", "Military Coup", "Naval Battle", "Siege", "Arms Race", "Mercenary Offer", "Military Parade", "War Declaration", "Peace Treaty", "Military Reform"],
    "Cultural": ["Great Artist", "Literary Movement", "Theater Opening", "Museum Founding", "Cultural Exchange", "Language Reform", "Historical Monument", "Music Revolution", "Architectural Wonder", "Cultural Renaissance"],
    "Natural": ["Flood", "Famine", "Plague", "Volcanic Eruption", "Hurricane", "Forest Fire", "Tsunami", "Meteor Shower", "Extreme Heat", "Blizzard"],
    "Technological": ["Steam Power", "Printing Press", "Navigation Tools", "Agricultural Innovation", "Medical Breakthrough", "Architectural Technique", "Metallurgy Advance", "Communication System", "Weaponry Innovation", "Industrial Revolution"],
    "Social": ["Women's Rights", "Slavery Abolition", "Labor Union", "Class Conflict", "Immigration Wave", "Public Health", "Housing Crisis", "Poverty Relief", "Social Mobility", "Population Boom"],
    "Religious": ["Temple Construction", "Prophet Arrival", "Religious War", "Inquisition", "Reformation", "Holy Relic", "Religious Tolerance", "Monastery Founding", "Divine Sign", "Religious Festival"]
}

# Generate 1500 events
events = []
for i in range(1, 1501):
    if i <= 100:
        # Use templates as-is for first 100
        events.append(generate_event(i))
    else:
        # Generate new events with variations
        category = random.choice(list(extra_titles.keys()))
        title = random.choice(extra_titles[category])
        
        descriptions = [
            f"Your advisors inform you about {title.lower()}",
            f"A crisis unfolds: {title}",
            f"An opportunity presents itself regarding {title.lower()}",
            f"Your kingdom faces {title.lower()}",
            f"Important decision needed about {title.lower()}"
        ]
        
        event = {
            "id": i,
            "title": title,
            "description": random.choice(descriptions),
            "category": category,
            "year": random.randint(1, 100),
            "choices": [
                {
                    "text": random.choice(["Aggressive action", "Bold approach", "Decisive intervention", "Full commitment"]),
                    "popularity": random.randint(-20, 20),
                    "stability": random.randint(-15, 15),
                    "resources": random.randint(-60, 30)
                },
                {
                    "text": random.choice(["Moderate response", "Balanced approach", "Careful action", "Measured response"]),
                    "popularity": random.randint(-10, 15),
                    "stability": random.randint(-5, 10),
                    "resources": random.randint(-30, 20)
                },
                {
                    "text": random.choice(["Conservative stance", "Minimal action", "Wait and see", "Status quo"]),
                    "popularity": random.randint(-15, 5),
                    "stability": random.randint(-5, 5),
                    "resources": random.randint(-10, 15)
                }
            ]
        }
        events.append(event)

data = {
    "version": "1.0",
    "total_events": len(events),
    "categories": list(all_event_templates.keys()),
    "events": events
}

with open('/workspaces/terraform-training/chronicle-data.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Generated {len(events)} chronicle events!")
