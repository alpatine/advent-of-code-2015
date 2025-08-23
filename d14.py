import re
from collections import defaultdict, namedtuple

import aoc

# Common
Reindeer = namedtuple('Reindeer', 'name, speed, fly_time, rest_time')

def parse_data(data: str) -> list[Reindeer]:
    reindeer = list()
    for line in data.splitlines():
        name, speed, fly_time, rest_time = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line).group(1, 2, 3, 4)
        reindeer.append(Reindeer(name, int(speed), int(fly_time), int(rest_time)))

    return reindeer

def calculate_distance(time_passed: int, speed: int, fly_time: int, rest_time: int) -> int:
    total_time = fly_time + rest_time
    cycles, remainder = divmod(time_passed, total_time)
    distance = speed * (cycles * fly_time + min(remainder,  fly_time))
    return distance

# Part 1
def p1(data: str, time_passed: int = 2503) -> int:
    all_reindeer = parse_data(data)
    distances = list()
    for reindeer in all_reindeer:
        distances.append(calculate_distance(time_passed, *reindeer[1:]))
    
    return max(distances)

# Part 2
def p2(data: str, time_passed: int = 2503) -> int:
    all_reindeer = parse_data(data)
    scores: dict[str, int] = defaultdict(int)
    for time in range(1, time_passed + 1):
        distances: dict[int, list[str]] = defaultdict(list)
        max_dist = 0
        for reindeer in all_reindeer:
            distance = calculate_distance(time, *reindeer[1:])
            if distance >= max_dist:
                distances[distance].append(reindeer.name)
                max_dist = distance
        for name in distances[max_dist]:
            scores[name] += 1
    
    return max(scores.values())

# Main
if __name__ == '__main__':
    data = aoc.d14_data()
    print(p1(data))
    print(p2(data))
