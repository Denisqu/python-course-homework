# DONE


#todo:
# Создайте лямбда функцию, которая принимает один параметр – строку.
# Переводит все буквы в нижний регистр и переворачивает их в обратном порядке. Пример входа: ‘ACbdzYx’,
# Вывод: 'xyzdbca'

my_lambda = lambda string: string.lower()[::-1]
var = my_lambda("ACbdzYx")
print(var)