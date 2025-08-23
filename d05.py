from collections import Counter
from itertools import pairwise

import aoc


def parseData(data: str) -> list[str]:
    return data.splitlines()

def has_three_vowels(s: str) -> bool:
    counter = Counter(s)
    vowel_count = sum(counter[v] for v in 'aeiou')
    return vowel_count >= 3

def has_double_letter(s: str) -> bool:
    prev_c = str()
    for c in s:
        if c == prev_c:
            return True
        prev_c = c
    return False

def has_bad_string(s: str) -> bool:
    for bad_s in ['ab', 'cd', 'pq', 'xy']:
        if bad_s in s:
            return True
    return False

def is_nice(s: str) -> bool:
    return has_three_vowels(s) and has_double_letter(s) and not has_bad_string(s)

def has_pair_twice(s: str) -> bool:
    pair_counter = Counter()
    prev_pair = ''

    for pair in pairwise(s):
        if pair != prev_pair:
            pair_counter[pair] += 1
        prev_pair = pair
    
    return pair_counter.most_common()[0][1] >= 2

def has_skip_repeat(s: str) -> bool:
    for pos in range(2, len(s)):
        if s[pos - 2] == s[pos]: return True

    return False

def is_nice2(s: str) -> bool:
    return has_pair_twice(s) and has_skip_repeat(s)

def p1(data: str) -> int:
    strings = parseData(data)
    count = sum(map(is_nice, strings))
    return count

def p2(data: str) -> int:
    strings = parseData(data)
    count = sum(map(is_nice2, strings))
    return count

if __name__ == '__main__':
    data = aoc.d05_data()
    print(p1(data))
    print(p2(data))
