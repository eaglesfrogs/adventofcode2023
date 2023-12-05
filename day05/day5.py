import re


files = open('day05/day5data.txt', 'r')
lines = files.readlines()


class Day5Map:

    def __init__(self, dest, source, range) -> None:
        self.dest = dest
        self.source = source
        self.source_max = source + range
        self.range = range

    def get_dest(self, source):
        pass

seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temp = []
temp_to_humidity = []
humidity_to_location = []

for line in lines:
    if line.startswith("seeds"):
