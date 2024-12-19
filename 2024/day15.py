import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer

test_data_1: str = \
    """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

test_data_2: str = \
    """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

test_data_3: str = \
    """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""


def draw_grid(grid):
    for row in grid:
        print("".join(row))


def move_robot(grid, robot, move):
    x, y = robot
    xm = 0
    ym = 0
    if move == "^":
        ym = -1
    elif move == "v":
        ym = 1
    elif move == "<":
        xm = -1
    elif move == ">":
        xm = 1

    moves = []
    i = 0
    can_move = True
    while True:
        moves.append((x + xm * i, y + ym * i))
        i += 1
        # print(f"Checking {x + xm * i}, {y + ym * i}: {grid[y + ym * i][x + xm * i]}")
        if grid[y + ym * i][x + xm * i] == "#":
            can_move = False
            break
        elif grid[y + ym * i][x + xm * i] == ".":
            break

    if can_move:
        robot = (x + xm, y + ym)
        for i, j in reversed(moves):
            grid[j][i], grid[j + ym][i + xm] = grid[j + ym][i + xm], grid[j][i]

    return robot


def calc_score(grid):
    score = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "O":
                score += y * 100 + x

    return score


def solve1(input):
    grid, moves = input

    robot = ()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "@":
                robot = (x, y)
                break

    # draw_grid(grid)
    for move in moves:
        robot = move_robot(grid, robot, move)
        # print(f"Moved robot {move}")
        # draw_grid(grid)

    return calc_score(grid)


def move_robot2(grid, robot, move):
    x, y = robot
    xm = 0
    ym = 0
    if move == "^":
        ym = -1
    elif move == "v":
        ym = 1
    elif move == "<":
        xm = -1
    elif move == ">":
        xm = 1

    moves = []
    i = 0
    can_move = True
    moveables = set([(x, y)])
    while True:
        for m in moveables:
            moves.append((m[0] + xm * i, m[1] + ym * i))
        i += 1
        # print(f"Checking {x + xm * i}, {y + ym * i}: {grid[y + ym * i][x + xm * i]}")
        all_good = True
        new_moveables = set()
        removed_moveables = set()
        for m in moveables:
            if grid[m[1] + ym * i][m[0] + xm * i] == "#":
                can_move = False
                break
            elif grid[m[1] + ym * i][m[0] + xm * i] == ".":
                removed_moveables.add((m[0], m[1]))
                continue
            elif grid[m[1] + ym * i][m[0] + xm * i] == "[":
                all_good = False
                if ym != 0:
                    new_moveables.add((m[0] + 1, m[1]))
            elif grid[m[1] + ym * i][m[0] + xm * i] == "]":
                all_good = False
                if ym != 0:
                    new_moveables.add((m[0] - 1, m[1]))
        moveables.update(new_moveables)
        moveables -= removed_moveables
        if all_good or not can_move:
            break

    if can_move:
        robot = (x + xm, y + ym)
        for i, j in reversed(moves):
            grid[j][i], grid[j + ym][i + xm] = grid[j + ym][i + xm], grid[j][i]

    return robot


def calc_score2(grid):
    score = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "[":
                score += y * 100 + x

    return score


def solve2(input):
    grid, moves = input

    new_grid = []
    for row in grid:
        new_row = []
        for pos in row:
            if pos == "#":
                new_row.append("#")
                new_row.append("#")
            elif pos == "O":
                new_row.append("[")
                new_row.append("]")
            elif pos == "@":
                new_row.append("@")
                new_row.append(".")
            else:
                new_row.append(".")
                new_row.append(".")
        new_grid.append(new_row)

    grid = new_grid

    robot = ()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "@":
                robot = (x, y)
                break

    # draw_grid(grid)
    for move in moves:
        robot = move_robot2(grid, robot, move)
        # print(f"Moved robot {move}")
        # draw_grid(grid)

    # draw_grid(grid)
    return calc_score2(grid)


def parse(data: str):
    parts = util.as_double_lines(data)
    input = ([list(row) for row in util.as_lines(parts[0])], list("".join(util.as_lines(parts[1]))))
    return input


def main():
    # sys.stdout = open("tt_my.txt", "w")

    data: str = util.get(15, 2024)
    # data = test_data_1
    # data = test_data_2
    # data = test_data_3
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
