# DONE


#todo: Напишите программу, в которой используется две функции.
# В одной программа «спит» 2 секунды, в другой – 3 секунды.
# Пусть каждая функция возвращает время, которое она «проспала».
# Главная программа запускает цикл от 0 до 10, если число четное,
# то запускает функцию с 2 секундами, если нечетное, то функцию с 3 секундами.
# Накапливает сон обеих функций отдельно и печатает две суммы.

# условие задания какое-то непонятное, но ладно...

import time

def f1():
    time.sleep(2)
    return 2

def f2():
    time.sleep(3)
    return 3

def f3():
    sum = 0
    for i in range(0, 10):
        if i % 2 == 0:
            sum += f1()
        else:
            sum += f2()
    return sum

print(f3())

