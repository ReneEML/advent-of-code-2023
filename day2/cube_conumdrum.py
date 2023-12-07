def parse_info(info: str):
    cubes = info.split(",")
    result = {}
    for cube in cubes:
        cube = cube.strip()
        cube = cube.split(" ")
        result[cube[1]] = int(cube[0])
    return result


def parse_game(line: str):
    amount = dict(red=0, blue=0, green=0)
    line = line.split(":")
    game_id = int(line[0].split(" ")[1])
    info_data = line[1].split(";")
    for info in info_data:
        cube_data = parse_info(info)
        for color, count in cube_data.items():
            amount[color] = max(amount[color], count)
    return game_id, amount


criteria = {"red": 12, "green": 13, "blue": 14}

part_1 = 0
part_2 = 0
data = open("input.txt")
for datum in data:
    game_id, amount = parse_game(datum)
    valid = True
    for color, count in criteria.items():
        if amount[color] > count:
            valid = False
    if valid:
        part_1 += game_id
    power = 1
    for color, count in amount.items():
        power *= count
    part_2 += power

print(part_1, part_2)
