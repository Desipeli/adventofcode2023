from utils.input import get_input_list

engine = get_input_list(3)

digits = "0123456789"

summa = 0

cords = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),            (1, 0),
    (-1, 1), (0, 1), (1, 1)
]

for line_number, line in enumerate(engine):

    number = ""
    adjacent = False
    for index, char in enumerate(line):
        if char in digits:
            number += char
            for cord in cords:
                x = cord[0]
                y = cord[1]
                pos_x = index + x
                if pos_x < 0 or pos_x >= len(engine[0]):
                    continue
                pos_y = line_number + y
                if pos_y < 0 or pos_y >= len(engine):
                    continue
                what_is_this = engine[pos_y][pos_x]
                if what_is_this not in digits and what_is_this != ".":
                    adjacent = True
                    break

        else:
            if adjacent:
                summa += int(number)
            number = ""
            adjacent = False

    if adjacent:
        summa += int(number)

print(summa)
