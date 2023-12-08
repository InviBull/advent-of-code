from aoc_helper import fetch, run
from math import lcm


class Solution:
    def __init__(self):
        self.directions, self.nodes, self.start = self._parse_data()
        self.length = len(self.directions)

    def _parse_data(self) -> (str, dict[str, list[str]], list[str]):
        raw_data = fetch("08", "2023").split("\n\n")
        directions = raw_data[0].strip()

        nodes = {
            node: element.replace("(", "").replace(")", "").split(", ")
            for line in raw_data[1].splitlines()
            for node, element in (line.split(" = "),)
        }

        start = [node for node in nodes if node.endswith("A")]

        return directions, nodes, start

    def _cal_moves(self, pos: str, part: {1, 2}) -> int:
        moves = 0
        curr = 0

        while (pos != "ZZZ" and part == 1) or (pos[-1] != "Z" and part == 2):
            elemIndex = 0 if self.directions[curr] == "L" else 1
            pos = self.nodes[pos][elemIndex]
            curr += 1
            curr %= self.length
            moves += 1

        return moves

    def calculate_p1(self) -> int:
        return self._cal_moves("AAA", 1)

    def calculate_p2(self) -> int:
        return lcm(*[self._cal_moves(pos, 2) for pos in self.start])

if __name__ == "__main__":
    run(Solution)
