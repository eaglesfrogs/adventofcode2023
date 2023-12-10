files = open('day10/day10data.txt', 'r')
map = files.readlines()
filtered_map = []

start = (0,0)

idx = 0
for line in map:
  line = line.strip()

  if 'S' in line:
    start = (idx, line.index('S'))

  filtered_map.append(['.'] * len(line))

  idx = idx + 1

pipe_dir_map = {
  '|': {
    (-1, 0): (-1, 0), # bottom to top
    (1, 0): (1, 0) # top to bottom
  },
  '-': {
    (0, 1): (0, 1), # left to right
    (0, -1): (0, -1) # right to left
  },
  'L': {
    (1, 0): (0, 1), # top to right
    (0, -1): (-1, 0) # right to top
  },
  'J': {
    (1, 0): (0, -1), # top to left
    (0, 1): (-1, 0) # left to top
  },
  '7': {
    (0, 1): (1, 0), # left to bottom
    (-1, 0): (0, -1) # bottom to left
  },
  'F': {
    (0, -1): (1, 0), # right to bottom
    (-1, 0): (0, 1) # bottom to right
  }
}

dirs = []

if map[start[0] - 1][start[1]] in ['|', '7', 'F']:
  dirs.append((-1, 0))
if map[start[0] + 1][start[1]] in ['|', 'L', 'J']:
  dirs.append((1, 0))
if map[start[0]][start[1] - 1] in ['-', 'L', 'F']:
  dirs.append((0, -1))
if map[start[0]][start[1] + 1] in ['-', '7', 'J']:
  dirs.append((0, 1))

dir1_coords = (start[0] + dirs[0][0], start[1] + dirs[0][1])
dir1_val = map[dir1_coords[0]][dir1_coords[1]]
dir1_prev = dirs[0]

dir2_coords = (start[0] + dirs[1][0], start[1] + dirs[1][1])
dir2_val = map[dir2_coords[0]][dir2_coords[1]]
dir2_prev = dirs[1]

filtered_map[start[0]][start[1]] = '-'
filtered_map[dir1_coords[0]][dir1_coords[1]] = dir1_val
filtered_map[dir2_coords[0]][dir2_coords[1]] = dir2_val


steps = 1
while dir1_coords != dir2_coords:
  dir1_next_dir = pipe_dir_map[dir1_val][dir1_prev]
  dir1_coords = (dir1_coords[0] + dir1_next_dir[0], dir1_coords[1] + dir1_next_dir[1])
  dir1_val = map[dir1_coords[0]][dir1_coords[1]]
  dir1_prev = dir1_next_dir

  dir2_next_dir = pipe_dir_map[dir2_val][dir2_prev]
  dir2_coords = (dir2_coords[0] + dir2_next_dir[0], dir2_coords[1] + dir2_next_dir[1])
  dir2_val = map[dir2_coords[0]][dir2_coords[1]]
  dir2_prev = dir2_next_dir

  filtered_map[dir1_coords[0]][dir1_coords[1]] = dir1_val
  filtered_map[dir2_coords[0]][dir2_coords[1]] = dir2_val

  steps = steps + 1

print(steps)

in_loop = False

tiles = 0

entry_char = ''
enter_chars = ['|', 'F', 'L']
exit_chars = []

out_loop_map = {
  '|': ['|'],
  'F': ['7', '|'],
  'L': ['J', '|']
}

swap_map = {
  'F': ['J', '|'],
  'L': ['7', '|']
}

swap = False

for i in range(len(filtered_map)):
  for j in range(len(filtered_map[i])):
    char = filtered_map[i][j]

    if in_loop:
      if char == '.':
        tiles = tiles + 1
        filtered_map[i][j] = 'X'
        continue

      if char in exit_chars:
        in_loop = False
        continue

      if char in swap_map:
        exit_chars = swap_map[char]

    else:
      if char in enter_chars:
        in_loop = True
        exit_chars = out_loop_map[char]


  print(''.join(filtered_map[i]))

print(tiles)


