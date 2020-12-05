def seating(vector, start, stop, bnd):
    if len(vector) == 1:
        if vector[0] == bnd[0]:
            return int(start)
        elif vector[0] == bnd[1]:
            return int(stop)
    else:
        middle = (start + stop + 1) / 2
        if vector[0] == bnd[0]:
            stop = middle - 1
        elif vector[0] == bnd[1]:
            start = middle
        vector = vector[1:]
        return seating(vector, start, stop, bnd)


with open('Day5_input.txt', 'r', encoding='utf-8') as boarding:
    highest = 0
    lowest = 813
    seats = set()
    for line in boarding:
        rs = seating(line[:7], 0, 127, 'FB')
        cs = seating(line[7:].strip('\n'), 0, 7, 'LR')
        seat_no = rs * 8 + cs
        seats.add(seat_no)
        if seat_no > highest:
            highest = seat_no
        if seat_no < lowest:
            lowest = seat_no

print('Highest seat no:', highest)
print('Your seat:', set(range(lowest, highest)) - seats)
