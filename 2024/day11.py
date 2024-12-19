import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer
from functools import cache 

test_data: str = \
    """125 17"""

stones_result = {}


def solve1(input):
    stones = input
    print(input)
    for i in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                split_stone = str(stone)
                # print(f"Split stone: {split_stone}: {split_stone[:len(split_stone) // 2]}, {split_stone[len(split_stone) // 2:]}")
                new_stones.append(int(split_stone[:len(split_stone) // 2]))
                new_stones.append(int(split_stone[len(split_stone) // 2:]))
            else:
                new_stones.append(stone* 2024)
        # print(new_stones)
        stones = new_stones
    
    return len(stones)


def calc_stone_five(stone):
    stones = [stone]
    for i in range(5):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                split_stone = str(stone)
                # print(f"Split stone: {split_stone}: {split_stone[:len(split_stone) // 2]}, {split_stone[len(split_stone) // 2:]}")
                new_stones.append(int(split_stone[:len(split_stone) // 2]))
                new_stones.append(int(split_stone[len(split_stone) // 2:]))
            else:
                new_stones.append(stone* 2024)
        # print(new_stones)
        stones = new_stones
    return (len(stones), stones)

@cache
def sum_stones(stone, iterations):
    if iterations == 1:
        return stones_result[stone][0]
    
    return sum([sum_stones(s, iterations - 1) for s in stones_result[stone][1]])


def solve2(input):
    stones = input
    print(input)
    iterations = 15
    
    new_stones = set()
    for stone in stones:
        if stone in stones_result:
            continue
        else:
            stones_result[stone] = calc_stone_five(stone)
            new_stones.update(stones_result[stone][1])
    for i in range(iterations):
        stones = list(new_stones)
        new_stones = set()
        for stone in stones:
            if stone in stones_result:
                continue
            else:
                stones_result[stone] = calc_stone_five(stone)
                new_stones.update(stones_result[stone][1])
        stones = new_stones
    
    return sum([sum_stones(s, iterations) for s in input])


def parse(data: str):
    lines = util.as_ssv_ints(data)
    return lines


def main():
    data: str = util.get(11, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
