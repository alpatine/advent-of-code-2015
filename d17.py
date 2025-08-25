import aoc


# Common
def parse_data(data: str) -> list[int]:
    return [int(line) for line in data.splitlines()]

# Part 1
def count_combinations(buckets: tuple[int, ...], target: int) -> int:
    num_buckets = len(buckets)
    if target < 0: return 0
    if num_buckets == 0:
        if target == 0:
            return 1
        else:
            return 0
    
    result = 0

    # Case: The first bucket is not used
    result += count_combinations(buckets[1:], target)

    # Case: The first bucket is used
    result += count_combinations(buckets[1:], target - buckets[0])

    return result

def p1(data: str, target: int) -> int:
    buckets = parse_data(data)
    buckets.sort()
    combos = count_combinations(tuple(buckets), target)
    return combos

# Part 2
def count_combinations2(buckets: tuple[int, ...], target: int, already_used: int) -> tuple[int, int]:
    num_buckets = len(buckets)
    if target < 0: return already_used, 0
    if num_buckets == 0:
        if target == 0:
            return already_used, 1
        else:
            return already_used, 0
    
    # Case: The first bucket is not used
    used1, result1 = count_combinations2(buckets[1:], target, already_used)

    # Case: The first bucket is used
    used2, result2 = count_combinations2(buckets[1:], target - buckets[0], already_used + 1)

    match  result1, result2:
        case 0,0: return 0,0
        case _,0: return used1, result1
        case 0,_: return used2, result2
        case _,_:
            if used1 < used2: return used1, result1
            elif used2 < used1: return used2, result2
            else: return used1, result1 + result2

def p2(data: str, target: int) -> int:
    buckets = parse_data(data)
    buckets.sort()
    min_buckets, combos = count_combinations2(tuple(buckets), target, 0)
    return combos

# Main
if __name__ == '__main__':
    data = aoc.d17_data()
    print(p1(data, 150))
    print(p2(data, 150))
