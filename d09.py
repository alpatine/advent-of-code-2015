from itertools import pairwise, permutations

import aoc


# Common
def parse_data(data: str) -> tuple[list[str], dict[tuple[str, str], int]]:
    places = set()
    distances = dict()

    for line in data.splitlines():
        start_and_finish, distance = line.split(" = ")
        start, finish = start_and_finish.split(" to ")
        places.add(start)
        places.add(finish)
        distances[(start, finish)] = int(distance)
        distances[(finish, start)] = int(distance)
    
    return (list(places), distances)

# Part 1
def p1(data: str) -> int:
    places, distances = parse_data(data)
    shortest_route_length = sum(distances.values())

    for route in permutations(places):
        route_distance = 0
        for pair in pairwise(route):
            route_distance += distances[pair]
        if route_distance < shortest_route_length:
            shortest_route_length = route_distance
    
    return shortest_route_length

# Part 2
def p2(data: str) -> int:
    places, distances = parse_data(data)
    longest_route_length = 0

    for route in permutations(places):
        route_distance = 0
        for pair in pairwise(route):
            route_distance += distances[pair]
        if route_distance > longest_route_length:
            longest_route_length = route_distance
    
    return longest_route_length

# Main
if __name__ == '__main__':
    data = aoc.d09_data()
    print(p1(data))
    print(p2(data))
