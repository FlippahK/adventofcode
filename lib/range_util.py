from typing import Tuple, List


class Range:

    def __init__(self, start: int, end: int, inclusive: bool = False):
        if inclusive and start > end:
            raise AssertionError(f"start: {start} is > end: {end}")
        if start >= end:
            raise AssertionError(f"start: {start} is >= to end: {end}")

        self.start = start
        self.end = end + (1 if inclusive else 0)
        self.inclusive = inclusive

    def __contains__(self, item):
        if type(item) == int:
            return self.start <= item < self.end
        elif type(item) == Range:
            return self.start <= item.start and item.end < self.end

    def intersection(self, other):
        if other.start <= self.start and self.end < other.end:  # Self contained in other
            return self, []
        elif other.end <= self.start or self.end <= other.start:  # Self and other do not intersect
            return None, []
        elif other.start <= self.start < other.end <= self.end:  # Self start within other
            if other.end == self.end:
                return Range(self.start, other.end), []
            return Range(self.start, other.end), [Range(other.end, self.end)]
        elif self.start <= other.start < self.end <= other.end:  # Other start within self
            if self.start == other.start:
                return Range(other.start, self.end), []
            return Range(other.start, self.end), [Range(self.start, other.start)]
        elif self.start <= other.start < other.end <= self.end:
            return other, [Range(self.start, other.start), Range(other.end, self.end)]
        else:
            print("ohno")
            print(self, other)

    def split_on(self, val: int):
        return Range(self.start, val - (1 if self.inclusive else 0), self.inclusive), Range(val, self.end - (1 if self.inclusive else 0), self.inclusive)

    def __str__(self):
        return f"{self.start}..{('=' if self.inclusive else '')}{self.end - (1 if self.inclusive else 0)}"

    def __repr__(self):
        return f"{self.start}..{('=' if self.inclusive else '')}{self.end - (1 if self.inclusive else 0)}"

    def __len__(self):
        return self.end - self.start

    def __iter__(self):
        yield from range(self.start, self.end)

    def __lt__(self, other):
        return self.start < other.start

    def __le__(self, other):
        return self.start <= other.start

    def __gt__(self, other):
        return self.start > other.start

    def __ge__(self, other):
        return self.start >= other.start

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


if __name__ == "__main__":
    test = Range(0, 100)

    print(test.intersection(Range(-100, 200)))

    print(test.intersection(Range(100, 200)))
    print(test.intersection(Range(-100, 0)))

    print(test.intersection(Range(-50, 50)))

    print(test.intersection(Range(50, 150)))

    print(test.intersection(Range(25, 75)))

    print(test < Range(-50, 50))
    print(test < Range(50, 150))
    inc = Range(0, 100, True)
    print(inc, len(inc))
