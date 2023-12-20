from typing import List
from math import lcm


files = open('day20/day20data.txt', 'r')
lines = files.readlines()


class Broadcaster:

    def __init__(self, dest: List[str]) -> None:
        self.dest = dest

    def process(self, input, src=None):
        return (input, self.dest)


class FlipFlop:

    def __init__(self, dest: List[str]) -> None:
        self.dest = dest
        self.state = 'off'

    def process(self, input, src=None):
        if input == 'high':
            return None

        if self.state == 'off':
            self.state = 'on'
            return ('high', self.dest)

        self.state = 'off'
        return ('low', self.dest)


class Conjunction:

    def __init__(self, dest: List[str]) -> None:
        self.dest = dest
        self.connections = {}

    def process(self, input, src=None):
        self.connections[src] = input

        if all(v == 'high' for v in self.connections.values()):
            return ('low', self.dest)

        return ('high', self.dest)


step_board = {}
conjunction_ids = []
for line in lines:
    line = line.strip()
    line_segs = line.split(' -> ')
    dest = line_segs[1].split(', ')

    if line_segs[0][0] == '%':
        id = line_segs[0][1:]
        step = FlipFlop(dest)
    elif line_segs[0][0] == '&':
        id = line_segs[0][1:]
        step = Conjunction(dest)
        conjunction_ids.append(id)
    else:
        id = 'broadcaster'
        step = Broadcaster(dest)

    step_board[id] = step

for id in step_board:
    step = step_board[id]
    for d in step.dest:
        if d in conjunction_ids:
            step_board[d].connections[id] = 'low'

start_pulse = ('low', 'broadcaster', None)

low_total = 0
high_total = 0
presses = 0

rx_pressed = False

counts = {
    'lm': 0,
    'dh': 0,
    'sg': 0,
    'db': 0
}

while not rx_pressed:
    pulses = [start_pulse]
    low_total += 1
    presses += 1

    while pulses:
        pulse = pulses.pop(0)
        pulse_val = pulse[0]
        pulse_dest = pulse[1]
        pulse_src = pulse[2]

        result = step_board[pulse_dest].process(pulse_val, pulse_src)

        if pulse_dest == 'jm' and pulse_val == 'high':
            counts[pulse_src] = presses

            if 0 not in counts.values():
                print(counts)
                print(lcm(*(counts.values())))
                exit()

        if result:
            result_pulse_val = result[0]
            result_pulse_dest = result[1]

            for r_dest in result_pulse_dest:
                if result_pulse_val == 'low':
                    low_total += 1
                elif result_pulse_val == 'high':
                    high_total += 1

                if r_dest in step_board:
                    pulses.append((result_pulse_val, r_dest, pulse_dest))
                else:
                    if result_pulse_val == 'low':
                        rx_pressed = True
