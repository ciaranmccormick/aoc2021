from pathlib import Path

from aoc.constants import INPUTS
from aoc.submarine import Submarine, SubmarineV1

INPUT = INPUTS / "day2" / "part1.txt"


def part_one(input_: Path) -> int:
    submarine = SubmarineV1()
    submarine.run_from_filepath(input_)
    return submarine.horizontal * submarine.depth


def part_two(input_: Path) -> int:
    submarine = Submarine()
    submarine.run_from_filepath(input_)
    return submarine.horizontal * submarine.depth


def main():
    print(f"The solution to part one is {part_one(INPUT)}")
    print(f"The solution to part two is {part_two(INPUT)}")


if __name__ == "__main__":
    main()
