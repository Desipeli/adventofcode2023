from utils.input import get_input_list

data = get_input_list(6)

times, dist = data[0], data[1]

times = times.split(":")[1].split()
dist = dist.split(":")[1].split()

time = int("".join(times))
dist = int("".join(dist))

margin = 0

beatable = False
for i in range(1, (time // 2)+1):
    if (time-i)*i > dist:
        beatable = True
        break
if beatable:
    margin = (time // 2) - (i-1)
    margin += margin - (not (time % 2))

print(margin)
