import re
from aoc_helper import fetch


def find_gear_positions():
    part_numbers, gears = {}, {}

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


def calculate_p1():
    return sum(list(part_numbers.values()))


def calculate_p2():
    return sum(list(g)[0] * list(g)[1] for g in gears.values() if len(g) == 2)


if __name__ == "__main__":
    data = fetch("03").splitlines()

    part_numbers, gears = find_gear_positions()

    # p1
    print("Part 1:", calculate_p1())

    # p2
    print("Part 2:", calculate_p2())
