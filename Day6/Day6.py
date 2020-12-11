from collections import Counter
with open('Day6_input.txt', 'r') as f:
    answers = f.read()
df = [user_data for user_data in (group.split('\n') for group in answers.split("\n\n"))]
print(df[1:3])
anyone = [set(''.join(i)) for i in df]
all_replies = [(''.join(i)) for i in df]
everyone = []
print('Task A:', sum(len(anyone[i]) for i in range(len(anyone))))
valid = 0
for i in range(len(df)):
    # print(df[i][0].intersection(df[i][1:]))
    count = Counter(all_replies[i])
    for j in anyone[i]:
        if count[j] == len(df[i]):
            valid += 1
print('Task B:', valid)



