import re

files = open('day01/day1data.txt', 'r')
lines = files.readlines()

total = 0

for line in lines:
    line = line.strip()
    filtered_line = re.sub(r'[a-zA-Z]', '', line)

    if len(filtered_line) == 0:
        continue

    new_int_string = filtered_line[0] + \
        filtered_line[len(filtered_line) - 1]
    total = total + int(new_int_string)

print(total)
