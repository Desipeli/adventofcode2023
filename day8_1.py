from utils.input import get_input_list

data = get_input_list(8)

instructions = data[0]
routes = {}

for rl in data[2:]:
    start, options = rl.split("=")
    start = start.strip()
    left, right = options[2:-1].split(",")
    right = right.strip()
    routes[start] = (left, right)

steps = 0
next_node = "AAA"

direction = {
    "L": 0,
    "R": 1,
}

while True:
    instruction_number = steps % len(instructions)
    instruction = instructions[instruction_number]
    # print(steps, instruction)
    next_node = routes[next_node][direction[instruction]]
    # print("next_node", next_node)
    steps += 1
    if next_node == "ZZZ":
        break
print(steps)
