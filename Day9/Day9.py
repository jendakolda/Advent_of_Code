from itertools import combinations


def validity(pos):
    sums = set(sum(pair) for pair in combinations(cipher[pos - 25:pos], 2))
    return cipher[pos] in sums


def contiguous():
    length = 1
    while length < 20:
        for j in range(len(short_cipher) - length):
            if sum(short_cipher[j:j + length]) == short_cipher[-1]:
                return min(short_cipher[j:j + length]) + max(short_cipher[j:j + length])
        length += 1


with open('Day9_input.txt', 'r', encoding='utf-8') as f:
    cipher = tuple(map(int, f.read().split('\n')))
for i in range(25, len(cipher)):
    if not validity(i):
        print(f'Task A: Number {cipher[i]} on position {i} not valid.')
        short_cipher = cipher[:i + 1]
        print('Task B:', contiguous())


