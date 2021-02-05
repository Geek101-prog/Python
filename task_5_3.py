with open('file_t3.txt', 'r', encoding='utf-8') as salary:
    salary_dic = {}
    for line in salary:
        key, value = line.split()
        salary_dic[key] = float(value)
        if float(value) < 20000:
            print(f'{key}')
            # print(f'{key}: {value}')
    print(f'Средняя з/п: {sum(salary_dic.values()) / len(salary_dic)}')
