import re
from collections import defaultdict
from itertools import pairwise, permutations
from typing import Generator

import aoc


# Common
def parse_data(data: str) -> tuple[list[str], defaultdict[str, defaultdict[str, int]]]:
    people_map = defaultdict(lambda: defaultdict(int))
    for line in data.splitlines():
        person, change, amount, neighbour = re.match(r'^(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).', line).group(1, 2, 3, 4)
        
        amount = int(amount)
        if change == 'lose':
            amount = -amount
        
        people_map[person][neighbour] = amount
    
    return list(people_map.keys()), people_map

def non_cyclic_permutations(items: list[str]) -> Generator[list[str], None, None]:
    last = items.pop()
    for perm in permutations(items, len(items)):
        yield list(perm) + [last]

def find_highest_score(names: list[str], people_map: defaultdict[str, defaultdict[str, int]]):
    highest_score = 0
    for arrangement in non_cyclic_permutations(names):
        first = arrangement[0]
        last = arrangement[-1]
        score = people_map[first][last] + people_map[last][first]        
        for left, right in pairwise(arrangement):
            score += people_map[left][right]
            score += people_map[right][left]
        if score > highest_score:
            highest_score = score
    return highest_score
        
# Part 1
def p1(data: str) -> int:
    names, people_map = parse_data(data)
    highest_score = find_highest_score(names, people_map)
    return highest_score

# Part 2
def p2(data: str) -> int:
    names, people_map = parse_data(data)
    names.append('yourself')
    highest_score = find_highest_score(names, people_map)
    return highest_score

# Main
if __name__ == '__main__':
    data = aoc.d13data()
    print(p1(data))
    print(p2(data))
