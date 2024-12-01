from enum import Enum
from typing import Generator, Iterator, Self


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y

        raise AttributeError(f"Invalid item for getitem: {item}")

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Point(self.x // other, self.y // other)

    def __hash__(self):
        return self.x * 31 + self.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.x < other.x or self.x == other.x and self.y < other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def iterate_internals(self) -> Generator[Iterator[Self], None, None]:
        for x in range(0, 1 if self.x == 0 else self.x, -1 if self.x < 0 else 1):
            for y in range(0, 1 if self.y == 0 else self.y, -1 if self.y < 0 else 1):
                yield Point(x, y)

    def manhattan(self, other: Self = None):
        if other is None:
            other = Point(0, 0)
        return abs(self.x - other.x) + abs(self.y - other.y)


class Direction(Point, Enum):
    RIGHT = 1, 0
    UP = 0, 1
    LEFT = -1, 0
    DOWN = 0, -1

    @classmethod
    def values(cls):
        return [Direction.RIGHT, Direction.UP, Direction.LEFT, Direction.DOWN]
