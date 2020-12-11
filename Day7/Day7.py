# def search_rule(color):
#     return set(key for key, value in rule_dict.items() if color in value)

def search_rule(color):
    if color in 

    return set(key for key, value in rule_dict.items() if color in value)


with open('Day7_input.txt', 'r', encoding='utf-8') as bag_rules:
    rule_dict = dict()
    for line in bag_rules:
        k, v = line.strip('.\n').split('bags contain')
        v = [i.strip(' bags')[2:] for i in v.strip(' ').split(', ')]
        if v != ['no other']:
            rule_dict[k.strip()] = v

rule_set = set(k for k in rule_dict.keys())

print(search_rule('shiny gold'))
print(search_rule('dark tomato'))
print(search_rule('pale brown'))
print(search_rule('bright red'))
print('bright red' in rule_set)

# for item in rule_set:
#     search_rule(item)




