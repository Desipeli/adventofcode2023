from utils.input import get_input_list
from math import lcm

data = get_input_list(8)

instructions = data[0]
routes = {}

for rl in data[2:]:
    start, options = rl.split("=")
    start = start.strip()
    left, right = options[2:-1].split(",")
    right = right.strip()
    routes[start] = (left, right)

next_node = "AAA"

direction = {
    "L": 0,
    "R": 1,
}


current_nodes = []

for node in routes:
    if node[-1] == "A":
        current_nodes.append(node)

print(current_nodes)

node_steps = {}

steps = 0
while True:
    instruction_number = steps % len(instructions)
    instruction = instructions[instruction_number]

    all_finished = True
    new_nodes = []
    for node in current_nodes:
        next_node = routes[node][direction[instruction]]
        # print("previious", node, "next", next_node)
        if next_node[-1] != "Z":
            all_finished = False
        new_nodes.append(next_node)

    current_nodes = new_nodes

    steps += 1

    for i, node in enumerate(new_nodes):
        if node[-1] == "Z":
            # print("TÄÄ", i, node, steps % len(instructions))
            if node not in node_steps:
                node_steps[node] = steps

            # print()

    if all_finished or len(node_steps) == len(current_nodes):
        break

print(steps)
print("node_steps", node_steps)
print("instruction lenght", len(instructions))
answer = 1
for found_steps in node_steps.values():
    answer *= found_steps

print("answer:", answer)
print("smallest answer", lcm(*node_steps.values()))
