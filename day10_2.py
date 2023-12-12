from utils.input import get_input_list
from utils.c_print import c_print
from collections import deque
import time

pipes = get_input_list(10)

alku = time.time()

# directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
# x,y
pipe_directions = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(-1, 0), (0, -1)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
    "*": [],
    "S": [(0, -1), (0, 1), (-1, 0), (1, 0)]
}


def create_spaces(pipes):
    map_with_spaces = []
    for i, row in enumerate(pipes):
        new_row = []
        for j, col in enumerate(row):
            new_row.append(col)
            new_row.append("*")
        map_with_spaces.append(new_row[:-1])
        map_with_spaces.append(["*" for x in range(len(pipes[0])*2)][:-1])

    for y, row in enumerate(map_with_spaces):
        for x, col in enumerate(row):
            if col not in pipe_directions:
                continue
            for direction in pipe_directions[col]:
                new_map_direction = (direction[0]*2, direction[1]*2)
                n_coord = can_move_direction(
                    (x, y), new_map_direction, map_with_spaces)
                if n_coord:
                    if can_move_neighbour(n_coord, direction, map_with_spaces):
                        # change the value between current and next
                        if map_with_spaces[y+direction[1]][x+direction[0]] != "*":
                            continue
                        if direction[0] == 0:
                            map_with_spaces[y+direction[1]
                                            ][x+direction[0]] = "|"
                        else:
                            map_with_spaces[y+direction[1]
                                            ][x+direction[0]] = "-"

    return map_with_spaces[:-1]


def can_move_neighbour(n_coord: tuple, direction: tuple, pipes) -> bool:
    n_symbol = pipes[n_coord[1]][n_coord[0]]
    if (-direction[0], -direction[1]) in pipe_directions[n_symbol]:
        return True
    return False


def can_move_direction(current_node: tuple, direction: tuple, pipes: list) -> tuple:
    n_coord = (current_node[0]+direction[0], current_node[1]+direction[1])
    if n_coord[0] > len(pipes[0])-1 or n_coord[0] < 0:
        return False
    if n_coord[1] > len(pipes)-1 or n_coord[1] < 0:
        return False
    return n_coord


def print_color_map(map):

    for y, row in enumerate(map):
        for x, col in enumerate(row):
            if (x, y) in inside:
                c_print(col, "GREEN")
            elif (x, y) in outside:
                c_print(col, "RED")
            else:
                c_print(col)
        print()


def find_start(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "S":
                return (x, y)


map_with_spaces = create_spaces(pipes)


start_pos = find_start(map_with_spaces)
next_nodes = deque()
next_nodes.append(start_pos)
main_loop = set()
main_loop.add(start_pos)

# print("start", start_pos)
# print("map", map_with_spaces)

# Check which nodes are part of the main loop

while next_nodes:
    c_coord = next_nodes.popleft()
    current_symbol = map_with_spaces[c_coord[1]][c_coord[0]]

    for direction in pipe_directions[current_symbol]:
        n_coord = can_move_direction(c_coord, direction, map_with_spaces)
        if not n_coord:
            continue
        if n_coord in main_loop:
            continue
        if n_coord:
            can_move = can_move_neighbour(n_coord, direction, map_with_spaces)
            if can_move:
                next_nodes.append(n_coord)
                main_loop.add(n_coord)


inside = set()
outside = set()
all_visited = set()

directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]


for y, row in enumerate(map_with_spaces):
    for x, col in enumerate(row):
        if (x, y) in all_visited or (x, y) in main_loop:
            continue
        next_nodes = deque()
        current_nodes_outside = False
        next_nodes.append((x, y))
        visited_nodes = set()
        all_visited.add((x, y))  # Lisätään kaikissa käytyuhin
        visited_nodes.add((x, y))  # Lisätään tämän kierroksen käytyihin

        # print_color_map(map_with_spaces)

        while next_nodes:
            c_coord = next_nodes.popleft()
            for direction in directions:  # Käydään kaikki 4 suuntaa
                n_coord = can_move_direction(
                    c_coord, direction, map_with_spaces)  # Jos suuntaan voi liikkua, saadaan sen noden coord
                if n_coord in main_loop:
                    continue
                if n_coord in all_visited:  # Jos on jo käyty siinä, katsotaan seuraava suunta
                    continue
                # Jos ei saatu kordinaattia tai se on ulkona olevissa, katsotaan seuraava suunta ja
                if not n_coord or n_coord in outside:
                    current_nodes_outside = True  # merkataan kaikki tämän kierroksen nodet ulkopuolisiksi
                    continue
                # Lisätään node seuraavaksi käytäviin
                next_nodes.append(n_coord)
                all_visited.add(n_coord)
                visited_nodes.add(n_coord)

        if current_nodes_outside:
            for node in visited_nodes:
                if map_with_spaces[node[1]][node[0]] not in main_loop:
                    if node[0] % 2 != 0 or node[1] % 2 != 0:
                        continue
                    outside.add(node)
        else:
            for node in visited_nodes:
                if map_with_spaces[node[1]][node[0]] not in main_loop:
                    if node[0] % 2 != 0 or node[1] % 2 != 0:
                        continue
                    inside.add(node)

        # print_color_map(map_with_spaces)


# for n in inside:
#     print(n)


# print_color_map(map_with_spaces)


answer = sum([1 for x in list(inside) if map_with_spaces[x[1]][x[0]] != "*"])

# print("main loop", main_loop)
# print(len(main_loop))

# print(inside)
print("aika", time.time() - alku)
print("VASTAUS", answer)
