import matplotlib.pyplot as plt
import networkx as nx
import math

files = open('day25/day25data.txt', 'r')
lines = files.readlines()

# visualized and just picked out the ones to remove
# delete vgs -> xjb
# delete ljl -> xhg
# delete lkm -> ffj

wiring_map = {}

G = nx.Graph()

for line in lines:
  wiring_segs = line.strip().split(': ')

  start_wire = wiring_segs[0]
  target_wires = wiring_segs[1].split(' ')

  if start_wire not in wiring_map:
    wiring_map[start_wire] = set()

  for t in target_wires:
    if t in ['vgs', 'xjb'] and start_wire in ['vgs', 'xjb']:
      continue
    if t in ['ljl', 'xhg'] and start_wire in ['ljl', 'xhg']:
      continue
    if t in ['lkm', 'ffj'] and start_wire in ['lkm', 'ffj']:
      continue

    wiring_map[start_wire].add(t)

    G.add_edge(start_wire, t)

    if t not in wiring_map:
      wiring_map[t] = set()

    wiring_map[t].add(start_wire)

pos = nx.spring_layout(G)

edges = [(u,v) for (u,v,d) in G.edges(data=True)]

label_map = {}

for w in wiring_map:
  label_map[w] = w

nx.draw_networkx_nodes(G, pos, node_size=700, nodelist=wiring_map.keys())
nx.draw_networkx_edges(G, pos, edgelist=edges)
nx.draw_networkx_labels(G, pos, font_size=12, labels=label_map)

print(math.prod(map(len, nx.connected_components(G))))

plt.axis('off')
plt.show()
