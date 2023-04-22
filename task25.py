# DONE


# todo:
#  Функция print_given()
#  Реализуйте функцию print_given(), которая принимает произвольное количество позиционных и именованных аргументов
#  и выводит все переданные аргументы, указывая тип каждого. Пары аргумент-тип должны выводиться каждая на отдельной строке,
#  в следующем формате:
#     для позиционных аргументов:
#     <значение аргумента> <тип аргумента>
#
#     для именованных аргументов:
#     <имя переменной> <значение аргумента> <тип аргумента>
#
#     Примечание 1. При выводе позиционные аргументы должны быть расположены в порядке их передачи,
#     именованные — в лексикографическом порядке имен переменных.
#     Примечание 2. При выводе сначала должны следовать все позиционные аргументы, затем — все именованные.
#     Примечание 3. Если в функцию ничего не передается, функция ничего не должна выводить.
#     Примечание 4. Тестовые данные доступны по ссылкам:
#
#     print_given(1, [1, 2, 3], 'three', two=2)
#     Output:
#     1 <class 'int'>
#     [1, 2, 3] <class 'list'>
#     three <class 'str'>
#     two 2 <class 'int'
#
#     Sample Input:
#     print_given(b=2, d=4, c=3, a=1)
#     Sample Output:
#     a 1 <class 'int'>
#     b 2 <class 'int'>
#     c 3 <class 'int'>
#     d 4 <class 'int'>

def print_given(*args, **kwargs):
    for i in args:
        arg_type = type(i)
        arg_value = i
        print(f"{arg_value} {arg_type}")

    # in lexicographical order:
    sorted_kwargs = dict(sorted(kwargs.items(), key=lambda i: i[0]))
    for key, value in sorted_kwargs.items():
        arg_value = value
        arg_name = key
        arg_type = type(arg_value)
        print(f"{arg_name} {arg_value} {arg_type}")

print_given(1, [1, 2, 3], 'three', two=2)
print("___________________")
print_given(b=2, d=4, c=3, a=1)