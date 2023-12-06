import re


files = open('day05/day5data.txt', 'r')
lines = files.readlines()


class Day5Map:

    def __init__(self, dest, source, range) -> None:
        self.dest = dest
        self.source = source
        self.source_max = source + range
        self.range = range

    def get_dest(self, item):
        if item >= self.source and item < self.source_max:
            offset = item - self.source
            return self.dest + offset

        return -1

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

for seed in seeds:
    soil = -1
    for s in seed_to_soil:
        soil = s.get_dest(seed)
        if soil > -1: break

    if soil == -1:
        soil = seed

    fertilizer = -1
    for s in soil_to_fertilizer:
        fertilizer = s.get_dest(soil)
        if fertilizer > -1: break

    if fertilizer == -1:
        fertilizer = soil

    water = -1
    for s in fertilizer_to_water:
        water = s.get_dest(fertilizer)
        if water > -1: break

    if water == -1:
        water = fertilizer

    light = -1
    for s in water_to_light:
        light = s.get_dest(water)
        if light > -1: break

    if light == -1:
        light = water

    temp = -1
    for s in light_to_temp:
        temp = s.get_dest(light)
        if temp > -1: break

    if temp == -1:
        temp = light

    humidity = -1
    for s in temp_to_humidity:
        humidity = s.get_dest(temp)
        if humidity > -1: break

    if humidity == -1:
        humidity = temp

    location = -1
    for s in humidity_to_location:
        location = s.get_dest(humidity)
        if location > -1: break

    if location == -1:
        location = humidity

    if location < lowest:
        lowest = location

print(f"Answer 1 is {lowest}")
