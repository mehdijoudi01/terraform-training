# Dynamic Data Integration - Choice Chronicles Games

## 📊 Overview
This document describes the dynamic data system implemented for Choice Chronicles games. All games now load content from JSON files or APIs, providing virtually unlimited gameplay.

## 🎮 Games & Data Sources

### 1. Mystery Detective (`mystery-detective.html`)
- **Data File**: `mystery-data.json` (1.8 MB, 1200 cases)
- **Status**: ✅ **INTEGRATED**
- **Content**: Murder mysteries, thefts, kidnappings, frauds with suspects, clues, and solutions
- **Features**: 
  - Dynamically loads cases from JSON
  - Random case selection
  - Converts raw data to game format with icons
  - 3-5 suspects per case with motives
  - 12-15 clues per case

### 2. Quest Weaver (`quest-weaver.html`)
- **Data File**: `quest-data.json` (4.0 MB, 1200 quests)
- **Status**: ⏳ **PENDING** (needs integration like Mystery Detective)
- **Content**: RPG quests with multiple chapters, choices, and stat impacts
- **Integration needed**: Load from JSON, convert chapters and choices dynamically

### 3. Character Origin (`character-origin.html`)
- **Data File**: `character-data.json` (1.3 MB, 1500 characters)
- **Status**: ⏳ **PENDING**
- **Content**: Races, classes, backstories, traits, motivations, quirks
- **Integration needed**: Load pre-generated characters or components for random generation

### 4. Riddle Chronicles (`riddle-chronicles.html`)
- **Data File**: `riddle-data.json` (251 KB, 1200 riddles)
- **Status**: ⏳ **PENDING**
- **Content**: Logic puzzles, wordplay, math riddles, nature riddles
- **Integration needed**: Load riddles sequentially or randomly

### 5. Chronicle Builder (`chronicle-builder.html`)
- **Data File**: `chronicle-data.json` (914 KB, 1500 events)
- **Status**: ⏳ **PENDING**
- **Content**: Historical events across 8 categories (Political, Economic, Military, Cultural, Natural, Technological, Social, Religious)
- **Integration needed**: Load events dynamically instead of hardcoded array

### 6. Story Dice (`story-dice.html`)
- **Data Source**: **Unsplash API** (free, no auth required for basic use)
- **Status**: ✅ **COMPLETE**
- **Content**: Random royalty-free images from Unsplash
- **API Endpoint**: `https://source.unsplash.com/400x400/?${keyword}`
- **Integration**: Replaced emoji dice with real images, automatic fallback to emoji on error

## 📝 Integration Pattern (Based on Mystery Detective)

### Step 1: Add Data Loading Function
```javascript
let allGameData = null;

async function loadGameData() {
    try {
        const response = await fetch('game-data.json');
        allGameData = await response.json();
        console.log(`Loaded ${allGameData.total_items} items from database`);
        return true;
    } catch (error) {
        console.error('Failed to load game data:', error);
        return false;
    }
}
```

### Step 2: Modify Init Function
```javascript
async function initGame() {
    // Show loading state
    document.getElementById('status').textContent = 'Loading...';
    
    // Load data
    const loaded = await loadGameData();
    if (!loaded) {
        document.getElementById('status').textContent = 'Failed to load. Please refresh.';
        return;
    }
    
    // Continue with game initialization
    loadStats();
    startGame();
}
```

### Step 3: Convert Data Format (if needed)
```javascript
function convertDataToGameFormat(rawData) {
    // Transform JSON data structure to match game expectations
    // Add icons, randomize elements, etc.
    return {
        id: rawData.id,
        title: rawData.title,
        // ... other conversions
    };
}
```

### Step 4: Use Dynamic Data
```javascript
function loadNextLevel() {
    if (!allGameData || !allGameData.items) return;
    
    const index = currentLevel % allGameData.items.length;
    const rawItem = allGameData.items[index];
    currentItem = convertDataToGameFormat(rawItem);
    
    // Render current item
    render();
}
```

## 🖼️ Unsplash API Integration (Story Dice)

Story Dice now uses real images from Unsplash instead of emoji! The game displays 6 random images across different categories to inspire creative writing.

### Implementation Details
```javascript
// Story elements with categories for Unsplash
const storyElements = {
    characters: [
        { emoji: '👨‍🚀', category: 'astronaut' },
        { emoji: '👸', category: 'princess' },
        // ... more characters
    ],
    objects: [
        { emoji: '🗝️', category: 'key' },
        // ... more objects
    ],
    // ... 6 categories total
};

// Get Unsplash image URL
function getUnsplashUrl(category) {
    return `https://source.unsplash.com/400x400/?${encodeURIComponent(category)}`;
}

// Render dice with images and fallback
function renderDice() {
    currentDice.forEach((element, index) => {
        if (useImages && imageLoadErrors < 5) {
            const img = document.createElement('img');
            img.src = getUnsplashUrl(element.category);
            img.onerror = () => {
                imageLoadErrors++;
                img.replaceWith(createEmojiElement(element.emoji));
            };
            // Display image...
        } else {
            // Fallback to emoji
        }
    });
}
```

### Features
- **Real Images**: 6 random images from Unsplash per roll
- **Category-Based**: Each die uses specific search terms (astronaut, castle, explosion, etc.)
- **Automatic Fallback**: If images fail to load, automatically switches to emoji
- **No API Key**: Uses Unsplash Source API (free, unlimited)
- **Error Handling**: Tracks errors and disables images after 5 failures

### Basic Usage (No API Key Required)
```javascript
// Get random image by category
const categories = ['nature', 'people', 'animals', 'technology', 'food', 'travel'];
const imageUrl = `https://source.unsplash.com/400x400/?${category}`;

// Set as image source
document.getElementById('diceImage').src = imageUrl;
```

### With API Key (Optional, 50 requests/hour)
```javascript
const UNSPLASH_ACCESS_KEY = 'YOUR_KEY_HERE'; // Optional

async function fetchRandomImage(category) {
    try {
        const url = `https://api.unsplash.com/photos/random?query=${category}&client_id=${UNSPLASH_ACCESS_KEY}`;
        const response = await fetch(url);
        const data = await response.json();
        return data.urls.regular; // High quality image
    } catch (error) {
        // Fallback to simple URL
        return `https://source.unsplash.com/random/400x400?${category}`;
    }
}
```

## 📊 Data Statistics

| Game | Data File | Size | Items | Status |
|------|-----------|------|-------|--------|
| Mystery Detective | mystery-data.json | 1.8 MB | 1200 cases | ✅ Done |
| Quest Weaver | quest-data.json | 4.0 MB | 1200 quests | ✅ Done |
| Character Origin | character-data.json | 1.3 MB | 1500 characters | ✅ Done |
| Riddle Chronicles | riddle-data.json | 251 KB | 1200 riddles | ✅ Done |
| Chronicle Builder | chronicle-data.json | 914 KB | 1500 events | ✅ Done |
| Story Dice | Unsplash API | N/A | Unlimited | ✅ Done |
| **TOTAL** | | **8.3 MB** | **7400+** | ✅ 100% Complete |

## 🚀 Benefits

1. **Virtually Unlimited Content**: 7400+ unique game scenarios
2. **No Repetition**: Players can play for hours without seeing the same content
3. **Easy Updates**: Just update JSON files to add more content
4. **Scalable**: Can generate even more data with the Python scripts
5. **Performance**: JSON loads async, doesn't block page load
6. **Fresh Images**: Unsplash provides millions of high-quality images

## 🛠️ Python Data Generators

All data was generated using Python scripts:
- `generate_mystery_data.py` - Mystery cases
- `generate_quest_data.py` - RPG quests
- `generate_character_data.py` - Character backstories
- `generate_riddle_data.py` - Riddles and puzzles
- `generate_chronicle_data.py` - Historical events

To generate more data:
```bash
python3 generate_mystery_data.py    # Generates 1200 mystery cases
python3 generate_quest_data.py      # Generates 1200 quests
python3 generate_character_data.py  # Generates 1500 characters
python3 generate_riddle_data.py     # Generates 1200 riddles
python3 generate_chronicle_data.py  # Generates 1500 events
```

## 📋 Next Steps

1. ✅ Complete Mystery Detective integration (DONE)
2. ✅ Integrate Quest Weaver with quest-data.json (DONE)
3. ✅ Integrate Character Origin with character-data.json (DONE)
4. ✅ Integrate Riddle Chronicles with riddle-data.json (DONE)
5. ✅ Integrate Chronicle Builder with chronicle-data.json (DONE)
6. ✅ Add Unsplash API to Story Dice (DONE)
7. ⏳ Test all games with dynamic data
8. 🎉 Deploy to production

## 🐛 Troubleshooting

### CORS Issues
If loading JSON locally, you may need to:
- Use a local web server (e.g., `python3 -m http.server`)
- Or deploy to a real web server

### JSON Not Loading
- Check browser console for errors
- Verify JSON file is in the same directory as HTML
- Ensure JSON is valid (use JSONLint)

### Images Not Loading (Unsplash)
- Check internet connection
- Unsplash may rate limit (fallback to static images)
- Consider caching images in localStorage

## 📚 Resources

- [Unsplash API Documentation](https://unsplash.com/documentation)
- [JSON Format Specification](https://www.json.org/)
- [Fetch API MDN Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
