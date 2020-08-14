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
    visited_rooms[current_room.id] = dict()

    for exit in current_room.get_exits():
        # Initialize all directions as "?" as this room has not been visited.
        visited_rooms[current_room.id][exit] = "?"

    # try: 
    #     visited_rooms[current_room.id][direction_of_prev] = prev_room.id
    # except:
    #     pass

    print(visited_rooms)

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
traversal_path = []

# TRAVERSAL TEST
visited_rooms = dict()
player.current_room = world.starting_room

# q of rooms visited
q = Queue()
q.enqueue([player.current_room])


while q.size() > 0:

    current_path = q.dequeue()
    current_room = current_path[-1] 

    print(f'CURRENT PATH: {current_path}')
    print(f'CURRENT ROOM: {current_room.name}')

    if current_room.id not in visited_rooms:
        initialize_room(current_room)

        for exit in current_room.get_exits():

            # check undiscovered:
            undiscovered_directions = [direction for (direction, room) in visited_rooms[current_room.id].items() if room == "?"]
            
            # update info
            visited_rooms[current_room.id][exit] = current_room.get_room_in_direction(exit).id

            print('moving ', exit)
            player.travel(exit)

            new_path = list(current_path)
            new_path.append(current_room.get_room_in_direction(exit))
            q.enqueue(new_path)
            traversal_path.append(exit)

            # print('moving ', exit)
            # player.travel(exit)




if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
    print(f'MAP: {visited_rooms}')
    print(f' TRAVERSAL: {traversal_path}')
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