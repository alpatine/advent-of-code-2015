import re

import aoc


# Common
def parse_data(data: str) -> tuple[int, int]:
    row, col = re.match(r'To continue, please consult the code grid in the manual\.  Enter the code at row (\d+), column (\d+)\.', data).group(1, 2)
    return int(row), int(col)

def T(n: int) -> int:
    if n < 1:
        return 0
    return (n * (n+1) // 2)

def calc_cell_number(row: int, col: int) -> int:
    if row < 1 or col < 1:
        return 0
    elif row == 1:
        return T(col)
    else:
        return T(col) + (row - 1) * col + T(row - 2)

# Part 1
def p1(data: str) -> int:
    row, col = parse_data(data)
    cell_number = calc_cell_number(row, col)

    code = 20151125
    for _ in range(2, cell_number + 1):
        code = (code * 252533) % 33554393

    return code   

# Part 2
def p2(data: str) -> int:
    pass    
    
# Main
if __name__ == '__main__':
    data = aoc.d25_data()
    print(p1(data))
    print(p2(data))
