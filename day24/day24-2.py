import z3

files = open('day24/day24data.txt', 'r')
lines = files.readlines()


class Hail:
  def __init__(self, x, y, z, vx, vy, vz) -> None:
    self.x = int(x)
    self.y = int(y)
    self.z = int(z)
    self.vx = int(vx)
    self.vy = int(vy)
    self.vz = int(vz)

hailstones = []

for line in lines:
  segments = line.strip().split(' @ ')
  locations = segments[0].split(', ')
  velocities = segments[1].split(', ')

  hail = Hail(locations[0], locations[1], locations[2], velocities[0], velocities[1], velocities[2])
  hailstones.append(hail)

hailstones = hailstones[:3] # you only need 3 vectors for this

# learned about z3. mostly copy/paste from https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/ker07t0/?utm_source=share&utm_medium=web2x&context=3
s = z3.Solver()

rock_x, rock_y, rock_z = z3.BitVecs("rock_x rock_y rock_z", 64)
rock_vx, rock_vy, rock_vz = z3.BitVecs("rock_vx rock_vy rock_vz", 64)

all_times = []

for i, stone in enumerate(hailstones):
    t = z3.BitVec(f"stone{i}_t", 64)
    s.add(t > 0)
    s.add(rock_x + rock_vx * t == stone.x + stone.vx * t)
    s.add(rock_y + rock_vy * t == stone.y + stone.vy * t)
    s.add(rock_z + rock_vz * t == stone.z + stone.vz * t)
    all_times.append(t)

s.add(z3.Distinct(all_times))

assert s.check() == z3.sat
print(
    s.model()[rock_x].as_long()
    + s.model()[rock_y].as_long()
    + s.model()[rock_z].as_long()
)
