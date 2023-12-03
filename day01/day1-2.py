import re


files = open('day01/day1data.txt', 'r')
lines = files.readlines()

total = 0

nummap = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

regex = r'([0-9]|one|two|three|four|five|six|seven|eight|nine)'

for line in lines:
    line = line.strip()

    result = re.findall(regex, line)

    firstchar = result[0]

    backwards_line = ''
    for i in range(len(line)):
        backwards_line = line[(-1 * i) - 1] + backwards_line
        result = re.findall(regex, backwards_line)

        if result:
            secondchar = result[0]
            break

    if len(firstchar) > 1:
        firstchar = nummap[firstchar]
    if len(secondchar) > 1:
        secondchar = nummap[secondchar]

    total = total + int(firstchar + secondchar)

print(total)
