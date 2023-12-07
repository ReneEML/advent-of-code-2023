three_letter = {"one": 1, "two": 2, "six": 6}
four_letter = {"four": 4, "five": 5, "nine": 9}
five_letter = {"three": 3, "seven": 7, "eight": 8}
token_maps = {
    3: three_letter,
    4: four_letter,
    5: five_letter
}


def first_num(l: str) -> int:
    n = len(l)
    for i in range(n):
        if l[i].isnumeric():
            return int(l[i])
        for length, token_map in token_maps.items():
            for token in token_map:
                if i + length < n and l[i:i + length] == token:
                    return token_map[token]
    return 0


def second_num(l: str) -> int:
    n = len(l)
    for i in range(n - 1, -1, -1):
        if l[i].isnumeric():
            return int(l[i])
        for length, token_map in token_maps.items():
            for token in token_map:
                if i - length >= 0 and l[i - length + 1:i + 1] == token:
                    return token_map[token]
    return 0


def parse_line(l: str):
    return 10 * first_num(l) + second_num(l)


f = open("input2.txt")
res = 0
for line in f:
    res += parse_line(line)
print("Result:", res)

