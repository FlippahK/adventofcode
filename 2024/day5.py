import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
import functools

test_data: str = \
    """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

incorrect = []
rules = {}

def solve1(input):
    for line in input[0]:
        rule = line.split('|')
        if (int(rule[0]) in rules):
            rules[int(rule[0])].append(int(rule[1]))
        else:
            rules[int(rule[0])] = [int(rule[1])]
    # print(rules)

    sum = 0
    for line in input[1]:
        pages = util.as_csv_of_ints(line)
        is_good = True
        for i, page in enumerate(pages):
            if page in rules:
                for check_page in pages[:i]:
                    if check_page in rules[page]:
                        is_good = False
                        break
        if is_good:
            sum += pages[len(pages) // 2]
            # print(f"Good: {pages}: {pages[len(pages) // 2]}")
        else:
            incorrect.append(pages)
            # print(f"Bad: {pages}")

    return sum


def cmp_pages(a, b):
    if a in rules:
        if b in rules[a]:
            return -1
    if b in rules:
        if a in rules[a]:
            return 1
    return 0


def solve2(input):
    sum = 0
    for pages in incorrect:
        sort_pages = sorted(pages, key=functools.cmp_to_key(cmp_pages))
        # print(f"{pages} -> {sort_pages}")

        sum += sort_pages[len(sort_pages) // 2]
    return sum


def parse(data: str):
    lines = [[], []]
    lines[0] = data.split('\n\n')[0].split('\n')
    lines[1] = data.split('\n\n')[1].split('\n')
    return lines


def main():
    data: str = util.get(5, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    print(f"Value of solve1: {solve1(input)}")
    print(f"Value of solve2: {solve2(input)}")


if __name__ == "__main__":
    main()
