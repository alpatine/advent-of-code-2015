import aoc


# Common
def parse_data(data: str) -> list[int]:
    return data

# Part 1

def check_password(password: str) -> bool:
    run_len = 0
    last_value = 0
    contains_straight = False

    for value in password:
        if value == last_value + 1:
            run_len += 1
        else:
            run_len = 1
        if run_len == 3:
            contains_straight = True
            break
        last_value = value

    run_len = 0
    last_value = 0
    double_count = 0

    for value in password:
        if value == last_value:
            run_len += 1
        else:
            run_len = 1
        if run_len == 2:
            double_count += 1
            run_len = 0
        if double_count == 2:
            break
        last_value = value

    return contains_straight and double_count >= 2
        

def increment(input: list[int]) -> list[int]:
    first = ord('a')
    last = ord('z')
    not_allowed = {ord('i'), ord('o'), ord('l')}

    output = input
    last_pos = len(output) - 1

    # check for any not-allowed characters. If found, reset future chars to first
    for check_pos in range(len(output)):
        if output[check_pos] in not_allowed:
            output[check_pos] += 1
            for reset_pos in range(check_pos + 1, len(output)):
                output[reset_pos] = first
            if check_password(output):
                return output
    
    # incremment the password
    do_increment = True
    increment_pos = last_pos
    while do_increment:
        do_increment = False
        output[increment_pos] += 1
        if output[increment_pos] in not_allowed:
            output[increment_pos] += 1
        if output[increment_pos] > last:
            do_increment = True
            increment_pos -= 1
            continue
        elif increment_pos < last_pos:
            for reset_pos in range(increment_pos + 1, last_pos + 1):
                output[reset_pos] = first
    
    return output

def p1(data: str) -> str:
    password = list(map(ord, data))

    while check_password(password) == False:
        password = increment(password)

    return ''.join(map(chr, password))

# Part 2
def p2(data: str) -> int:
    password = increment(list(map(ord, p1(data))))

    while check_password(password) == False:
        password = increment(password)

    return ''.join(map(chr, password))

# Main
if __name__ == '__main__':
    data = aoc.d11_data()
    print(p1(data))
    print(p2(data))
