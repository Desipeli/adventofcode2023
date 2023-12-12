from utils.input import get_input_list
from utils.c_print import c_print

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


def get_combinations(springs: str, numbers: list):
    springs = springs.strip(".")
    if len(numbers) == 0 and "#" not in springs:  # kaikki sijoitettu
        return 1
    if len(springs) == 0 or len(numbers) == 0:
        return 0
    number = numbers[0]

    combinations = 0
    for i in range(len(springs)):
        s = springs[i:]
        next_string = get_next_string(s, number)
        if next_string != False:
            combinations += get_combinations(next_string, numbers[1:])
        if s[0] == "#":  # "#" ei voi jäädä vasemmalle puolelle
            break

    return combinations


combinations = 0
for springs_numbers in spring_map:
    springs, numbers = springs_numbers.split()
    numbers = [int(x) for x in numbers.split(",")]
    # print(springs, numbers)
    combinations += get_combinations(springs, numbers)
print(combinations)

# print(get_combinations("###????????", [3, 2, 1]))
# print(get_next_string("??#", 1))

# print(get_next_string("#", 1))
# print(get_combinations("?????###", [3]))
