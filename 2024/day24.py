import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import util
from timeit import default_timer as timer

test_data: str = \
    """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""


test_data_2: str = \
    """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""


test_data_3: str = \
    """x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00"""


def solve1(input):
    print (input)

    def_wires, gates = input

    wires = {}
    for wire in def_wires:
        wires[wire[0]] = int(wire[1])

    while True:
        has_changed = False
        for gate in gates:
            if gate[2] in wires:
                continue
            if gate[3] == "AND":
                if gate[0] in wires and gate[1] in wires:
                    wires[gate[2]] = wires[gate[0]] & wires[gate[1]]
                    has_changed = True
            elif gate[3] == "OR":
                if gate[0] in wires and gate[1] in wires:
                    wires[gate[2]] = wires[gate[0]] | wires[gate[1]]
                    has_changed = True
            elif gate[3] == "XOR":
                if gate[0] in wires and gate[1] in wires:
                    wires[gate[2]] = wires[gate[0]] ^ wires[gate[1]]
                    has_changed = True
            else:
                wires[gate[1]] = wires[gate[0]]
                has_changed = True

        if not has_changed:
            break

    sum = 0
    for wire in sorted([w for w in wires if w[0] == 'z'], reverse=True):
        sum *= 2
        sum += wires[wire]

    return sum


def solve2(input):
    _, gates = input

    # Smart people figured out that it is a simple adder circuit with carry on the last bit
    # This gives the following rules for finding the incorrect gates

    # Each z must be output of an XOR (except z45 which is last)
    error_gates = set([gate[2] for gate in gates if gate[3] != "XOR" and gate[2][0] == "z" and gate[2] != "z45"])
    # print(error_gates)

    # Each AND must go to an OR (besides the first bit as it starts the carry flag) 
    and_outputs = [gate[2] for gate in gates if gate[3] == "AND"]
    or_inputs = [gate[0] for gate in gates if gate[3] == "OR"] + [gate[1] for gate in gates if gate[3] == "OR"]
    first_carry = [gate[2] for gate in gates if gate[3] == "AND" and gate[0] == "x00" and gate[1] == "y00"]
    error_gates.update(set(and_outputs) - set(or_inputs) - set(first_carry))
    # print(error_gates)

    # Each XOR must to go to XOR or AND
    xor_outputs = [gate[2] for gate in gates if gate[3] == "XOR"]
    xor_inputs = [gate[0] for gate in gates if gate[3] == "XOR"] + [gate[1] for gate in gates if gate[3] == "XOR"]
    and_inputs = [gate[0] for gate in gates if gate[3] == "AND"] + [gate[1] for gate in gates if gate[3] == "AND"]
    error_gates.update([w for w in set(xor_outputs) - set(xor_inputs) - set(and_inputs) if w[0] != "z"])
    # print(error_gates)

    # Each XOR must be connected to an x, y, or z (either input or output)
    error_gates.update([g[2] for g in gates if g[3] == "XOR" and g[0][0] not in "xyz" and g[1][0] not in "xyz" and g[2][0] not in "xyz"])
    # print(error_gates)

    return ",".join(sorted(error_gates))


def parse(data: str):
    parts = util.as_double_lines(data)

    return ([tuple(v.split(": ")) for v in util.as_lines(parts[0])], [(t[0], t[2], t[4], t[1]) for t in [v.split(" ") for v in util.as_lines(parts[1])]])


def main():
    data: str = util.get(24, 2024)
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
