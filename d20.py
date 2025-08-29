from collections import defaultdict

import aoc


# Common
def parse_data(data: str) -> int:
    return int(data)

# Part 1
def p1(data: str) -> int:
    wanted_presents = parse_data(data)
    
    visitors = defaultdict(list)
    house_number = 1
    while True:
        visitors[house_number].append(house_number)
        presents = 10 * sum(visitors[house_number])
        if presents >= wanted_presents:
            return house_number
        
        for visitor in visitors[house_number]:
            visitors[house_number + visitor].append(visitor)
        del visitors[house_number]
        house_number += 1

# Part 2
def p2(data: str) -> int:
    wanted_presents = parse_data(data)
    
    visitors = defaultdict(list)
    houses_visited = defaultdict(int)
    house_number = 1
    while True:
        visitors[house_number].append(house_number)
        presents = 11 * sum(visitors[house_number])
        if presents >= wanted_presents:
            return house_number
        
        for visitor in visitors[house_number]:
            houses_visited[visitor] += 1
            if houses_visited[visitor] == 50:
                continue
            visitors[house_number + visitor].append(visitor)
        del visitors[house_number]
        house_number += 1

# Main
if __name__ == '__main__':
    data = aoc.d20_data()
    print(p1(data))
    print(p2(data))
