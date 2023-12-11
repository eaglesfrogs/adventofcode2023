import re

files = open('day11/day11data.txt', 'r')
lines = files.readlines()

space = []

for line in lines:
    line = line.strip()
    space.append([*line])

    if re.match(r'^\.+$', line):
        space.append([*line])

only_space_columns = []

for i in range(len(space[0])):
    is_space = True

    for j in range(len(space)):
        if space[j][i] == '#':
            is_space = False
            break

    if is_space:
        only_space_columns.append(i)

only_space_columns.reverse()

for idx in only_space_columns:
    for row in space:
        row.insert(idx, '.')

galaxies = []

for i in range(len(space)):
    row = space[i]
    for j in range(len(row)):
        if space[i][j] == '#':
            galaxies.append((i, j))

distance = 0

for start_galaxy_idx in range(len(galaxies)):
    start_galaxy = galaxies[start_galaxy_idx]

    for dest_galaxy_idx in range(start_galaxy_idx + 1, len(galaxies)):
        dest_galaxy = galaxies[dest_galaxy_idx]

        row_distance = abs(dest_galaxy[0] - start_galaxy[0])
        col_distance = abs(dest_galaxy[1] - start_galaxy[1])

        distance = distance + row_distance + col_distance

print(distance)
