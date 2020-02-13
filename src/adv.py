from room import Room
from player import Player
from item import Item
import textwrap
import random

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declaring items, will update item descriptions.
item = {
    'battleaxe': Item("battleaxe", "description"),
    'bat': Item("bat", "description"),
    'goblet': Item("goblet'", "description"),
    'potion': Item("potion", "description"),
    'mace': Item("mace", "description"),
    'square-shield': Item("square-shield", "description"),
    'scimitar': Item("scimitar", "description")
}

# Declaring where items are located
room['outside'].add_item = item['battleaxe']
room['foyer'].add_item = item['bat']
room['overlook'].add_item = item['goblet']
room['narrow'].add_item = item['mace']
room['treasure'].add_item = item['scimitar']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
current_player = Player("Alec", room['outside'])
moving_list = ["walks briskly", "quickly teleports",
               "Naruto runs", "skips joyfully", "saunters", "playfully rolls"]
walking_pattern = random.choice(moving_list)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while True:
    cur_play = current_player
    # Printing current room name and description
    print("\n")
    print("-------------------------------------------------------------------")
    print(textwrap.fill(  # TODO: randomize the "walks briskly"
        f"\n  The traveler, {cur_play.name}, {walking_pattern} into \n ", 65))  # This is for the player name, coming from the class Player
    print(textwrap.fill(
        f"\n  the {cur_play.room}. \n ", 65))  # This is for the room, coming from the class Player
    print("------------------------------------------------------------------- \n")
    print("An item is found within the room:\n")
    print(f"{cur_play.room.add_item}\n")

    # Allowing for user input
    user_input = input("~~~~> ")

    # User goes North, "n"
    if user_input == "n":
        if cur_play.room.n_to == None:
            print(
                f"That area is blocked, {cur_play.name}. Please select a new direction.")
        else:
            cur_play.room = cur_play.room.n_to
    # User goes South, "s"
    elif user_input == "s":
        if cur_play.room.s_to == None:
            print(
                f"That area is blocked, {cur_play.name}. Please select a new direction.")
        else:
            cur_play.room = cur_play.room.s_to
    # User goes East, "e"
    elif user_input == "e":
        if cur_play.room.e_to == None:
            print(
                f"That area is blocked, {cur_play.name}. Please select a new direction.")
        else:
            cur_play.room = cur_play.room.e_to
    # User goes West, "w"
    elif user_input == "w":
        if cur_play.room.w_to == None:
            print(
                f"That area is blocked, {cur_play.name}. Please select a new direction.")
        else:
            cur_play.room = cur_play.room.w_to
    # User quits the game
    elif user_input == "q":
        print(f"\nHave fun exploring the outside world, {cur_play.name}.\n")
        break
    # User selected something outside of N, S, E, W, or Q
    else:
        print(
            f"\n Oof, that should not have happened. \n This is embarrassing. \n You tried moving to a location that does not exist! \n")
