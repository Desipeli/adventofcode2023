from utils.input import get_input_list

engine = get_input_list(3)

digits = "0123456789"

summa = 0

cords = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),            (1, 0),
    (-1, 1), (0, 1), (1, 1)
]


def get_leftmost_number_x(start_x, y, engine):
    x = start_x
    while True:
        if x - 1 < 0:
            break
        if engine[y][x-1] not in digits:
            break
        x -= 1
    return x


def collect_numbers(start_x, y, engine, visited):
    x = start_x
    number = ""
    while True:
        if x >= len(engine[0]):
            break
        visited.append((x, y))
        if engine[y][x] in digits:
            number += engine[y][x]
        else:
            break
        x += 1
    return int(number)


for line_number, line in enumerate(engine):
    for index, char in enumerate(line):
        if char != "*":
            continue
        visited_cords = []
        adjacent_numbers = []
        for cord in cords:
            rel_x = cord[0]
            rel_y = cord[1]
            abs_cord_x = index + rel_x
            if abs_cord_x < 0 or abs_cord_x >= len(engine[0]):
                continue
            abs_cord_y = line_number + rel_y
            if abs_cord_y < 0 or abs_cord_y >= len(engine):
                continue

            if (abs_cord_x, abs_cord_y) in visited_cords:
                continue
            if engine[abs_cord_y][abs_cord_x] not in digits:
                continue

            number = ""
            leftest_number_x = get_leftmost_number_x(
                abs_cord_x, abs_cord_y, engine)

            number = collect_numbers(
                leftest_number_x, abs_cord_y, engine, visited_cords)

            if number:
                adjacent_numbers.append(number)
                number = ""

        if len(adjacent_numbers) == 2:
            summa += adjacent_numbers[0]*adjacent_numbers[1]


print(summa)
