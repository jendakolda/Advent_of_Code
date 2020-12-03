# not my solution

import re

with open("Day2_input.txt") as raw_data:
    lines = raw_data.readlines()
arr = []
regex = re.compile(r'(?P<min>\d+)-(?P<max>\d+)\s(?P<char>.):\s(?P<password>.*)$')

for item in lines:
    arr.extend([match.groupdict() for match in regex.finditer(item)])

def day2_1():
    count = 0
    for item in arr:
        char_count = item["password"].count(item["char"])
        if int(item["min"]) <= char_count <= int(item["max"]):
            count += 1
    return count

def day2_2():
    count = 0
    for item in arr:
        pos1, pos2 = int(item["min"]) - 1, int(item["max"]) - 1
        cond = sorted((item["password"][pos1] == item["char"], item["password"][pos2] == item["char"]))
        if cond == [False, True]:
            count += 1
    return count

print(f"Day 2.1: {day2_1()}")
print(f"Day 2.2: {day2_2()}")