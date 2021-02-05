import json

my_dic = {}
my_list = []
with open('file_t7.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        name, firm, income, costs = line.split()
        profit = int(income) - int(costs)
        my_dic[name] = profit
        if profit > 0:
            my_list.append(profit)
my_list = sum(my_list) / len(my_list)
new_list = [my_dic, {'profit': my_list}]

with open('file_t7.json', 'w', encoding='utf-8') as f1:
    json.dump(new_list, f1)
with open('file_t7.json', encoding='utf-8') as f1:
    print(json.load(f1))
