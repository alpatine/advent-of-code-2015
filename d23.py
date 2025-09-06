from collections import namedtuple
from typing import Self

import aoc

# Common
Instruction = namedtuple('Instruction', ['code', 'param'])

class Computer:
    def __init__(self: Self) -> None:
        self.a: int = 0
        self.b: int = 0
        self.offset: int = 0
    
    def op_hlf(self: Self, register: str) -> None:
        setattr(self, register, getattr(self, register) // 2)
        self.offset += 1
    
    def op_tpl(self: Self, register: str) -> None:
        setattr(self, register, getattr(self, register) * 3)
        self.offset += 1

    def op_inc(self: Self, register: str) -> None:
        setattr(self, register, getattr(self, register) + 1)
        self.offset += 1
    
    def op_jmp(self: Self, relative_offset: str) -> None:
        relative_offset = int(relative_offset)
        self.offset += relative_offset
    
    def op_jie(self: Self, param: str) -> None:
        register, relative_offset = param.split(', ')
        relative_offset = int(relative_offset)
        will_jump = getattr(self, register) % 2 == 0
        if will_jump:
            self.offset += relative_offset
        else:
            self.offset += 1
    
    def op_jio(self: Self, param: str) -> None:
        register, relative_offset = param.split(', ')
        relative_offset = int(relative_offset)
        will_jump = getattr(self, register) == 1
        if will_jump:
            self.offset += relative_offset
        else:
            self.offset += 1

    def run_program(self: Self, program: list[Instruction]) -> None:
        program_length = len(program)
        operations: dict[str, callable[[str], None]] = {
            'hlf': self.op_hlf,
            'tpl': self.op_tpl,
            'inc': self.op_inc,
            'jmp': self.op_jmp,
            'jie': self.op_jie,
            'jio': self.op_jio,
        }

        while self.offset < program_length:
            instruction = program[self.offset]
            operations[instruction.code](instruction.param)

def parse_data(data: str) -> list[Instruction]:
    return [Instruction(*line.split(maxsplit=1)) for line in data.splitlines()]

# Part 1
def p1(data: str) -> int:
    instructions = parse_data(data)
    computer = Computer()
    computer.run_program(instructions)
    return computer.b

# Part 2
def p2(data: str) -> int:
    instructions = parse_data(data)
    computer = Computer()
    computer.a = 1
    computer.run_program(instructions)
    return computer.b

# Main
if __name__ == '__main__':
    data = aoc.d23_data()
    print(p1(data))
    print(p2(data))
