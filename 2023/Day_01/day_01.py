import re
from read_input import fetch

data = fetch("01").splitlines()
p1 = 0

for word in data:
    x = ""

    indices = {}

    for match in re.compile(r'\d+').finditer(word):
        for i in range(match.start(), match.end()):
            indices[i] = word[i]

    req = list(sorted(indices.keys()))
    p1 += int(indices[req[0]] + indices[req[-1]])

print(p1)

# p2
p2 = 0
digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
          "nine": "9"}

for word in data:
    x = ""

    indices = {}
    for i in digits:
        for j in [m.start() for m in re.finditer(i, word)]:
            indices[j] = digits[i]

    for match in re.compile(r'\d+').finditer(word):
        for i in range(match.start(), match.end()):
            indices[i] = word[i]

    req = list(sorted(indices.keys()))
    p2 += int(indices[req[0]] + indices[req[-1]])

print(p2)
