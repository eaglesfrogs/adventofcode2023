import re


files = open('day03/day3data.txt', 'r')
lines = files.readlines()

special_chars = set()

for i in range(len(lines)):
  lines[i] = lines[i].strip()
  for j in range(len(lines[i])):
    if re.match(r'[0-9]|\.', lines[i][j]):
      continue
    special_chars.add(lines[i][j])

def does_it_count(line, row, start, end):
  top_line = ''
  bottom_line = ''
  prev_char = ''
  next_char = ''

  if row > 0:
    top_line_start = start
    if top_line_start > 0:
      top_line_start = top_line_start - 1

    top_line_end = end
    if top_line_end < len(line):
      top_line_end = top_line_end + 1

    top_line = lines[row - 1][top_line_start:top_line_end]

  if row < len(lines) - 1:
    bottom_line_start = start
    if bottom_line_start > 0:
      bottom_line_start = bottom_line_start - 1

    bottom_line_end = end
    if bottom_line_end < len(line):
      bottom_line_end = bottom_line_end + 1

    bottom_line = lines[row + 1][bottom_line_start:bottom_line_end]

  if start > 0:
    prev_char = line[start - 1]

  if end < len(line) - 1:
    next_char = line[end]

  if any(elem in top_line for elem in special_chars):
    return True
  if any(elem in bottom_line for elem in special_chars):
    return True
  if any(elem in prev_char for elem in special_chars):
    return True
  if any(elem in next_char for elem in special_chars):
    return True

  return False

total = 0

for i in range(len(lines)):
  line = lines[i]

  matches = re.finditer(r'[0-9]+', line)

  for match in matches:
    start = match.start()
    end = match.end()

    if does_it_count(line, i, start, end):
      total = total + int(match[0])

print(total)
