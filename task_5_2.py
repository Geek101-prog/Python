with open('file_t1_t2.txt', encoding='utf-8') as f_obj:
    num_lines = 0
    num_words = 0
    for line in f_obj:
        words = line.split()
        num_lines += 1
        num_words += len(words)
    print(num_lines, num_words)
