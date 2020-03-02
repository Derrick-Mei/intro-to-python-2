# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.items = {}

    def add_item(self, item):
        self.items[item] = item

    def remove_item(self, item):
        self.items.pop(item, None)
