def row_seating(vector, start=0, stop=127):
    if len(vector) == 1:
        if vector[0] == 'F':
            return int(start)
        elif vector[0] == 'B':
            return int(stop)
    else:
        middle = (start + stop + 1) / 2
        if vector[0] == 'F':
            stop = middle - 1
        elif vector[0] == 'B':
            start = middle
        vector = vector[1:]
        return row_seating(vector, start, stop)


def column_seating(vector, start=0, stop=7):
    if len(vector) == 1:
        if vector[0] == 'L':
            return int(start)
        elif vector[0] == 'R':
            return int(stop)
    else:
        middle = (start + stop + 1) / 2
        if vector[0] == 'L':
            stop = middle - 1
        elif vector[0] == 'R':
            start = middle
        vector = vector[1:]
        return column_seating(vector, start, stop)


with open('Day5_input.txt', 'r', encoding='utf-8') as boarding:
    highest = 0
    lowest = 813
    seats = set()
    for line in boarding:
        rs = row_seating(line[:7])
        cs = column_seating(line[7:].strip('\n'))
        seat_no = rs * 8 + cs
        seats.add(seat_no)
        if seat_no > highest:
            highest = seat_no
        if seat_no < lowest:
            lowest = seat_no

print('Highest seat no:', highest)
for seat in range(lowest, highest):
    if seat not in seats:
        print('Your seat:', seat)





