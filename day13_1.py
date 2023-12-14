from utils.input import get_input_list

patterns_input = get_input_list(13)
blocks = []
block = []

for line in patterns_input:
    if line == "":
        blocks.append(block.copy())
        print("saved", block)
        block.clear()
        continue
    block.append(line)
blocks.append(block)


def find_reflections(block: list, istart: int = 0, iplus: int = 0):
    i1 = istart - iplus
    i2 = istart + iplus + 1
    if i1 == len(block)-1:  # Ei voida aloittaa viimeiseltä riviltä
        return False
    if i1 < 0 or i2 >= len(block):  # Ollaan menty rajan yli, eli löytyi
        return True
    if not block[i1] == block[i2]:
        return False
    return find_reflections(block, istart, iplus+1)


def flip_block(block):
    flipped = []
    for x in range(len(block[0])):
        column = [i[x] for i in block]
        flipped.append("".join(column))
    return flipped


total_sum = 0

for block in blocks:
    found = False
    for i in range(len(block)):
        if find_reflections(block, i):
            found = True
            break
    if found:
        total_sum += (i+1)*100
    else:
        flipped_block = flip_block(block)
        for i in range(len(flipped_block)):
            if find_reflections(flipped_block, i):
                total_sum += i+1
                break

print(total_sum)
