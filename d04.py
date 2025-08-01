import hashlib

import aoc


def p1(data: str) -> int:
    secret_key = data

    salt = 0
    while True:
        result = hashlib.md5(bytes(secret_key + str(salt), 'ascii')).hexdigest()
        if result.startswith('00000'):
            return salt
        salt += 1

def p2(data: str) -> int:
    secret_key = data

    salt = 0
    while True:
        result = hashlib.md5(bytes(secret_key + str(salt), 'ascii')).hexdigest()
        if result.startswith('000000'):
            return salt
        salt += 1

if __name__ == '__main__':
    data = aoc.d04data()
    print(p1(data))
    print(p2(data))
