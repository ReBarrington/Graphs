from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()

def initialize_room(current_room):
    print(f' Initializing {current_room.name}')
    visited_rooms.add(current_room.name)
    mapped_dict[current_room.id] = dict()

    for exit in current_room.get_exits():
        # Initialize all directions as "?" as this room has not been visited.
        mapped_dict[current_room.id][exit] = "?"

    try: 
        mapped_dict[current_room.id][direction_of_prev] = prev_room.id
    except:
        pass

    print(mapped_dict)

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
mapped_dict = dict()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

q = Queue()
q.enqueue(player.current_room)

# for move in traversal_path:
# while q.size() > 0:
while len(room_graph) > len(visited_rooms):

    # let current_room be equal to q.dequeue
    current_room = q.dequeue()

    print(f'CURRENT ROOM: {current_room}')

    if current_room.name not in visited_rooms:
        initialize_room(current_room)

        for exit in current_room.get_exits():

            mapped_dict[current_room.id][exit] = current_room.get_room_in_direction(exit).id
            print(' UPDATING INFO: ', mapped_dict)

            prev_room = player.current_room
            direction_of_prev = player.current_room.return_opposite_direction(exit)

            traversal_path.append(exit)
            q.enqueue(current_room.get_room_in_direction(exit))

            print('moving ', exit)
            player.travel(exit)

            print(q.queue, ' is queue')
            # print(traversal_path, ' is traversal path')



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