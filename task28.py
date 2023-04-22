# DONE


#todo:
#    Дан список чисел.  Превратить его в список суммы цифр каждого числа. Пример входа: lst = [123, 234, 345, 456]
#    Вывод: [6, 9, 12, 15]
#    При решении используйте map и lambda

lst = [123, 234, 345, 456]

sum_digits = lambda number: 0 if number == 0 else (number % 10) + sum_digits(number // 10)
new_lst = list(map(sum_digits, lst))

print(new_lst)