from utils.input import get_input_list
from utils.c_print import c_print
import time

spring_map = get_input_list(12)


def get_next_string(springs: str, number: int):
    """
    returns:
        str: fits
        False: Does not fit
    """
    if len(springs) == 0 and number:
        return False
    if "." in springs[:number]:
        return False
    if len(springs) < number:
        return False
    if len(springs) > number:
        # Seuraava on #, joten ei mahdolilinen
        if springs[number] == "#":
            return False
        if springs[number] == "?":
            return springs[number+1:]

    return springs[number:]


def get_combinations(springs: str, numbers: list, memo: dict):
    springs = springs.strip(".")
    if len(numbers) == 0 and "#" not in springs:  # kaikki sijoitettu
        return 1
    if len(springs) == 0 or len(numbers) == 0:
        return 0
    number = numbers[0]

    combinations = 0
    memo_key = springs+"".join([str(x) for x in numbers])
    if memo_key not in memo:
        for i in range(len(springs)):
            s = springs[i:]
            next_string = get_next_string(s, number)
            if next_string != False:
                c = get_combinations(
                    next_string,
                    numbers[1:], memo)
                combinations += c

            if s[0] == "#":  # "#" ei voi jäädä vasemmalle puolelle
                break
        memo[memo_key] = combinations
    else:
        return memo[memo_key]
    return combinations


aika_alku = time.time()

unfolded_springs = []
for line in spring_map:
    conditions, groups = line.split()
    new_conditions = conditions
    new_groups = groups
    for i in range(4):
        new_conditions += "?"+conditions
        new_groups += ","+groups
    unfolded_springs.append((new_conditions, new_groups))

aika_unfoldattu = time.time()

combinations = 0
for springs_numbers in unfolded_springs:
    memo = {}  # key=str, value: int esim ("????11": 3)
    springs, numbers = springs_numbers
    numbers = [int(x) for x in numbers.split(",")]
    combinations += get_combinations(springs, numbers, memo)

aika_loppu = time.time()
c_print(f"Vastaus: {combinations}", "RED", end="\n")
c_print(f"unfoldaus: {aika_unfoldattu-aika_alku}", "BLUE", end="\n")
c_print(f"koko aika: {aika_loppu-aika_alku}", "GREEN", end="\n")
