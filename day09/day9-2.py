files = open('day09/day9data.txt', 'r')
lines = files.readlines()

def calculate_next(values):
  diffs = []

  for i in range(1, len(values)):
    diff = values[i] - values[i-1]
    diffs.append(diff)

  if all(d == 0 for d in diffs):
    return values[0]

  next_value = calculate_next(diffs)

  return values[0] - next_value

total = 0

for line in lines:
  line = line.strip()
  values = line.split(' ')
  values = [int(v) for v in values]

  total = total + calculate_next(values)

print(total)
