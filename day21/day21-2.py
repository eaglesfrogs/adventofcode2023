import numpy
from scipy import interpolate

files = open('day21/day21data.txt', 'r')
lines = files.readlines()

total_steps = 26501365
total_full_board_steps = (total_steps - 65) / 131

starting_point = (2 * 131 + 65, 2 * 131 + 65)

board = []

# gonna build out a big extrapolated board.
# we will do a flood fill to the edge of the first square (65 steps) and count
# then do a flood fill to the next edge (+131 steps) and count
# then do a flood fill to the next edge again (131 steps) and count
# then we extrapolate the quadractic formula

for x in range(5):
    for i in range(len(lines)):
        line = lines[i].strip()
        board_line = []

        for y in range(5):
            for j in range(len(line)):
                c = line[j]
                board_line.append(c)

        board.append(board_line)


def count(start):
    total = 0

    for i in range(len(board)):
        b = board[i]
        for c in b:
            start = not start
            if c == '!' and start:
                total = total + 1

    return total


step_increments = [65, 131, 131]
total_step_increments = sum(step_increments)

queue = [[starting_point]]
board[starting_point[0]][starting_point[1]] = '!'

i = 0

pause = step_increments.pop(0)

values = []

while queue and i < total_step_increments:
    q = queue.pop()
    i += 1

    new_queue = []

    for curr in q:
        if board[curr[0] - 1][curr[1]] in ['.', 'S']:
            new_queue.append((curr[0] - 1, curr[1]))
            board[curr[0] - 1][curr[1]] = '!'
        if board[curr[0] + 1][curr[1]] in ['.', 'S']:
            new_queue.append((curr[0] + 1, curr[1]))
            board[curr[0] + 1][curr[1]] = '!'
        if board[curr[0]][curr[1] - 1] in ['.', 'S']:
            new_queue.append((curr[0], curr[1] - 1))
            board[curr[0]][curr[1] - 1] = '!'
        if board[curr[0]][curr[1] + 1] in ['.', 'S']:
            new_queue.append((curr[0], curr[1] + 1))
            board[curr[0]][curr[1] + 1] = '!'
    queue.append(new_queue)

    if i == pause:
        values.append(count(pause % 2 == 1))

        if step_increments:
            pause += step_increments.pop(0)

print(values)

# took me a minute to find a good extrapolation formula..https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/keao4q8/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button


def f(n, a, b, c): return a+n*(b-a+(n-1)*(c-b-b+a)//2)


print(f(26501365 // 131, *values))
