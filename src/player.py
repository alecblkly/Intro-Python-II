# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap


class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def __str__(self):
        return f"{self.name}, {self.room}"

    def move(self, direction):
        next_room = getattr(self.room, f"{direction}_to")
        if next_room == None:
            print(
                f"That area is blocked, {self.name}. Please select a new direction.\n")
        else:
            self.room = next_room
            print(textwrap.fill(
                f"\n You walk into the {self.room}. \n ", 65))

    def add_inventory(self, inventory):
        self.inventory.append(inventory)
        return f"{self.inventory}"

    def remove_inventory(self, inventory):
        self.inventory.remove(inventory)
        return f"{self.inventory}"
