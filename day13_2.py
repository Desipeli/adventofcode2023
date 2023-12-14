from utils.input import get_input_list

patterns_input = get_input_list(13)
blocks = []
block = []

for line in patterns_input:
    if line == "":
        blocks.append(block.copy())
        block.clear()
        continue
    block.append(line)
blocks.append(block)


def find_reflections(block: list, istart: int = 0, iplus: int = 0, smudge: bool = False):
    i1 = istart - iplus
    i2 = istart + iplus + 1
    if i1 == len(block)-1:  # Ei voida aloittaa viimeiseltä riviltä
        return False
    if i1 < 0 or i2 >= len(block):  # Ollaan menty rajan yli, eli löytyi
        return smudge
    if not block[i1] == block[i2]:
        if sum([1 for x in range(len(block[i1])) if block[i1][x] != block[i2][x]]) == 1:
            print("YHDEN ERO")
            print(block[i1], i1)
            print(block[i2], i2)
            print()
            if smudge:
                return False
            else:
                smudge = True
        else:
            return False
    return find_reflections(block, istart, iplus+1, smudge)


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
            print("I", i)
            total_sum += (i+1)*100
            found = True
            break
    if found:
        continue
    flipped_block = flip_block(block)
    for i in range(len(flipped_block)):
        if find_reflections(flipped_block, i):
            total_sum += i+1
            break

print(total_sum)


# block = [
#     "12345",
#     "12345",
#     "12345",
#     "12345"
# ]

# for b in block:
#     print(b)
# print()

# for b in flip_block(block):
#     print(b)
# print()

# c = list(zip(*block))

# for b in c:
#     print(b)
# print()
