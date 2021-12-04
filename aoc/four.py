from pathlib import Path
from aoc.constants import INPUTS
from aoc.bingo import Bingo

INPUT = INPUTS / "day4" / "part1.txt"


def part_one(input_: Path) -> int:
    bingo = Bingo.from_path(input_)
    for number in bingo.numbers:
        for board in bingo.boards:
            board.mark_numbers(number)
            if board.is_bingo():
                return sum(r.value for r in board.squares if not r.checked) * number
    return -1


def part_two(input_: Path) -> int:
    bingo = Bingo.from_path(input_)
    boards = bingo.boards
    for number in bingo.numbers:
        boards = [b for b in boards if not b.has_won]
        for board in boards:
            board.mark_numbers(number)
            if board.is_bingo() and len(boards) == 1:
                return sum(r.value for r in board.squares if not r.checked) * number
    return -1


def main():
    print(f"The solution to part one is {part_one(INPUT)}")
    print(f"The solution to part two is {part_two(INPUT)}")


if __name__ == "__main__":
    main()
