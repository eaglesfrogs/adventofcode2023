files = open('day13/day13data.txt', 'r')
lines = files.readlines()

puzzle = []
rotate_puzzle = []

def count_rows(pzl):
  total = 0

  for i in range(len(pzl) - 1):
    if pzl[i] == pzl[i + 1]:
      j = 1
      while i - j >= 0 and i + 1 + j < len(pzl):
        if pzl[i - j] == pzl[i + 1 + j]:
          j += 1
        else:
          break

      if i - j == -1 or i + 1 + j == len(pzl):
        return i + 1

  return 0


total = 0

for line in lines:
  line = line.strip()

  if line == '':
    for i in range(len(puzzle[0])):
      rotated_line = ''

      for j in reversed(range(len(puzzle))):
        rotated_line += puzzle[j][i]

      rotate_puzzle.append(rotated_line)

    pzl1_count = count_rows(puzzle)
    pzl2_count = count_rows(rotate_puzzle)

    total = total + pzl2_count + (pzl1_count * 100)

    puzzle = []
    rotate_puzzle = []
  else:
    puzzle.append(line)

if puzzle:
  for i in range(len(puzzle[0])):
    rotated_line = ''

    for j in reversed(range(len(puzzle))):
      rotated_line += puzzle[j][i]

    rotate_puzzle.append(rotated_line)

  pzl1_count = count_rows(puzzle)
  pzl2_count = count_rows(rotate_puzzle)

  total = total + pzl2_count + (pzl1_count * 100)

  puzzle = []
  rotate_puzzle = []

print(total)

