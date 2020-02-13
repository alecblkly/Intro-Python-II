# Class for items, to be picked up/dropped by players
# Items will also exist within rooms


class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}\n\n{self.description}"
