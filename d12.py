import json
import re

import aoc


# Common
def parse_data(data: str):
    result = json.loads(data)
    return result

# Part 1
def p1(data: str) -> str:
    return sum(map(int, re.findall(r'-?\d+', data)))

# Part 2
def sum_thing(thing: list | dict | str | int) -> int:
    if isinstance(thing, list):
        return sum(sum_thing(x) for x in thing)
    elif isinstance(thing, dict):
        if 'red' in thing.values():
            return 0
        else:
            return sum(sum_thing(x) for x in thing.values())
    elif isinstance(thing, str):
        return 0
    elif isinstance(thing, int):
        return thing

    return 0

def p2(data: str) -> int:
    thing = parse_data(data)
    result = sum_thing(thing)
    return result

# Main
if __name__ == '__main__':
    data = aoc.d12_data()
    print(p1(data))
    print(p2(data))
