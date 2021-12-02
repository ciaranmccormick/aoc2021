from typing import List
from aoc.utils import filepath_to_ints
from aoc.constants import INPUTS

INPUT = INPUTS / "day1" / "part1.txt"


def part_one(ints: List[int]) -> int:
    return len([j - i for i, j in zip(ints, ints[1:]) if j - i > 0])


def part_two(ints: List[int]) -> int:
    sums = [sum(ints[i : i + 3]) for i in range(len(ints) - 2)]
    return part_one(sums)


def main():
    ints = filepath_to_ints(INPUT)
    print(f"The solution to part one is {part_one(ints)}")
    print(f"The solution to part two is {part_two(ints)}")


if __name__ == "__main__":
    main()
