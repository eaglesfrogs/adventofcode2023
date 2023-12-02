import re

files = open('day02/day2data.txt', 'r')
lines = files.readlines()


class Game:
    def __init__(self, id) -> None:
        self.id = id
        self.groups = []

    def valid(self, max_red, max_green, max_blue):
        for group in self.groups:
            if group['red'] > max_red or group['green'] > max_green or group['blue'] > max_blue:
                return False

        return True

    def power(self):
        min_red = 0
        min_green = 0
        min_blue = 0

        for group in self.groups:
            if group['red'] > min_red:
                min_red = group['red']
            if group['green'] > min_green:
                min_green = group['green']
            if group['blue'] > min_blue:
                min_blue = group['blue']

        return min_red * min_green * min_blue


games = []


for line in lines:
    line_split = line.split(':')
    game_header = line_split[0]

    game_id = int(game_header.split(' ')[1])

    game = Game(game_id)

    game_pulls_split = line_split[1].strip().split(';')

    for game_pull in game_pulls_split:
        result = re.findall(
            r'([0-9]+ red|[0-9]+ green|[0-9]+ blue)', game_pull)
        pull = {
            'red': 0, 'green': 0, 'blue': 0
        }

        for r in result:
            if 'red' in r:
                pull['red'] = int(r.split(' ')[0])
            if 'green' in r:
                pull['green'] = int(r.split(' ')[0])
            if 'blue' in r:
                pull['blue'] = int(r.split(' ')[0])

        game.groups.append(pull)

    games.append(game)

total = 0
total_power = 0
for game in games:
    if game.valid(12, 13, 14):
        total = total + game.id

    total_power = total_power + game.power()

print("Answer to part 1 is: ")
print(total)

print("Answer for total power is ")
print(total_power)
