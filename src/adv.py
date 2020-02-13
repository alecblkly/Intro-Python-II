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
    'goblet': Item("goblet", "description"),
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
# Allowing user to pick their name
current_player = Player(input("How may I refer to you? "), room['outside'])

# Starter text, welcomes player to the world and lets them know their options
print(
    f"\nThat is a lovely name, {current_player.name}. Welcome to the world!\n")
print(
    f"As you enter the world, you are currently standing in the {current_player.room}\n")
print("You have several options to pick from:\n")
print("'n' - To move North\n")
print("'s' - To move South\n")
print("'e' - To move East\n")
print("'w' - To move West\n")
print("'get [item name]' - To add an item to your inventory\n")
print("'drop [item name]' - To drop the item in the current room\n")
print("'i' - To check your current inventory\n")
print("------------------------")
print("'q' - To leave the world\n\n")


moving_list = ["walked briskly", "quickly teleported",
               "Naruto ran", "skipped joyfully", "sauntered", "playfully rolled"]
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

    # Allowing for user input
    user_input = input("~~~~> ")

    # User goes North, "n"
    if user_input == "n":
        if cur_play.room.n_to == None:
            print(
                f"That area is blocked, {cur_play.name}. Please select a new direction.\n")
        else:
            cur_play.room = cur_play.room.n_to
            print(textwrap.fill(
                f"\n  You {walking_pattern} into the {cur_play.room}. \n ", 65))
            print("---------------------------------------------------------------------")
            print("The following items are found within the room:\n")
            print(f"{cur_play.room.add_item}\n")
    # User goes South, "s"
    elif user_input == "s":
        if cur_play.room.s_to == None:
            print(
                f"That area is blocked, {cur_play.name}. Please select a new direction.")
        else:
            cur_play.room = cur_play.room.s_to
            print(textwrap.fill(
                f"\n  You {walking_pattern} into the {cur_play.room}. \n ", 65))
            print("---------------------------------------------------------------------")
            print("The following items are found within the room:\n")
            print(f"{cur_play.room.add_item}\n")
    # User goes East, "e"
    elif user_input == "e":
        if cur_play.room.e_to == None:
            print(
                f"That area is blocked, {cur_play.name}. Please select a new direction.")
        else:
            cur_play.room = cur_play.room.e_to
            print(textwrap.fill(
                f"\n  You {walking_pattern} into the {cur_play.room}. \n ", 65))
            print("---------------------------------------------------------------------")
            print("The following items are found within the room:\n")
            print(f"{cur_play.room.add_item}\n")
    # User goes West, "w"
    elif user_input == "w":
        if cur_play.room.w_to == None:
            print(
                f"That area is blocked, {cur_play.name}. Please select a new direction.")
        else:
            cur_play.room = cur_play.room.w_to
            print(textwrap.fill(
                f"\n  You {walking_pattern} into the {cur_play.room}. \n ", 65))
            print("---------------------------------------------------------------------")
            print("The following items are found within the room:\n")
            print(f"{cur_play.room.add_item}\n")
    # User quits the game
    elif user_input == "q":
        print(f"\nHave fun exploring the outside world, {cur_play.name}.\n")
        break
    # User selected something outside of N, S, E, W, or Q
    else:
        print(
            f"\n Oof, that should not have happened. \n This is embarrassing. \n You tried moving to a location that does not exist! \n")
