from collections import Counter

import aoc


def p1(data: str) -> int:
    c = Counter(data)
    return c['('] - c[')']

def p2(data: str) -> int:
    floor = 0
    for i, c in enumerate(data):
        match c:
            case '(': floor += 1
            case ')': floor -= 1
        if floor == -1:
            return i + 1

if __name__ == '__main__':
    data = aoc.d01data()
    print(p1(data))
    print(p2(data))
