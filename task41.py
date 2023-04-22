# DONE


#todo:
# В Python существуют ключевые слова, которые нельзя использовать для названия переменных, функций и классов.
# Для получения списка всех ключевых слов можно воспользоваться
# атрибутом kwlist из модуля keyword. Приведенный ниже код:
# import keyword
# print(keyword.kwlist)
# выводит: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>.

from keyword import kwlist

def f(string):
    new_string = string
    for i in kwlist:
        new_string = new_string.replace(i, "<kw>")

    return new_string


a = "this is a False statement! Yes, that's was True."
a = f(a)
print(a)