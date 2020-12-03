def slope(left, down=1):
    coordinate = 0
    tree = 0
    step = 0
    with open('Day3_input.txt', 'r', encoding='utf-8') as plan:
        for line in plan:
            line = line.strip()
            if step % down == 0:
                if line[coordinate] == '#':
                    tree += 1
                coordinate = (coordinate + left) % len(line)
            step += 1
    return tree


a = slope(1)
b = slope(3)
c = slope(5)
d = slope(7)
e = slope(1, 2)
print('result of 1st task:', b)
print('result of 2nd task:', a * b * c * d * e)
