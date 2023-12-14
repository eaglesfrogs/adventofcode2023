# used tutorial to solve this one: https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day12p1.py

import re


def count_springs(pattern, counts):
    if pattern == '':
        if counts:
            return 0
        else:
            return 1

    if not counts:
        if '#' in pattern:
            return 0
        else:
            return 1

    c = 0

    if pattern[0] in '.?':
        c += count_springs(pattern[1:], counts)

    if pattern[0] in '#?':
        if counts[0] <= len(pattern) and '.' not in pattern[:counts[0]] and (counts[0] == len(pattern) or pattern[counts[0]] != '#'):
            c += count_springs(pattern[counts[0]+1:], counts[1:])

    return c


files = open('day12/day12data.txt', 'r')
lines = files.readlines()

total = 0

for line in lines:
    line = line.strip()
    pattern = line.split(' ')[0]
    group_counts = [int(i) for i in line.split(' ')[1].split(',')]

    total += count_springs(pattern, group_counts)

print(total)
