files = open('day18/day18data.txt', 'r')
lines = files.readlines()

directions = []

for line in lines:
    line = line.strip()
    chunks = line.split(' ')
    dir = chunks[0]
    steps = int(chunks[1])
    color = chunks[2]

    directions.append((dir, steps, color))

lagoon_hash = {}

next_space = (0, 0)

min_x = 0
max_x = 0
min_y = 0
max_y = 0

for dir in directions:
    for i in range(dir[1]):
        lagoon_hash[next_space] = dir[2]

        if dir[0] == 'R':
            next_space = (next_space[0], next_space[1] + 1)
            if next_space[1] > max_x:
                max_x = next_space[1]
        elif dir[0] == 'L':
            next_space = (next_space[0], next_space[1] - 1)
            if next_space[1] < min_x:
                min_x = next_space[1]
        elif dir[0] == 'U':
            next_space = (next_space[0] - 1, next_space[1])
            if next_space[0] < min_y:
                min_y = next_space[0]
        elif dir[0] == 'D':
            next_space = (next_space[0] + 1, next_space[1])
            if next_space[0] > max_y:
                max_y = next_space[0]

lagoon_array = []

row_count = abs(min_y) + abs(max_y) + 3
col_count = abs(min_x) + abs(max_x) + 3

# plus three to add a border around the whole thing for an exterior flood fill
for i in range(row_count):
    lagoon_array_row = []
    for j in range(col_count):
        lagoon_array_row.append('.')
    lagoon_array.append(lagoon_array_row)

# plus 1 on coordinates to account for floodfill border
for l in lagoon_hash:
    lagoon_array[l[0] + abs(min_y) + 1][l[1] + abs(min_x) + 1] = '#'

flood_fill_stack = [(0, 0)]

while flood_fill_stack:
    f = flood_fill_stack.pop()
    lagoon_array[f[0]][f[1]] = 'X'

    if f[0] > 0 and lagoon_array[f[0] - 1][f[1]] == '.':
        flood_fill_stack.append((f[0] - 1, f[1]))
    if f[0] < row_count - 1 and lagoon_array[f[0] + 1][f[1]] == '.':
        flood_fill_stack.append((f[0] + 1, f[1]))
    if f[1] > 0 and lagoon_array[f[0]][f[1] - 1] == '.':
        flood_fill_stack.append((f[0], f[1] - 1))
    if f[1] < col_count - 1 and lagoon_array[f[0]][f[1] + 1] == '.':
        flood_fill_stack.append((f[0], f[1] + 1))

total = 0
for row in lagoon_array:
    for c in row:
        if c == '#' or c == '.':
            total += 1

print(total)
