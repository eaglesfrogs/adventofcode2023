import sys
import heapq
import copy

files = open('day23/day23data.txt', 'r')
lines = files.readlines()
grid = []

for line in lines:
  line = line.strip()
  grid.append([*line])


node_map = {}

rows = len(grid)
cols = len(grid[0])

node_map[(0, 1)] = []

def get_conns(prev_coord, coord):
  conns = []
  row = coord[0]
  col = coord[1]

  if row > 0 and (row-1, col) != prev_coord and lines[row - 1][col] != '#':
    conns.append((row-1,col))
  if row < rows - 1 and (row+1, col) != prev_coord and lines[row + 1][col] != '#':
    conns.append((row+1,col))
  if col > 0 and (row, col-1) != prev_coord and lines[row][col - 1] != '#':
    conns.append((row,col - 1))
  if col < cols - 1 and (row, col+1) != prev_coord and lines[row][col + 1] != '#':
    conns.append((row,col + 1))

  return conns

nodes = [((0, 1), get_conns(None, (0, 1)))]

while nodes:
  starting_node, starting_node_conns = nodes.pop()

  while starting_node_conns:
    steps = 1

    prev_node = starting_node
    next_node = starting_node_conns.pop()

    conns = get_conns(prev_node, next_node)

    while len(conns) == 1:
      steps += 1
      prev_node = next_node
      next_node = conns[0]

      conns = get_conns(prev_node, next_node)

    if (steps, next_node) not in node_map[starting_node]:
      node_map[starting_node].append((steps, next_node))

    if next_node in node_map:
      if (steps, starting_node) not in node_map[next_node]:
        node_map[next_node].append((steps, starting_node))
    else:
      node_map[next_node] = [(steps, starting_node)]
      nodes.append((next_node, conns))

start_node = (0, 1)
end_node = (rows - 1, cols - 2)

node_counts = {}
for node in node_map:
  node_counts[node] = 0

visited = set()

def dfs(node, steps):
  if node == end_node:
    return steps

  visited.add(node)

  step_totals = []

  neighbors = node_map[node]
  for neighbor in neighbors:
    if neighbor[1] not in visited:
      s = dfs(neighbor[1], neighbor[0])

      if s:
        step_totals.append(s + steps)

  visited.remove(node)

  if step_totals:
    return max(step_totals)
  else:
    return None

print(dfs(start_node, 0))

