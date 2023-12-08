import re
import math

files = open('day08/day8data.txt', 'r')
lines = files.readlines()

instructions = lines[0].strip()
direction_map = {}

starting_locations = []

for i in range(2, len(lines)):
    line = lines[i]
    start = line[0:3]
    left = line[7:10]
    right = line[12:15]

    direction_map[start] = (left, right)

    if start[2] == 'A':
        starting_locations.append(start)

steps = 0
steps_list = []

for starting_location in starting_locations:
    location = starting_location
    steps = 0

    while True:
        for i in range(len(instructions)):
            steps = steps + 1
            instruction = instructions[i]
            direction = direction_map[location]

            if instruction == 'L':
                location = direction[0]
            else:
                location = direction[1]

            if location[2] == 'Z':
                break

        if location[2] == 'Z':
            break

    steps_list.append(steps)

print(math.lcm(*steps_list))
