import sys
import heapq
import copy

files = open('day23/day23data.txt', 'r')
lines = files.readlines()

node_map = {}

rows = len(lines)
cols = 0

for row in range(len(lines)):
  line = lines[row].strip()

  cols = len(line)

  for col in range(len(line)):
    c = line[col]

    connections = []

    if c == '#':
      continue

    if c == '.':
      if row > 0 and lines[row - 1][col] in '.^':
        connections.append((row-1,col))
      if row < len(lines) - 1 and lines[row + 1][col] in '.v':
        connections.append((row+1,col))
      if col > 0 and lines[row][col - 1] in '.<':
        connections.append((row,col - 1))
      if col < len(line) - 1 and lines[row][col + 1] in '.>':
        connections.append((row,col + 1))
    elif c == '>':
      connections.append((row, col+1))
    elif c == '<':
      connections.append((row, col-1))
    elif c == 'v':
      connections.append((row+1, col))
    elif c == '^':
      connections.append((row-1, col))

    node_map[(row, col)] = connections

start_node = (0, 1)
end_node = (rows - 1, cols - 2)

shortest_path = {}

max_val = sys.maxsize

for node in node_map:
  shortest_path[node] = {'steps': -1 * max_val, 'visited': set()}

shortest_path[start_node]['steps'] = 0

target_node = None

pq = [(0, start_node)]

while len(pq) > 0:
  current_distance, current_node = heapq.heappop(pq)

  if current_node == end_node:
    target_node = current_node

  if current_distance < shortest_path[current_node]['steps']:
    continue

  visited = copy.copy(shortest_path[current_node]['visited'])
  visited.add(current_node)

  neighbors = node_map[current_node]
  for neighbor in neighbors:
    if neighbor in visited:
      continue

    tentative_value = current_distance + 1

    if tentative_value > shortest_path[neighbor]['steps']:
      shortest_path[neighbor] = {'steps': tentative_value, 'visited': visited}
      heapq.heappush(pq, (tentative_value, neighbor))

print(shortest_path[target_node]['steps'])
