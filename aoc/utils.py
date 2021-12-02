from pathlib import Path

from aoc.constants import NEWLINE


def filepath_to_ints(filepath: Path):
    """
    Read a file containing integers, one integer per line and return a list of ints.
    """
    with filepath.open("r") as f:
        return list(map(int, (s.replace(NEWLINE, "") for s in f.readlines())))
