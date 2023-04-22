# #todo Задача 1. Транспонирование матрицы, transpose(matrix)
# Создайте списковое включение, которое генерирует следующую последовательность: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10

# l = [[1,2,3],[4,5,6]]
# flattened_l = [item for sublist in l for item in sublist]
# print flattened_l # prints [1,2,3,4,5,6]

ex_1 = [item for sublist in [[j for i in range(j)] for j in range(10)] for item in sublist]
print(ex_1)

# #todo Задача 2. Транспонирование матрицы, transpose(matrix)
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.
# Пример:
# >>> transpose([[1, 2, 3], [4, 5, 6]])
#
# [[1, 4], [2, 5], [3, 6]]
#
#
# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
#                ||3 6||

def transpose(matrix):
    new_len = len(matrix[0])
    transposed_matrix = [[row[i] for row in matrix] for i in range(new_len)]
    return transposed_matrix

print(transpose([[1, 2, 3], [4, 5, 6]]))
print(transpose([[1, 4], [2, 5], [3, 6]]))


# #todo Задача 3. Найти сумму элементов матрицы
# Написать msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.
#
# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)

def msum(matrix):
    sum_of_matrix = sum([element for row in matrix for element in row])
    return sum_of_matrix


a = msum([[1, 2, 3], [4, 5, 6]])
print(a)
