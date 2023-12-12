from utils.input import get_input_list


data = get_input_list(9)

history = []
for line in data:
    history.append([int(x) for x in line.split()])


def print_pyramid(all_diffs):
    for i, d in enumerate(all_diffs):
        print(" "*i*2, end="")
        print(d)
    print()


a = 20
summa = 0
for history_line in history:
    differernces = history_line.copy()
    all_diffs = [history_line.copy()]

    while True:
        differernces = [
            differernces[i]-differernces[i-1]
            for i, line in enumerate(differernces)
            if i > 0
        ]
        all_diffs.append(differernces)
        if not any(differernces):
            break
    print_pyramid(all_diffs)

    all_diffs.reverse()
    this_sum = 0
    for i in range(len(all_diffs)):
        if i == 0:
            continue
        all_diffs[i].append(
            all_diffs[i][-1]+all_diffs[i-1][-1]
        )
    summa += all_diffs[-1][-1]
    print("summa", all_diffs[-1][-1])

    print()


print(summa)
