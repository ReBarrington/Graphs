from room import Room
from player import Player
from world import World
from util import Stack

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
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
mapped_dict = dict()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

s = Stack()
s.push([player.current_room])

# for move in traversal_path:
while s.size() > 0:
# while len(room_graph) != len(visited_rooms):

    # let current_room be equal to q.dequeue
    current_path = s.pop()
    current_room = current_path[-1]

    print(f'CURRENT ROOM: {current_room.name}')

    for path in current_path:
        print(path.name, ' in current path')

    if current_room.name not in visited_rooms:
        initialize_room(current_room)

        # for exit in current_room.get_exits():

        # if "?" in mapped_dict[current_room.id].values():

        for direction, room in mapped_dict[current_room.id].items():

            if room == "?":

                print(f'undiscovered exits: {direction}')

                mapped_dict[current_room.id][direction] = current_room.get_room_in_direction(direction).id
                # print(' UPDATING INFO: ', mapped_dict)

                prev_room = player.current_room
                if player.current_room.return_opposite_direction(direction) is not None:
                    direction_of_prev = player.current_room.return_opposite_direction(direction)
                
                traversal_path.append(direction)
                new_path = list(current_path)
                new_path.append(current_room.get_room_in_direction(direction))
                s.push(new_path)
                print('moving ', direction)
                player.travel(direction)
                print("JUST MOVED TO: ", player.current_room.name)
                break
            continue




if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
    # print(f'VISITED ROOMS: {visited_rooms} ')
    print(f'traversal path: ', traversal_path)
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