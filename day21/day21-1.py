files = open('day21/day21data.txt', 'r')
lines = files.readlines()

total_steps = 64

starting_point = None

board = []

for i in range(len(lines)):
    line = lines[i].strip()
    board_line = []

    for j in range(len(line)):
        c = line[j]
        if c == 'S':
            board_line.append('.')
            starting_point = (i, j)
        else:
            board_line.append(c)

    board.append(board_line)

print(starting_point)

# flood fill
queue = [[starting_point]]
board[starting_point[0]][starting_point[1]] = '!'

i = 0

while queue and i < total_steps:
    q = queue.pop()
    i += 1

    new_queue = []

    for curr in q:
        if board[curr[0] - 1][curr[1]] == '.':
            new_queue.append((curr[0] - 1, curr[1]))
            board[curr[0] - 1][curr[1]] = '!'
        if board[curr[0] + 1][curr[1]] == '.':
            new_queue.append((curr[0] + 1, curr[1]))
            board[curr[0] + 1][curr[1]] = '!'
        if board[curr[0]][curr[1] - 1] == '.':
            new_queue.append((curr[0], curr[1] - 1))
            board[curr[0]][curr[1] - 1] = '!'
        if board[curr[0]][curr[1] + 1] == '.':
            new_queue.append((curr[0], curr[1] + 1))
            board[curr[0]][curr[1] + 1] = '!'
    queue.append(new_queue)


def odd_lambda(a): return a % 2 == 1
def even_lambda(a): return a % 2 == 0


character_eval_function = even_lambda
total = 0

starting_spot = 'even'
if starting_point[1] % 2 == 1:
    starting_spot = 'odd'

if total_steps % 2 == 1:
    starting_spot = 'even' if starting_spot == 'odd' else 'odd'

for steps in range(total_steps + 1):
    if steps % 2 == 0 and starting_spot == 'even':
        character_eval_function = even_lambda
    elif steps % 2 == 0 and starting_spot == 'odd':
        character_eval_function = odd_lambda
    elif steps % 2 == 1 and starting_spot == 'even':
        character_eval_function = odd_lambda
    else:
        character_eval_function = even_lambda

    lines_to_parse = []

    if steps == 0:
        lines_to_parse.append(board[starting_point[0]])
    else:
        lines_to_parse.append(board[starting_point[0] - steps])
        lines_to_parse.append(board[starting_point[0] + steps])

    for line in lines_to_parse:
        for j in range(len(line)):
            if line[j] == '!' and character_eval_function(j):
                total += 1

print(total)
