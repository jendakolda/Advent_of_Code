# with open('Day11_input.txt', 'r', encoding='utf-8') as f:
#     seat_map = tuple(f.read().split('\n'))
# print(seat_map[0])


def change_state():
    for row in seat_map:
        for seat in range(len(row)):
            pass


seat_map = []
for line in open('Day11_input.txt').read().splitlines():
    seat_map.append([False if x == 0 else None for x in line])


print(seat_map[0])
before = None
while seat_map != before:
    before = seat_map
    change_state()