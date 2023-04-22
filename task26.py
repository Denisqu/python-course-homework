# DONE


# todo:
#  Напишите функцию, которая принимает два аргумента, lst - список чисел и x – число.
#  Функция возвращает список, содержащий квадраты чисел из lst, которые больше числа x.
#  Сделайте несколько вариантов решений:
#  1) Просто цикл с условием.
#  2) Воспользуйтесь функцией filter, для чего создайте функцию проверки числа больше x

def f_cycle(lst, x):
    returned_lst = []
    for i in lst:
        if i ** 2 > x: returned_lst.append(i)
    return returned_lst


def f_filter(lst, x):
    returned_lst = list(filter(lambda i: i**2 > x, lst))
    return returned_lst


print(f_cycle([124, 12, -10, 10000], 1000))
print("________")
print(f_filter([124, 12, -10, 10000], 1000))