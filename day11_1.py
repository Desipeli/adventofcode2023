from utils.input import get_input_list

image = get_input_list(11)

expanded_lines = []

for y, line in enumerate(image):
    expanded_lines.append([x for x in line])
    if "#" not in line:
        expanded_lines.append(["." for x in range(len(line))])

expanded_cols = []

for x in range(len(expanded_lines[0])):
    column = [i[x] for i in expanded_lines]
    expanded_cols.append(column)
    if "#" not in column:
        expanded_cols.append(["." for x in range(len(column))])

expanded_image = []

for x in range(len(expanded_cols[0])):
    column = [i[x] for i in expanded_cols]
    expanded_image.append(column)

locations = []

for y, row in enumerate(expanded_image):
    for x, col in enumerate(row):
        if col == "#":
            locations.append((x, y))

locations.sort(key=lambda x: (x[1], x[0]))

print("locations", locations)

total_sum = 0

for i, loc in enumerate(locations):
    for j in range(i+1, len(locations)):
        x_diff = abs(locations[j][0] - loc[0])
        y_diff = abs(locations[j][1] - loc[1])
        local_sum = x_diff+y_diff
        total_sum += local_sum

print(total_sum)
