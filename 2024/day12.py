import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util

test_data: str = \
    """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def solve1(input):
    visited = set()
    plants = [list(line) for line in input]
    sum = 0
    for i in range(len(plants)):
        for j in range(len(plants[i])):
            if (i, j) in visited:
                continue
            plant = plants[i][j]
            candidates = set([(i, j)])
            area = set()
            perimiter = 0
            while candidates:
                x, y = candidates.pop()
                if (x, y) in area:
                    continue
                if plants[x][y] == plant:
                    area.add((x, y))
                    visited.add((x, y))
                    if x > 0 and plants[x - 1][y] == plant:
                        candidates.add((x - 1, y))
                    else:
                        perimiter += 1
                    if y > 0 and plants[x][y - 1] == plant:
                        candidates.add((x, y - 1))
                    else:
                        perimiter += 1
                    if x < len(plants) - 1 and plants[x + 1][y] == plant:
                        candidates.add((x + 1, y))
                    else:
                        perimiter += 1
                    if y < len(plants[x]) - 1 and plants[x][y + 1] == plant:
                        candidates.add((x, y + 1))
                    else:
                        perimiter += 1
            sum += len(area) * perimiter

    return sum


def calc_perimiter(perimiter):
    perimiters = 0

    perm = [(p[0], p[1], p[4]) for p in perimiter if p[0] == p[2]]
    for y in set([p[1] for p in perm]):
        perimiters += 1
        xs = sorted([(pi[0], pi[2]) for pi in perm if pi[1] == y], key=lambda x: x[0])
        for i in range(len(xs) - 1):
            if xs[i][0] + 1 != xs[i + 1][0] or xs[i][1] != xs[i + 1][1]:
                perimiters += 1

    perm = [(p[0], p[1], p[4]) for p in perimiter if p[1] == p[3]]
    for x in set([p[0] for p in perm]):
        perimiters += 1
        ys = sorted([(pi[1], pi[2]) for pi in perm if pi[0] == x], key=lambda x: x[0])
        for i in range(len(ys) - 1):
            if ys[i][0] + 1 != ys[i + 1][0] or ys[i][1] != ys[i + 1][1]:
                perimiters += 1

    return perimiters


def solve2(input):
    visited = set()
    plants = [list(line) for line in input]
    sum = 0
    for i in range(len(plants)):
        for j in range(len(plants[i])):
            if (i, j) in visited:
                continue
            plant = plants[i][j]
            candidates = set([(i, j)])
            area = set()
            perimiter = set()
            while candidates:
                x, y = candidates.pop()
                if (x, y) in area:
                    continue
                if plants[x][y] == plant:
                    area.add((x, y))
                    visited.add((x, y))
                    if x > 0 and plants[x - 1][y] == plant:
                        candidates.add((x - 1, y))
                    else:
                        perimiter.add((x - 1, y, x, y, '>'))
                    if y > 0 and plants[x][y - 1] == plant:
                        candidates.add((x, y - 1))
                    else:
                        perimiter.add((x, y - 1, x, y, 'v'))
                    if x < len(plants) - 1 and plants[x + 1][y] == plant:
                        candidates.add((x + 1, y))
                    else:
                        perimiter.add((x, y, x + 1, y, '<'))
                    if y < len(plants[x]) - 1 and plants[x][y + 1] == plant:
                        candidates.add((x, y + 1))
                    else:
                        perimiter.add((x, y, x, y + 1, '^'))
            if plants[i][j] == 'O':
                print("Found it")
            sum += len(area) * calc_perimiter(perimiter)
            print(f"Area: {len(area)}, Sides: {calc_perimiter(perimiter)}")

    return sum
# 878098 low

def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(12, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    # print(f"Value of solve1: {solve1(input)}")
    print(f"Value of solve2: {solve2(input)}")


if __name__ == "__main__":
    main()
