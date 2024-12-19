import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from math import trunc
from timeit import default_timer as timer

test_data: str = \
    """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""


def run_program(a, b, c, program):
    ip = 0
    output = []
    while ip < len(program):
        instr = program[ip]
        literal = program[ip + 1]
        # print(f"ip={ip} [{a}, {b}, {c}] {instr} {literal}")
        combo = literal
        if combo == 4:
            combo = a
        elif combo == 5:
            combo = b
        elif combo == 6:
            combo = c
        elif combo == 7 and instr in [0, 2, 5]:
            print("Invalid combo")
            break

        if instr == 0:
            a = trunc(a // (2**combo))
        elif instr == 1:
            b = b ^ literal
        elif instr == 2:
            b = combo % 8
        elif instr == 3:
            if a != 0:
                ip = literal
                continue
        elif instr == 4:
            b = b ^ c
        elif instr == 5:
            output.append(combo % 8)
        elif instr == 6:
            b = trunc(a // (2**combo))
        elif instr == 7:
            c = trunc(a // (2**combo))
        else:
            print("Unknown instruction")
            break
        ip += 2

    # print(output)
    return output


def solve1(input):
    # print(input)

    a, b, c, program = input
    output = run_program(a, b, c, program)

    return ",".join([str(x) for x in output])


def find_partial_solve(program, program_counter, partial_result):
    for i in range(8):
        if run_program(partial_result * 8 + i, 0, 0, program) == program[program_counter:]:
            if program_counter == 0:
                return partial_result * 8 + i
            ret = find_partial_solve(program, program_counter - 1, partial_result * 8 + i)
            if ret is not None:
                return ret
    return None


def solve2(input):
    # print(input[3])
    return find_partial_solve(input[3], len(input[3]) - 1, 0)


def parse(data: str):
    lines = util.as_double_lines(data)
    input = (int(lines[0].split("\n")[0].split(": ")[1]), int(lines[0].split("\n")[1].split(": ")[1]), int(lines[0].split("\n")[2].split(": ")[1]), [int(x) for x in lines[1].split(": ")[1].split(",")])
    return input


def main():
    data: str = util.get(17, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()

# 0, 1, 2, 3, 4, 5, 7
# 0  1  2  3     5  7