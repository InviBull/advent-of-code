from read_input import read_input
data = read_input("03", "2015")

x1, y1 = 0, 0
p1 = set()
p1.add((x1, y1))

for char in data:
    if char == ">":
        x1 += 1
    elif char == "<":
        x1 -= 1
    elif char == "^":
        y1 += 1
    elif char == "v":
        y1 -= 1

    p1.add((x1, y1))

print(len(set(p1)))

x1, y1 = 0, 0
x2, y2 = 0, 0
p2 = set()
p2.add((x1, y1))

for i in range(0, len(data), 2):
    char = data[i]
    if char == ">":
        x1 += 1
    elif char == "<":
        x1 -= 1
    elif char == "^":
        y1 += 1
    elif char == "v":
        y1 -= 1

    char = data[i+1]
    if char == ">":
        x2 += 1
    elif char == "<":
        x2 -= 1
    elif char == "^":
        y2 += 1
    elif char == "v":
        y2 -= 1

    p2.add((x1, y1))
    p2.add((x2, y2))

print(len(set(p2)))