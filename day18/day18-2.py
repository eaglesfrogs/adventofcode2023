import shapely

files = open('day18/day18data.txt', 'r')
lines = files.readlines()

directions = []

perimeter = 0

for line in lines:
    line = line.strip()
    chunks = line.split(' ')
    hex = chunks[2].replace('(', '').replace(')', '').replace('#', '')

    dir = hex[-1]
    if dir == '0':
        dir = 'R'
    if dir == '1':
        dir = 'D'
    if dir == '2':
        dir = 'L'
    if dir == '3':
        dir = 'U'

    steps = int(hex[0:5], 16)

    perimeter += steps

    directions.append((dir, steps))

lagoon_list = []

current_space = (0, 0)
min_x = 0
min_y = 0

for dir in directions:
    next_space = None

    if dir[0] == 'R':
        next_space = (current_space[0], current_space[1] + dir[1])
    elif dir[0] == 'L':
        next_space = (current_space[0], current_space[1] - dir[1])
    elif dir[0] == 'U':
        next_space = (current_space[0] - dir[1], current_space[1])
    elif dir[0] == 'D':
        next_space = (current_space[0] + dir[1], current_space[1])

    lagoon_list.append(next_space)
    current_space = next_space

# knew i had to figure out the area, found a library to calculate the area instead of implement shoelace formula
# https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
polygon = shapely.Polygon(lagoon_list)

# like a dummy i forgot that i gotta count for the area of the border
# https://www.reddit.com/r/adventofcode/comments/18l2tap/comment/kdv8imu/?utm_source=share&utm_medium=web2x&context=3
area = polygon.area + (perimeter/2) + 1

print(area)
