from utils.input import get_input_list

data = get_input_list(6)

races = []

times, dist = data[0], data[1]

times = times.split(":")[1].split()
dist = dist.split(":")[1].split()

for i in range(len(times)):
    races.append((int(times[i]), int(dist[i])))

print(races)

margin = 1

for race in races:
    beatable = False
    for i in range(1, (race[0] // 2)+1):
        if (race[0]-i)*i > race[1]:
            beatable = True
            break
    if not beatable:
        continue
    new_margin = (race[0] // 2) - (i-1)
    new_margin += new_margin - (not (race[0] % 2))
    margin *= new_margin


print(margin)
