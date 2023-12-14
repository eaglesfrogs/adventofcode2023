files = open('day14/day14data.txt', 'r')
lines = files.readlines()

platform = []

for line in lines:
    line = line.strip()
    platform.append([*line])

cols = len(platform[0])
rows = len(platform)

total = 0

for c in range(cols):
    stop_row = 0

    for r in range(rows):
        char = platform[r][c]

        if char == '#':
            stop_row = r + 1
        elif char == 'O' and stop_row < r:
            platform[r][c] = '.'
            platform[stop_row][c] = 'O'

            total += rows - stop_row

            stop_row = stop_row + 1
        elif char == 'O' and stop_row == r:
            total += rows - stop_row
            stop_row = stop_row + 1

print(total)
