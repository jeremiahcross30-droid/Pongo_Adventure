# Pongo's City Adventure - Combined Room and Item Dictionary Version
# Updated based on instructor feedback to merge items and rooms into a single dictionary

rooms = {
    "The Park": {
        "North": "Grocery Store",
        "South": "Pet Store",
        "East": "Vet Office",
        "West": "Backyard",
        "item": None
    },
    "Grocery Store": {
        "South": "The Park",
        "East": "Alley",
        "item": "Bone"
    },
    "Alley": {
        "West": "Grocery Store",
        "item": "Stray Cat"
    },
    "Pet Store": {
        "North": "The Park",
        "East": "Empty Building",
        "item": "Treat Bag"
    },
    "Empty Building": {
        "West": "Pet Store",
        "item": "Stray Dog"
    },
    "Vet Office": {
        "West": "The Park",
        "North": "Shelter",
        "item": "Leash"
    },
    "Shelter": {
        "South": "Vet Office",
        "item": None
    },
    "Backyard": {
        "East": "The Park",
        "item": "Key"
    }
}

inventory = []
current_room = "The Park"
TOTAL_ITEMS = 6

def show_status():
    print(f"\nYou are in the {current_room}.")
    exits = ', '.join([d for d in rooms[current_room] if d != 'item'])
    print(f"Exits: {exits}")
    item_here = rooms[current_room]['item']
    if item_here:
        print(f"You see a {item_here} here.")
    print(f"Inventory: {inventory}")

def move(direction_raw):
    global current_room
    direction = direction_raw.strip().title()
    if direction not in rooms[current_room]:
        print(f"You can't go {direction} from here.")
        return
    current_room = rooms[current_room][direction]
    print(f"You move {direction} to the {current_room}.")

def get_item(item_raw):
    item = item_raw.strip().title()
    item_here = rooms[current_room]['item']
    if item_here is None:
        print("There is no item to pick up here.")
        return
    if item != item_here:
        print(f"That item isn't here. Try: get {item_here}")
        return
    inventory.append(item_here)
    rooms[current_room]['item'] = None
    print(f"Picked up: {item_here}")

print("Welcome to Pongo's City Adventure! Type 'go <direction>' or 'get <item>' or 'exit' to quit.")

game_running = True
while game_running:
    show_status()
    if current_room == "Shelter":
        if len(inventory) == TOTAL_ITEMS:
            print("You have all items! Pongo escapes safely. YOU WIN!")
        else:
            print("Dog Catcher grabs Pongo. GAME OVER.")
        break

    command = input("\n> ").strip().lower()
    if command == "exit":
        print("Thanks for playing! Goodbye.")
        break
    elif command.startswith("go "):
        move(command[3:])
    elif command.startswith("get "):
        get_item(command[4:])
    else:
        print("Invalid command! Use 'go <direction>' or 'get <item>'.")
