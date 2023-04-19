# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.

def sumn(n):
    if n != 0:
        val = n+sumn(n-1)
    else:
        val = n
    return val

print(sumn(100))