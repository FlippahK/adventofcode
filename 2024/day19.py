import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer
from functools import cache

test_data: str = \
    """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

available_patterns = []

@cache
def find_match(pattern):
    if pattern == "":
        return True

    for available_pattern in available_patterns:
        if pattern.startswith(available_pattern):
            res = find_match(pattern[len(available_pattern):])
            if res:
                return True

    return False


def solve1(input):
    # print(input)

    sum = 0
    for line in input:
        if find_match(line):
            # print(f"Matched {line}")
            sum += 1
        # else:
        #     print(f"  Could not match {line}")

    return sum


@cache
def find_match2(pattern):
    if pattern == "":
        return 1

    res = 0
    for available_pattern in available_patterns:
        if pattern.startswith(available_pattern):
            res += find_match2(pattern[len(available_pattern):])

    return res


def solve2(input):
    sum = 0
    for line in input:
        matches = find_match2(line)
        # print(f"Matched {line} {matches} times")
        sum += matches

    return sum


def parse(data: str):
    lines = util.as_double_lines(data)
    available_patterns.extend(lines[0].split(", "))

    return util.as_lines(lines[1])


def main():
    data: str = util.get(19, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
