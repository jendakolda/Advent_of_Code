from collections import Counter
with open('Day6_input.txt', 'r') as f:
    answers = f.read()
df = [user_data for user_data in (group.split('\n') for group in answers.split("\n\n"))]
anyone = [set(''.join(i)) for i in df]
all_replies = [(''.join(i)) for i in df]
print('Task A:', sum(len(anyone[i]) for i in range(len(anyone))))
valid = 0
for i in range(len(df)):
    count = Counter(all_replies[i])
    for j in anyone[i]:
        if count[j] == len(df[i]):
            valid += 1
print('Task B:', valid)



