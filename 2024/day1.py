import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer

test_data: str = \
    """"""


def solve1(input):
    col1 = sorted(input[0])
    col2 = sorted(input[1])

    sum = 0
    for i in range(len(col1)):
        sum += abs(col1[i] - col2[i])

    return sum

def solve2(input):
    dic = {}
    for num in input[1]:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    # print(dic)

    sum = 0
    for num in input[0]:
        if num in dic:
            sum += num * dic[num]
            # print(f"{num}, {dic[num]}")

    return sum

def parse(data: str):
    lines = util.as_lines(data)
    cols = [util.as_ssv_ints(line) for line in lines]

    res = [[], []]
    for line in cols:
        res[0].append(line[0])
        res[1].append(line[1])
    return res

def main():
    data: str = util.get(1, 2024)
    input = parse(data)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")

if __name__ == "__main__":
    main()
