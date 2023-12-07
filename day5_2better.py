from utils.input import get_input_list
import math
from time import time


almanac = get_input_list(5)

times = []

for i in range(1):

    koko_alku = time()

    seeds = [int(s) for s in almanac[0].split(":")[1].split()]

    seed_ranged = [
        (seeds[x-1], seeds[x])
        for x in range(len(seeds)) if x % 2 != 0
    ]

    map_list = []
    map = []

    for index, row in enumerate(almanac[2:]):
        if ":" in row:
            continue

        if row != "":
            map.append([int(x) for x in row.split()])

        if row == "" or index == len(almanac)-3:
            min_value = min([x[0] for x in map])
            if min_value > 0:
                map.append([0, 0, min_value])
            max_value = max(x[0]+x[2] for x in map)
            map.append([max_value, max_value, math.inf])

            map.sort(key=lambda x: x[0])
            map_list.append(map.copy())
            map.clear()
            continue

    map_list.reverse()

    def get_range(tuotu_alku, tuotu_range, taman_alku, taman_range):
        rang = min(
            min(
                tuotu_alku + tuotu_range-taman_alku,
                taman_alku + taman_range-tuotu_alku
            ),
            min(
                tuotu_range,
                taman_range
            )
        )
        return rang

    def sukellus(map_list: list, level: int, tuotu_kaista: list, seed_ranged: list, sukellukset) -> int:
        sukellukset.append((level, tuotu_kaista))

        if level == len(map_list):
            for seed_range in seed_ranged:
                if get_range(tuotu_kaista[0], tuotu_kaista[1], seed_range[0], seed_range[1]) > 0:
                    ero = max(tuotu_kaista[0] - seed_range[0], 0)
                    sukellukset.append((level, seed_range[0]+ero))
                    return seed_range[0]+ero
            return None
        if level == 0:
            for taman_tason_kaista in map_list[level]:
                muutos_lisa = taman_tason_kaista[0]-taman_tason_kaista[1]
                value = sukellus(
                    map_list, level+1,
                    [taman_tason_kaista[1], taman_tason_kaista[2]], seed_ranged, sukellukset)
                return value+muutos_lisa
        else:
            for taman_tason_kaista in map_list[level]:
                alku = max([tuotu_kaista[0], taman_tason_kaista[0]])
                rang = get_range(
                    tuotu_kaista[0], tuotu_kaista[1], taman_tason_kaista[0], taman_tason_kaista[2])
                if rang <= 0:
                    continue

                uusi_kaista = alku + \
                    (taman_tason_kaista[1]-taman_tason_kaista[0])

                value = sukellus(
                    map_list, level+1,
                    [uusi_kaista, rang], seed_ranged, sukellukset)

                if value:
                    sukellukset.append((level, value+(alku-uusi_kaista)))
                    return value+(alku-uusi_kaista)
        return None

    sukellukset = []

    vastaus = sukellus(map_list, 0, None, seed_ranged, sukellukset)

    print("vastaus", vastaus)
    loppu = time()
    times.append(loppu-koko_alku)
    # print(loppu-koko_alku)

average = sum(times)/len(times)
print("AVERAGE:", average)
print(vastaus)

just = 20

print(f'{"Location" : <{just}}{"Humidity" : <{just}}{"temperature" : <{just}}{"light" : <{just}}{"water" : <{just}}{"fertilizer" : <{just}}{"soil" : <{just}}')

index = 1
for s, kaista in sukellukset[1:]:

    content = f"{s}"
    oma_viiva = just*sukellukset[index][0]
    print(f'{content:<20}', end="")

    if s == 7:
        seuraavan_viiva = just*(sukellukset[index+1][0]-1)
        print()
        print(f'{"":\x20<{seuraavan_viiva}}', end="")
        if sukellukset[index-1][0] == 7:
            break
    index += 1
