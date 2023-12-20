import copy

files = open('day19/day19data.txt', 'r')
lines = files.readlines()

operations = {}


def get_gt_func(val):
    def gt_func(x_range):
        if x_range[1] < val:
            return False

        return (val + 1, x_range[1])

    return gt_func


def get_lt_func(val):
    def lt_func(x_range):
        if val < x_range[0]:
            return False

        return (x_range[0], val - 1)

    return lt_func


for line in lines:
    line = line.strip()

    if line == '':
        continue

    if line[0] == '{':
        pass
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
        operations[label] = {
            'op_chain': op_chain,
            'range': None
        }

accepted = []

start = operations['in']
start['range'] = { 'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
process_nodes = [start]

while process_nodes:
    operation = process_nodes.pop()
    r = operation['range']
    op_chain = operation['op_chain']

    for op in op_chain:
        if op['data'] == None and op['function'] == None and op['target'] == 'A':
            accepted.append(r)
        elif op['data'] == None and op['function'] == None and op['target'] == 'R':
            pass
        elif op['data'] == None and op['function'] == None:
            ops = operations[op['target']]
            ops['range'] = r
            process_nodes.append(ops)
        else:
            data = op['data']
            function = op['function']
            result = function(r[data])

            if not result:
                continue

            accepted_result = copy.copy(r)
            accepted_result[data] = result

            if result[1] == r[data][1]:
                r[data] = (r[data][0], result[0] - 1)
            else:
                r[data] = (result[1] + 1, r[data][1])

            if result and op['target'] == 'A':
                accepted.append(accepted_result)
            elif result and op['target'] == 'R':
                pass
            elif result:
                ops = operations[op['target']]
                ops['range'] = accepted_result
                process_nodes.append(ops)

total = 0
for ac in accepted:
    x = ac['x'][1] - ac['x'][0] + 1
    m = ac['m'][1] - ac['m'][0] + 1
    a = ac['a'][1] - ac['a'][0] + 1
    s = ac['s'][1] - ac['s'][0] + 1
    total += x*m*a*s

print(total)
