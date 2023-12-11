import re

files = open('day11/day11data.txt', 'r')
lines = files.readlines()

space = []

only_space_rows = []

for i in range(len(lines)):
    line = lines[i].strip()
    space.append([*line])

    if re.match(r'^\.+$', line):
        only_space_rows.append(i)

only_space_columns = []

for i in range(len(space[0])):
    is_space = True

    for j in range(len(space)):
        if space[j][i] == '#':
            is_space = False
            break

    if is_space:
        only_space_columns.append(i)

galaxies = []

for i in range(len(space)):
    row = space[i]
    for j in range(len(row)):
        if space[i][j] == '#':
            galaxies.append((i, j))

distance = 0


def is_between(num, start, end):
    min_num = min(start, end)
    max_num = max(start, end)
    return min_num <= num <= max_num


for start_galaxy_idx in range(len(galaxies)):
    start_galaxy = galaxies[start_galaxy_idx]

    for dest_galaxy_idx in range(start_galaxy_idx + 1, len(galaxies)):
        dest_galaxy = galaxies[dest_galaxy_idx]

        row_distance = abs(dest_galaxy[0] - start_galaxy[0])
        for r in only_space_rows:
            if is_between(r, dest_galaxy[0], start_galaxy[0]):
                row_distance = row_distance + 999999

        col_distance = abs(dest_galaxy[1] - start_galaxy[1])
        for c in only_space_columns:
            if is_between(c, dest_galaxy[1], start_galaxy[1]):
                col_distance = col_distance + 999999

        distance = distance + row_distance + col_distance

print(distance)
