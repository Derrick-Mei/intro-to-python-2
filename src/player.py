# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room, health):
        self.current_room = current_room
        self.items = {}
        self.health = health
        self.attack = 10
        self.defence = 10

    def add_item(self, item):
        self.items[item.name] = item

    def remove_item(self, item):
        self.items.pop(item.name, None)
