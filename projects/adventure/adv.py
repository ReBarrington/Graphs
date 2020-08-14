from room import Room
from player import Player
from world import World

import random
from util import Queue
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
traversal_path = ['n']

q = Queue()
q.enqueue([traversal_path])

# TRAVERSAL TEST
visited_rooms = set()
mapped_dict = dict()

player.current_room = world.starting_room

def initialize_room():
    print(f' Initializing {player.current_room.name}')
    visited_rooms.add(player.current_room.name)
    mapped_dict[player.current_room.id] = dict()

    for exit in player.current_room.get_exits():
        # Initialize all directions as "?" as this room has not been visited.
        mapped_dict[player.current_room.id][exit] = "?"

    try: 
        mapped_dict[player.current_room.id][direction_of_prev] = prev_room.id
    except:
        pass

    print(mapped_dict)


while q.size() > 0:

    last_direction = q.dequeue()

    print(f'in  {player.current_room.name}')
    print(f'exits: {player.current_room.get_exits()}')
    print(f' visited:  {visited_rooms}' )

    if player.current_room.name not in visited_rooms:
        initialize_room()

    # for each possible direction
    for key, value in (mapped_dict[player.current_room.id].items()):

        if value == "?":
            print(key,' is unexplored.')
            move = key

            prev_room = player.current_room
            direction_of_prev = player.current_room.return_opposite_direction(move)

            mapped_dict[player.current_room.id][move] = player.current_room.get_room_in_direction(move).id
            print(' UPDATING INFO: ', mapped_dict)

            q.enqueue(move)
            print('moving ', move)
            player.travel(move)
            
            if player.current_room.name not in visited_rooms:
                break


    print("No unexplored directions in this room.")
    continue


if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
