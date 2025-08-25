import aoc

# Common
Grid = list[list[str]]

def parse_data(data: str) -> Grid:
    return [[c for c in r] for r in data.splitlines()]

def count_on(lights: Grid) -> int:
    lights_on = 0
    for r in lights:
        for c in r:
            if c == '#':
                lights_on += 1
    return lights_on

def step(grid: Grid) -> Grid:
    next_grid = [['x' for c in r] for r in grid]
    rows = len(next_grid)
    cols = len(next_grid[0])
    for r in range(rows):
        for c in range(cols):
            # Count neighbours
            neighbours_on = 0
            for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                check_r = r + dr
                check_c = c + dc
                if 0 <= check_r < rows and 0 <= check_c < cols:
                    if grid[check_r][check_c] == '#':
                        neighbours_on += 1
                
            # Update output light
            if grid[r][c] == '#':
                if neighbours_on in (2, 3):
                    next_grid[r][c] = '#'
                else:
                    next_grid[r][c] = '.'
            else:
                if neighbours_on == 3:
                    next_grid[r][c] = '#'
                else:
                    next_grid[r][c] = '.'
    return next_grid

# Part 1
def process_steps(initial_lights: Grid, num_steps: int) -> Grid:
    grid = initial_lights

    for _ in range(num_steps):
        grid = step(grid)
    
    return grid

def p1(data: str, num_steps: int) -> int:
    initial_lights = parse_data(data)
    grid = process_steps(initial_lights, num_steps)
    lights_on = count_on(grid)
    return lights_on

# Part 2
def activate_corners(grid: Grid) -> None:
    grid[0][0] = '#'
    grid[0][-1] = '#'
    grid[-1][0] = '#'
    grid[-1][-1] = '#'

def process_steps2(initial_lights: Grid, num_steps: int) -> Grid:
    grid = initial_lights

    for _ in range(num_steps):
        grid = step(grid)
        activate_corners(grid)
    
    return grid

def p2(data: str, num_steps: int) -> int:
    initial_lights = parse_data(data)
    activate_corners(initial_lights)
    grid = process_steps2(initial_lights, num_steps)
    lights_on = count_on(grid)
    return lights_on

# Main
if __name__ == '__main__':
    data = aoc.d18_data()
    print(p1(data, 100))
    print(p2(data, 100))
