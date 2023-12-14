import regex

files = open('day13/day13data.txt', 'r')
lines = files.readlines()

puzzle = []
rotate_puzzle = []

def count_rows(pzl):

  for i in range(len(pzl) - 1):
    res = regex.fullmatch(r'(%s){s<=1}'%pzl[i], pzl[i+1])

    if res:
      match = True
      found_bug = False

      if pzl[i] != pzl[i+1]:
        found_bug = True

      j = 1
      while i - j >= 0 and i + 1 + j < len(pzl):
        res = regex.fullmatch(r'(%s){s<=1}'%pzl[i-j], pzl[i+1+j])

        if res:
          if found_bug and pzl[i-j] != pzl[i+1+j]:
            match = False
            break

          if pzl[i-j] != pzl[i+1+j]:
            found_bug = True

          j += 1
        else:
          match = False
          break

      if match and (i - j == -1 or i + 1 + j == len(pzl)) and found_bug:
        return i + 1

  return 0


total = 0

for line in lines:
  line = line.strip().replace('.', 'x').replace('#', 'M') # using regex fuzzy matches works weird with # and . so change them to x and M i guess

  if line == '':
    for i in range(len(puzzle[0])):
      rotated_line = ''

      for j in reversed(range(len(puzzle))):
        rotated_line += puzzle[j][i]

      rotate_puzzle.append(rotated_line)

    pzl1_count = 0
    pzl2_count = 0

    pzl1_count = count_rows(puzzle)
    pzl2_count = count_rows(rotate_puzzle)

    total = total + (pzl1_count * 100) + pzl2_count

    puzzle = []
    rotate_puzzle = []
  elif line:
    puzzle.append(line)

if puzzle:
  for i in range(len(puzzle[0])):
    rotated_line = ''

    for j in reversed(range(len(puzzle))):
      rotated_line += puzzle[j][i]

    rotate_puzzle.append(rotated_line)

  pzl1_count = 0
  pzl2_count = 0

  pzl1_count = count_rows(puzzle)
  pzl2_count = count_rows(rotate_puzzle)

  total = total + (pzl1_count * 100) + pzl2_count

print(total)

