import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
import collections

test_data: str = \
    """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def solve1(input):
    sum = 0
    for xs in range(len(input)):
        for ys in range(len(input[xs])):
            if input[xs][ys] == 0:
                # print(f"Found 0 at {xs}, {ys}")
                pos = collections.deque([(0, xs, ys)])
                goals = set()
                while pos:
                    d, x, y = pos.pop()
                    if (d == 9 and input[x][y] == 9):
                        goals.add((x, y))
                    else:
                        if (x > 0 and input[x - 1][y] == d + 1):
                            pos.append((d + 1, x - 1, y))
                        if (y > 0 and input[x][y - 1] == d + 1):
                            pos.append((d + 1, x, y - 1))
                        if (x < len(input) - 1 and input[x + 1][y] == d + 1):
                            pos.append((d + 1, x + 1, y))
                        if (y < len(input[x]) - 1 and input[x][y + 1] == d + 1):
                            pos.append((d + 1, x, y + 1))
                # print(f"Found {len(goals)} goals at {xs}, {ys}")
                sum += len(goals)

    return sum


def solve2(input):
    sum = 0
    for xs in range(len(input)):
        for ys in range(len(input[xs])):
            if input[xs][ys] == 0:
                # print(f"Found 0 at {xs}, {ys}")
                pos = collections.deque([(0, xs, ys)])
                goals = []
                while pos:
                    d, x, y = pos.pop()
                    if (d == 9 and input[x][y] == 9):
                        goals.append((x, y))
                    else:
                        if (x > 0 and input[x - 1][y] == d + 1):
                            pos.append((d + 1, x - 1, y))
                        if (y > 0 and input[x][y - 1] == d + 1):
                            pos.append((d + 1, x, y - 1))
                        if (x < len(input) - 1 and input[x + 1][y] == d + 1):
                            pos.append((d + 1, x + 1, y))
                        if (y < len(input[x]) - 1 and input[x][y + 1] == d + 1):
                            pos.append((d + 1, x, y + 1))
                # print(f"Found {len(goals)} goals at {xs}, {ys}")
                sum += len(goals)

    return sum

def parse(data: str):
    lines = [list(map(int, line)) for line in util.as_lines(data)]
    return lines


def main():
    data: str = util.get(10, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    print(f"Value of solve1: {solve1(input)}")
    print(f"Value of solve2: {solve2(input)}")


if __name__ == "__main__":
    main()
