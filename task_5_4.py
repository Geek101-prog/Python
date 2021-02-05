with open('file_t4.txt', encoding='utf-8') as x:
    lines = x.readlines()
with open('file_t4_trans.txt', 'w', encoding='utf-8') as x:
    for i in lines:
        if '1' in i:
            i = i.replace('One', 'Один')
        elif '2' in i:
            i = i.replace('Two', 'Два')
        elif '3' in i:
            i = i.replace('Three', 'Три')
        elif '4' in i:
            i = i.replace('Four', 'Четыри')
        x.write(i)
