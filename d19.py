import re
import sys
from collections import defaultdict

import aoc

# Common
Mapping = defaultdict[str, list[str]]

def parse_data(data: str) -> tuple[Mapping, str]:
    replacements, molocule = data.split('\n\n')
    mapping: Mapping = defaultdict(list)
    for line in replacements.splitlines():
        source, target = line.split(' => ')
        mapping[source].append(target)
    
    return mapping, molocule

# Part 1
def calibrate(mapping: Mapping, base_molecule: str) -> set[str]:
    molecules: set[str] = set()
    for source, targets in mapping.items():
        source_positions = [m.start() for m in re.finditer(source, base_molecule)]
        for target in targets:
            for position in source_positions:
                new_molecule = base_molecule[:position] + target + base_molecule[position+len(source):]
                molecules.add(new_molecule)
    
    return molecules

def p1(data: str) -> int:
    mapping, molecule = parse_data(data)
    molecules = calibrate(mapping, molecule)
    return len(molecules)

# Part 2
def reverse_mapping(mapping: Mapping) -> dict[str, str]:
    result = dict()
    for source, targets in mapping.items():
        for target in targets:
            result[target[::-1]] = source[::-1]
    return result

def manufacture(mapping: dict[str, str], base_molecule: str, wanted_molecule: str) -> int:
    steps = 0
    molecule = base_molecule
    while molecule != wanted_molecule:
        # Find the earliest possible replacement
        earliest_replacement = (sys.maxsize, '', '')
        for source, target in mapping.items():
            if source in molecule:
                position = molecule.index(source)
                replacement = (position, source, target)
                if replacement < earliest_replacement:
                    earliest_replacement = replacement
        
        # Do the replacement
        molecule = molecule.replace(earliest_replacement[1], earliest_replacement[2], 1)
        steps += 1
    
    return steps

def p2(data: str) -> int:
    # A recursive depth first trial of growing the molecule from 'e' did not
    # work. A recursive depth first trial of replacements from the left did not
    # work.
    #    
    # Exploration:
    # 
    # Rn, Ar, Y, C are tokens on the right but not on the left of any mapping
    # rule,meaning once they appear they will not be replaced. Replacing all of
    # the tokens on the left with x yields the following unique outputs on the
    # right: xx, xRnxAr, xRnxYxAr, CRnxAr, CRnxYxYxAr, CRnxYxAr.
    # 
    # Forward replacements done in a position will replace the term at that
    # position and grow the string to the right of that position. Nothing to the
    # left of that position is changed, and it should not be changed when trying
    # to reverse the mapping. Given all of this, this algorithm reverses all of
    # the strings to effectively find the right-most possible replacement and
    # then makes it, iterating on this until 'e' is reached. This does not solve
    # the examples given.

    mapping, base_molecule = parse_data(data)
    reverse_map = reverse_mapping(mapping)
    steps = manufacture(reverse_map, base_molecule[::-1], 'e')
    return steps

# Main
if __name__ == '__main__':
    data = aoc.d19_data()
    print(p1(data))
    print(p2(data))
