import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer
from collections import deque

test_data: str = \
    """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


def calc_track(grid):
    width = len(grid[0])
    height = len(grid)

    for y in range(height):
        for x in range(width):
            if grid[y][x] == 'S':
                start = (x, y)
            if grid[y][x] == 'E':
                end = (x, y)
    grid[end[1]][end[0]] = '.'
    visited = set(start)
    track = {start: 0}

    steps = deque([(start, 0)])
    while steps:
        pos, steps_taken = steps.popleft()
        x, y = pos
        if pos == end:
            break
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if grid[new_y][new_x] == '.' and (new_x, new_y) not in track:
                visited.add((new_x, new_y))
                track[(new_x, new_y)] = steps_taken + 1
                steps.append(((new_x, new_y), steps_taken + 1))
    grid[end[1]][end[0]] = 'E'

    return track


def print_grid(grid, cheat_x, cheat_y):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if x == cheat_x and y == cheat_y:
                print('C', end='')
            else:
                print(grid[y][x], end='')
        print()


def solve1(input):
    grid = input

    track = calc_track(grid)
    cheats = {}
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == '#':
                if (x - 1, y) in track and (x + 1, y) in track:
                    cheat_moves = abs(track[(x - 1, y)] - track[(x + 1, y)]) - 2
                    # print(f"({x}, {y}) {cheat_moves}")
                    # print_grid(grid, x, y)
                    if cheat_moves in cheats:
                        cheats[cheat_moves] += 1
                    else:
                        cheats[cheat_moves] = 1
                if (x, y - 1) in track and (x, y + 1) in track:
                    cheat_moves = abs(track[(x, y - 1)] - track[(x, y + 1)]) - 2
                    # print(f"({x}, {y}) {cheat_moves}")
                    # print_grid(grid, x, y)
                    if cheat_moves in cheats:
                        cheats[cheat_moves] += 1
                    else:
                        cheats[cheat_moves] = 1

    return sum(value for cheat_moves, value in cheats.items() if cheat_moves >= 100)


def cheat_endpoints(pos, track):
    i, j = pos
    output = set()
    for dx in range(-20, 21):
        dymax = 20 - abs(dx) # Since we are looking for a manhattan distance of max 20
        for dy in range(-dymax, dymax + 1):
            if (i + dx, j + dy) in track:
                output.add((i + dx, j + dy))
    return output


def manhattan_distance(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


def solve2(input):
    track = calc_track(input)
    cheats = 0
    for pos in track:
        pot_endpoints = cheat_endpoints(pos, track)
        for other_pos in pot_endpoints:
            if track[other_pos] - track[pos] - manhattan_distance(pos, other_pos) >= 100:
                cheats += 1

    return cheats


def parse(data: str):
    lines = [list(line) for line in util.as_lines(data)]
    return lines


def main():
    data: str = util.get(20, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
