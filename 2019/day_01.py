from aoc_helper import fetch, run

class Solution:
    def __init__(self):
        self.data = self.parse_data()

    def parse_data(self) -> list[int]:
        return [int(x) for x in fetch("01", "2019").splitlines()]

    def calculate_p1(self) -> int:
        p1 = 0
        for x in self.data:
            p1 += (x //3) - 2
        return p1

    def calculate_p2(self) -> int:
        p2 = 0
        for x in self.data:
            while x >= 7:
                x = (x // 3) - 2
                p2 += x
        return p2

if __name__ == "__main__":
    run(Solution)
