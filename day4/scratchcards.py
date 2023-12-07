def parse_nums(nums: str):
    parsed = nums.strip().split(" ")
    return [int(num) for num in parsed if num != ""]


def parse_data(data: list[str]) -> list[tuple[list[int], list[int]]]:
    scratch_card_data = []
    for line in data:
        card_data = line.split(":")[1].split("|")
        scratch_card_data.append((parse_nums(card_data[0]), parse_nums(card_data[1])))
    return scratch_card_data


def num_matching(winning_nums, nums):
    return sum(1 for num in nums if num in set(winning_nums))


def calculate_score(winning_nums, nums):
    matching = num_matching(winning_nums, nums)
    if matching == 0:
        return 0
    return 2 ** (matching - 1)


def part_1(parsed: list[tuple[list[int], list[int]]]):
    return sum(calculate_score(winning_nums, nums) for winning_nums, nums in parsed)


def part_2(parsed: list[tuple[list[int], list[int]]]):
    cardCount = [1] * len(parsed)
    for i in range(len(parsed)):
        for j in range(0, num_matching(parsed[i][0], parsed[i][1])):
            cardCount[i + j + 1] += cardCount[i]
    return sum(cardCount)


def driver():
    f = open("input.txt")
    scratchcards = [line for line in f]
    parsed = parse_data(scratchcards)
    print("Answers:", "\nPart 1 -", part_1(parsed), "Part 2 -", part_2(parsed))


driver()
