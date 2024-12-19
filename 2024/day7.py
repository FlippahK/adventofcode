import sys
from pathlib import Path
from itertools import product
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer

test_data: str = \
    """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def solve_case(sum, terms, ops):
    for op in ops:
        termsum = terms[0]
        for i in range(len(terms) - 1):
            if op[i] == '+':
                termsum += terms[i+1]
            elif op[i] == '*':
                termsum *= terms[i+1]
            else:
                termsum = int(str(termsum) + str(terms[i+1]))
            # if termsum > sum: # optimization
            #     break
        if termsum == sum:
            return True
    return False

def solve1(input):
    total_sum = 0
    for case in input:
        ops = list(product(['+', '*'], repeat=(len(case[1]) - 1)))
        if solve_case(case[0], case[1], ops):
            total_sum += case[0]

    return total_sum


def solve2(input):
    total_sum = 0
    for case in input:
        ops = list(product(['+', '*', '||'], repeat=(len(case[1]) - 1)))
        if solve_case(case[0], case[1], ops):
            total_sum += case[0]

    return total_sum


def parse(data: str):
    lines = util.as_lines(data)
    return [[int(t[0]), util.as_ssv_ints(t[1])] for t in [line.split(": ") for line in lines]]


def main():
    data: str = util.get(7, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
