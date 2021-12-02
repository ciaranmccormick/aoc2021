from aoc.constants import INPUTS
from aoc.two import part_one, part_two

TEST = INPUTS / "day2" / "part1test.txt"


def test_part_one():
    assert part_one(TEST) == 150


def test_part_two():
    assert part_two(TEST) == 900
