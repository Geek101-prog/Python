# Решение/попытка №1

class Matrix_f:
    def __init__(self, input_data):
        self.input = input_data

    def str(self):
        return '\n'.join(map(str, self.input))

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'The length is different'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in summed_line]) + '\n'
        else:
            return 'The length is different'
        return answer


matrix_1 = Matrix_f([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix_f([[2, 3], [4, 5], [6, 7], [10, 20]])

print(matrix_1 + matrix_2)

print('*' * 60)


# Решение/попытка №2

class Matrix_f1:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        matrix_3 = []
        for i in range(len(self.lists)):
            matrix_3.append([])
            for l in range(len(self.lists[0])):
                matrix_3[i].append(self.lists[i][l] + other.lists[i][l])
                return '\n'.join(map(str, matrix_3))


matrix_1_1 = Matrix_f1([[5, 4], [6, 5], [8, 9]])
matrix_2_2 = Matrix_f1([[9, 10], [10, 11], [11, 12]])

print(matrix_1 + matrix_2)

print('*' * 60)

# Решение/попытка №3

import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        matrix_3 = np.array(self.matrix + other.matrix)
        return matrix_3

    # Не понимаю как можно применить # def __str__(self):
    # def __str__(self):
    #     return '\n'.join(map(str, self.matrix_3))


matrix_1_3 = Matrix([[5, 4], [6, 5], [8, 9]])
matrix_2_3 = Matrix([[9, 10], [10, 11], [11, 12]])
m = matrix_1_3 + matrix_2_3
print(m)
