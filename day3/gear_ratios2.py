directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def extract_number(data, i, j):
    m = len(data[0])
    num = data[i][j]
    for index in range(j + 1, m):
        if data[i][index].isnumeric():
            num += data[i][index]
        else:
            break
    for index in range(j - 1, -1, -1):
        if data[i][index].isnumeric():
            num = data[i][index] + num
        else:
            break
    return int(num)


def gear_ratios(data):
    n = len(data)
    m = len(data[0])
    print(n, m)
    result = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == "*":
                nums = []
                for direction, offset in directions.items():
                    next_i = i + offset[0]
                    next_j = j + offset[1]
                    if 0 <= next_i < n and 0 <= next_j < m:
                        value = data[next_i][next_j]
                        if value.isnumeric():
                            nums.append(extract_number(data, next_i, next_j))
                        elif direction == "up" or direction == "down":
                            if next_j + 1 < m and data[next_i][next_j + 1].isnumeric():
                                nums.append(extract_number(data, next_i, next_j + 1))
                            if next_j - 1 >= 0 and data[next_i][next_j - 1].isnumeric():
                                nums.append(extract_number(data, next_i, next_j - 1))
                if len(nums) == 2:
                    result += nums[0] * nums[1]
    return result


f = open("input.txt")
schematic = [line.strip() for line in f if line]
print("Answer:", gear_ratios(schematic))
