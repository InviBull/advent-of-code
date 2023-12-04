from aoc_helper import fetch


def parse_card(card):
    num, winning_num = card.split(": ")[1].split(" | ")
    return list(map(int, num.split())), list(map(int, winning_num.split()))


def calculate_p1():
    p1 = 0
    for i in range(len(nums)):
        curr_nums, curr_win_nums = nums[i], win_nums[i]
        matched = sum(1 for num in curr_nums if num in curr_win_nums)
        p1 += 2 ** (matched - 1) if matched > 0 else 0
    return p1


def calculate_p2():
    occurrences = {}

    for i, card in enumerate(data):
        curr_nums, curr_win_nums = nums[i], win_nums[i]
        occurrences[i] = occurrences.get(i, 0) + 1
        scratched = i

        for num in curr_nums:
            if num in curr_win_nums:
                scratched += 1
                occurrences[scratched] = occurrences.get(scratched, 0) + occurrences[i]

    return sum(occurrences.values())


if __name__ == "__main__":
    data = fetch("04").splitlines()

    nums, win_nums = zip(*[parse_card(card) for card in data])

    # p1
    print("Part 1:", calculate_p1())

    # p2
    print("Part 2:", calculate_p2())
