import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
import re

test_data: str = \
    """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def solve1(input):
    robots = [list(map(int, re.split(" |,", s.replace("p=", "").replace("v=", "")))) for s in input]  # Flatten the list comprehension
    print(robots)

    boardx = 101
    boardy = 103
    quad1 = 0
    quad2 = 0
    quad3 = 0
    quad4 = 0
    for robot in robots:
        x = (100 * boardx + robot[0] + robot[2] * 100) % boardx
        y = (100 * boardy + robot[1] + robot[3] * 100) % boardy
        if x < boardx // 2 and y < boardy // 2:
            quad1 += 1
        elif x > boardx // 2 and y < boardy // 2:
            quad2 += 1
        elif x < boardx // 2 and y > boardy // 2:
            quad3 += 1
        elif x > boardx // 2 and y > boardy // 2:
            quad4 += 1
        # print(f"Robot: {robot}, x: {x}, y: {y}")

    # print(f"Quad1: {quad1}, Quad2: {quad2}, Quad3: {quad3}, Quad4: {quad4}")
    return quad1 * quad2 * quad3 * quad4


def print_robots(robots):
    grid = [["." for _ in range(101)] for _ in range(103)]
    for robot in robots:
        grid[robot[1]][robot[0]] = "#"

    for row in grid:
        print("".join(row))


def solve2(input):
    robots = [list(map(int, re.split(" |,", s.replace("p=", "").replace("v=", "")))) for s in input]  # Flatten the list comprehension
    # print(robots)

    boardx = 101
    boardy = 103
    # best_score = 10000000000
    best_iteration = -1
    for i in range(boardx * boardy):
        # First idea: smallest score is the picture - incorrect
        # quad1 = 0
        # quad2 = 0
        # quad3 = 0
        # quad4 = 0
        for robot in robots:
            robot[0] = (robot[0] + boardx + robot[2]) % boardx
            robot[1] = (robot[1] + boardy + robot[3]) % boardy
        #     if robot[0] < boardx // 2 and robot[1] < boardy // 2:
        #         quad1 += 1
        #     elif robot[0] > boardx // 2 and robot[1] < boardy // 2:
        #         quad2 += 1
        #     elif robot[0] < boardx // 2 and robot[1] > boardy // 2:
        #         quad3 += 1
        #     elif robot[0] > boardx // 2 and robot[1] > boardy // 2:
        #         quad4 += 1
        # score = quad1 * quad2 * quad3 * quad4
        # if score < best_score:
        #     best_score = score
        #     best_iteration = i
        #     print(f"New best score: {best_score}, iteration: {best_iteration}")
        #     print_robots(robots)

        # Second idea: picture appears when all robots are in unique positions
        pos = [(robot[0], robot[1]) for robot in robots]
        if len(set(pos)) == len(pos):
            print(f"Found unique positions at iteration: {i + 1}")
            print_robots(robots)
            best_iteration = i + 1
            break

    return best_iteration


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(14, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    print(f"Value of solve1: {solve1(input)}")
    print(f"Value of solve2: {solve2(input)}")


if __name__ == "__main__":
    main()
