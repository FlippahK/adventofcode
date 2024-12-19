import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from collections import deque
from timeit import default_timer as timer

test_data: str = \
    """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def calc_shortest_path(grid):
    width = len(grid[0])
    height = len(grid)

    visited = set()
    pos = (0, 0)
    steps = deque([(pos, 0)])
    while steps:
        pos, steps_taken = steps.popleft()
        x, y = pos
        if x == width - 1 and y == height - 1:
            return steps_taken
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if new_x >= 0 and new_x < width and new_y >= 0 and new_y < height and grid[new_y][new_x] == '.' and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                steps.append(((new_x, new_y), steps_taken + 1))

    return None


def solve1(input):
    width = 71 if len(input) > 1024 else 7
    height = 71 if len(input) > 1024 else 7
    bytes = 1024 if len(input) > 1024 else 12

    grid = [['.' for _ in range(width)] for _ in range(height)]
    for (x, y) in input[:bytes]:
        grid[y][x] = '#'

    return calc_shortest_path(grid)


def solve2(input):
    width = 71 if len(input) > 1024 else 7
    height = 71 if len(input) > 1024 else 7

    min_block = 0
    max_block = len(input)
    while min_block < max_block:
        mid = (min_block + max_block) // 2
        grid = [['.' for _ in range(width)] for _ in range(height)]
        for (x, y) in input[:mid]:
            grid[y][x] = '#'
        if calc_shortest_path(grid) is not None:
            min_block = mid + 1
        else:
            max_block = mid

    return f"{input[min_block - 1][0]},{input[min_block - 1][1]}"


def parse(data: str):
    lines = util.as_csv_lines_of_ints(data)
    return lines


def main():
    data: str = util.get(18, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
