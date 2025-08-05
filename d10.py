import aoc


# Common
def parse_data(data: str) -> str:
    return data

def look_and_say(in_str: str) -> str:
    check_char = in_str[0]
    run_len = 0
    output = list()

    for c in in_str:
        if c == check_char:
            run_len += 1
        else:
            output.append(run_len)
            output.append(check_char)
            check_char = c
            run_len = 1
    output.append(run_len)
    output.append(check_char)
    
    result = ''.join(map(str, output))
    return result 

# Part 1
def p1(data: str, applications: int = 40) -> int:
    out_str = data
    for _ in range(applications):
        in_str = out_str
        out_str = look_and_say(in_str)

    return len(out_str)

# Part 2
def p2(data: str, applications: int = 50) -> int:
    out_str = data
    for _ in range(applications):
        in_str = out_str
        out_str = look_and_say(in_str)

    return len(out_str)

# Main
if __name__ == '__main__':
    data = aoc.d10data()
    print(p1(data))
    print(p2(data))
