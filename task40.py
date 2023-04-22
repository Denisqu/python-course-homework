# DONE


# todo: Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.

import calendar

def f(year, month):
    return [i for i in range(1, calendar.monthrange(year, month)[1] + 1)]

print(f(2000, 2))