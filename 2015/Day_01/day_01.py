from read_input import read_input
data = read_input("01", "2015")
p1, p2 = 0, 0

for pos, char in enumerate(data):
    if char == "(": p1 += 1
    elif char == ")": p1 -= 1
    if p1 < 0 and p2 == 0: p2 = pos + 1

print(p1)
print(p2)