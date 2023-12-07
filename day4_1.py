from utils.input import get_input_list

cards = get_input_list(4)

summa = 0

for card in cards:
    _, content = card.split(":")
    winning_numbers, my_numbers = content.split("|")
    winning_numbers = winning_numbers.strip().split()
    my_numbers = my_numbers.strip().split()

    count = 0
    for my_number in my_numbers:
        if my_number in winning_numbers:
            count += 1

    summa += (2**count)//2

print(summa)
