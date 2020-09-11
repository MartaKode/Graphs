from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk ---------> Needs our work DFT or DFS???? Do we need a path?
# traversal_path = ['n', 'n']
traversal_path = []


def dft(starting_room):

    opposite_directions = {
        's':'n',
        'n':'s',
        'e':'w',
        'w':'e'
        }
    # keep track of main path
    path = []
    # hash current room as key and exits as values
    rooms = {}
    # travel through 1 path and keep track of how we got there(store the reverse directions)
    backup_path = []

    # initiate starting room with its exits
    # rooms[player.current_room.id] = player.current_room.get_exits()
    # while we havent visited all the rooms, we must travel
    while len(rooms) < len(room_graph) - 1:

        # if room was not visited
        if player.current_room.id not in rooms:
            # add current room to rooms with all available exits
            rooms[player.current_room.id] = player.current_room.get_exits()
            #  get rid of the direction we just traveled if we already traveled (backup path wont be empty if we just traveled)
            if len(backup_path):
                # we want to remove the inverse of what we just traveled so we dont accidentally start going backwards (move only towards unexplored directions/rooms)
                inverse_direction = backup_path[-1]
                # print(inverse_direction)
                rooms[player.current_room.id].remove(inverse_direction)


        # print(rooms)

        # if we get to a room with no exits, we need to travel backwards(backup to a room with possible exits to use)
        while not len(rooms[player.current_room.id]):
            if len(backup_path):
                # the last direction in backup path is first backing move 
                backing_direction = backup_path.pop() 
                # main path needs to keep track of backing up
                path.append(backing_direction)
                #  travel backwards and repeat until we get to a room with at least 1 exit
                player.travel(backing_direction)
                # print(backup_path)
            # if backup path is empty, we must've traveled all the rooms, STOP
            else:
                break

        # travel to first available exit:
        # remove one of the exit options from current room (that will be our next move)
        next_direction = rooms[player.current_room.id].pop()

        # add the move to main path and the inverse to backup path
        path.append(next_direction)
        backup_path.append(opposite_directions[next_direction])

        # travel to the next direction and start over until we travel all the rooms
        player.travel(next_direction)
        
    return path
                    

# print(dft(player.current_room)) 
traversal_path = dft(player.current_room)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

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


# def get_neighbors(current_room, exits):
#     neighbors = []

#     neighbor_dir = {}

#     neighbor_dir[current_room.id] = set()

#     for direction in exits:
#         neighbors.append(current_room.get_room_in_direction(direction)) 

#         neighbor_dir[current_room.id].add((direction, current_room.get_room_in_direction(direction).id))
#     return [neighbors, neighbor_dir]

# 🍝

    # rooms[starting_room.id] = set()
    # neighbors = {}
    # for direction in starting_room.get_exits():
    #     neighbors[direction] = starting_room.get_room_in_direction(direction).id
    #     # rooms[0].add((direction, starting_room.get_room_in_direction(direction).id))
    # rooms[starting_room.id] = neighbors



# # # Create a queue to hold rooms to visit
#     # to_visit = Queue()

# 	# # Create a set to hold visited rooms
#     # visited = set()

# 	# # Initalize: add the initial room to the queue
#     # to_visit.enqueue([random.choice(initial_room.get_exits())])

#     # # While queue not empty:
#     # while to_visit.size() > 0:
# 	# 	# dequeue first entry -> current room
#     #     current_path = to_visit.dequeue()
#     #     print(current_path)
#     #     direction = current_path[-1]

#     #     current_room = initial_room.get_room_in_direction(direction)

# 	# 	# if current room is not visited:
#     #     if current_room.id not in visited:
# 	# 		# Add it to the visited set
#     #         visited.add(current_room.id)

#     #         # # enqueue all its neighbors exits
#     #         # for neighbor in get_neighbors(current_room, current_room.get_exits()):
#     #         #     to_visit.enqueue(neighbor)
#     #         #     path.append(neighbor.id)
#     #         for exit in current_room.get_exits():
#     #             new_path = current_path[:]
#     #             new_path.append(exit)
#     #             to_visit.enqueue(new_path)

#     # return visited, current_path

#     # Create a stack to hold rooms to visit
#     to_visit = Stack()
#     # Create a set to hold visited rooms
#     visited = []
#     # Initalize: add the starting room to the queue
#     to_visit.push(starting_room)
#     # While stacl not empty:
#     while to_visit.size() > 0:
#         # pop first entry
#         v = to_visit.pop()
#         # if not visited:
#         if v.id not in visited:
#             # Add it to the visited set
#             visited.append(v.id)
#             # enqueue all its neighbors
#             for n in get_neighbors(v, v.get_exits())[0]:
#                 to_visit.push(n)
#                 # print(get_neighbors(v, v.get_exits())[1])
#         # Dictionary of exits
