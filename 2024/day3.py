import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer

test_data: str = \
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


def parse_num(line: str, start: int) -> int:
    num = ''
    for i in range(start, len(line)):
        if line[i].isdigit():
            num += line[i]
        else:
            break
    return int(num)


def solve1(input):
    sum = 0
    for line in input:
        for i in range(len(line)):
            if line[i:].startswith('mul('):
                # print(line[i:])
                num1 = parse_num(line, i + 4)
                if line[i + 4 + len(str(num1))] == ',':
                    num2 = parse_num(line, i + 4 + len(str(num1)) + 1)
                    # print(f"num1: {num1}, num2: {num2}")
                    if line[i + 4 + len(str(num1)) + 1 + len(str(num2))] == ')':
                        # print(f"num1: {num1}, num2: {num2}")
                        sum += num1 * num2

    return sum


def solve2(input):
    sum = 0
    is_do = True
    for line in input:
        for i in range(len(line)):
            if line[i:].startswith('do()'):
                is_do = True
            elif line[i:].startswith('don\'t()'):
                is_do = False
            elif is_do and line[i:].startswith('mul('):
                # print(line[i:])
                num1 = parse_num(line, i + 4)
                if line[i + 4 + len(str(num1))] == ',':
                    num2 = parse_num(line, i + 4 + len(str(num1)) + 1)
                    # print(f"num1: {num1}, num2: {num2}")
                    if line[i + 4 + len(str(num1)) + 1 + len(str(num2))] == ')':
                        # print(f"num1: {num1}, num2: {num2}")
                        sum += num1 * num2

    return sum


def parse(data: str):
    lines = util.as_lines(data.replace(' ', ''))
    return lines


def main():
    data: str = util.get(3, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
