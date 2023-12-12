from utils.input import get_input_list
from collections import deque

pipes = get_input_list(10, 1)

# directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
# x,y
node_directions = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(-1, 0), (0, -1)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
    "S": [(0, -1), (0, 1), (-1, 0), (1, 0)]
}


def find_start(pipes):
    for y in range(len(pipes)):
        for x in range(len(pipes[y])):
            if pipes[y][x] == "S":
                return (x, y)


def can_move_neighbour(n_coord, direction, pipes):
    n_symbol = pipes[n_coord[1]][n_coord[0]]
    if (-direction[0], -direction[1]) in node_directions[n_symbol]:
        return True
    return False


def can_move_direction(current_node, direction, pipes):
    n_coord = (current_node[0]+direction[0], current_node[1]+direction[1])
    if n_coord[0] > len(pipes[0]) or n_coord[0] < 0:
        return False
    if 0 > n_coord[1] > len(pipes) or n_coord[1] < 0:
        return False
    return n_coord


start_pos = find_start(pipes)

next_nodes = deque()
next_nodes.append(start_pos)
visited_nodes = {}
visited_nodes[start_pos] = 0


while next_nodes:

    c_coord = next_nodes.popleft()
    current_symbol = pipes[c_coord[1]][c_coord[0]]

    for direction in node_directions[current_symbol]:
        n_coord = can_move_direction(c_coord, direction, pipes)
        if not n_coord:
            continue
        if n_coord in visited_nodes:
            continue
        if n_coord:
            can_move = can_move_neighbour(n_coord, direction, pipes)
            if can_move:
                next_nodes.append(n_coord)
                visited_nodes[n_coord] = visited_nodes[c_coord] + 1


print("visited")
# for k, v in visited_nodes.items():
#     print(k, v)

print(list(visited_nodes.values())[-1])


def create_map(original, visited):
    new_map = []
    for y in original:
        new_map.append(["." for x in range(len(original[0]))])

    for k, v in visited.items():
        new_map[k[1]][k[0]] = v

    return new_map


for row in create_map(pipes, visited_nodes):
    for value in row:
        print(value, end="")
    print()

# can_move_direction()
