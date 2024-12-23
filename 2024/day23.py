import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer
import itertools

test_data: str = \
    """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


def solve1(input):
    list_of_twos = set()
    for pairs in itertools.combinations(input, 2):
        if pairs[0][0] == pairs[1][0] or pairs[0][1] == pairs[1][0] or pairs[0][0] == pairs[1][1] or pairs[0][1] == pairs[1][1]:
            list_of_twos.add(tuple(sorted(pairs)))
    # print(list_of_twos)

    list_of_threes = set()
    for pair in input:
        for list_of_two in list_of_twos:
            if pair == list_of_two[0] or pair == list_of_two[1]:
                continue
            if pair[0] == list_of_two[0][0] or pair[0] == list_of_two[0][1] or pair[0] == list_of_two[1][0] or pair[0] == list_of_two[1][1]:
                if pair[1] == list_of_two[0][0] or pair[1] == list_of_two[0][1] or pair[1] == list_of_two[1][0] or pair[1] == list_of_two[1][1]:
                    list_of_threes.add(tuple(sorted((list_of_two[0], list_of_two[1], pair))))
    # print(list_of_threes)

    res = sum([1 for pairs in list_of_threes if 't' == pairs[0][0][0] or 't' == pairs[0][1][0] or 't' == pairs[1][0][0] or 't' == pairs[1][1][0]])

    return res


def solve2(input):
    connections = {}
    for pair in input:
        if pair[0] not in connections:
            connections[pair[0]] = [pair[1]]
        else:
            connections[pair[0]].append(pair[1])
        if pair[1] not in connections:
            connections[pair[1]] = [pair[0]]
        else:
            connections[pair[1]].append(pair[0])

    sets2 = set()
    for key in connections:
        for value in connections[key]:
            for key2 in connections[value]:
                if key2 != key:
                    sets2.add(tuple(sorted([tuple(sorted([key, value])), tuple(sorted([key2, value]))])))

    sets3 = set()
    for s in sets2:
        if s[0][0] != s[1][0]:
            key1 = s[0][0]
        else:
            key1 = s[0][1]
        key2 = s[1][0] if s[1][0] != s[0][0] and s[1][0] != s[0][1] else s[1][1]
        if key2 in connections[key1]:
            sets3.add(tuple(sorted([s[0], s[1], tuple(sorted([key1, key2]))])))

    # print(sets3)

    curr_sets = sets3
    while True:
        new_sets = set()
        for curr_set in curr_sets:
            needed_keys = set([elem for pair in curr_set for elem in pair])
            for key in connections:
                if key in needed_keys:
                    continue
                if needed_keys.issubset(connections[key]):
                    new_set = set(curr_set)
                    new_set.update([tuple(sorted([key, value])) for value in needed_keys])
                    new_sets.add(tuple(sorted(new_set)))
        if new_sets:
            curr_sets = new_sets
        else:
            break

    ans = ",".join(sorted(set([elem for pair in curr_set for elem in pair])))
    return ans


def parse(data: str):
    lines = util.as_lines(data)
    pairs = [tuple(sorted(line.split('-'))) for line in lines]
    return pairs


def main():
    data: str = util.get(23, 2024)
    # data = test_data
    input = parse(data)
    # print(input)
    start = timer()
    print(f"Value of solve1: {solve1(input)} after {timer() - start} seconds")
    start = timer()
    print(f"Value of solve2: {solve2(input)} after {timer() - start} seconds")


if __name__ == "__main__":
    main()
