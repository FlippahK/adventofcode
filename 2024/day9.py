import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util

test_data: str = \
    """2333133121414131402"""


def solve1(input):
    disk_input = [int(x) for x in input[0]]

    disk = []
    for i, p in enumerate(disk_input):
        if i % 2 == 0:
            disk.extend([i // 2 for _ in range(p)])
        else:
            disk.extend([-1 for _ in range(p)])

    left = 0
    right = len(disk) - 1
    while left < right:
        if disk[left] != -1:
            left += 1
        elif disk[right] == -1:
            right -= 1
        else:
            disk[left] = disk[right]
            disk[right] = -1
            left += 1
            right -= 1

    sum = 0
    for i, p in enumerate(disk):
        if p != -1:
            sum += i * p

    return sum


def print_disk(disk):
    s = ""
    for d in disk:
        for i in range(d[0]):
            if d[2]:
                s += str(d[1])
            else:
                s += "."
    print(s)


def solve2(input):
    disk = [(int(x), i // 2, i % 2 == 0) for i, x in enumerate(input[0])]
    # print(disk)

    right = len(disk) - 1
    # print_disk(disk)
    while right > 0:
        if disk[right][2]:
            for i in range(right):
                if not disk[i][2] and disk[i][0] >= disk[right][0]:
                    if disk[i][0] >= disk[right][0]:
                        rest = (disk[i][0] - disk[right][0], 0, False)
                        disk[i] = (disk[right][0], disk[i][1], disk[i][2])
                        disk.insert(i + 1, rest)
                        right += 1
                    disk[i], disk[right] = disk[right], disk[i]
                    break
        right -= 1
        # print_disk(disk)

    # print(disk)
    sum = 0
    i = 0
    for d in disk:
        for _ in range(d[0]):
            if d[2]:
                sum += i * d[1]
            i += 1

    return sum


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(9, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    print(f"Value of solve1: {solve1(input)}")
    print(f"Value of solve2: {solve2(input)}")


if __name__ == "__main__":
    main()
