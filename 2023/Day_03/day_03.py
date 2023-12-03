import re
from read_input import fetch

data = fetch("03").splitlines()

gears = {}
part_numbers = {}

for y, line in enumerate(data):
    for match in re.compile(r'\d+').finditer(line):
        x1, x2 = match.start(), match.end()
        for i in range(x1, x2):
            num = int(line[x1:x2])
            for direction in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                a, b = y + direction[0], i + direction[1]
                if 0 <= a < len(data) and 0 <= b < len(line):
                    if data[a][b] != "." and not data[a][b].isdigit():
                        part_numbers[f"{y}-{x1}-{x2}"] = num

                        if data[a][b] == "*":
                            pos = f"{a}-{b}"
                            if pos in gears:
                                gears[pos].add(num)
                            else:
                                gears[pos] = {num}

# p1
p1 = sum(part_numbers.values())
print(p1)

# p2
p2 = 0
for g in gears.values():
    g = list(g)
    if len(g) == 2:
        p2 += g[0] * g[1]
print(p2)
