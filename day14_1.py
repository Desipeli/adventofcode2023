from utils.input import get_input_list

rocks = get_input_list(14)


last_free_row = 0

total_load = 0

# sarakkeet läpi
for col in range(len(rocks[0])):
    for row in range(len(rocks)):
        symbol = rocks[row][col]
        if symbol == "#":
            last_free_row = row + 1
        if symbol == "O":
            new_pos = min(last_free_row, row)
            total_load += len(rocks) - new_pos
            last_free_row = new_pos + 1
    last_free_row = 0


print(total_load)
