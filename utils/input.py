def get_input_list(day: int, variant: int = 0) -> list:
    path = f"inputs/day{day}.txt"
    if variant:
        path = f"inputs/day{day}_{variant}.txt"
    with open(path, "r") as file:
        data = [line.rstrip("\n") for line in file.readlines()]
    return data

def get_input_string(day: int, variant: int = 0) -> list:
    path = f"inputs/day{day}.txt"
    if variant:
        path = f"inputs/day{day}_{variant}.txt"
    with open(path, "r") as file:
        data = [x.rstrip("\n") for x in file.readlines()]
    return data
