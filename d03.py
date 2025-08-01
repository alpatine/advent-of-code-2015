from collections import defaultdict
import aoc

def p1(data: str) -> int:
    visited: dict[tuple[int, int], int] = defaultdict(int)
    x: int = 0
    y: int = 0

    #starting position
    visited[(0,0)] += 1
    x = y = 0
    
    for move in data:
        match move:
            case '^': y += 1
            case '>': x += 1
            case 'v': y -= 1
            case '<': x -= 1
        visited[(x, y)] += 1
    
    return len(visited)

def p2(data: str) -> int:
    visited: dict[tuple[int, int], int] = defaultdict(int)
    movers = [(0,0), (0,0)]
    turn = 0

    visited[(0,0)] += 1

    for move in data:
        x, y = movers[turn]
        match move:
            case '^': y += 1
            case '>': x += 1
            case 'v': y -= 1
            case '<': x -= 1
        visited[(x, y)] += 1
        movers[turn] = (x, y)
        turn = (turn + 1) % 2
    
    return len(visited)

if __name__ == '__main__':
    data = aoc.d03data()
    print(p1(data))
    print(p2(data))
