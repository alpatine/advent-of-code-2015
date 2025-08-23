import re

import aoc


# Common
def parse_data(data: str) -> str:
    sues = list()
    for line in data.splitlines():
        number, thing1, thing1_num, thing2, thing2_num, thing3, thing3_num = re.match(r'^Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)$', line).group(1, 2, 3, 4, 5, 6, 7)
        sue = {'number': int(number),
               thing1: int(thing1_num),
               thing2: int(thing2_num),
               thing3: int(thing3_num)}
        sues.append(sue)
    return sues

# Part 1
def filter_sues(sues:list[dict[str, int]], filter: dict[str, int]) -> list[int]:
    result = list()
    for sue in sues:
        keep_sue = True
        for filter_k, filter_v in filter.items():
            if filter_k in sue and filter_v != sue[filter_k]:
                keep_sue = False
        if keep_sue:
            result.append(sue['number'])

    return result

def p1(data: str) -> int:
    sues = parse_data(data)
    filter = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
              'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
    possible_sues = filter_sues(sues, filter)
    return possible_sues

# Part 2
def filter_sues2(sues:list[dict[str, int]], filter: dict[str, int]) -> list[int]:
    result = list()
    for sue in sues:
        keep_sue = True

        for thing in sue.keys() & filter.keys():
            if thing in ('cats', 'trees'):
                if not sue[thing] > filter[thing]:
                    keep_sue = False
            elif thing in ('pomeranians', 'goldfish'):
                if not sue[thing] < filter[thing]:
                    keep_sue = False
            else:
                if sue[thing] != filter[thing]:
                    keep_sue = False
                    
        if keep_sue:
            result.append(sue['number'])

    return result

def p2(data: str) -> int:
    sues = parse_data(data)
    filter = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
              'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
    possible_sues = filter_sues2(sues, filter)
    return possible_sues

# Main
if __name__ == '__main__':
    data = aoc.d16_data()
    print(p1(data))
    print(p2(data))
