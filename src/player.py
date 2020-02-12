from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player(Room):
    def __init__(self, name, current_room, description):
        super().__init__(name, description)
        self.current_room = current_room

    def __str__(self):
        return f"{self.name} {self.current_room} {self.description}"
