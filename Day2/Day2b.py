with open('day2_input.txt', 'r', encoding='utf-8') as pwd:
    count = 0
    for line in pwd:
        interval, letter, password = line.split()
        interval = list(map(int, interval.split('-')))
        letter = letter.rstrip(':')
        if (password[interval[0]-1] == letter) ^ (password[interval[1]-1] == letter):
            count += 1
print(count)