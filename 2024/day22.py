import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer

test_data: str = \
    """1
10
100
2024"""


test_data_2: str = \
    """1
2
3
2024"""


def solve1(input):
    sum = 0
    for i in input:
        num = i
        for _ in range(2000):
            xor_num = num * 64
            num = num ^ xor_num
            num = num % 16777216

            xor_num = num // 32
            num = num ^ xor_num
            num = num % 16777216

            xor_num = num * 2048
            num = num ^ xor_num
            num = num % 16777216

        # print(f"Input: {i}, output: {num}")
        sum += num

    return sum


def solve2(input):
    monkeys_series = []
    for i in input:
        monkey_nums = []
        num = i
        last_num = 0
        for _ in range(2000):
            xor_num = num * 64
            num = num ^ xor_num
            num = num % 16777216

            xor_num = num // 32
            num = num ^ xor_num
            num = num % 16777216

            xor_num = num * 2048
            num = num ^ xor_num
            num = num % 16777216

            n = num % 10
            monkey_nums.append((n, n - last_num))
            last_num = n

        monkeys_series.append(monkey_nums)

    monkeys_sequences = []
    for series in monkeys_series:
        seq = {}
        for i in range(1, len(series) - 3):
            s = tuple([d for n, d in series[i:i + 4]]) 
            if s not in seq:
                seq[s] = series[i + 3][0]
        monkeys_sequences.append(seq)

    all_sequences = set()
    for d in monkeys_sequences:
        all_sequences.update(d.keys())
    print(f"Number of sequences found: {len(all_sequences)}")

    best_sum = 0
    best_sequence = None
    for sequence in sorted(all_sequences):
        sum = 0
        for i in monkeys_sequences:
            if sequence in i:
                sum += i[sequence]

        if sum > best_sum:
            best_sum = sum
            best_sequence = sequence
            # print(f"Best sum: {best_sum}, sequence: {sequence}")

        # print(f"Sequence: {sequence}, sum: {sum}")

    # print(f"Best sequence: {best_sequence}, sum: {best_sum}")

    return best_sum


def parse(data: str):
    lines = util.as_lines_of_int(data)
    return lines


def main():
    data: str = util.get(22, 2024)
    # data = test_data
    # data = test_data_2
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
