import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util

test_data: str = \
    """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

dirs = ['^', '>', 'v', '<']
walked_solve1 = []


def find_start(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] in dirs:
                return x, y


def next_dir(dir):
    if dir == dirs[-1]:
        return dirs[0]
    else:
        return dirs[dirs.index(dir) + 1]


def next_pos(x, y, dir):
    if dir == '^':
        return x - 1, y
    elif dir == '>':
        return x, y + 1
    elif dir == 'v':
        return x + 1, y
    elif dir == '<':
        return x, y - 1


def solve1(input):
    x, y = find_start(input)
    dir = input[x][y]

    walked = [['.' for _ in range(len(input[0]))] for _ in range(len(input))]

    walked[x][y] = 'X'

    rounds = 0
    while (True): # (x >= 0 and x < len(input) and y >= 0 and y < len(input[0])):
        rounds += 1
        xn, yn = next_pos(x, y, dir)
        if (xn < 0 or xn >= len(input) or yn < 0 or yn >= len(input[0])):
            break
        elif input[xn][yn] == '#':
            dir = next_dir(dir)
        else:
            x, y = xn, yn
            walked[x][y] = 'X'
        # print("\n".join(["".join(row) for row in walked]))

    print(f"Rounds: {rounds}")
    print("\n".join(["".join(row) for row in walked]))
    global walked_solve1
    walked_solve1 = walked

    return sum([row.count('X') for row in walked])


def solve2(input):
    loop = [['.' for _ in range(len(input[0]))] for _ in range(len(input))]

    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '.' and walked_solve1[i][j] == 'X':
                input[i][j] = '#'
                x, y = find_start(input)
                dir = input[x][y]
                walked = [[[] for _ in range(len(input[0]))] for _ in range(len(input))]
                walked[x][y].append(dir)

                rounds = 0
                while (True):
                    rounds += 1
                    xn, yn = next_pos(x, y, dir)
                    if (xn < 0 or xn >= len(input) or yn < 0 or yn >= len(input[0])):
                        # print("Out of bounds")
                        break
                    elif input[xn][yn] == '#':
                        dir = next_dir(dir)
                        if dir in walked[x][y]:
                            # print(f"Loop at {xn}, {yn}")
                            loop[i][j] = 'L'
                            break
                        else:
                            walked[x][y].append(dir)
                    else:
                        x, y = xn, yn
                        if dir not in walked[x][y]:
                            walked[x][y].append(dir)
                        else:
                            # print(f"Loop at {xn}, {yn}")
                            loop[i][j] = 'L'
                            break
                input[i][j] = '.'

    return sum([row.count('L') for row in loop])


def parse(data: str):
    lines = util.as_lines(data)
    grid = [list(line) for line in lines]
    return grid


def main():
    data: str = util.get(6, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    print(f"Value of solve1: {solve1(input)}")
    print(f"Value of solve2: {solve2(input)}")


if __name__ == "__main__":
    main()
