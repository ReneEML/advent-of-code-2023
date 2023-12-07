import typing as T

directions = [
    [-1, -1],
    [-1, 1],
    [-1, 0],
    [1, 0],
    [1, -1],
    [1, 1],
    [0, 1],
    [0, -1]
]


def check_surrounding(i: int, j: int, n: int, m: int, data: T.List[str]):
    for direction in directions:
        next_i = i + direction[0]
        next_j = j + direction[1]
        if (
                0 <= next_i < n
                and 0 <= next_j < m
                and not data[next_i][next_j].isnumeric()
                and data[next_i][next_j] != "."
        ):
            return True
    return False


def increment_sum(num: str, num_in_schematic: bool) -> int:
    if num_in_schematic:
        return int(num)
    return 0


def sum_of_part_no(data: T.List[str]) -> int:
    n = len(data)
    m = len(data[0])
    print(n, m)
    result = 0
    num, num_in_schematic = "", False
    for i in range(n):
        result += increment_sum(num, num_in_schematic)
        num, num_in_schematic = "", False
        for j in range(m):
            if data[i][j].isnumeric():
                num += data[i][j]
                num_in_schematic = num_in_schematic or check_surrounding(i, j, n, m, data)
            else:
                result += increment_sum(num, num_in_schematic)
                num, num_in_schematic = "", False
    result += increment_sum(num, num_in_schematic)
    return result


f = open("input.txt")
schematic = [line.strip() for line in f if line]

print("Answer:", sum_of_part_no(schematic))
