files = open('day14/day14data.txt', 'r')
lines = files.readlines()

platform = []

for line in lines:
    line = line.strip()
    platform.append([*line])

cols = len(platform[0])
rows = len(platform)

total = 0

cache = []


def roll_north():
    for c in range(cols):
        stop_row = 0

        for r in range(rows):
            char = platform[r][c]

            if char == '#':
                stop_row = r + 1
            elif char == 'O' and stop_row < r:
                platform[r][c] = '.'
                platform[stop_row][c] = 'O'

                stop_row = stop_row + 1
            elif char == 'O' and stop_row == r:
                stop_row = stop_row + 1


def roll_south():
    for c in range(cols):
        stop_row = rows - 1

        for r in reversed(range(rows)):
            char = platform[r][c]

            if char == '#':
                stop_row = r - 1
            elif char == 'O' and stop_row > r:
                platform[r][c] = '.'
                platform[stop_row][c] = 'O'

                stop_row = stop_row - 1
            elif char == 'O' and stop_row == r:
                stop_row = stop_row - 1


def roll_west():
    for r in range(rows):
        stop_col = 0

        for c in range(cols):
            char = platform[r][c]

            if char == '#':
                stop_col = c + 1
            elif char == 'O' and stop_col < c:
                platform[r][c] = '.'
                platform[r][stop_col] = 'O'

                stop_col = stop_col + 1
            elif char == 'O' and stop_col == c:
                stop_col = stop_col + 1


def roll_east():
    for r in range(rows):
        stop_col = cols - 1

        for c in reversed(range(cols)):
            char = platform[r][c]

            if char == '#':
                stop_col = c - 1
            elif char == 'O' and stop_col > c:
                platform[r][c] = '.'
                platform[r][stop_col] = 'O'

                stop_col = stop_col - 1
            elif char == 'O' and stop_col == c:
                stop_col = stop_col - 1


i = 0

while i < 1000000000:
    s = [p[:] for p in platform]

    if s in cache:
        original_occurence = cache.index(s)
        current_occurence = i
        loop_length = current_occurence - original_occurence

        remaining_loops = 1000000000 - i
        magelo_value = remaining_loops % loop_length

        platform = cache[original_occurence + magelo_value]
        break

    cache.append(s)

    roll_north()
    roll_west()
    roll_south()
    roll_east()

    i += 1

for r in range(rows):
    for c in platform[r]:
        if c == 'O':
            total += rows - r

print(total)
