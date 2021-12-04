from pathlib import Path
from typing import List, Optional

BOARD_SIZE = 5


class Number:
    def __init__(self, value: int):
        self.value = value
        self.checked = False

    def __bool__(self):
        return self.checked

    def __str__(self):
        return f"{self.value} - {self.checked}"

    def __repr__(self):
        return f"Number(value={self.value})"


class Board:
    def __init__(self, squares: List[Number]) -> None:
        self.squares = squares
        self.has_won = False

    def __str__(self):
        return " ".join(str(i.value) for i in self.squares)

    def get_row(self, pos):
        start = BOARD_SIZE * pos
        return self.squares[start : start + BOARD_SIZE]

    def get_column(self, pos):
        return self.squares[pos::BOARD_SIZE]

    def mark_numbers(self, number):
        for i in self.squares:
            if i.value == number:
                i.checked = True

    def is_bingo(self):
        if row := self.check_rows():
            self.has_won = True
            return row
        if column := self.check_columns():
            self.has_won = True
            return column

        return None

    def check_rows(self) -> Optional[List[Number]]:
        for pos in range(BOARD_SIZE):
            start = BOARD_SIZE * pos
            end = start + BOARD_SIZE
            row = self.squares[start:end]
            if all(row):
                return row

        return None

    def check_columns(self) -> Optional[List[Number]]:
        for pos in range(BOARD_SIZE):
            numbers = self.squares[pos::BOARD_SIZE]
            if all(numbers):
                return numbers

        return None

    @classmethod
    def from_list(cls, row):
        row = "".join(row).replace("\n", " ").strip().split()
        numbers = [Number(int(v)) for v in row]
        return cls(numbers)


class Bingo:
    def __init__(self, numbers: List[int], boards: List[Board]):
        self.numbers = numbers
        self.boards = boards

    @classmethod
    def from_path(cls, path: Path):
        with path.open("r") as f:
            lines = f.readlines()
            numbers = [int(s) for s in lines[0].replace("\n", "").split(",")]
            lines = lines[2:]
            boards = []
            for pos in range(0, len(lines), BOARD_SIZE + 1):
                row = lines[pos : pos + BOARD_SIZE + 1]
                boards.append(Board.from_list(row))

        return cls(numbers, boards)
