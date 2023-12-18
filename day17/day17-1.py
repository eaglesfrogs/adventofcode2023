import sys
import heapq

files = open('day17/day17data.txt', 'r')
lines = files.readlines()

node_values = []
node_hash = {}

rows = len(lines)
cols = 0

for i in range(len(lines)):
  line = lines[i].strip()

  if cols == 0:
    cols = len(line)

  node_values_row = []

  for j in range(len(line)):
    value = line[j]
    node_values_row.append(int(value))

    for k in range(1, 4):
      if i - k >= 0:
        node_hash[(i - k, j, 'n', k)] = []
      if i + k < len(lines):
        node_hash[(i + k, j, 's', k)] = []
      if j - k >= 0:
        node_hash[(i, j - k, 'w', k)] = []
      if j + k < len(line):
        node_hash[(i, j + k, 'e', k)] = []

  node_values.append(node_values_row)

for node in node_hash:
  connections = node_hash[node]

  if node[2] == 'n':
    if node[3] < 3 and node[0] > 0 and (node[0] - 1, node[1], 'n', node[3] + 1) in node_hash:
      connections.append({ 'conn': (node[0] - 1, node[1], 'n', node[3] + 1), 'val': node_values[node[0] - 1][node[1]] })
    if node[1] > 0 and (node[0], node[1] - 1, 'w', 1) in node_hash:
      connections.append({ 'conn': (node[0], node[1] - 1, 'w', 1), 'val': node_values[node[0]][node[1] - 1] })
    if node[1] < cols - 1 and (node[0], node[1] + 1, 'e', 1) in node_hash:
      connections.append({ 'conn': (node[0], node[1] + 1, 'e', 1), 'val': node_values[node[0]][node[1] + 1] })

  if node[2] == 's':
    if node[3] < 3 and node[0] < rows - 1 and (node[0] + 1, node[1], 's', node[3] + 1) in node_hash:
      connections.append({ 'conn': (node[0] + 1, node[1], 's', node[3] + 1), 'val': node_values[node[0] + 1][node[1]] })
    if node[1] > 0 and (node[0], node[1] - 1, 'w', 1) in node_hash:
      connections.append({ 'conn': (node[0], node[1] - 1, 'w', 1), 'val': node_values[node[0]][node[1] - 1] })
    if node[1] < cols - 1 and (node[0], node[1] + 1, 'e', 1) in node_hash:
      connections.append({ 'conn': (node[0], node[1] + 1, 'e', 1), 'val': node_values[node[0]][node[1] + 1] })

  if node[2] == 'w':
    if node[3] < 3 and node[1] > 0 and (node[0], node[1] - 1, 'w', node[3] + 1) in node_hash:
      connections.append({ 'conn': (node[0], node[1] - 1, 'w', node[3] + 1), 'val': node_values[node[0]][node[1] - 1] })
    if node[0] > 0 and (node[0] - 1, node[1], 'n', 1) in node_hash:
      connections.append({ 'conn': (node[0] - 1, node[1], 'n', 1), 'val': node_values[node[0] - 1][node[1]] })
    if node[0] < rows - 1 and (node[0] + 1, node[1], 's', 1) in node_hash:
      connections.append({ 'conn': (node[0] + 1, node[1], 's', 1), 'val': node_values[node[0] + 1][node[1]] })

  if node[2] == 'e':
    if node[3] < 3 and node[1] < cols - 1 and (node[0], node[1] + 1, 'e', node[3] + 1) in node_hash:
      connections.append({ 'conn': (node[0], node[1] + 1, 'e', node[3] + 1), 'val': node_values[node[0]][node[1] + 1] })
    if node[0] > 0 and (node[0] - 1, node[1], 'n', 1) in node_hash:
      connections.append({ 'conn': (node[0] - 1, node[1], 'n', 1), 'val': node_values[node[0] - 1][node[1]] })
    if node[0] < rows - 1 and (node[0] + 1, node[1], 's', 1) in node_hash:
      connections.append({ 'conn': (node[0] + 1, node[1], 's', 1), 'val': node_values[node[0] + 1][node[1]] })

node_hash[(0, 0, 'x', 0)] = [
  {'conn': (1, 0, 's', 1), 'val': node_values[1][0]},
  {'conn': (0, 1, 'e', 1), 'val': node_values[0][1]}
]

shortest_path = {}

max_val = sys.maxsize

for node in node_hash:
  shortest_path[node] = max_val

start_node = (0, 0, 'x', 0)
target_node_coords = (rows - 1, cols - 1)

shortest_path[start_node] = 0

target_node = None

pq = [(0, start_node)]

while len(pq) > 0:
  current_distance, current_node = heapq.heappop(pq)

  if current_node[0] == target_node_coords[0] and current_node[1] == target_node_coords[1]:
    target_node = current_node
    break

  if current_distance > shortest_path[current_node]:
    continue

  neighbors = node_hash[current_node]
  for neighbor in neighbors:
    tentative_value = current_distance + neighbor['val']

    if tentative_value < shortest_path[neighbor['conn']]:
      shortest_path[neighbor['conn']] = tentative_value
      heapq.heappush(pq, (tentative_value, neighbor['conn']))

print(shortest_path[target_node])
