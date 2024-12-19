import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer

test_data: str = \
    """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def compAsc(a, b):
    if a < b:
        if b - a <= 3:
            return True
    return False

def compDesc(a, b):
    if a > b:
        if a - b <= 3:
            return True
    return False

def is_good_series(vals):
    for i in (range(len(vals) - 1)):
        if i == 0:
            dir = 'asc' if vals[i] < vals[i + 1] else 'desc'
        if dir == 'asc' and not compAsc(vals[i], vals[i + 1]) or dir == 'desc' and not compDesc(vals[i], vals[i + 1]):
            return False

    return True

def solve1(input):
    safe = 0
    for line in input:
        vals = util.as_ssv_ints(line)
        isgood = True
        for i in (range(len(vals) - 1)):
            if i == 0:
                dir = 'asc' if vals[i] < vals[i + 1] else 'desc'
            if dir == 'asc' and not compAsc(vals[i], vals[i + 1]) or dir == 'desc' and not compDesc(vals[i], vals[i + 1]):
                isgood = False
                break
        if isgood:
            # print(line)
            safe += 1

    return safe


def solve2(input):
    safe = 0
    for line in input:
        vals = util.as_ssv_ints(line)
        isgood = is_good_series(vals)
        if not isgood:
            for i in range(len(vals)):
                new_vals = vals[:i] + vals[i + 1:]
                isgood = is_good_series(new_vals)
                if isgood:
                    break

        if isgood:
            safe += 1
            
    return safe


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(2, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
