from aoc_helper import fetch, run


class Solution:
    def __init__(self):
        self.raw_data = fetch("02")
        self.games = self.process_data()

    def process_data(self):
        games = {}
        for game in self.raw_data.splitlines():
            i, records = game.split(": ")
            i = int(i.split()[1])
            games[i] = {"r": 0, "g": 0, "b": 0}
            for record in records.split("; "):
                for values in record.split(", "):
                    num, color = values.split()
                    games[i][color[0]] = max(int(num), games[i][color[0]])
        return games

    def calculate_p1(self):
        p1 = 0
        for i in self.games:
            game = self.games[i]
            if game["r"] <= 12 and game["g"] <= 13 and game["b"] <= 14:
                p1 += i
        return p1

    def calculate_p2(self):
        p2 = 0
        for i in self.games:
            game = self.games[i]
            p2 += game["r"] * game["g"] * game["b"]
        return p2


if __name__ == "__main__":
    run(Solution)
