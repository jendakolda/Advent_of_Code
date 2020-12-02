with open('day2_input.txt', 'r', encoding='utf-8') as pwd:
    count = 0
    for line in pwd:
        interval, letter, password = line.split()
        interval = list(map(int, interval.split('-')))
        letter = letter.rstrip(':')
        if interval[0] <= password.count(letter) <= interval[1]:
            count += 1
print(count)