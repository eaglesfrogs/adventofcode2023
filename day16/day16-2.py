files = open('day16/day16data.txt', 'r')
lines = files.readlines()

class Tile:

  def __init__(self, value) -> None:
    self.value = value
    self.energized = False
    self.directions = []

  def reset(self):
    self.energized = False
    self.directions = []


board = []
starts = []

for line in lines:
  line = line.strip()
  row = []

  for c in line:
    row.append(Tile(c))

  board.append(row)

for i in range(len(board)):
  starts.append((i, 0, '>'))
  starts.append((i, len(board[i]) - 1, '<'))

for j in range(len(board[0])):
  starts.append((0, j, 'v'))
  starts.append((len(board) - 1, j, '^'))

def check_next_square(row, col, dir):
  # beam going off the board
  if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
    return False

  # beam already passed through in this direction
  if dir in board[row][col].directions:
    return False

  return True

max_total = 0
for start in starts:
  for row in board:
    for tile in row:
      tile.reset()

  active_beams = [start]

  while active_beams:

    new_active_beams = []

    for beam in active_beams:
      tile = board[beam[0]][beam[1]]
      tile.energized = True
      tile.directions.append(beam[2])

      if tile.value == '|' and (beam[2] == '>' or beam[2] == '<'):
        if check_next_square(beam[0] - 1, beam[1], '^'):
          new_active_beams.append((beam[0] - 1, beam[1], '^'))
        if check_next_square(beam[0] + 1, beam[1], 'v'):
          new_active_beams.append((beam[0] + 1, beam[1], 'v'))
      elif tile.value == '|' and beam[2] == 'v':
        if check_next_square(beam[0] + 1, beam[1], 'v'):
          new_active_beams.append((beam[0] + 1, beam[1], 'v'))
      elif tile.value == '|' and beam[2] == '^':
        if check_next_square(beam[0] - 1, beam[1], '^'):
          new_active_beams.append((beam[0] - 1, beam[1], '^'))

      elif tile.value == '-' and (beam[2] == 'v' or beam[2] == '^'):
        if check_next_square(beam[0], beam[1] - 1, '<'):
          new_active_beams.append((beam[0], beam[1] - 1, '<'))
        if check_next_square(beam[0], beam[1] + 1, '>'):
          new_active_beams.append((beam[0], beam[1] + 1, '>'))
      elif tile.value == '-' and beam[2] == '>':
        if check_next_square(beam[0], beam[1] + 1, '>'):
          new_active_beams.append((beam[0], beam[1] + 1, '>'))
      elif tile.value == '-' and beam[2] == '<':
        if check_next_square(beam[0], beam[1] - 1, '<'):
          new_active_beams.append((beam[0], beam[1] - 1, '<'))

      elif tile.value == '\\' and beam[2] == '>':
        if check_next_square(beam[0] + 1, beam[1], 'v'):
          new_active_beams.append((beam[0] + 1, beam[1], 'v'))
      elif tile.value == '\\' and beam[2] == '<':
        if check_next_square(beam[0] - 1, beam[1], '^'):
          new_active_beams.append((beam[0] - 1, beam[1], '^'))
      elif tile.value == '\\' and beam[2] == '^':
        if check_next_square(beam[0], beam[1] - 1, '<'):
          new_active_beams.append((beam[0], beam[1] - 1, '<'))
      elif tile.value == '\\' and beam[2] == 'v':
        if check_next_square(beam[0], beam[1] + 1, '>'):
          new_active_beams.append((beam[0], beam[1] + 1, '>'))

      elif tile.value == '/' and beam[2] == '>':
        if check_next_square(beam[0] - 1, beam[1], '^'):
          new_active_beams.append((beam[0] - 1, beam[1], '^'))
      elif tile.value == '/' and beam[2] == '<':
        if check_next_square(beam[0] + 1, beam[1], 'v'):
          new_active_beams.append((beam[0] + 1, beam[1], 'v'))
      elif tile.value == '/' and beam[2] == '^':
        if check_next_square(beam[0], beam[1] + 1, '>'):
          new_active_beams.append((beam[0], beam[1] + 1, '>'))
      elif tile.value == '/' and beam[2] == 'v':
        if check_next_square(beam[0], beam[1] - 1, '<'):
          new_active_beams.append((beam[0], beam[1] - 1, '<'))

      elif tile.value == '.' and beam[2] == '>':
        if check_next_square(beam[0], beam[1] + 1, '>'):
          new_active_beams.append((beam[0], beam[1] + 1, '>'))
      elif tile.value == '.' and beam[2] == '<':
        if check_next_square(beam[0], beam[1] - 1, '<'):
          new_active_beams.append((beam[0], beam[1] - 1, '<'))
      elif tile.value == '.' and beam[2] == '^':
        if check_next_square(beam[0] - 1, beam[1], '^'):
          new_active_beams.append((beam[0] - 1, beam[1], '^'))
      elif tile.value == '.' and beam[2] == 'v':
        if check_next_square(beam[0] + 1, beam[1], 'v'):
          new_active_beams.append((beam[0] + 1, beam[1], 'v'))

    active_beams = new_active_beams

  total = 0
  for row in board:
    for tile in row:
      if tile.energized:
        total += 1

  if total > max_total:
    max_total = total

print(max_total)
