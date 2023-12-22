files = open('day22/day22data.txt', 'r')
lines = files.readlines()


class Piece:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.supported_by = []

    def touches(self, other_piece):
        other_piece_coords = other_piece.get_all_coords()
        level_up_coords = [(x[0], x[1], x[2]+1) for x in self.get_all_coords()]

        return not set(level_up_coords).isdisjoint(other_piece_coords)

    def get_all_coords(self):
        if self.start == self.end:
            return [self.start]

        coords = []

        if self.start[0] != self.end[0]:
            for x in range(self.start[0], self.end[0] + 1):
                coords.append((x, self.start[1], self.start[2]))
        elif self.start[1] != self.end[1]:
            for y in range(self.start[1], self.end[1] + 1):
                coords.append((self.start[0], y, self.start[2]))
        elif self.start[2] != self.end[2]:
            for z in range(self.start[2], self.end[2] + 1):
                coords.append((self.start[0], self.start[1], z))

        return coords

    def get_supportable_coords(self):
        coords = []

        if self.start == self.end or self.start[2] != self.end[2]:
            return [self.start]
        elif self.start[0] != self.end[0]:
            for x in range(self.start[0], self.end[0] + 1):
                coords.append((x, self.start[1], self.start[2]))
        elif self.start[1] != self.end[1]:
            for y in range(self.start[1], self.end[1] + 1):
                coords.append((self.start[0], y, self.start[2]))

        return coords

    def get_supporting_coords(self):
        coords = []

        if self.start == self.end or self.start[2] != self.end[2]:
            return [self.end]
        elif self.start[0] != self.end[0]:
            for x in range(self.start[0], self.end[0] + 1):
                coords.append((x, self.start[1], self.start[2]))
        elif self.start[1] != self.end[1]:
            for y in range(self.start[1], self.end[1] + 1):
                coords.append((self.start[0], y, self.start[2]))

        return coords

    def drop(self, z_board):
        if self.start == self.end:
            min_z = z_board[self.start[0]][self.start[1]] + 1
            if min_z == self.start[2]:  # already at the lowest
                return

            self.start = (self.start[0], self.start[1], min_z)
            self.end = (self.end[0], self.end[1], min_z)
        elif self.start[2] != self.end[2]:
            min_z = z_board[self.start[0]][self.start[1]] + 1
            if min_z == self.start[2]:  # already at the lowest
                return

            diff = self.start[2] - min_z
            self.start = (self.start[0], self.start[1], self.start[2] - diff)
            self.end = (self.end[0], self.end[1], self.end[2] - diff)
        elif self.start[1] != self.end[1]:
            min_z = 0
            for y in range(self.start[1], self.end[1] + 1):
                if z_board[self.start[0]][y] > min_z:
                    min_z = z_board[self.start[0]][y]

            min_z += 1
            if min_z == self.start[2]:  # already at the lowest
                return

            self.start = (self.start[0], self.start[1], min_z)
            self.end = (self.end[0], self.end[1], min_z)
        elif self.start[0] != self.end[0]:
            min_z = 0
            for x in range(self.start[0], self.end[0] + 1):
                if z_board[x][self.start[1]] > min_z:
                    min_z = z_board[x][self.start[1]]

            min_z += 1
            if min_z == self.start[2]:  # already at the lowest
                return

            self.start = (self.start[0], self.start[1], min_z)
            self.end = (self.end[0], self.end[1], min_z)


pieces = []

max_x = 0
max_y = 0
max_z = 0

for line in lines:
    line = line.strip()
    coords = line.split('~')
    start = tuple([int(x) for x in coords[0].split(',')])
    end = tuple([int(x) for x in coords[1].split(',')])

    if start[0] > max_x:
        max_x = start[0]
    if start[1] > max_y:
        max_y = start[1]
    if start[2] > max_z:
        max_z = start[2]

    if end[0] > max_x:
        max_x = end[0]
    if end[1] > max_y:
        max_y = end[1]
    if end[2] > max_z:
        max_z = end[2]

    piece = Piece(start, end)
    pieces.append(piece)

tower = []

for x in range(max_x + 1):
    tower_y = []

    for y in range(max_y + 1):
        tower_z = []

        for z in range(max_z + 1):
            tower_z.append(None)

        tower_y.append(tower_z)

    tower.append(tower_y)


current_z_floor = [[0] * (max_y+1) for i in range(max_x + 1)]
pieces.sort(key=lambda p: p.start[2])

all_supporting_pieces = set(pieces)

for piece in pieces:
    piece.drop(current_z_floor)
    coords = piece.get_all_coords()
    supportable_coords = piece.get_supportable_coords()

    for c in coords:
        current_z_floor[c[0]][c[1]] = c[2]
        tower[c[0]][c[1]][c[2]] = piece

    supporting_pieces = set()
    for supportable_coord in supportable_coords:
        if supportable_coord[2] - 1 == 0 or tower[supportable_coord[0]][supportable_coord[1]][supportable_coord[2] - 1] is None:
            continue

        supporting_pieces.add(
            tower[supportable_coord[0]][supportable_coord[1]][supportable_coord[2] - 1])

    piece.supported_by = supporting_pieces

pieces.sort(key=lambda p: p.start[2])

total = 0

for piece in pieces:
    pieces_that_fell = set()
    falling_pieces = set()

    supporting_coords = piece.get_supporting_coords()
    for supporting_coord in supporting_coords:
        if tower[supporting_coord[0]][supporting_coord[1]][supporting_coord[2] + 1] is None:
            continue

        p = tower[supporting_coord[0]
                  ][supporting_coord[1]][supporting_coord[2] + 1]
        if len(p.supported_by) == 1:
            pieces_that_fell.add(p)
            falling_pieces.add(p)

    while falling_pieces:
        falling_piece = falling_pieces.pop()
        supporting_coords = falling_piece.get_supporting_coords()

        for supporting_coord in supporting_coords:
            if tower[supporting_coord[0]][supporting_coord[1]][supporting_coord[2] + 1] is None:
                continue

            p = tower[supporting_coord[0]][supporting_coord[1]
                                           ][supporting_coord[2] + 1]

            supporting_pieces = p.supported_by

            if len(supporting_pieces) == 1 or all(s in pieces_that_fell for s in supporting_pieces):
                pieces_that_fell.add(p)
                falling_pieces.add(p)

    total += len(pieces_that_fell)

print(total)
