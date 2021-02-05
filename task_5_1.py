with open('file_t1_t2.txt', 'w', encoding='utf-8') as f_obj:
    while True:
        line = input('Введите данные:')
        if not line:
            break
        print(line, file=f_obj)
