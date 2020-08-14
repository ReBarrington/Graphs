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

    try: 
        visited_rooms[current_room.id][direction_of_prev] = prev_room.id
    except:
        pass

    print(visited_rooms)

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
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


while len(room_graph) > len(visited_rooms):

    current_room = player.current_room
    print(f'CURRENT ROOM: {current_room.name}')

    if current_room.id not in visited_rooms:
        initialize_room(current_room)

    # check undiscovered:
    undiscovered_directions = [direction for (direction, room) in visited_rooms[current_room.id].items() if room == "?"]

    # True: follow undiscovered
    if len(undiscovered_directions) > 0:
        for direction in undiscovered_directions:

            visited_rooms[current_room.id][direction] = current_room.get_room_in_direction(direction).id
            print('moving ', direction)
            traversal_path.append(direction)

            prev_room = player.current_room
            if player.current_room.return_opposite_direction(exit) is not None:
                direction_of_prev = player.current_room.return_opposite_direction(exit)


            player.travel(direction)
            break

    # False. Room has been visited and explored in all directions:
    else:
        print('Room has been visited and explored in all directions ')
        direction_of_last_room = current_room.return_opposite_direction(traversal_path[-1])
        print(direction_of_last_room, ' is direction of last room')
        traversal_path.append(direction_of_last_room)

        prev_room = player.current_room
        if player.current_room.return_opposite_direction(exit) is not None:
            direction_of_prev = player.current_room.return_opposite_direction(exit)

        player.travel(direction_of_last_room) 
        break

    print(traversal_path, ' is traversal path')
    print(visited_rooms, ' is visited rooms')
    
        # print(q.queue, ' is queue')
        # print(traversal_path, ' is traversal path')



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