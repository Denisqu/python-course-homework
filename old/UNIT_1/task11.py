#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr[:] = [i + 1 for i in arr]

[print(i) for i in arr]