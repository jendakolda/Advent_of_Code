# not my solution
ids = set()
for line in open('Day5_input.txt').read().splitlines():
    ids.add(int(''.join('0' if x in 'LF' else '1' for x in line), 2))
print('Part 1:', max(ids))
print('Part 2:', *[x for x in range(min(ids), max(ids)) if x not in ids])