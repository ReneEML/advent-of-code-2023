
def sanitize_nums(nums: str):
    return nums.strip().split(" ")


def parse_nums(nums: list[str]) -> list[int]:
    return [int(num) for num in nums if num != ""]


def parse_data(data: list[str]) -> list[tuple[list[int], list[int]]]:
    scratch_card_data = []
    for line in data:
        line = line.split(":")
        card_data = line[1].split("|")
        winning_nums = parse_nums(sanitize_nums(card_data[0]))
        nums = parse_nums(sanitize_nums(card_data[1]))
        scratch_card_data.append((winning_nums, nums))
    return scratch_card_data


def num_matching(winning_nums, nums):
    winning_set = set(winning_nums)
    return sum(1 for num in nums if num in winning_set)


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
        score = num_matching(parsed[i][0], parsed[i][1])
        for j in range(0, score):
            cardCount[i + j + 1] += cardCount[i]
    return sum(cardCount)


def driver():
    f = open("input.txt")
    scratchcards = [line for line in f]
    parsed = parse_data(scratchcards)
    print("Answers:", "\nPart 1 -", part_1(parsed), "Part 2 -", part_2(parsed))


driver()
