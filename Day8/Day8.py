def goto(tuple_index):
    global acc
    if instr_list[tuple_index][0] == 'acc':
        acc += instr_list[tuple_index][1]
        return tuple_index + 1
    elif instr_list[tuple_index][0] == 'jmp':
        return tuple_index + instr_list[tuple_index][1]
    elif instr_list[tuple_index][0] == 'nop':
        return tuple_index + 1


with open('Day8_input.txt', 'r', encoding='utf-8') as f:
    instr_list = tuple([instr, int(step)] for instr, step in (i.split() for i in f.read().split('\n')))

acc = 0
used_instr = set()
tup_ind = 0
while tup_ind not in used_instr:
    used_instr.add(tup_ind)
    tup_ind = goto(tup_ind)
print('Task A:', acc)

