from utils.input import get_input_list

games = get_input_list(2)

summa = 0

for line in games:
    game, rounds = line.split(":")
    rounds = rounds.split(";")
    # print(game, end="\n")

    colors = {"red": 0, "blue": 0, "green": 0}

    for round in rounds:
        cubes = round.split(",")
        for single_color_cubes in cubes:
            count, color = single_color_cubes.strip().split(" ")
            count = int(count)
            if colors[color] < count:
                colors[color] = count

    power = 1
    for value in colors.values():
        power *= value
    summa += power

print(summa)
