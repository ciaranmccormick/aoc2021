from aoc.constants import INPUTS
from aoc.three import part_one, part_two

TEST = INPUTS / "day3" / "part1test.txt"


def test_part_one():
    assert part_one(TEST) == 198


def test_part_two():
    assert part_two(TEST) == 230
