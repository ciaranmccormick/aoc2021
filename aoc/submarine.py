from pathlib import Path
from typing import List


class Diagnositcs:
    def __init__(self, report: List[str]) -> None:
        self.report = report
        self.column_len = len(report[0])
        self.row_len = len(report)

    def get_row(self, pos) -> str:
        return self.report[pos]

    def get_column(self, pos, start="") -> str:
        return "".join(r[pos] for r in self.report if r.startswith(start))

    @property
    def gamma_rate(self):
        gamma = []
        for pos in range(self.column_len):
            column = self.get_column(pos)
            if column.count("0") > column.count("1"):
                gamma.append("0")
            else:
                gamma.append("1")
        return int("".join(gamma), 2)

    @property
    def epsilon_rate(self):
        epsilon = []
        for pos in range(self.column_len):
            column = self.get_column(pos)
            if column.count("0") < column.count("1"):
                epsilon.append("0")
            else:
                epsilon.append("1")
        return int("".join(epsilon), 2)

    def get_rating(self, func):
        bits = []
        for position in range(self.column_len):
            start = "".join(bits)
            column = self.get_column(position, start=start)

            if len(column) == 1:
                bits.append(column[0])
                continue

            if func(column.count("0"), column.count("1")):
                bits.append("0")
            else:
                bits.append("1")

        return int("".join(bits), 2)

    @property
    def oxygen_generator_rating(self):
        return self.get_rating(lambda z, o: z > o)

    @property
    def co2_scubber_rating(self):
        return self.get_rating(lambda z, o: z <= o)

    @classmethod
    def from_path(cls, path):
        with path.open("r") as f:
            return cls([line.replace("\n", "") for line in f.readlines()])


class Command:
    def __init__(self, direction: str, magnitude: int):
        self.direction: str = direction
        self.magnitude: int = magnitude

    @classmethod
    def from_string(cls, s: str):
        s = s.replace("\n", "")
        direction, magnitude = s.split(" ")
        return cls(direction=direction, magnitude=int(magnitude))


class SubmarineV1:
    def __init__(self, horizontal: int = 0, depth: int = 0):
        self.horizontal = horizontal
        self.depth = depth

    def forward(self, magnitude: int):
        self.horizontal += magnitude

    def down(self, magnitude: int):
        self.depth += magnitude

    def up(self, magnitude):
        self.depth -= magnitude

    def run_from_filepath(self, filepath: Path):
        with filepath.open("r") as f:
            for line in f.readlines():
                command = Command.from_string(line)
                self.run_command(command)

    def run_command(self, command: Command):
        direction = getattr(self, command.direction)
        direction(command.magnitude)


class Submarine(SubmarineV1):
    def __init__(self, horizontal: int = 0, depth: int = 0, aim: int = 0):
        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim

    def forward(self, magnitude: int):
        self.horizontal += magnitude
        self.depth += self.aim * magnitude

    def down(self, magnitude: int):
        self.aim += magnitude

    def up(self, magnitude):
        self.aim -= magnitude
