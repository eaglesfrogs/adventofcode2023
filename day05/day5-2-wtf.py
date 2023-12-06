import re
import pandas as pd


files = open('day05/day5data.txt', 'r')
lines = files.readlines()


class Day5Map:

    def __init__(self, dest, source, range) -> None:
        self.dest = dest
        self.source = source
        self.source_max = source + range
        self.source_interval = pd.Interval(self.source, self.source_max, closed='both')
        self.range = range

    def get_dest(self, item):
        if item >= self.source and item < self.source_max:
            offset = item - self.source
            return self.dest + offset

        return -1

    def get_overlap(self, start, end):
        incoming_interval = pd.Interval(start, end, closed='both')
        if not self.source_interval.overlaps(incoming_interval):
            return False

        overlap_start = max(start, self.source)
        overlap_end = min(end, self.source_max)

        return {
            'overlap_start': overlap_start,
            'overlap_end': overlap_end,
            'dest_start': self.dest + overlap_start - self.source,
            'dest_end': self.dest + overlap_end - self.source
        }

seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temp = []
temp_to_humidity = []
humidity_to_location = []

current_list = None

for line in lines:
    if line.strip() == '':
        continue

    if line.startswith("seeds"):
        seeds_txt = re.findall(r'[0-9]+', line)
        for seed in seeds_txt:
            seeds.append(int(seed))
    elif 'seed-to-soil' in line:
        current_list = seed_to_soil
    elif 'soil-to-fertilizer' in line:
        current_list = soil_to_fertilizer
    elif 'fertilizer-to-water' in line:
        current_list = fertilizer_to_water
    elif 'water-to-light' in line:
        current_list = water_to_light
    elif 'light-to-temperature' in line:
        current_list = light_to_temp
    elif 'temperature-to-humidity' in line:
        current_list = temp_to_humidity
    elif 'humidity-to-location' in line:
        current_list = humidity_to_location
    else:
        seeds_txt = re.findall(r'[0-9]+', line)
        day_5_map = Day5Map(
            int(seeds_txt[0]),
            int(seeds_txt[1]),
            int(seeds_txt[2])
        )

        current_list.append(day_5_map)

lowest = 9999999999

for i in range(0, len(seeds), 2):
    seed_start = seeds[i]
    seed_end = seed_start + seeds[i+1]

    seed = [(seed_start, seed_end)]

    soil = []
    while(seed):
        found = False
        j = seed.pop()

        for s in seed_to_soil:
            overlap = s.get_overlap(j[0], j[1])
            if overlap:
                found=True
                soil.append((overlap['dest_start'], overlap['dest_end']))
                if j[0] < overlap['overlap_start']:
                    seed.append((j[0], overlap['overlap_start']-1))
                if j[1] > overlap['overlap_end']:
                    seed.append((overlap['overlap_end']+1, j[1]))

                break

        if not found:
            soil.append(j)

    fertilizer = []
    while(soil):
        found = False
        j = soil.pop()

        for s in soil_to_fertilizer:
            overlap = s.get_overlap(j[0], j[1])
            if overlap:
                found=True
                fertilizer.append((overlap['dest_start'], overlap['dest_end']))
                if j[0] < overlap['overlap_start']:
                    soil.append((j[0], overlap['overlap_start']-1))
                if j[1] > overlap['overlap_end']:
                    soil.append((overlap['overlap_end']+1, j[1]))

                break

        if not found:
            fertilizer.append(j)

    water = []
    while(fertilizer):
        found = False
        j = fertilizer.pop()

        for s in fertilizer_to_water:
            overlap = s.get_overlap(j[0], j[1])
            if overlap:
                found=True
                water.append((overlap['dest_start'], overlap['dest_end']))
                if j[0] < overlap['overlap_start']:
                    fertilizer.append((j[0], overlap['overlap_start']-1))
                if j[1] > overlap['overlap_end']:
                    fertilizer.append((overlap['overlap_end']+1, j[1]))

                break

        if not found:
            water.append(j)

    light = []
    while(water):
        found = False
        j = water.pop()

        for s in water_to_light:
            overlap = s.get_overlap(j[0], j[1])
            if overlap:
                found=True
                light.append((overlap['dest_start'], overlap['dest_end']))
                if j[0] < overlap['overlap_start']:
                    water.append((j[0], overlap['overlap_start']-1))
                if j[1] > overlap['overlap_end']:
                    water.append((overlap['overlap_end']+1, j[1]))

                break

        if not found:
            light.append(j)

    temp = []
    while(light):
        found = False
        j = light.pop()

        for s in light_to_temp:
            overlap = s.get_overlap(j[0], j[1])
            if overlap:
                found=True
                temp.append((overlap['dest_start'], overlap['dest_end']))
                if j[0] < overlap['overlap_start']:
                    light.append((j[0], overlap['overlap_start']-1))
                if j[1] > overlap['overlap_end']:
                    light.append((overlap['overlap_end']+1, j[1]))

                break

        if not found:
            temp.append(j)

    humidity = []
    while(temp):
        found = False
        j = temp.pop()

        for s in temp_to_humidity:
            overlap = s.get_overlap(j[0], j[1])
            if overlap:
                found=True
                humidity.append((overlap['dest_start'], overlap['dest_end']))
                if j[0] < overlap['overlap_start']:
                    temp.append((j[0], overlap['overlap_start']-1))
                if j[1] > overlap['overlap_end']:
                    temp.append((overlap['overlap_end']+1, j[1]))

                break

        if not found:
            humidity.append(j)

    location = []
    while(humidity):
        found = False
        j = humidity.pop()

        for s in humidity_to_location:
            overlap = s.get_overlap(j[0], j[1])
            if overlap:
                found=True
                location.append((overlap['dest_start'], overlap['dest_end']))
                if j[0] < overlap['overlap_start']:
                    humidity.append((j[0], overlap['overlap_start']-1))
                if j[1] > overlap['overlap_end']:
                    humidity.append((overlap['overlap_end']+1, j[1]))

                break

        if not found:
            location.append(j)

    for l in location:
        if l[0] < lowest:
            lowest = l[0]

print(f"Answer 2 is {lowest}")
