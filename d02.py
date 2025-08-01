import aoc

def parseData(data: str) -> list[tuple[int, int, int]]:
    return [tuple(int(v) for v in line.split('x')) for line in data.splitlines()]

def p1(data: str) -> int:
    total_paper = 0
    boxes = parseData(data)
    for (l, w, h) in boxes:
        areas = (l*w, l*h, w*h)
        min_area = min(areas)
        paper_for_box = 2 * sum(areas) + min_area
        total_paper += paper_for_box
    
    return total_paper

def p2(data: str) -> int:
    total_ribbon = 0
    boxes = parseData(data)
    for (l, w, h) in boxes:
        volume = l * w * h
        min_perimiter = min((2*(l+w), 2*(l+h), 2*(w+h)))
        ribbon_for_box = min_perimiter + volume
        total_ribbon += ribbon_for_box
    
    return total_ribbon

if __name__ == '__main__':
    data = aoc.d02data()
    print(p1(data))
    print(p2(data))
