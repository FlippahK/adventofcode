import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util

test_data: str = \
    """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def solve1(input):
    antenna_types = set([item for sublist in input for item in sublist])
    antenna_types.remove('.')
    print(antenna_types)
    antinodes = [['.' for _ in range(len(input[0]))] for _ in range(len(input))]
    print(antinodes)
    for x in range(len(input)):
        for y in range(len(input[x])):
            if input[x][y] in antenna_types:
                for i in range(len(input)):
                    if i < x:
                        continue
                    for j in range(len(input[i])):
                        if i == x and j <= y:
                            continue
                        if input[i][j] == input[x][y]:
                            diffx = x - i
                            diffy = y - j
                            if (x + diffx) >= 0 and (y + diffy) >= 0 and (y + diffy) < len(input):
                                antinodes[x + diffx][y + diffy] = '#'
                            if (i - diffx) < len(input) and (j - diffy) >= 0 and (j - diffy) < len(input[0]):
                                antinodes[i - diffx][j - diffy] = '#'

    print("\n".join(["".join(row) for row in antinodes]))
    return sum([row.count('#') for row in antinodes])


def solve2(input):
    antenna_types = set([item for sublist in input for item in sublist])
    antenna_types.remove('.')
    antinodes = [['.' for _ in range(len(input[0]))] for _ in range(len(input))]
    for x in range(len(input)):
        for y in range(len(input[x])):
            if input[x][y] in antenna_types:
                for i in range(len(input)):
                    if i < x:
                        continue
                    for j in range(len(input[i])):
                        if i == x and j <= y:
                            continue
                        if input[i][j] == input[x][y]:
                            antinodes[x][y] = '#'
                            antinodes[i][j] = '#'
                            diffx = x - i
                            diffy = y - j
                            cdiffx = diffx
                            cdiffy = diffy
                            while (x + cdiffx) >= 0 and (x + cdiffx) < len(input) and (y + cdiffy) >= 0 and (y + cdiffy) < len(input[0]):
                                antinodes[x + cdiffx][y + cdiffy] = '#'
                                cdiffx += diffx
                                cdiffy += diffy
                            cdiffx = diffx
                            cdiffy = diffy
                            while (i - cdiffx) >= 0 and (i - cdiffx) < len(input) and (j - cdiffy) >= 0 and (j - cdiffy) < len(input[0]):
                                antinodes[i - cdiffx][j - cdiffy] = '#'
                                cdiffx += diffx
                                cdiffy += diffy

    print("\n".join(["".join(row) for row in antinodes]))
    return sum([row.count('#') for row in antinodes])


def parse(data: str):
    lines = util.as_lines(data)
    matrix = [list(line) for line in lines]
    return matrix


def main():
    data: str = util.get(8, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    print(f"Value of solve1: {solve1(input)}")
    print(f"Value of solve2: {solve2(input)}")


if __name__ == "__main__":
    main()
