def goto(tuple_index):
    global acc
    if instr_list[tuple_index][0] == 'acc':
        acc += instr_list[tuple_index][1]
        return tuple_index + 1
    elif instr_list[tuple_index][0] == 'jmp':
        return tuple_index + instr_list[tuple_index][1]
    elif instr_list[tuple_index][0] == 'nop':
        return tuple_index + 1


def switch(switch_index):
    if instr_list[switch_index][0] == 'jmp':
        instr_list[switch_index][0] = 'nop'
    elif instr_list[switch_index][0] == 'nop':
        instr_list[switch_index][0] = 'jmp'


with open('Day8_input.txt', 'r', encoding='utf-8') as f:
    original_list = [[instr, int(step)] for instr, step in (i.split() for i in f.read().split('\n'))]


indices = [i for i in range(len(original_list)) if original_list[i][0] == 'nop' or original_list[i][0] == 'jmp']
print(indices)

for i in indices:
    instr_list = original_list
    switch(i)
    acc = 0
    tup_ind = 0
    counter = 0
    while counter < len(instr_list):
        counter += 1
        del_ind = tup_ind
        try:
            tup_ind = goto(tup_ind)
            del instr_list[del_ind]
            if not instr_list:
                print('Task A:', acc)
        except IndexError:
            pass


