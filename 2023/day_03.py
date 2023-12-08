from aoc_helper import fetch, run
import re


class Solution:
    def __init__(self):
        self.raw_data = fetch("03")
        self.part_numbers, self.gears = self.process_data()

    def process_data(self):
        part_numbers, gears = {}, {}
        data = self.raw_data.splitlines()
        for y, line in enumerate(data):
            for match in re.finditer(r'\d+', line):
                x1, x2 = match.start(), match.end()
                gear_num = int(match.group())

                for x in range(x1, x2):
                    for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                        a, b = y + dy, x + dx
                        if 0 <= a < len(data) and 0 <= b < len(line) and data[a][b] != "." and not data[a][b].isdigit():
                            part_numbers[f"{y}-{x1}-{x2}"] = gear_num
                            if data[a][b] == "*":
                                gears.setdefault(f"{a}-{b}", set()).add(gear_num)

        return part_numbers, gears

    def calculate_p1(self):
        return sum(list(self.part_numbers.values()))

    def calculate_p2(self):
        return sum(list(g)[0] * list(g)[1] for g in self.gears.values() if len(g) == 2)


if __name__ == "__main__":
    run(Solution)
