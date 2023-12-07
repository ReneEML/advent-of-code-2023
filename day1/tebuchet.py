def parse_line(line: str):
    num = ""
    for c in line:
        if c.isnumeric():
            num += c
            break

    for c in reversed(line):
        if c.isnumeric():
            num += c
            break
    return int(num)

f = open("input.txt")

result = 0
for line in f:
    result += parse_line(line)
print(result)


