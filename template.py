import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util

test_data: str = \
    """"""


def solve1(input):
    return


def solve2(input):
    return


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(1, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    print(f"Value of solve1: {solve1(input)}")
    print(f"Value of solve2: {solve2(input)}")


if __name__ == "__main__":
    main()
