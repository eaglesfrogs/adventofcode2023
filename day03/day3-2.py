import re


files = open('day03/day3data.txt', 'r')
lines = files.readlines()

for i in range(len(lines)):
  lines[i] = re.sub('[^0-9*.]', '.', lines[i].strip())

total = 0

# sample data does not have a star in the first row, last row, or the first/last 3 columns so skipping all those error checks
for i in range(1, len(lines) - 1):
  line = lines[i]

  for j in range(len(line)):
    prev_line = lines[i - 1]
    next_line = lines[i + 1]

    matrix = []

    if line[j] == '*':
      matrix.append(prev_line[j - 3: j + 4])
      matrix.append(line[j - 3: j + 4])
      matrix.append(next_line[j -3: j + 4])

      line1s = re.finditer('[0-9]+', matrix[0])
      line2s = re.finditer('[0-9]+', matrix[1])
      line3s = re.finditer('[0-9]+', matrix[2])

      valid_numbers = []

      for l in line1s:
        if (l.start() >= 2 and l.start() <= 4) or (l.end() >= 3 and l.end() <= 5):
          valid_numbers.append(int(l[0]))

      for l in line2s:
        if l.end() == 3 or l.start() == 4:
          valid_numbers.append(int(l[0]))

      for l in line3s:
        if (l.start() >= 2 and l.start() <= 4) or (l.end() >= 3 and l.end() <= 5):
          valid_numbers.append(int(l[0]))

      if len(valid_numbers) == 2:
        total = total + (valid_numbers[0] * valid_numbers[1])

print(total)
