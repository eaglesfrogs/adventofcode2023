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
boxes = {}

for i in range(256):
    boxes[i] = []

for code in codes:
    if '-' in code:
        label = code[:-1]
        label_code_num = calculate_code_num(label)

        box_contents = boxes[label_code_num]
        new_box_contents = []

        for content in box_contents:
            if content[0] != label:
                new_box_contents.append(content)

        boxes[label_code_num] = new_box_contents
    else:
        label = code.split('=')[0]
        label_code_num = calculate_code_num(label)
        lense = int(code.split('=')[1])
        lense_tuple = (label, lense)

        box_contents = boxes[label_code_num]

        found = False
        for i in range(len(box_contents)):
            box_content = box_contents[i]
            if box_content[0] == label:
                box_contents[i] = lense_tuple
                found = True

        if not found:
            box_contents.append(lense_tuple)

total = 0

for i in range(256):
    box_content = boxes[i]

    for j in range(len(box_content)):
        lense_tuple = box_content[j]

        total += (i + 1) * (j + 1) * (lense_tuple[1])

print(total)
