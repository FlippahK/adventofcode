import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer

test_data: str = \
    """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def solve1(input):
    sum = 0
    for line in input:
        for i in range(len(line) - 3):
            word = line[i:i+4]
            if word == "XMAS" or word == "SAMX":
                sum += 1

    for x in range(len(input) - 3):
        for y in range(len(input[0])):
            word = input[x][y] + input[x+1][y] + input[x+2][y] + input[x+3][y]
            if word == "XMAS" or word == "SAMX":
                sum += 1

    for x in range(len(input) - 3):
        for y in range(len(input[0]) - 3):
            word = input[x][y] + input[x+1][y+1] + input[x+2][y+2] + input[x+3][y+3]
            if word == "XMAS" or word == "SAMX":
                sum += 1

    for x in range(3, len(input)):
        for y in range(len(input[0]) - 3):
            word = input[x][y] + input[x-1][y+1] + input[x-2][y+2] + input[x-3][y+3]
            if word == "XMAS" or word == "SAMX":
                sum += 1

    return sum


def solve2(input):
    sum = 0
    for x in range(len(input) - 2):
        for y in range(len(input[0]) - 2):
            if input[x+1][y+1] == "A":
                if input[x+0][y+0] + input[x+2][y+2] in ["MS", "SM"] and input[x+2][y+0] + input[x+0][y+2] in ["MS", "SM"]:
                    sum += 1

    return sum


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(4, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
