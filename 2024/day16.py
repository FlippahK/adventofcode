import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer

test_data_1: str = \
    """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

test_data_2: str = \
    """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""


def print_grid(grid):
    for row in grid:
        print("".join(row))


def solve(input):
    grid = [list(line) for line in input]

    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char == "S":
                start = (x, y)
            elif char == "E":
                end = (x, y)
                grid[x][y] = "." # Change end to a path

    print_grid(grid)
    dir = ">"
    print(start, end)

    path = []
    path.append((start, dir, 0, set([start])))
    best_visisted = {}
    best_score = 1000 * (len(grid) + len(grid[0])) # 100_000_000 - assume we do not rotate once for each step

    while path:
        pos, dir, score, visisted = path.pop()
        x, y = pos
        if score > best_score:
            continue
        if (x, y, dir) in best_visisted and best_visisted[(x, y, dir)] < score:
            continue
        best_visisted[(x, y, dir)] = score

        if pos == end:
            if best_score > score:
                best_score = score
                best_end_visisted = set(visisted)
            elif best_score == score:
                best_end_visisted = best_end_visisted.union(visisted)
            continue

        if dir == ">":
            if grid[x - 1][y] == ".":
                path.append(((x - 1, y), "^", score + 1001, visisted | {(x - 1, y)}))
            if grid[x + 1][y] == ".":
                path.append(((x + 1, y), "v", score + 1001, visisted | {(x + 1, y)}))
            if grid[x][y + 1] == ".":
                path.append(((x, y + 1), ">", score + 1, visisted | {(x, y + 1)}))
        elif dir == "<":
            if grid[x - 1][y] == ".":
                path.append(((x - 1, y), "^", score + 1001, visisted | {(x - 1, y)}))
            if grid[x + 1][y] == ".":
                path.append(((x + 1, y), "v", score + 1001, visisted | {(x + 1, y)}))
            if grid[x][y - 1] == ".":
                path.append(((x, y - 1), "<", score + 1, visisted | {(x, y - 1)}))
        elif dir == "^":
            if grid[x][y - 1] == ".":
                path.append(((x, y - 1), "<", score + 1001, visisted | {(x, y - 1)}))
            if grid[x][y + 1] == ".":
                path.append(((x, y + 1), ">", score + 1001, visisted | {(x, y + 1)}))
            if grid[x - 1][y] == ".":
                path.append(((x - 1, y), "^", score + 1, visisted | {(x - 1, y)}))
        elif dir == "v":
            if grid[x][y - 1] == ".":
                path.append(((x, y - 1), "<", score + 1001, visisted | {(x, y - 1)}))
            if grid[x][y + 1] == ".":
                path.append(((x, y + 1), ">", score + 1001, visisted | {(x, y + 1)}))
            if grid[x + 1][y] == ".":
                path.append(((x + 1, y), "v", score + 1, visisted | {(x + 1, y)}))

    for x, y in best_end_visisted:
        grid[x][y] = "O"
    print_grid(grid)
    return (best_score, len(best_end_visisted))


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(16, 2024)
    # data = test_data_1
    # data = test_data_2
    input = parse(data)
    # print(input)
    start = timer()
    res = solve(input)
    print(f"Value of solve1: {res[0]} after {timer() - start} seconds")
    print(f"Value of solve2: {res[1]} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
