from utils.input import get_input_list

cards = get_input_list(4)

summa = 0

collected_cards = {}

for i in range(len(cards)):
    collected_cards[i] = 1

for card_number, card in enumerate(cards):
    _, content = card.split(":")

    winning_numbers, my_numbers = content.split("|")
    winning_numbers = winning_numbers.strip().split()
    my_numbers = my_numbers.strip().split()

    count = 0

    for my_number in my_numbers:
        if my_number not in winning_numbers:
            continue
        count += 1

        collected_cards[card_number + count] += collected_cards[card_number]


print(sum(collected_cards.values()))
