import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer

test_data: str = \
    """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def solve1(input):
    sum = 0
    for machine in input:
        smallest = 0
        for i in range(1, 100):
            for j in range(1, 100):
                if machine[0] * i + machine[2] * j == machine[4] and machine[1] * i + machine[3] * j == machine[5]:
                    if 3 * i + j < smallest or smallest == 0:
                        smallest = 3 * i + j
        sum += smallest

    return sum


def solve2(input):
    machines = []
    for machine in input:
        machines.append((machine[0], machine[1], machine[2], machine[3], machine[4] + 10000000000000, machine[5] + 10000000000000))

    # for machine in machines:
    #     print(machine)

    sum = 0
    for machine in machines:
        a = (machine[5]*machine[2] - machine[4]*machine[3]) / (machine[1]*machine[2] - machine[0]*machine[3])
        b = (machine[4] - a*machine[0]) / machine[2]
        if a == int(a) and b == int(b):
            sum += int(3 * a + b)

    return sum


def parse(data: str):
    lines = util.as_double_lines(data)
    machines = []
    for line in lines:
        m = line.split("\n")
        a = [int(but.split('+')[1]) for but in m[0].split(",")]
        b = [int(but.split('+')[1]) for but in m[1].split(",")]
        p = [int(but.split('=')[1]) for but in m[2].split(",")]
        machines.append((a[0], a[1], b[0], b[1], p[0], p[1]))
    return machines


def main():
    data: str = util.get(13, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()

# a*x1 + b*x2 = c
# a*y1 + b*y2 = d

# b = (c - a*x1) / x2
# a*y1 + (c - a*x1) / x2 * y2 = d
# a*y1 + c*y2/x2 - a*x1*y2/x2 = d
# a*y1 - a*x1*y2/x2 = d - c*y2/x2
# a(y1*x2 - x1*y2) = d*x2 - c*y2
# a = (d*x2 - c*y2) / (y1*x2 - x1*y2)
