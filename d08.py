import re
from collections import Counter

import aoc


# Common
def parse_data(data: str) -> list[str]:
    return data.splitlines()

# Part 1
def p1(data: str, desired_wire: str = 'a') -> int:
    total_code_len = 0
    total_memory_len = 0

    escaped_hex = re.compile(r'^\\x[0-9a-fA-F]{2}')

    strings = parse_data(data)
    for string in strings:
        total_code_len += len(string)
        working = string[1:-1]
        position_stop = len(working)
        position = 0
        while position < position_stop:
            total_memory_len += 1
            if escaped_hex.match(working[position:position+4]):
                position += 4
            elif working[position:position+2] in {'\\"', '\\\\'}:
                position += 2
            else:
                position += 1

    return total_code_len - total_memory_len

# Part 2
def p2(data: str, desired_wire: str = 'a') -> int:
    raw_code_len = 0
    encoded_code_len = 0

    strings = parse_data(data)
    for string in strings:
        raw_code_len += len(string)
        c = Counter(string)
        encoded_code_len += len(string) + c['"'] + c['\\'] + 2

    return encoded_code_len - raw_code_len

# Main
if __name__ == '__main__':
    data = aoc.d08data()
    print(p1(data))
    print(p2(data))
