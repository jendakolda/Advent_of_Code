def validity(data):
    return len(data) == 8 or (len(data) == 7 and 'cid' not in data.keys())


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
