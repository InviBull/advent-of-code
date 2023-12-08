from aoc_helper import fetch, run
import math

class Solution:
    def __init__(self):
        self.raw_data = fetch("06", "2023").splitlines()
        self.data = self.parse_data()

    def parse_data(self):
        times = [int(time) for time in self.raw_data[0].split(": ")[1].split()]
        distances = [int(distance) for distance in self.raw_data[1].split(": ")[1].split()]
        return list(zip(times, distances))

    def calculate_p1(self):
        p1 = 1
        for T, D in self.data:
            rootD = (T**2 - 4 * D) ** 0.5
            p1 *= (math.ceil((T - rootD) / 2) - math.floor((T + rootD) / 2) + 1)
        return p1

    def calculate_p2(self):
        T, D = "", ""   
        for t, d in self.data:
            T += str(t)
            D += str(d)
        T, D = int(T), int(D)

        rootD = (T**2 - 4 * D) ** 0.5
        t1, t2 = math.ceil((T - rootD) / 2), math.floor((T + rootD) / 2)
        return t2 - t1 + 1

if __name__ == "__main__":
    run(Solution)
