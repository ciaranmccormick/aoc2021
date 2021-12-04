from pathlib import Path

from aoc.constants import INPUTS
from aoc.submarine import Diagnositcs

INPUT = INPUTS / "day3" / "part1.txt"


def part_one(input_: Path) -> int:
    diagnostics = Diagnositcs.from_path(input_)
    return diagnostics.gamma_rate * diagnostics.epsilon_rate


def part_two(input_: Path) -> int:
    report = Diagnositcs.from_path(input_)
    return report.oxygen_generator_rating * report.co2_scubber_rating


def main():
    print(f"The solution to part one is {part_one(INPUT)}")
    print(f"The solution to part two is {part_two(INPUT)}")


if __name__ == "__main__":
    main()
