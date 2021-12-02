from pathlib import Path


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
