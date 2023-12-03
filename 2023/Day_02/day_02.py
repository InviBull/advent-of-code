# import re
from read_input import fetch

data = fetch("02").splitlines()
p1, p2 = 0, 0

for index, game in enumerate(data):
    is_possible = True
    sets = game.split(": ")[1].split(";")
    r, g, b = 0, 0, 0

    for set_ in sets:
        for val in set_.split(", "):
            num, color = val.split()
            if color == "red":
                if int(num) > 12: is_possible = False
                r = max(int(num), r)
            if color == "green":
                if int(num) > 13: is_possible = False
                g = max(int(num), g)
            if color == "blue":
                if int(num) > 14: is_possible = False
                b = max(int(num), b)

    if is_possible:
        p1 += index + 1
    p2 += r * g * b

print(p1)
print(p2)
