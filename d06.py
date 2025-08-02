import re

import aoc

# Common
def parse_data(data: str) -> list[tuple[str, int, int, int, int]]:
    operations = list()
    extract_pattern = re.compile(r'(?:turn (on|off)|(toggle)) (\d+),(\d+) through (\d+),(\d+)')
    for line in data.splitlines():
        values = extract_pattern.match(line)
        operations.append((
            values.group(1) or values.group(2),
            *values.group(3, 4, 5, 6)
        ))
    return operations

# Part 1
def build_grid_1(rows: int, cols: int) -> list[list[bool]]:
    return [[False for c in range(cols)] for r in range(rows)]

def apply_instruction_1(grid: list[list[bool]],
                      instruction: tuple[str, int, int, int, int]) -> None:
    match instruction[0]:
        case 'on': action = lambda x: True
        case 'off': action = lambda x: False
        case 'toggle': action = lambda x: not x

    (start_x, start_y, end_x, end_y) = map(int, instruction[1:])

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            grid[x][y] = action(grid[x][y])

def p1(data: str) -> int:
    instructions = parse_data(data)
    grid = build_grid_1(1000, 1000)
    for i in instructions:
        apply_instruction_1(grid, i)
    lights_lit = sum(sum(c for c in r) for r in grid)
    return lights_lit

# Part 2
def build_grid_2(rows: int, cols: int) -> list[list[int]]:
    return [[0 for c in range(cols)] for r in range(rows)]

def apply_instruction_2(grid: list[list[bool]],
                      instruction: tuple[str, int, int, int, int]) -> None:
    match instruction[0]:
        case 'on': action = lambda x: x + 1
        case 'off': action = lambda x: max(x - 1, 0)
        case 'toggle': action = lambda x: x + 2

    (start_x, start_y, end_x, end_y) = map(int, instruction[1:])

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            grid[x][y] = action(grid[x][y])

def p2(data: str) -> int:
    instructions = parse_data(data)
    grid = build_grid_2(1000, 1000)
    for i in instructions:
        apply_instruction_2(grid, i)
    lights_lit = sum(sum(c for c in r) for r in grid)
    return lights_lit

# Main
if __name__ == '__main__':
    data = aoc.d06data()
    print(p1(data))
    print(p2(data))
