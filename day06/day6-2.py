import re
import math


files = open('day06/day6data.txt', 'r')
lines = files.readlines()

times_str = re.findall(f'[0-9]+', lines[0])
distances_str = re.findall(f'[0-9]+', lines[1])

time = int(times_str[0] + times_str[1] + times_str[2] + times_str[3])
distance = int(distances_str[0] + distances_str[1] + distances_str[2] + distances_str[3])

a = -1
b = time
c = -distance

d = (b**2) - (4*a*c)
max = (-b - math.sqrt(d))/(2*a)
min = (-b + math.sqrt(d))/(2*a)

max = math.floor(max)
min = math.ceil(min)

print(min)
print(max)

total = max - min + 1

print(total)


