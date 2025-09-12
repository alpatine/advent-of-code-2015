from math import prod

import aoc


# Common
def parse_data(data: str) -> list[int]:
    return list(map(int, data.splitlines()))

def find_groups(weights: tuple[int, ...], target: int) -> list[list[int]]:
    
    weights_total = sum(weights)
    weights_count = len(weights)
    table: list[list[tuple[int,int,list[int]]]] = [[] for _ in range(target+1)]
    table[0].append((0,weights_total,[]))

    for pos in range(target):
        for next_weight_pos, reachable, sequence in table[pos]:
            for weight_pos in range(next_weight_pos, weights_count):
                if reachable < target:
                    break
                weight = weights[weight_pos]
                target_pos = pos + weight
                if target_pos <= target:
                    table[target_pos].append((weight_pos + 1, reachable, sequence + [weight]))
                reachable -= weight

    result = [x[2] for x in table[target]]
    return result

# Part 1
def p1(data: str) -> int:
    weights = tuple(sorted(parse_data(data), reverse=True))
    total_weight = sum(weights)
    target_group_weight = total_weight // 3
    
    all_groups = find_groups(weights, target_group_weight)
    sortable_groups = [(len(g), prod(g), g) for g in all_groups]
    sortable_groups.sort()

    for num_packages, quantum_entanglement, sequence in sortable_groups:
        remaining_weights = tuple(sorted(set(weights) - set(sequence), reverse=True))
        possible_second_groups = find_groups(remaining_weights, target_group_weight)
        if len(possible_second_groups) > 0:
            return quantum_entanglement    

# Part 2
def p2(data: str) -> int:
    weights = tuple(sorted(parse_data(data), reverse=True))
    total_weight = sum(weights)
    target_group_weight = total_weight // 4
    
    all_groups = find_groups(weights, target_group_weight)
    sortable_groups = [(len(g), prod(g), g) for g in all_groups]
    sortable_groups.sort()

    # Repeating code is ugly, but it's a quick path to solving part 2.
    for num_packages_g1, quantum_entanglement_g1, sequence_g1 in sortable_groups:
        remaining_weights_g2 = tuple(sorted(set(weights) - set(sequence_g1), reverse=True))
        all_second_groups = find_groups(remaining_weights_g2, target_group_weight)
        sorted_second_groups = [(len(g), prod(g), g) for g in all_second_groups]
        sorted_second_groups.sort()
        if len(sorted_second_groups) > 0:
            for num_packages_g2, quantum_entanglement_g2, sequence_g2 in sorted_second_groups:
                remaining_weights_g3 = tuple(sorted(set(remaining_weights_g2) - set(sequence_g2), reverse=True))
                possible_third_groups = find_groups(remaining_weights_g3, target_group_weight)
                if len(possible_third_groups) > 0:
                    return quantum_entanglement_g1    
    
# Main
if __name__ == '__main__':
    data = aoc.d24_data()
    print(p1(data))
    print(p2(data))
