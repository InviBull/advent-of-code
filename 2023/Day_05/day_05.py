from aoc_helper import fetch, run


class Solution:
    def __init__(self):
        self.raw_data = fetch("05", "2023").split("\n\n")
        self.length = len(self.raw_data)
        self.seeds = list(map(int, self.raw_data[0].split(": ")[1].split()))
        self.data = self.parse_data()

    def parse_data(self):
        data = []
        for i in range(1, self.length):
            data.append([list(map(int, x.split())) for x in self.raw_data[i].splitlines()[1:]])
        return data

    def calculate_p1(self):
        p1 = 0
        for seed in self.seeds:
            temp_ = seed
            for mapIndex in range(7):
                for dest, start, range_ in self.data[mapIndex]:
                    if start <= temp_ < start + range_:
                        temp_ += dest - start
                        break
            p1 = temp_ if p1 == 0 else min(p1, temp_)
        return p1

    def calculate_p2(self):
        p2 = 0
        seeds = self.seeds[::2]
        for mapIndex1 in range(7):
            for _, start, _ in self.data[mapIndex1]:
                temp_ = start
                for mapIndex in range(mapIndex1-1, -1, -1):
                    for dest2, start2, range_ in self.data[mapIndex]:
                        if dest2 <= temp_ < dest2 + range_:
                            temp_ -= dest2 - start2
                            break
                seeds.append(temp_)

        for seed in seeds:
            isAllowed = False
            for i in range(0, len(self.seeds), 2):
                if 0 <= seed - self.seeds[i] < self.seeds[i+1]:
                    isAllowed = True
                    break
            
            if isAllowed:
                temp_ = seed
                for mapIndex in range(7):
                    for dest, start, range_ in self.data[mapIndex]:
                        if start <= temp_ < start + range_:
                            temp_ += dest - start
                            break
                p2 = temp_ if p2 == 0 else min(p2, temp_)

        return p2


if __name__ == "__main__":
    run(Solution)
