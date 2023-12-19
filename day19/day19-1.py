files = open('day19/day19data.txt', 'r')
lines = files.readlines()

operations = {}
parts = []


def get_gt_func(val):
    return lambda x: x > val


def get_lt_func(val):
    return lambda x: x < val


for line in lines:
    line = line.strip()

    if line == '':
        continue

    if line[0] == '{':
        line = line.replace('{', '').replace('}', '')
        vals = line.split(',')
        parts.append({
            'x': int(vals[0][2:]),
            'm': int(vals[1][2:]),
            'a': int(vals[2][2:]),
            's': int(vals[3][2:])
        })
    else:
        chunks = line.split('{')
        label = chunks[0]
        ops = chunks[1].replace('}', '').split(',')
        op_chain = []
        for op in ops:
            op_data = None
            op_function = None
            op_target = None

            if ':' in op:
                op_pieces = op.split(':')
                op_target = op_pieces[1]

                if '>' in op_pieces[0]:
                    op_comp_vals = op_pieces[0].split('>')
                    op_data = op_comp_vals[0]
                    op_function = get_gt_func(int(op_comp_vals[1]))
                else:
                    op_comp_vals = op_pieces[0].split('<')
                    op_data = op_comp_vals[0]
                    op_function = get_lt_func(int(op_comp_vals[1]))
            else:
                op_target = op

            op_chain.append({
                'data': op_data,
                'function': op_function,
                'target': op_target
            })
        operations[label] = op_chain

accepted = []

for part in parts:
    print(part)

    ops = operations['in']
    i = 0

    while True:
        op = ops[i]
        i += 1

        if op['data'] == None and op['function'] == None and op['target'] == 'A':
            accepted.append(part)
            break
        if op['data'] == None and op['function'] == None and op['target'] == 'R':
            break

        if op['data'] == None and op['function'] == None:
            ops = operations[op['target']]
            i = 0
        else:
            data = op['data']
            function = op['function']
            result = function(part[data])

            if result and op['target'] == 'A':
                accepted.append(part)
                break
            if result and op['target'] == 'R':
                break
            if result:
                ops = operations[op['target']]
                i = 0

total = 0
for a in accepted:
    total += a['x']
    total += a['m']
    total += a['a']
    total += a['s']

print(total)
