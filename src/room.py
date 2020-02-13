# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.inventory = []

    def __str__(self):
        return f"{self.name}, {self.description}"

    def add_item(self, inventory):
        self.inventory.append(inventory)
        return f"{self.inventory}"

    def remove_item(self, inventory):
        self.inventory.remove(inventory)
        return f"{self.inventory}"
