def validity(data):
    return (len(data) == 8 or (len(data) == 7 and 'cid' not in data.keys())) and \
           (1920 <= int(data['byr']) <= 2002) and \
           (2010 <= int(data['iyr']) <= 2020) and \
           (2020 <= int(data['eyr']) <= 2030) and \
           valid_height(data['hgt']) and \
           valid_hair(data['hcl']) and \
           data['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
           len(data['pid']) == 9


def valid_height(height):
    return (height.endswith('cm') and (150 <= int(height[:-2]) <= 193)) or \
            (height.endswith('in') and (59 <= int(height[:-2]) <= 76))



def valid_hair(hair):
    valid_vector = [i in (list(map(str, range(10))) + list('abcdef')) for i in hair[1::]]
    return hair.startswith('#') and \
           len(hair) == 7 and \
           all(valid_vector)


with open('Day4_input.txt', 'r', encoding='utf-8') as pass_file:
    pass_data = pass_file.read()

pass_data = pass_data.split('\n\n')
pass_list = [i.split() for i in pass_data]
valid_count = 0
for i in pass_list:
    person = dict()
    for j in i:
        k, v = j.split(':')
        person[k] = v
    if validity(person):
        valid_count += 1

print('Valid passports:', valid_count)
