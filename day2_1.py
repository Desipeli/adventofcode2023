from utils.input import get_input_list

games = get_input_list(2)

index = 1

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

summa = 0

for line in games:
    game, rounds = line.split(":")
    rounds = rounds.split(";")
    # print(game, end="\n")
    possible = True
    for round in rounds:
        cubes = round.split(",")
        for single_color_cubes in cubes:
            count, color = single_color_cubes.strip().split(" ")
            count = int(count)

            if max_cubes[color] < count:
                possible = False
                break
        if not possible:
            break
    if possible:
        summa += index
    index += 1

print(summa)
