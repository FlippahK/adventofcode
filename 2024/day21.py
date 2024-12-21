import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer
from functools import cache
from itertools import pairwise

test_data: str = \
    """029A
980A
179A
456A
379A"""


pad1 = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['', '0' , 'A']]
pad2 = [['', '^', 'A'], ['<', 'v', '>']]

def find_coordinates(pad, char):
    for y, row in enumerate(pad):
        for x, cell in enumerate(row):
            if cell == char:
                return x, y
    return None, None


@cache
def solve_pad(pad_nr, line, start, x_first):
    pad = pad1 if pad_nr == 1 else pad2
    (x, y) = start
    alt_pushes = set()
    push = []
    c = line[0]
    destx, desty = find_coordinates(pad, c)
    # (desty, destx) = [(i, j) for i, row in enumerate(pad) for j, cell in enumerate(row) if cell == c][0] # slower by 25 %
    while True:
        if pad[y][x] == '':
            Exception("Forbidden position")
        elif c == pad[y][x]:
            push.append('A')
            break
        elif x_first and x > destx and pad[y][x - 1] != '':
            x -= 1
            push.append('<')
        elif x_first and x < destx:
            x += 1
            push.append('>')
        elif y > desty and pad[y - 1][x] != '':
            y -= 1
            push.append('^')
        elif y < desty and pad[y + 1][x] != '':
            y += 1
            push.append('v')
        elif x > destx and pad[y][x - 1] != '':
            x -= 1
            push.append('<')
        elif x < destx:
            x += 1
            push.append('>')

    if len(line) > 1:
        push_x = solve_pad(pad_nr, line[1:], (x, y), True)
        push_y = solve_pad(pad_nr, line[1:], (x, y), False)
        alt_pushes.update(["".join(push) + p for p in push_x])
        alt_pushes.update(["".join(push) + p for p in push_y])
    else:
        alt_pushes.add("".join(push))

    return alt_pushes


def solve1(input):
    sum = 0

    for line in input:
        alt_pushes = solve_pad(1, line, (2, 3), True)
        alt_pushes.update(solve_pad(1, line, (2, 3), False))

        alt_pushes2 = set()
        for push in alt_pushes:
            alt_pushes2.update(solve_pad(2, push, (2, 0), True))
            alt_pushes2.update(solve_pad(2, push, (2, 0), False))

        alt_pushes3 = set()
        for push in alt_pushes2:
            alt_pushes3.update(solve_pad(2, push, (2, 0), True))
            alt_pushes3.update(solve_pad(2, push, (2, 0), False))

        min_push = min(len(push) for push in alt_pushes3)
        sum += int(line[0:line.index('A')]) * min_push
        # print(f"Line {line}, Push1: {len(alt_pushes)}, Push2: {len(alt_pushes2)}, Push3: {len(alt_pushes3)}, len: {min_push}, val: {int(line[0:line.index('A')])}")

    return sum


moves = {"AA": "A", "A^": "<A", "A>": "vA", "Av": "<vA", "A<": "v<<A",
            "^A": ">A", "^^": "A", "^>": "v>A", "^v": "vA", "^<": "v<A",
            ">A": "^A", ">^": "<^A", ">>": "A", ">v": "<A", "><": "<<A",
            "vA": "^>A", "v^": "^A", "v>": ">A", "vv": "A", "v<": "<A",
            "<A": ">>^A", "<^": ">^A", "<>": ">>A", "<v": ">A", "<<": "A"}


def split_into_pairs(s):
    return ["".join(pair) for pair in pairwise(s)]
    # return [s[i:i+2] for i in range(len(s) - 1)]


@cache
def best_push(push, robots):
    if robots == 1:
        return len(moves[push])
    sum = 0
    for pair in split_into_pairs("A" + moves[push]):
        sum += best_push(pair, robots - 1)

    return sum


def solve2(input):
    sum = 0

    for line in input:
        # print(line)
        alt_pushes = solve_pad(1, line, (2, 3), True)
        alt_pushes.update(solve_pad(1, line, (2, 3), False))

        best_res = 1000_000_000_000_000
        for pushes in alt_pushes:
            res = 0
            best_push.cache_clear()
            for pair in split_into_pairs("A" + pushes):
                res += best_push(pair, 25)
            if res < best_res:
                best_res = res
        sum += int(line[0:line.index('A')]) * best_res

        # print(f"Line {line}, {alt_pushes}, len: {best_res}, val: {int(line[0:line.index('A')])}, complexity: {best_res * int(line[0:line.index('A')])}")
    return sum


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(21, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
