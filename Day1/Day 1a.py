from itertools import combinations

with open('day1a_input.txt', 'r', encoding='utf-8') as expenses:
    numbers = expenses.readlines()
numbers = set(int(number.strip('\n')) for number in numbers)


def generator1(value):
    pairs = combinations(value, 3)
    yield from pairs


gen1 = generator1(numbers)

while True:
    a, b, c = next(gen1)
    if a + b + c == 2020:
        print(a*b*c)
        break
