import re
import math


files = open('day06/day6data.txt', 'r')
lines = files.readlines()

times_str = re.findall(f'[0-9]+', lines[0])
distances_str = re.findall(f'[0-9]+', lines[1])

times = [int(t) for t in times_str]
distances = [int(d) for d in distances_str]

total = 1

for i in range(len(times)):
  a = -1
  b = times[i]
  c = -distances[i]

  d = (b**2) - (4*a*c)
  max = (-b - math.sqrt(d))/(2*a)
  min = (-b + math.sqrt(d))/(2*a)

  max = math.floor(max)
  min = math.ceil(min)

  print(min)
  print(max)

  total = (max - min + 1) * total

print(total)


