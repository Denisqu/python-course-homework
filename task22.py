#todo: Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря. Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.


def code(string, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alph_len = len(alphabet)
    new_string = ""

    for char in string:
        if char.lower() not in alphabet:
            new_string += char
            continue
        is_lower = char.islower()
        index = alphabet.index(char.lower())
        new_index = (index + n) % alph_len
        new_string += alphabet[new_index] if is_lower else alphabet[new_index].upper()
    return new_string


input = input("input a string to code: \n")
print(code(input, 23))