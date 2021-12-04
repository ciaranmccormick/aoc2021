from aoc.constants import INPUTS
from aoc.four import part_one, part_two

TEST = INPUTS / "day4" / "part1test.txt"


def test_part_one():
    assert part_one(TEST) == 4512


def test_part_two():
    assert part_two(TEST) == 1924
