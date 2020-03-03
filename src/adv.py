import textwrap
from room import Room
from player import Player

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

derrick = Player(room['outside'])
current_room = room['outside']
quit = False

while quit is False:
    print(f'Current Room: {derrick.current_room}')
    print(
        f'Description: {textwrap.wrap(current_room.description)}')

    command = input(
        '\nWhat do you want to do???\n(E)xplore Current Room\n(G)o to new Room\n(Q)uit\n\n\n')
    if command == '':
        continue

    command = command.strip().lower()[0]

    if command == 'q':
        quit = True

    elif command == 'e':
        print("There's nothing here to be found")

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
