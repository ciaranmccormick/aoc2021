from aoc.one import part_one, part_two
from aoc.constants import INPUTS
from aoc.utils import filepath_to_ints

TEST = INPUTS / "day1" / "part1test.txt"


def test_part_one():
    ints = filepath_to_ints(TEST)
    assert part_one(ints) == 7


def test_part_two():
    ints = filepath_to_ints(TEST)
    assert part_two(ints) == 5
