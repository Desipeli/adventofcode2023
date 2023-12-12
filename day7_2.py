from utils.input import get_input_list

data = get_input_list(7)

hands = [(x.split()[0], x.split()[1]) for x in data]

cards = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "J": 1,
}

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

max_comparison_value = 141414141400

# (hand, bid, strength, comparison_value)
valued_hands = []


def get_card_count(hand):
    hand_dict = {}
    for card in hand:
        if card not in hand_dict:
            hand_dict[card] = 0
        hand_dict[card] += 1
    return hand_dict


def translate_jokers(hand):
    cards = get_card_count(hand)
    # most cards
    card_count_sorted = sorted(
        [
            (x, cards[x])
            for x in cards
        ], key=lambda x: x[1])
    most_common_card = "J"
    most_common_card = card_count_sorted[-1][0]
    if most_common_card == "J":
        if len(card_count_sorted) > 1:
            most_common_card = card_count_sorted[-2][0]
        else:
            most_common_card = "A"

    jokers_replaced = ""
    for card in hand:
        if card != "J":
            jokers_replaced += card
        else:
            jokers_replaced += most_common_card
    return jokers_replaced


def get_type(hand, bid, hand_dict, comparison_value):
    print("GET TYPE, hand", hand)
    type_strength = 0
    if len(hand_dict) == 1:  # five of a kind
        type_strength = FIVE_OF_A_KIND
    elif len(hand_dict) == 2:  # four or full house
        if 2 in list(hand_dict.values()):  # full house
            type_strength = FULL_HOUSE
        else:
            type_strength = FOUR_OF_A_KIND
    elif len(hand_dict) == 3:  # three of a kind or two pair
        three = False
        for value in hand_dict.values():
            if value == 3:  # three of a kind
                type_strength = THREE_OF_A_KIND
                three = True
                break
        if not three:
            type_strength = TWO_PAIR
    elif len(hand_dict) == 4:  # one pair
        type_strength = ONE_PAIR
    else:
        type_strength = HIGH_CARD
    print("TYPE IS", type_strength)
    return (hand, int(bid), comparison_value +
            (type_strength*max_comparison_value))


for hand, bid in [hand for hand in hands]:
    # strength
    comparison_value = 0
    hand_dict = {}
    for i, card in enumerate(hand):
        value = 0
        if card in cards:
            value = cards[card]
        else:
            value = int(card)
        comparison_multiplier = 100**(len(hand)-i)
        comparison_value += value * comparison_multiplier
        if card not in hand_dict:
            hand_dict[card] = 0
        hand_dict[card] += 1

    translated_hand = translate_jokers(hand)
    card_count = get_card_count(translated_hand)
    valued_hands.append(get_type(translated_hand, bid,
                        card_count, comparison_value))

valued_hands.sort(key=lambda x: x[2])

winnings = 0
for i, card in enumerate(valued_hands):
    winnings += (i+1)*card[1]

for h in valued_hands:
    print(h)
print(winnings)
