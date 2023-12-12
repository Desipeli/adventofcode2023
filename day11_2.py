from utils.input import get_input_list
from utils.c_print import c_print
import time

image = get_input_list(11)

expanded_lines = [y for y, line in enumerate(image) if "#" not in line]
expanded_cols = [
    x for x in range(len(image[0]))
    if "#" not in [i[x] for i in image]
]

EXPANSE = 1000_000

locations = []
for y, row in enumerate(image):
    for x, col in enumerate(row):
        if col == "#":
            locations.append((x, y))


total_sum = 0

alku = time.time()

for i, loc in enumerate(locations):
    for j in range(i+1, len(locations)):
        x_diff = abs(locations[j][0] - loc[0])
        y_diff = abs(locations[j][1] - loc[1])
        local_sum = x_diff+y_diff

        # expanse

        for e_col in expanded_cols:
            if e_col > min(loc[0], locations[j][0]) and e_col < max(loc[0], locations[j][0]):
                total_sum += EXPANSE-1

        for e_row in expanded_lines:
            if e_row > min(loc[1], locations[j][1]) and e_row < max(loc[1], locations[j][1]):
                total_sum += EXPANSE-1

        total_sum += local_sum


def print_color_expanded(image, e_lines, e_cols):
    for y in range(len(image)):
        for x in range(len(image[y])):
            color = None
            if x in e_cols or y in e_lines:
                color = "GREEN"
            else:
                color = "RED"
            c_print(image[y][x], color)
        print()


loppu = time.time()-alku

print("lines", expanded_lines)
print("cols", expanded_cols)
print_color_expanded(image, expanded_lines, expanded_cols)
print("answer:", total_sum)
print(loppu)
