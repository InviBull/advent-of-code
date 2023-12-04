from aoc_helper import fetch, run


class Solution:
    def __init__(self):
        self.raw_data = fetch("04").splitlines()
        self.n = len(self.raw_data)
        self.nums, self.win_nums = self.process_data()

    def process_data(self):
        nums, win_nums = [], []
        for card in self.raw_data:
            num, win_num = card.split(": ")[1].split(" | ")
            nums.append(list(map(int, num.split())))
            win_nums.append(list(map(int, win_num.split())))

        return nums, win_nums

    def calculate_p1(self):
        p1 = 0
        for i in range(len(self.nums)):
            curr_nums, curr_win_nums = self.nums[i], self.win_nums[i]
            matched = sum(1 for num in curr_nums if num in curr_win_nums)
            p1 += 2 ** (matched - 1) if matched > 0 else 0
        return p1

    def calculate_p2(self):
        occurrences = {}

        for i in range(self.n):
            curr_nums, curr_win_nums = self.nums[i], self.win_nums[i]
            occurrences[i] = occurrences.get(i, 0) + 1
            scratched = i

            for num in curr_nums:
                if num in curr_win_nums:
                    scratched += 1
                    occurrences[scratched] = occurrences.get(scratched, 0) + occurrences[i]

        return sum(occurrences.values())


if __name__ == "__main__":
    run(Solution)
