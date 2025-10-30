"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Lemanuel Devane


AI Usage: ChatGPT (GPT-5) helped with organization, finding syntax errors as well as creating dictionary for loading characters.
"""

import random
import os  

#calculate_stats function
def calculate_stats(role, level):
    """
    Calculates base stats based on role and level.
    Each level adds +5 to all stats.
    """
    base_stats = {
        "Assassin":  (15, 8, 70),
        "Healer":    (7, 15, 90),
        "Tank":      (12, 10, 110),
        "Assault":   (10, 10, 100),
        "Unclassified": (20, 20, 150)
    }

    if role in base_stats:
        strength, magic, health = base_stats[role]
    else:
        strength, magic, health = (10, 10, 100)

    # Add +5 to each stat for every level up
    strength += (level - 1) * 5
    magic += (level - 1) * 5
    health += (level - 1) * 5

    return strength, magic, health


#create_character function
def create_character(name):
    """
    Creates a character with a random role and type.
    Returns: character dictionary
    """
    roles = ["Assassin", "Healer", "Tank", "Assault", "Unclassified"]

    # assigns random role to character
    index = random.randint(0, len(roles)-1)
    role = roles[index]  

    #assigns your character type based on your role
    if role in ["Assassin", "Assault"]:
        type_ = "Striker"
    elif role == "Tank":
        type_ = "Vanguard"
    elif role == "Healer":
        type_ = "Support"
    else:
        type_ = "Special"
    
    level = 1
    strength, magic, health = calculate_stats(role, level)

    character = {
        "name": name,
        "role": role,
        "type": type_,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }

    return character


#display_character function
def display_character(character):
    """Prints formatted character sheet."""
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Role: {character['role']}")
    print(f"Type: {character['type']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("\n")

#save_character funct
def save_character(character, filename):
    """
    Saves the character to a text file.
    Returns True if successful, False if filename is empty.
    """
    if filename == "":
        print("No filename entered. Character not saved.")
        return False
    else:
        file = open(filename, "w")
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Role: {character['role']}\n")
        file.write(f"Type: {character['type']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
        file.close()
        return True

# load_character function
def load_character(filename):
    """
    Loads character from text file.
    Returns character dictionary if file exists, None otherwise.
    """
    if not os.path.exists(filename):
        print("File not found. Please check the name and try again.")
        return None
    else:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        data = {}
        for line in lines:
            parts = line.strip().split(": ")
            if len(parts) == 2:
                key = parts[0]
                value = parts[1]
                data[key] = value

        character = {
            "name": data["Character Name"],
            "role": data["Role"],
            "type": data["Type"],
            "level": int(data["Level"]),
            "strength": int(data["Strength"]),
            "magic": int(data["Magic"]),
            "health": int(data["Health"]),
            "gold": int(data["Gold"])
        }
        return character


# level_up function
def level_up(character):
    """Increases level and recalculates stats."""
    character["level"] += 1
    strength, magic, health = calculate_stats(character["role"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    print(f"\n{character['name']} has leveled up to Level {character['level']}!\n")



# MAIN PROGRAM
if __name__ == "__main__":
    print("=== SOLO LEVELING CHARACTER CREATOR ===\n")
    name = input("Enter your character's name: ")

    # Create character
    char = create_character(name)
    display_character(char)

    # Main loop
    running = True
    while running:
        print("Options:")
        print("1. Level Up")
        print("2. Save Character")
        print("3. Load Character")
        print("4. Display Character")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            confirm = input("Level up? (y/n): ").lower()
            if confirm == "y":
                level_up(char)
                display_character(char)
        elif choice == "2":
            filename = input("Enter filename to save (e.g., my_char.txt): ")
            success = save_character(char, filename)
            if success:
                print("Character saved successfully!\n")
        elif choice == "3":
            filename = input("Enter filename to load: ")
            loaded = load_character(filename)
            if loaded is not None:
                char = loaded
                print("Character loaded!\n")
                display_character(char)
        elif choice == "4":
            display_character(char)
        elif choice == "5":
            print("Goodbye, Hunter.")
            running = False
        else:
            print("Invalid option. Try again.\n")
