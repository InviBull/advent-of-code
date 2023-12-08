from aoc_helper import fetch, run
import re


class Solution:
    def __init__(self):
        self.raw_data = fetch("01")
        self.digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
                       "nine": 9}
        self.numbers = self.process_data()

    def process_data(self):
        numbers = []
        for word in self.raw_data.splitlines():
            indices = {}
            for num in self.digits:
                for i in [m.start() for m in re.finditer(num, word)]:
                    indices[i] = num

            for match in re.compile(r'\d+').finditer(word):
                for i in range(match.start(), match.end()):
                    indices[i] = int(word[i])

            numbers.append(list(dict(sorted(indices.items())).values()))

        return numbers

    def calculate_p1(self):
        p1 = 0
        for line in self.numbers:
            for i, num in enumerate(line):
                if num not in self.digits:
                    p1 += 10 * num
                    break

            for i, num in enumerate(line[::-1]):
                if num not in self.digits:
                    p1 += num
                    break

        return p1

    def calculate_p2(self):
        p2 = 0
        for line in self.numbers:
            p2 += 10 * self.digits[line[0]] if line[0] in self.digits else 10 * line[0]
            p2 += self.digits[line[-1]] if line[-1] in self.digits else line[-1]

        return p2


if __name__ == "__main__":
    run(Solution)
