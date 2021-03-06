import textwrap
from room import Room
from player import Player
from item import Item

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

sword = Item("sword", 10, 0)
shield = Item("shield", 0, 10)
magic_ring = Item("magic_ring", 5, 5)
treasure = Item('treasure', 0, 0)

room['outside'].add_item(shield)
room['overlook'].add_item(sword)
room['narrow'].add_item(magic_ring)
room['treasure'].add_item(treasure)

derrick = Player(room['outside'], 100)
current_room = room['outside']
quit = False

while quit is False:
    print(f'\n\nCurrent Room: {derrick.current_room}')
    print(
        f'Description: {textwrap.wrap(current_room.description)}')

    if current_room.name == 'Treasure Chamber':
        print("***** YOU HAVE FOUND THE TREASURE ROOM *****")

    command = input(
        '\nWhat do you want to do???\n(E)xplore Current Room\n(G)o to new Room\n(I)nspect Inventory\n(Q)uit\n\n\n')
    if command == '':
        continue

    command = command.strip().lower()[0]

    if command == 'q':
        quit = True

    elif command == 'e':

        if not current_room.items:
            print("There's nothing here to be found")
        else:
            for key, value in current_room.items.items():
                print(f"You have found a {key} do you want to pick it up?")

                i_want = input('***\n(y)es\n(n)o\n***')
                i_want = i_want.strip().lower()[0]
                if i_want == 'y':
                    derrick.add_item(value)
            for key, value in derrick.items.items():
                current_room.remove_item(value)


    elif command == 'g':
        direction = input(
            '\nWhich Direction Do you want to go???\n(n)orth\n(e)ast\n(s)outh\n(w)est\n(q)uit\n\n\n')

        while direction not in ('n', 's', 'e', 'w', 'q'):
            print('*** Please choose valid cardinal direction or q for quit***')
            direction = input(
                '\nWhich Direction Do you want to go???\n(n)orth\n(e)ast\n(s)outh\n(w)est\n(q)uit\n\n\n')

        if direction == 'q':
            quit = True
            continue

        direction = direction.strip().lower()[0] +"_to"
        print(f"You have chosen to go {direction}")

        other_room = getattr(current_room, direction)

        if other_room is None:
            print("a room doesn't exist in that direction")
        else:
            current_room = derrick.current_room = other_room
            print(f"derrick's current room: {derrick.current_room}")

    elif command == 'i':

        if not derrick.items:
            print("You don't have any items")
        else:
            for key, value in derrick.items.items():
                print(f"You are carrying a {key}")
                command = input('What do you want to do with your item?\n(d)rop it\n(n)othing\n')

                if command == 'd':
                    current_room.add_item(value)

            for key, value in current_room.items.items():
                derrick.remove_item(value)