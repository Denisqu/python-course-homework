# DONE


#todo:
#  Реализуйте функцию convert(), которая принимает один аргумент:
#  number — целое число
#  Функция должна возвращать кортеж из трех элементов, расположенных в следующем порядке:
#  двоичное представление числа number в виде строки без префикса 0b
#  восьмеричное представление числа number в виде строки без префикса 0o
#  шестнадцатеричное представление числа number в виде строки в верхнем регистре без префикса 0x
#  Примечание 1. В задаче удобно воспользоваться функциями bin(), oct() и hex().
#  Задачу решить доступным способом
#  Задачу решить с помощью применения функции map и lambda

def convert_1(number):
    conv_bin = bin(number)[2:]
    conv_oct = oct(number)[2:]
    conv_hex = hex(number)[2:]
    return conv_bin, conv_oct, conv_hex

def convert_2(number):
    conv_bin = bin(number)
    conv_oct = oct(number)
    conv_hex = hex(number)
    returned_tuple = conv_bin, conv_oct, conv_hex
    returned_tuple = tuple(map(lambda i: i[2:], returned_tuple))
    return returned_tuple

my_tuple = convert_1(101)
print(my_tuple)

print("______")

my_tuple = convert_2(101)
print(my_tuple)