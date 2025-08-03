from collections import deque

import aoc


# Common
def parse_data(data: str) -> dict[str, str]:
    gates = dict()
    for line in data.splitlines():
        gate_in, gate_out = line.split(' -> ')
        gates[gate_out] = gate_in
    return gates

def get_value(wire_values: dict[str, int],
              wire: str) -> int:
    if wire.isnumeric():
        return int(wire)
    elif wire in wire_values:
        return wire_values[wire]
    else:
        return None

def process_one_part(wire_values: dict[str, int],
                     work_stack: deque[str],
                     out_wire: str,
                     gate_input: list[str]):
    left = gate_input[0]
    left_value = get_value(wire_values, left)

    if left_value is not None:
        wire_values[out_wire] = left_value
    else:
        work_stack.append(out_wire)
        work_stack.append(left)

def process_two_parts(wire_values: dict[str, int],
                      work_stack: deque[str],
                      out_wire: str,
                      gate_input: list[str]):
    op, left = gate_input
    left_value = get_value(wire_values, left)
    
    if left_value is not None:
        wire_values[out_wire] = evaluate(op, left_value, None)
    else:
        work_stack.append(out_wire)
        work_stack.append(left)

def process_three_parts(wire_values: dict[str, int],
                        work_stack: deque[str],
                        out_wire: str,
                        gate_input: list[str]):
    left, op, right = gate_input
    left_value = get_value(wire_values, left)
    right_value = get_value(wire_values, right)

    if left_value is not None and right_value is not None:
        wire_values[out_wire] = evaluate(op, left_value, right_value)
    else:
        work_stack.append(out_wire)
        if left_value is None:
            work_stack.append(left)
        if right_value is None:
            work_stack.append(right)

def evaluate(op: str,left: int, right: int) -> int:
    match op:
        case 'AND': return left & right
        case 'OR': return left | right
        case 'LSHIFT': return left * (2**right) % 2**16
        case 'RSHIFT': return left // (2**right)
        case 'NOT': return (~left) % (2**16)

def process_work(gates, wire_values, work_stack):
    while work_stack:
        out_wire = work_stack.pop()
        if out_wire in wire_values: continue
        gate_input = gates[out_wire].split()
        match len(gate_input):
            case 3:
                process_three_parts(wire_values, work_stack, out_wire, gate_input)
            case 2:
                process_two_parts(wire_values, work_stack, out_wire, gate_input)
            case 1:
                process_one_part(wire_values, work_stack, out_wire, gate_input)

# Part 1
def p1(data: str, desired_wire: str = 'a') -> int:
    gates = parse_data(data)
    wire_values: dict[str, int] = dict()
    work_stack: deque[str] = deque([desired_wire])
    process_work(gates, wire_values, work_stack)

    return wire_values[desired_wire]

# Part 2
def p2(data: str, desired_wire: str = 'a') -> int:
    gates = parse_data(data)
    wire_values: dict[str, int] = dict()
    work_stack: deque[str] = deque([desired_wire])
    process_work(gates, wire_values, work_stack)
    
    wire_values = {'b': wire_values[desired_wire]}
    work_stack.append(desired_wire)
    process_work(gates, wire_values, work_stack)
    
    return wire_values[desired_wire]

# Main
if __name__ == '__main__':
    data = aoc.d07data()
    print(p1(data, 'a'))
    print(p2(data, 'a'))
