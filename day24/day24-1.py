files = open('day24/day24data.txt', 'r')
lines = files.readlines()

MIN = 200000000000000
MAX = 400000000000000
# MIN = 7
# MAX = 27

class Hail:
  def __init__(self, x, y, vx, vy) -> None:
    self.x = int(x)
    self.y = int(y)
    self.vx = int(vx)
    self.vy = int(vy)

    self.slope = self.vy / self.vx

    self.a = -self.slope
    self.b = 1
    self.c = (-self.y) + (self.slope * self.x)

  def does_intersect(self, hailb) -> bool:
    det = (self.a * hailb.b) - (hailb.a * self.b)

    if det == 0:
      return False

    x = ((self.b * hailb.c) - (hailb.b * self.c)) / det
    y = ((self.c * hailb.a) - (hailb.c * self.a)) / det

    if MIN <= x <= MAX and MIN <= y <= MAX:
      if self.vx < 0 and self.vy < 0 and x > self.x and y > self.y:
        return False # down to left
      elif self.vx < 0 and self.vy > 0 and x > self.x and y < self.y:
        return False # up to left
      elif self.vx > 0 and self.vy < 0 and x < self.x and y > self.y:
        return False # down to right
      elif self.vx > 0 and self.vy > 0 and x < self.x and y < self.y:
        return False # up to right
      elif hailb.vx < 0 and hailb.vy < 0 and x > hailb.x and y > hailb.y:
        return False # down to left
      elif hailb.vx < 0 and hailb.vy > 0 and x > hailb.x and y < hailb.y:
        return False # up to left
      elif hailb.vx > 0 and hailb.vy < 0 and x < hailb.x and y > hailb.y:
        return False # down to right
      elif hailb.vx > 0 and hailb.vy > 0 and x < hailb.x and y < hailb.y:
        return False # up to right
      return True

    return False


hailstones = []

for line in lines:
  segments = line.strip().split(' @ ')
  locations = segments[0].split(', ')
  velocities = segments[1].split(', ')

  hail = Hail(locations[0], locations[1], velocities[0], velocities[1])
  hailstones.append(hail)

total = 0

for i in range(len(hailstones) - 1):
  hailA = hailstones[i]

  for j in range(i + 1, len(hailstones)):
    hailB = hailstones[j]

    if hailA.does_intersect(hailB):
      total += 1

print(total)
