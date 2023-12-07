import time
from utils.input import get_input_list


almanac = get_input_list(5) + [""]

seed_ranges = [int(s) for s in almanac[0].split(":")[1].split()]

levels = []

collected_values = []


def get_values_from_almanac(almanac):
    for line in almanac[2:]:
        if ":" in line:
            continue
        if line == "":
            values = collected_values.copy()
            values.sort()
            levels.append(values)
            collected_values.clear()
            continue
        collected_values.append([int(v) for v in line.split()])

    return levels


def find_next_value(levels: list, level_index: int, value: int):
    new_value = value
    for level in levels[level_index]:
        if value >= level[0] and value < level[0]+level[2]:
            new_value = level[1] + value - level[0]
    return new_value


def is_value_in_seeds(value, seed_ranges):
    for i, s in enumerate(seed_ranges):
        if i % 2 == 0:
            continue
        if value >= seed_ranges[i-1] and value < s + seed_ranges[i-1]:
            return True
    return False


smallest_location = None

levels = get_values_from_almanac(almanac)

seed_range_tuples = []
for i, v in enumerate(seed_ranges):
    if i % 2 != 0:
        seed_range_tuples.append((seed_ranges[i-1], v))

seed_range_tuples.sort()

levels.reverse()

start = time.time()

for i in range(1000_000_000):
    if i % 10000 == 0:
        print(i)
    value = i
    for j in range(len(levels)):
        value = find_next_value(levels, j, value)

    if is_value_in_seeds(value, seed_ranges):
        smallest_location = i
        print("TÄÄ", value)
        break

print("##########################")
print("Vastaus", smallest_location)
print("##########################")

print("duration", time.time() - start)
