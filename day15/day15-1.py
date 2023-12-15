files = open('day15/day15data.txt', 'r')
lines = files.readlines()

codes = lines[0].split(',')


def calculate_code_num(code):
    num = 0

    for c in code:
        ascii_num = ord(c)

        num += ascii_num
        num = num * 17
        num = num % 256

    return num


total = 0
for code in codes:
    total += calculate_code_num(code)

print(total)
