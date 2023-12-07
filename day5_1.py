from utils.input import get_input_list

almanac = get_input_list(5)


seeds = [int(s) for s in almanac[0].split(":")[1].split()]


def get_mapped_values(original_values: list, mappings: list) -> list:
    new_values = []
    for value in original_values:
        found = False
        for mapping in mappings:
            if value >= mapping[1] and value < mapping[1] + mapping[2]:
                diff = value-mapping[1]
                new_value = mapping[0] + diff
                new_values.append(new_value)
                found = True
                break
        if not found:
            new_values.append(value)
    return new_values


current_values = seeds.copy()
collect_values = False
current_mappings = []

for index, line in enumerate(almanac[1:]):
    if ":" in line:
        collect_values = True
        continue
    if line == "" or index == len(almanac)-2:
        current_values = get_mapped_values(current_values, current_mappings)
        collect_values = False
        current_mappings.clear()
        continue
    if collect_values:
        current_mappings.append([int(v) for v in line.split()])
        continue

print(current_values)
smallest = current_values[0]
smallest_index = 0
for index, value in enumerate(current_values):
    if value < smallest:
        smallest = value
        smallest_index = index

print("Smallest location", smallest)
print("smallest index", smallest_index)
print("smallest seed", seeds[smallest_index])
